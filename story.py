import random

from weasyprint import HTML

#   STORY

# choices:  (label, target, required_item | None)
# gives:    items picked up on entering the location
# reset:    if True, every choice leaving this location clears the inventory
story = {
    "start": {
        "title": "Hallway",
        "text": "A dark hallway. The kitchen is to your left, a locked door straight ahead.",
        "choices": [
            ("Go to the kitchen", "kitchen", None),
            ("Examine the locked door", "door", None),
        ],
    },
    "kitchen": {
        "title": "Kitchen",
        "text": "A rusty key lies on the counter. You pocket it.",
        "gives": {"key"},
        "choices": [
            ("Back to the hallway", "start", None),
        ],
    },
    "door": {
        "title": "The Locked Door",
        "text": "A heavy oak door with a keyhole.",
        "choices": [
            ("Unlock it with the key", "vault", "key"),
            ("Step back", "start", None),
        ],
    },
    "vault": {
        "title": "The Vault",
        "text": "You found the evidence! The case is solved.",
        "reset": True,
        "choices": [
            ("Play again", "start", None),
        ],
    },
}

RULES = [
    (
        "This is a detective game played entirely inside this PDF. Click the "
        "blue buttons to make your choices and move between pages."
    ),
    (
        "Your inventory is shown at the top of every page. Some choices are "
        "greyed out until you are carrying the right item."
    ),
    (
        "Page numbers are shuffled, so flipping ahead will not help you. "
        "Use the buttons, not the scroll bar."
    ),
]


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
            nxt = (target, carried | frozenset(story[target].get("gives", ())))
            out.append((label, nxt))
            if nxt not in seen:
                seen.add(nxt)
                todo.append(nxt)
        edges[(node, inv)] = out
    return first, edges


first, edges = explore(story)

#   SHUFFLED PAGE NUMBERS
rest = [s for s in edges if s != first]
random.Random(7).shuffle(rest)  # fixed seed = reproducible
num = {s: i + 1 for i, s in enumerate([first, *rest])}  # start is always page 1
ordered = sorted(num.items(), key=lambda kv: kv[1])
print(f"Game pages: {len(num)}, total PDF pages: {len(num) + 1}")

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
    html += (
        f'<section class="page" id="p{n}">'
        f'<div class="inv">{inv_txt}</div>'
        f'<h1>{data["title"]}</h1><p>{data["text"]}</p>{btns}'
        f'<div class="pn">{n}</div></section>'
    )

HTML(string=html).write_pdf("main.pdf")