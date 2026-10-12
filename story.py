import json
import random
from pathlib import Path

from weasyprint import HTML

#   STORY  (loaded from story.json)

# Each node in story.json looks like:
#   "title", "text"
#   "choices": [{"label": ..., "target": node_id, "requires": item (optional)}]
#   "gives":   items picked up on entering the location (optional)
#   "drops":   items removed from the inventory on entering the location (optional)
#   "reset":   true = every choice leaving this location clears the inventory
#   "ending":  "success" or "fail" -> the page gets an ending banner
data = json.loads(Path(__file__).with_name("story.json").read_text(encoding="utf-8"))

START = data["start"]
story = {}
for node_id, node in data["story"].items():
    story[node_id] = {
        **node,
        # the engine works with (label, target, required_item | None) tuples
        "choices": [(c["label"], c["target"], c.get("requires")) for c in node["choices"]],
    }

ENDING_NO = {
    k: i + 1 for i, k in enumerate(k for k, v in story.items() if v.get("ending"))
}

RULES = [r.format(endings=len(ENDING_NO)) for r in data["rules"]]


#   STATE-SPACE EXPLORATION
def explore(story, start="start"):
    first = (start, frozenset(story[start].get("gives", ())))
    seen, todo, edges = {first}, [first], {}
    while todo:
        node, inv = todo.pop()
        out = []
        for label, target, need in story[node]["choices"]:
            if need and need not in inv:
                out.append((label, None))  # locked choice
                continue
            carried = frozenset() if story[node].get("reset") else inv
            gained = frozenset(story[target].get("gives", ()))
            lost = frozenset(story[target].get("drops", ()))
            nxt = (target, (carried | gained) - lost)
            out.append((label, nxt))
            if nxt not in seen:
                seen.add(nxt)
                todo.append(nxt)
        edges[(node, inv)] = out
    return first, edges


def validate(story, edges):
    for name, node in story.items():
        assert node["choices"], f"{name} has no choices (dead end)"
        assert len(node["choices"]) <= 5, f"{name} has too many buttons"
        for label, target, need in node["choices"]:
            assert target in story, f"{name} -> unknown node {target}"
    reached = {n for n, _ in edges}
    assert reached == set(story), f"unreachable: {sorted(set(story) - reached)}"
    # every state must be able to reach an ending
    ok = {s for s in edges if story[s[0]].get("ending")}
    grew = True
    while grew:
        grew = False
        for s, out in edges.items():
            if s not in ok and any(n in ok for _, n in out if n):
                ok.add(s)
                grew = True
    stuck = [s for s in edges if s not in ok]
    assert not stuck, f"states that cannot reach any ending: {stuck[:5]}"


first, edges = explore(story, START)
validate(story, edges)

#   SHUFFLED PAGE NUMBERS
rest = [s for s in edges if s != first]
random.Random(7).shuffle(rest)  # fixed seed = reproducible
num = {s: i + 1 for i, s in enumerate([first, *rest])}  # start is always page 1
ordered = sorted(num.items(), key=lambda kv: kv[1])
print(
    f"Story nodes: {len(story)}, endings: {len(ENDING_NO)}, "
    f"game pages: {len(num)}, total PDF pages: {len(num) + 1}"
)

#   RENDERING
css = """
@page { size: 148mm 200mm; margin: 0; background: #111; }
.page { box-sizing: border-box; height: 169mm; padding: 12mm;
        page-break-after: always; color: #eee;
        font-family: sans-serif; position: relative; }
.inv  { font-size: 9pt; color: #888; margin-bottom: 4mm; }
.pn   { position: absolute; bottom: 8mm; right: 12mm; font-size: 9pt; color: #555; }
a.btn { display: block; border: 1px solid #6fd3e6; color: #6fd3e6;
        padding: 3mm; margin-bottom: 2mm; text-decoration: none; }
span.locked { display: block; border: 1px solid #444; color: #555;
              padding: 3mm; margin-bottom: 2mm; }
a.bottom-btn { position: absolute; bottom: 12mm; left: 12mm; right: 12mm;
               margin: 0; text-align: center; }
.end  { font-size: 9pt; letter-spacing: 1pt; margin-bottom: 2mm; }
.end.success { color: #7ddc8a; }
.end.fail    { color: #ff7a7a; }
"""

rules_html = "".join(f"<p>{r}</p>" for r in RULES)

html = f"<style>{css}</style>"

#   intro rules page (first page of the PDF)
html += (
    '<section class="page" id="rules">'
    f"<h1>Rules</h1>{rules_html}"
    '<a class="btn bottom-btn" href="#p1">Start game</a>'
    "</section>"
)

#   game pages, in page-number order
for state, n in ordered:
    node, inv = state
    data = story[node]
    btns = ""
    for label, nxt in edges[state]:
        if nxt is None:
            btns += f'<span class="locked">{label} (locked)</span>'
        else:
            btns += f'<a class="btn" href="#p{num[nxt]}">{label}</a>'
    inv_txt = "Inventory: " + (", ".join(sorted(inv)) if inv else "empty")
    banner = ""
    if data.get("ending"):
        kind = "SUCCESS" if data["ending"] == "success" else "FAILURE"
        banner = (
            f'<div class="end {data["ending"]}">'
            f"ENDING {ENDING_NO[node]} OF {len(ENDING_NO)} - {kind}</div>"
        )
    html += (
        f'<section class="page" id="p{n}">'
        f'<div class="inv">{inv_txt}</div>{banner}'
        f'<h1>{data["title"]}</h1><p>{data["text"]}</p>{btns}'
        f'<div class="pn">{n}</div></section>'
    )

HTML(string=html).write_pdf("main.pdf")