from weasyprint import HTML

pages = {
    1: ("Start", "You stand in front of a closed door.", [("Knock", 2), ("Leave", 3)]),
    2: ("The door", "Nobody answers.", [("Vissza", 1)]),
    3: ("End", "You went home. The case remains unsolved.", [("Restart", 1)]),
}

css = """
@page { size: 148mm 210mm; margin: 0; background: #111; }
.page { height: 209mm; padding: 12mm; page-break-after: always; color: #eee; }
a.btn { display: block; border: 1px solid #6fd3e6; color: #6fd3e6;
        padding: 3mm; margin-bottom: 2mm; text-decoration: none; }
"""

html = f"<style>{css}</style>"
for n, (title, text, choices) in pages.items():
    btns = "".join(f'<a class="btn" href="#p{t}">{label}</a>' for label, t in choices)
    html += (
        f'<section class="page" id="p{n}"><h1>{title}</h1><p>{text}</p>{btns}</section>'
    )

HTML(string=html).write_pdf("main.pdf")
