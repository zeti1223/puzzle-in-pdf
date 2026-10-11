import random

from weasyprint import HTML

#   STORY

# choices:  (label, target, required_item | None)
# gives:    items picked up on entering the location
# reset:    if True, every choice leaving this location clears the inventory
# drops:    items removed from the inventory on entering the location
#           (keeps the number of page variants under control)
# ending:   "success" or "fail" -> the page gets an ending banner
PLAY_AGAIN = [("Play again", "start", None)]

story = {
    #   ACT 1: THE ATTACK
    "start": {
        "title": "Start",
        "text": (
            "It is 3 a.m. Your phone buzzes on the nightstand: an alert from "
            "your homelab. Something is very wrong."
        ),
        "choices": [
            ("Open the dashboard", "ddos", None),
        ],
    },
    "ddos": {
        "title": "Homelab DDoS",
        "text": (
            "Traffic graphs are through the roof. Thousands of requests per "
            "second are hammering your homelab. The router fans are screaming. "
            "You have to act now."
        ),
        "choices": [
            ("Remove the Internet connection", "remove_internet", None),
            ("Close all open ports on the router", "close_ports", None),
        ],
    },
    "remove_internet": {
        "title": "Remove Internet connection",
        "text": (
            "You rip the ethernet cable out of the router. The blinking "
            "lights go quiet. But the attack was already writing to your "
            "disks when the link dropped."
        ),
        "choices": [
            ("Check the damage", "data_loss_a", None),
        ],
    },
    "close_ports": {
        "title": "Close all open ports on router",
        "text": (
            "You log into the router and shut every forwarded port: SSH, "
            "HTTPS, the Jellyfin stream, everything. The router is quiet for "
            "a moment, then the logs start scrolling again."
        ),
        "choices": [
            ("Check the damage", "data_loss_b", None),
            ("Check the server console", "kernel_deleted", None),
        ],
    },
    "data_loss_a": {
        "title": "20% data loss",
        "text": (
            "A fifth of your files are gone or corrupted. The rest of the "
            "lab is cut off from the world."
        ),
        "choices": [
            ("Stay offline and think", "no_internet", None),
            ("Plug the ethernet cable back in", "plug_back", None),
        ],
    },
    "data_loss_b": {
        "title": "20% data loss",
        "text": (
            "The ports are closed, but the attacker was already inside. "
            "A fifth of your files are gone or corrupted, and the system "
            "is acting strangely."
        ),
        "choices": [
            ("Look at the system more closely", "kernel_deleted", None),
        ],
    },
    "no_internet": {
        "title": "No internet",
        "text": (
            "Silence. Without a connection you cannot look up fixes, ask for "
            "help or download anything. You are alone with the damage."
        ),
        "choices": [
            ("Plug the ethernet cable back in", "plug_back", None),
        ],
    },
    "plug_back": {
        "title": "Plug back ethernet",
        "text": (
            "The link light turns green again. For a few seconds everything "
            "looks fine. Then the traffic graph spikes."
        ),
        "choices": [
            ("Check the graphs", "still_attacking", None),
        ],
    },
    "still_attacking": {
        "title": "Still attacking",
        "text": (
            "The attack never stopped. Whoever is behind it is still "
            "hammering your lab, and the router is wide open again."
        ),
        "choices": [
            ("Close all open ports on the router", "close_ports", None),
        ],
    },
    "kernel_deleted": {
        "title": "Kernel deleted",
        "text": (
            "You open the console. The kernel has been deleted. The machine "
            "is still running from memory, but it will not survive a reboot. "
            "You need to get it back, and fast."
        ),
        "choices": [
            ("Ask an AI how to recover the kernel", "ask_ai", None),
            ("Ask Reddit how to recover the kernel", "ask_reddit", None),
        ],
    },
    "ask_ai": {
        "title": "Ask an AI",
        "text": (
            "You paste the panic-induced error logs into an AI chatbot. It "
            "confidently outputs a multi-step kernel compilation and "
            "reinstallation command string. You copy-paste and execute it."
        ),
        "choices": [
            ("See what happens", "unknown_event", None),
        ],
        "gives": ("Ai answer",),
    },
    "ask_reddit": {
        "title": "Ask Reddit",
        "text": (
            "You post on r/homelab with the title: 'PLEASE HELP MY KERNEL IS DELETED"
        ),
        "choices": [
            ("Execute the Reddit advice", "unknown_event", None),
        ],
        "gives": ("random guy from reddit",),
    },
    "unknown_event": {
        "title": "Something happened",
        "text": (
            "The terminal flashes a cascade of cryptic messages. The screen "
            "freezes for a moment. You aren't entirely sure what just executed, "
            "but the system state has fundamentally shifted."
        ),
        "choices": [
            ("Try to revert using the AI method", "kernel_deleted", "Ai answer"),
            ("Wait for the system response", "blackout", "random guy from reddit"),
        ],
    },
    "blackout": {
        "title": "Everything goes black",
        "text": (
            "The monitors click off. The server chassis fans wind down to "
            "complete silence. Total darkness fills the room."
        ),
        "choices": [
            ("Hit the physical power button to restart", "restart", None),
            ("Wait in the dark", "blackout", None),
        ],
        "reset": True,
    },
    "restart": {
        "title": "Restart",
        "text": (
            "The BIOS splash screen appears. Services begin initializing "
            "one by one as the OS boots back up from disk."
        ),
        "choices": [
            ("Check the container status", "containers_down", None),
        ],
    },
    "containers_down": {
        "title": "Containers offline",
        "text": (
            "SSH access is restored, and the base OS is healthy. However, "
            "Docker is completely empty—all your containers, databases, "
            "and media servers failed to start up automatically."
        ),
        "choices": [
            
        ],
    },
ENDING_NO = {
    k: i + 1 for i, k in enumerate(k for k, v in story.items() if v.get("ending"))
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
    (
        f"There are {len(ENDING_NO)} different endings. Some are triumphant. "
        "Some are educational."
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


first, edges = explore(story)
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