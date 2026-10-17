import json
import random
from html import escape
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
raw = json.loads(Path(__file__).with_name("story.json").read_text(encoding="utf-8"))

START = raw["start"]
story = {}
for node_id, node in raw["story"].items():
    story[node_id] = {
        **node,
        # the engine works with (label, target, required_item | None) tuples
        "choices": [(c["label"], c["target"], c.get("requires")) for c in node["choices"]],
    }

ENDING_NO = {
    k: i + 1 for i, k in enumerate(k for k, v in story.items() if v.get("ending"))
}

RULES = [r.format(endings=len(ENDING_NO)) for r in raw["rules"]]


#   STATE-SPACE EXPLORATION
def explore(story, start="start"):
    first = (start, frozenset(story[start].get("gives", ())))
    seen, todo, edges = {first}, [first], {}
    while todo:
        node, inv = todo.pop()
        out = []
        for label, target, need in story[node]["choices"]:
            if need and need not in inv:
                out.append((label, None, need))  # locked choice
                continue
            carried = frozenset() if story[node].get("reset") else inv
            gained = frozenset(story[target].get("gives", ()))
            lost = frozenset(story[target].get("drops", ()))
            nxt = (target, (carried | gained) - lost)
            out.append((label, nxt, need))
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
            if s not in ok and any(n in ok for _, n, _ in out if n):
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
TOTAL = len(num)
print(
    f"Story nodes: {len(story)}, endings: {len(ENDING_NO)}, "
    f"game pages: {len(num)}, total PDF pages: {len(num) + 1}"
)

#   RENDERING
css = """
@page { size: 148mm 200mm; margin: 0; background: #0e0f12; }
* { box-sizing: border-box; }

.page {
  position: relative;
  height: 199mm;               /* just under the page height: no blank pages */
  overflow: hidden;
  padding: 16mm 15mm 0 15mm;
  page-break-after: always;
  background: #0e0f12;
  color: #b8bcc4;
  font-family: "Inter", "DejaVu Sans", "Helvetica Neue", Arial, sans-serif;
  font-size: 10.5pt;
  line-height: 1.6;
}

.bar {
  margin-bottom: 12mm;
  font-size: 7.5pt;
  letter-spacing: 0.4pt;
  color: #5d626c;
}
.bar .label { text-transform: uppercase; letter-spacing: 1pt; margin-right: 2mm; }
.bar .item { color: #8a909b; }
.bar .item + .item::before { content: " / "; color: #3a3d44; }

h1 {
  margin: 0 0 4mm 0;
  font-size: 18pt;
  line-height: 1.2;
  font-weight: normal;
  color: #e6e8ec;
}
.story-text { margin: 0 0 9mm 0; font-size: 10.5pt; color: #a4a9b3; }

.notice { margin: -4mm 0 8mm 0; font-size: 8.5pt; color: #8a909b; }
.notice b { font-weight: normal; color: #c4c8d0; }

a.btn, span.locked {
  display: block;
  margin-bottom: 2mm;
  padding: 2.8mm 4mm;
  border-radius: 1.5mm;
  text-decoration: none;
}
a.btn { border: 1px solid #2b2e35; color: #cfd3da; }
span.locked { border: 1px solid #1a1c21; color: #4a4e57; }
.k { display: inline-block; width: 6mm; font-size: 8.5pt; color: #5d626c; }
.need { display: block; margin: 0.5mm 0 0 6mm; font-size: 7.5pt; color: #4a4e57; }

.end-banner {
  margin-bottom: 4mm;
  font-size: 7.5pt;
  letter-spacing: 1pt;
  text-transform: uppercase;
  color: #6b707a;
}
.end-banner.success { color: #7fa389; }
.end-banner.fail    { color: #a98084; }

.foot {
  position: absolute;
  left: 15mm;
  right: 15mm;
  bottom: 9mm;
  font-size: 7.5pt;
  color: #4a4e57;
}
.foot a { color: #5d626c; text-decoration: none; }
.foot .pn { float: right; }

.eyebrow {
  margin-bottom: 3mm;
  font-size: 7.5pt;
  letter-spacing: 1.2pt;
  text-transform: uppercase;
  color: #5d626c;
}
.rule { margin: 0 0 4mm 0; padding-left: 8mm; position: relative; color: #a4a9b3; }
.rule .n { position: absolute; left: 0; top: 0; font-size: 8.5pt; color: #5d626c; }
a.bottom-btn {
  position: absolute;
  bottom: 15mm;
  left: 15mm;
  right: 15mm;
  margin: 0;
  text-align: center;
  color: #e6e8ec;
  border: 1px solid #3a3d44;
}
"""

TOTAL_LABEL = f"{TOTAL:02d}"


def pad(n):
    return f"{n:02d}"


html = f"<style>{css}</style>"

#   intro rules page (first page of the PDF)
rules_html = "".join(
    f'<div class="rule"><span class="n">{i + 1:02d}</span>{escape(r)}</div>'
    for i, r in enumerate(RULES)
)
html += (
    '<section class="page" id="rules">'
    '<div class="eyebrow">Interactive detective game</div>'
    f"<h1>Rules</h1>{rules_html}"
    '<a class="btn bottom-btn" href="#p1">Start game</a>'
    "</section>"
)

#   game pages, in page-number order
for state, n in ordered:
    node, inv = state
    info = story[node]
    kind = info.get("ending")

    # choices
    btns = ""
    for i, (label, nxt, need) in enumerate(edges[state], start=1):
        if nxt is None:
            btns += (
                f'<span class="locked"><span class="k">{i}</span>{escape(label)}'
                f'<span class="need">requires: {escape(need)}</span></span>'
            )
        else:
            btns += (
                f'<a class="btn" href="#p{num[nxt]}"><span class="k">{i}</span>'
                f'{escape(label)}</a>'
            )

    # status bar: inventory chips
    if inv:
        chips = "".join(f'<span class="item">{escape(x)}</span>' for x in sorted(inv))
    else:
        chips = '<span class="item">empty</span>'
    bar = f'<div class="bar"><span class="label">Inventory</span>{chips}</div>'

    # "item picked up / lost" notices
    notices = ""
    for item in info.get("gives", ()):
        notices += f'<div class="notice">Picked up: <b>{escape(item)}</b></div>'
    for item in info.get("drops", ()):
        notices += f'<div class="notice lost">Lost: <b>{escape(item)}</b></div>'

    # ending banner
    banner = ""
    if kind:
        label_kind = "Success" if kind == "success" else "Failure"
        banner = (
            f'<div class="end-banner {kind}">'
            f"Ending {ENDING_NO[node]} of {len(ENDING_NO)} - {label_kind}</div>"
        )

    cls = f"is-{kind}" if kind else ""
    html += (
        f'<section class="page {cls}" id="p{n}">'
        f"{bar}{banner}"
        f'<h1>{escape(info["title"])}</h1>'
        f'<p class="story-text">{escape(info["text"])}</p>'
        f"{notices}"
        f'<div class="choices">{btns}</div>'
        "</section>"
    )

doc = (
    '<html lang="en"><head><meta charset="utf-8">'
    "<title>Homelab Detective</title></head>"
    f"<body>{html}</body></html>"
)
HTML(string=doc).write_pdf("main.pdf")