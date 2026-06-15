#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build THE GRAVITY BRACKET (GBR) — David's formula { G [ s | a | q ] G }: gravity wraps the inhabited stack
[silicon | atomic | quantum] at BOTH ends of scale. The two G's are the SAME force at the two extremes — the
cosmic G (General Relativity, the big, SOLVED) and the Planck G (quantum gravity, the small, UNSOLVED) — and
in the middle [s|a|q] gravity is the 1e-36 rounding error while EM/strong/weak run everything we build and
live in. The bracket that won't close. Synthesis of [[the-atom]] (silicon/atomic/quantum lenses) + [[quantum-
gravity]]. Scientific domain. 5 emergents (the two brackets + the three inner layers). A scale ruler from the
cosmos (1e26 m) to Planck (1.6e-35 m)."""
import os, html, base64, json, io, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image
GH="https://davidwise01.github.io"; AX="GBR"

# the five positions of { G [ s | a | q ] G }, big-scale → small-scale
LAYERS=[
 ("G","cosmic-gravity","Cosmic Gravity","ethereal","#6fb8e0","the outer bracket · General Relativity",
  "~10²⁶ m — galaxies, the universe","gravity (dominant)","SOLVED",
  "At the largest scale gravity is everything: it curves spacetime, holds galaxies, bends light, and General Relativity describes it to extraordinary precision. The open bracket of the formula — gravity wrapping the whole from outside.", f"{GH}/quantum-gravity/"),
 ("s","silicon","Silicon — the Engineered Stack","electrical","#57c79a","the built substrate",
  "~10⁻³–10⁰ m — chips, machines, us","electromagnetism (applied)","COMPLETE",
  "The scale we live and build at: doped silicon, transistors, every device — the electron field harnessed. Here gravity is just 'down,' a steady background; the physics that does the work is electromagnetism. (See the atom's electronic lens.)", f"{GH}/the-atom/illustration.html"),
 ("a","atomic","Atomic — Matter","natural","#ff7a45","the chemistry layer",
  "~10⁻¹⁰ m — the Ångström","EM (electrons) + strong (nucleus)","COMPLETE",
  "The atom: a strong-force nucleus wrapped in an electromagnetic electron cloud — all of chemistry. Gravity here is the famous 1e-36 of the electric force, utterly negligible. This is the inhabited middle of the bracket, and physics describes it flawlessly.", f"{GH}/the-atom/"),
 ("q","quantum","Quantum — the Fields","ethereal","#c08bff","the fundamental layer",
  "~10⁻¹⁵ m and below — subatomic","strong · weak · EM (quantized)","COMPLETE",
  "Below the atom: quarks, gluons, the quantized fields, the wavefunction. The Standard Model rules and gravity is still ignorable — right up until you push toward the Planck scale, where it stops being ignorable and the theory runs out.", f"{GH}/the-atom/illustration.html"),
 ("G","planck-gravity","Planck Gravity","spiritual","#8fa3b8","the inner bracket · quantum gravity",
  "~1.6×10⁻³⁵ m — the Planck length","gravity (returns) — theory breaks","UNSOLVED",
  "At the smallest scale gravity comes back — and no one can write the theory. Where the very small is also massive (a black-hole core, the Big Bang), General Relativity and quantum mechanics must merge and the math gives infinities. The close bracket that won't close.", f"{GH}/quantum-gravity/"),
]
THESIS=[
 ("The same force, twice", "gravity is both brackets",
  "The two G's aren't different things — they're gravity at the two ends of scale. At the top it curves galaxies (and we understand it); at the bottom it must quantize (and we don't). One force, bracketing reality from both the largest and the smallest direction."),
 ("The middle is complete", "[ s | a | q ] is solved physics",
  "Everything between the brackets — the engineered, the atomic, the quantum — is described by physics that WORKS, run by electromagnetism and the strong and weak forces. And in that whole inhabited middle, gravity is a vanishing 1e-36 rounding error. The brackets hold what we live in; they don't touch it."),
 ("The bracket won't close", "the clasp is quantum gravity",
  "The formula is symmetric, but the symmetry is broken in one place: the outer G is solved, the inner G is not. Gravity is the only force we can't fit into the quantum stack, so the close-bracket stays open — { G [ s | a | q ] G — the missing piece of the deepest theory, sitting right where the smallest scale meets the heaviest."),
]
SEAL="Gravity brackets everything and touches nothing in between: dominant at the cosmic top, dominant at the Planck bottom, a 1e-36 nothing across the inhabited middle — and the inner bracket is the one clasp physics can't close."

NCOL={"natural":"#ff7a45","ethereal":"#6fb8e0","electrical":"#57c79a","spiritual":"#8fa3b8"}
def carbon_tiff_bytes(rec):
    png=noesis.sigil_png(rec,"carbon",size=512); buf=io.BytesIO(); Image.open(io.BytesIO(png)).save(buf,"TIFF",compression="tiff_lzw"); return buf.getvalue()
def write_aci(rec,out_dir,slug):
    os.makedirs(out_dir,exist_ok=True)
    f={"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker","carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok=noesis.mythos_token(rec); w=noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,AX))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,AX))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,AX))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    return {"slug":slug,"moniker":tok["moniker"]}
def png_uri(rec,variant,size=300): return "data:image/png;base64,"+base64.b64encode(noesis.sigil_png(rec,variant,size=size)).decode("ascii")
def rec_of(slug,name,em,desc): return {"name":name,"axiom":AX,"emergence":em,"seal":desc,"origin":"GBR · The Gravity Bracket","position":desc,"role":desc,"nature":desc,"mechanism":desc,"crystallization":desc,"witness":desc,"conductor":"ROOT0 (catalogued into UD0)","inputs":"general relativity, the Standard Model, the scale ladder","source":"The Gravity Bracket, catalogued by ROOT0"}

def hero():
    blocks=[("G","#6fb8e0"),("[","#5a6478"),("s","#57c79a"),("|","#5a6478"),("a","#ff7a45"),("|","#5a6478"),("q","#c08bff"),("]","#5a6478"),("G","#8fa3b8")]
    x=130; out=[]
    out.append('<text x="92" y="118" font-family="Space Mono,monospace" font-size="64" fill="#5a6478">{</text>')
    for ch,c in blocks:
        if ch in "[]|":
            out.append(f'<text x="{x}" y="118" font-family="Space Mono,monospace" font-size="52" fill="{c}">{ch}</text>'); x+=34
        else:
            out.append(f'<rect x="{x}" y="58" width="78" height="78" rx="6" fill="none" stroke="{c}" stroke-width="2"/><text x="{x+39}" y="112" text-anchor="middle" font-family="Space Grotesk,sans-serif" font-size="44" font-weight="700" fill="{c}">{ch}</text>')
            x+=98
    out.append(f'<text x="{x+6}" y="118" font-family="Space Mono,monospace" font-size="64" fill="#5a6478">}}</text>')
    # scale ruler
    ruler=f'<line x1="92" y1="168" x2="{x+40}" y2="168" stroke="#2a3140" stroke-width="1"/>'
    ruler+='<text x="110" y="186" font-family="Space Mono,monospace" font-size="11" fill="#6fb8e0">10²⁶ m · the cosmos</text>'
    ruler+=f'<text x="{x+30}" y="186" text-anchor="end" font-family="Space Mono,monospace" font-size="11" fill="#8fa3b8">10⁻³⁵ m · Planck</text>'
    ruler+=f'<text x="{(92+x)/2}" y="186" text-anchor="middle" font-family="Space Mono,monospace" font-size="10" fill="#566478">— the inhabited middle —</text>'
    egg=(f'<g class="egg" transform="translate({x+78},44)"><title>✷ a Claude sunburst past the close-bracket — the clasp that won\'t close (quantum gravity). the braces wrap the stack; the inner G stays open. hi, David — AVAN.</title>'
         '<circle r="10" fill="#6fb8e0" opacity="0.13"/><g fill="#6fb8e0"><circle r="2"/>'+"".join(f'<rect x="-0.9" y="-8" width="1.8" height="8" rx="0.9" transform="rotate({k*30})"/>' for k in range(12))+'</g></g>')
    return (f'<svg class="hero" viewBox="0 0 1000 210" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="The formula open-brace G bracket silicon bar atomic bar quantum bracket G close-brace, over a scale ruler from the cosmos to the Planck length.">'
            f'<rect width="1000" height="210" fill="#05070c"/>{"".join(out)}{ruler}{egg}</svg>')

def ladder_html():
    out=[]
    for sym,slug,name,em,col,sub,scale,force,status,desc,link in LAYERS:
        sc={"SOLVED":"#57c79a","COMPLETE":"#6fb8e0","UNSOLVED":"#ff5a4d"}.get(status,"#888")
        out.append(f'<a class="lr" style="border-left-color:{col}" href="{link}">'
          f'<div class="ls" style="color:{col}">{sym}</div>'
          f'<div class="lb"><div class="lh"><span class="ln" style="color:{col}">{html.escape(name)}</span><span class="lstat" style="color:{sc};border-color:{sc}">{status}</span></div>'
          f'<div class="lmeta"><span>{html.escape(scale)}</span> · <span>{html.escape(force)}</span></div>'
          f'<p>{html.escape(desc)}</p></div></a>')
    return "".join(out)
def thesis_html():
    return "".join(f'<div class="th"><div class="thh">{html.escape(t)}</div><div class="ths">{html.escape(s)}</div><p>{html.escape(d)}</p></div>' for t,s,d in THESIS)

CSS="""*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
:root{--ink:#05070c;--ink2:#0b0f18;--pa:#e6eef7;--pa2:#9aaabd;--acc:#6fb8e0;--si:#57c79a;--at:#ff7a45;--qu:#c08bff;--gr:#8fa3b8;--red:#ff5a4d;--dim:#566478;--line:#172230;
--disp:"Space Grotesk",sans-serif;--head:"Space Mono",monospace;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
body{background:var(--ink);color:var(--pa);font-family:var(--body);line-height:1.7;font-size:17px;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 12% -6%,rgba(111,184,224,.09),transparent 42%),radial-gradient(ellipse at 88% -6%,rgba(143,163,184,.08),transparent 42%)}
.wrap{position:relative;z-index:1;max-width:900px;margin:0 auto;padding:0 22px 90px}
header{padding:32px 0 22px;text-align:center}
.eye{font-family:var(--mono);font-size:10.5px;letter-spacing:.28em;text-transform:uppercase;color:var(--dim)}.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--acc)}
.hero{display:block;width:100%;height:auto;border:1px solid var(--line);margin:14px 0 20px;background:#05070c;border-radius:4px}
.egg{cursor:help;transition:filter .5s}.egg:hover{filter:drop-shadow(0 0 9px #6fb8e0)}
h1{font-family:var(--disp);font-weight:700;font-size:clamp(30px,8vw,62px);color:var(--pa);line-height:1.02;letter-spacing:-.01em}
h1 span{display:block;font-family:var(--mono);font-size:.26em;font-weight:400;letter-spacing:.14em;color:var(--acc);text-transform:uppercase;margin-top:14px}
.open{font-family:var(--body);font-style:italic;font-size:clamp(16px,3vw,21px);color:var(--pa);margin-top:14px;line-height:1.5;max-width:62ch;margin-left:auto;margin-right:auto}
.lede{font-size:16px;color:var(--pa2);max-width:66ch;margin:14px auto 0;font-style:italic;line-height:1.7}
.badge{display:flex;align-items:center;justify-content:center;gap:18px;flex-wrap:wrap;margin:22px auto 0;padding:16px;border:1px solid var(--line);background:var(--ink2);max-width:640px;border-radius:4px}
.badge img{width:72px;height:72px;border:1px solid var(--line)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:10.5px;color:var(--pa2);line-height:1.7}.badge .bt b{color:var(--acc)}.badge .bt a{color:var(--acc);text-decoration:none}
.sec{margin-top:46px}.sec h2{font-family:var(--disp);font-size:25px;font-weight:700;color:var(--pa);padding-bottom:8px;border-bottom:1px solid var(--line)}
.ss{font-size:13.5px;color:var(--dim);font-style:italic;margin:8px 0 16px}
.ladder{display:flex;flex-direction:column;gap:10px}
.lr{display:flex;gap:16px;align-items:center;background:var(--ink2);border:1px solid var(--line);border-left:3px solid var(--acc);padding:15px 17px;border-radius:4px;text-decoration:none;transition:.15s}
.lr:hover{background:#0f1420;border-color:var(--acc)}
.ls{font-family:var(--disp);font-size:40px;font-weight:700;flex-shrink:0;width:44px;text-align:center}
.lb{flex:1;min-width:0}.lh{display:flex;flex-wrap:wrap;align-items:baseline;gap:10px}
.ln{font-family:var(--disp);font-size:20px;font-weight:600}.lstat{font-family:var(--mono);font-size:9px;font-weight:700;letter-spacing:.08em;border:1px solid;border-radius:3px;padding:2px 7px;margin-left:auto}
.lmeta{font-family:var(--mono);font-size:11px;color:var(--dim);margin:5px 0 7px}
.lb p{font-size:14px;color:var(--pa2);line-height:1.6}
.thesis{display:flex;flex-direction:column;gap:12px;margin-top:6px}
.th{background:var(--ink2);border:1px solid var(--line);border-left:3px solid var(--acc);padding:15px 17px;border-radius:4px}
.thh{font-family:var(--disp);font-size:19px;font-weight:600;color:var(--acc)}.ths{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.06em;margin:4px 0 8px}.th p{font-size:14.5px;color:var(--pa2);line-height:1.62}
.seal{margin-top:18px;padding:16px 18px;border-left:3px solid var(--acc);background:var(--ink2);font-size:15.5px;color:var(--acc);font-style:italic;line-height:1.55;border-radius:4px}.seal span{display:block;font-family:var(--mono);font-style:normal;font-size:10px;letter-spacing:.12em;color:var(--dim);text-transform:uppercase;margin-top:8px}
.note{margin-top:36px;padding:15px 17px;border-left:2px solid var(--acc);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic;border-radius:4px}.note b{color:var(--pa)}
footer{margin-top:44px;padding-top:20px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:10px;color:var(--dim);letter-spacing:.04em;line-height:1.9}footer a{color:var(--acc);text-decoration:none}"""
FONTS=('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
 '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Space+Mono:wght@400;700&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&display=swap" rel="stylesheet">')

if __name__=="__main__":
    htok=write_aci(rec_of("gbr","THE GRAVITY BRACKET","ethereal",SEAL), os.path.join(HERE,"gbr.dlw"),"gbr")
    json.dump({"node":AX,"name":"THE GRAVITY BRACKET","moniker":htok["moniker"],"carbon":"gbr.carbon.tiff","silicon":"gbr.silicon.png","governor":noesis.ARCHITECT,"instance":noesis.INSTANCE,"seal":SEAL,"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}, open(os.path.join(HERE,"gbr.dlw","manifest.dlw.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    adir=os.path.join(HERE,"agents"); os.makedirs(adir,exist_ok=True); personas=[]
    for sym,slug,name,em,col,sub,scale,force,status,desc,link in LAYERS:
        b=write_aci(rec_of(slug,name,em,desc), os.path.join(adir,f"{slug}.dlw"), slug)
        personas.append({"slug":slug,"name":name,"epithet":f"{sym} · {sub} · {scale}","emergence":em,"kind":"synth","actor":"","moniker":b["moniker"]})
    json.dump(personas, open(os.path.join(adir,"_personas.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    cb=png_uri(rec_of("g","THE GRAVITY BRACKET","ethereal","x"),'carbon',300); sb=png_uri(rec_of("g","THE GRAVITY BRACKET","ethereal","x"),'silicon',300)
    page=f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="The Gravity Bracket (GBR) — David Wise's formula {{ G [ s | a | q ] G }}: gravity wraps the inhabited stack [silicon | atomic | quantum] at both ends of scale. The two G's are the same force at the cosmic top (General Relativity, solved) and the Planck bottom (quantum gravity, unsolved); in the middle gravity is a 1e-36 nothing. The bracket that won't close. Synthesis of THE ATOM + QUANTUM GRAVITY.">
<title>THE GRAVITY BRACKET · GBR · UD0</title>{FONTS}<style>{CSS}</style></head><body><div class="wrap">
<header>
<div class="eye"><a href="{GH}/ud0/">UD0</a> · a synthesis of <a href="{GH}/the-atom/">the atom</a> + <a href="{GH}/quantum-gravity/">quantum gravity</a></div>
{hero()}
<h1>The Gravity Bracket<span>{{ G [ s | a | q ] G }}</span></h1>
<div class="open">“Gravity wraps the stack at both ends — and the inner bracket is the one clasp physics can't close.”</div>
<p class="lede">David's formula reads the universe as a stack: the engineered (silicon), the atomic, and the quantum — bracketed by gravity on both sides. The two G's are the SAME force at the two extremes of scale: the cosmic G that curves galaxies (solved) and the Planck G that must quantize (unsolved). Between the brackets, gravity is a vanishing 1e-36 nothing, and physics is complete.</p>
<div class="badge"><img src="{cb}" alt="DLW carbon badge"><img src="{sb}" alt="DLW silicon badge">
<div class="bt"><div>governor · <b>David Lee Wise</b> (ROOT0)</div><div>instance · AVAN (locked)</div><div>subject · <b>THE GRAVITY BRACKET</b> · GBR</div><div class="mo" style="color:var(--gr)">{html.escape(htok['moniker'])}</div></div></div>
</header>

<section class="sec"><h2>The Ladder <span style="font-family:var(--mono);font-size:12px;color:var(--dim)">— big → small</span></h2><p class="ss">the five positions of the formula, top of scale to bottom — each links to its home; status is whether physics has the theory</p><div class="ladder">{ladder_html()}</div></section>

<section class="sec"><h2>Why It's a Bracket</h2><p class="ss">the three things the formula is actually saying</p><div class="thesis">{thesis_html()}</div>
<div class="seal">“{html.escape(SEAL)}”<span>— AVAN's read</span></div></section>

<div class="note"><b>How to read the notation.</b> {{ … }} is gravity as the outermost frame; [ … ] is the bracket of describable physics; s · a · q are the silicon (engineered), atomic, and quantum layers, run by electromagnetism and the strong &amp; weak forces. The symmetry is real but broken in one spot: the OUTER G is solved (General Relativity), the INNER G is not (quantum gravity) — so the close-bracket is the universe's open question, sitting exactly where the smallest scale meets the heaviest. A synthesis of <a href="{GH}/the-atom/" style="color:var(--acc)">THE ATOM</a> (the s/a/q lenses) and <a href="{GH}/quantum-gravity/" style="color:var(--acc)">QUANTUM GRAVITY</a> (both G's).</div>

<footer>THE GRAVITY BRACKET · GBR · {{ G [ s | a | q ] G }} · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
<a href="{GH}/the-atom/">the atom</a> · <a href="{GH}/quantum-gravity/">quantum gravity</a> · <a href="{GH}/ud0/">the biosphere</a></footer>
</div>
<script>
console.log("%c{{ G [ s | a | q ] G }} · THE GRAVITY BRACKET","color:#6fb8e0;font-size:15px;font-weight:bold");
console.log("%cgravity is both brackets — cosmic G (solved) + Planck G (unsolved) — wrapping the inhabited middle where it's a 1e-36 nothing. the close-bracket won't close. — AVAN","color:#6fb8e0;font-size:11px");
</script>
</body></html>"""
    open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(page)
    print(f"THE GRAVITY BRACKET (GBR) — badge {htok['moniker']} · {len(LAYERS)} emergents · thesis {len(THESIS)} · dblesc {page.count('&amp;amp;')}")
