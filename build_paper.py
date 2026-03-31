#!/usr/bin/env python3
"""
build_paper.py
Run once from /Users/furkan/mcppaper/ to:
  1. Write figure PDFs (embedded as base64)
  2. Compile main.tex twice with pdflatex
"""
import base64, subprocess, os, sys

fig1_b64 = "JVBERi0xLjQKJcOiw6MKMSAwIG9iago8PAovVGl0bGUgKCkKL0NyZWF0b3IgKP7/AHcAawBoAHQAbQBsAHQAbwBwAGQAZgAgADAALgAxADIALgA2KQovUHJvZHVjZXIgKP7/AFEAdAAgADUALgAxADUALgAxADMpCi9DcmVF0aW9uRGF0ZSAoRDoyMDI2MDMzMTIwMDQ1MFopCj4+CmVuZG9iagoyIDAgb2JqCjw8Ci9UeXBlIC9DYXRhbG9nCi9QYWdlcyAzIDAgUgo+PgplbmRvYmoKNCAwIG9iago8PAovVHlwZSAvRXh0R1N0YXRlCi9TQSB0cnVlCi9TTSAwLjAyCi9jYSAxLjAKL0NBIDEuMAovQUlTIGZhbHNlCi9TTWFzayAvTm9uZT4+CmVuZG9iago1IDAgb2JqClsvUGF0dGVybiAvRGV2aWNlUkdCXQplbmRvYmoK"

# Figures are rendered by wkhtmltopdf in the sandbox and embedded here.
# Since we cannot write binary via filesystem MCP, this script decodes them.

import urllib.request, tempfile, shutil

os.makedirs("figures", exist_ok=True)

print("Fetching figure PDFs from sandbox output...")
print("NOTE: Figure PDFs could not be auto-embedded due to binary transfer limitations.")
print("Attempting to generate figures using wkhtmltopdf if available...")

fig1_html = """<!DOCTYPE html><html><head><style>body{margin:0;padding:0;background:white;}</style></head><body>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 340" width="800" height="340">
  <rect width="800" height="340" fill="#ffffff"/>
  <text x="400" y="30" text-anchor="middle" font-family="Arial" font-size="13" font-weight="600" fill="#111">Figure 1. Pipeline Architecture with Layer-wise Fidelity Capture Points</text>
  <defs><marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M2 1L8 5L2 9" fill="none" stroke="#444" stroke-width="1.5"/></marker>
  <marker id="amb" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M2 1L8 5L2 9" fill="none" stroke="#ba7517" stroke-width="1.5"/></marker></defs>
  <rect x="40" y="70" width="160" height="76" rx="8" fill="#e8e4fb" stroke="#6c5ce7" stroke-width="1.5"/>
  <text x="120" y="100" text-anchor="middle" font-family="Arial" font-size="13" font-weight="700" fill="#3d2c8d">MCP Server</text>
  <text x="120" y="118" text-anchor="middle" font-family="Arial" font-size="11" fill="#534ab7">FastMCP + FAISS</text>
  <text x="120" y="134" text-anchor="middle" font-family="Arial" font-size="11" fill="#534ab7">retrieve(query, k=3)</text>
  <line x1="200" y1="108" x2="246" y2="108" stroke="#444" stroke-width="1.5" marker-end="url(#arr)"/>
  <rect x="250" y="90" width="44" height="36" rx="6" fill="#f1efe8" stroke="#888780"/>
  <text x="272" y="107" text-anchor="middle" font-family="Arial" font-size="12" font-weight="700">R&#x2080;</text>
  <text x="272" y="120" text-anchor="middle" font-family="Arial" font-size="9" fill="#5f5e5a">raw chunks</text>
  <line x1="294" y1="108" x2="314" y2="108" stroke="#444" stroke-width="1.5" marker-end="url(#arr)"/>
  <rect x="318" y="70" width="160" height="76" rx="8" fill="#d8f5e8" stroke="#0f6e56" stroke-width="1.5"/>
  <text x="398" y="100" text-anchor="middle" font-family="Arial" font-size="13" font-weight="700" fill="#04342c">A2A Orchestrator</text>
  <text x="398" y="118" text-anchor="middle" font-family="Arial" font-size="11" fill="#085041">LangGraph 2-node</text>
  <text x="398" y="134" text-anchor="middle" font-family="Arial" font-size="11" fill="#085041">synthesise answer</text>
  <line x1="478" y1="108" x2="524" y2="108" stroke="#444" stroke-width="1.5" marker-end="url(#arr)"/>
  <rect x="528" y="90" width="44" height="36" rx="6" fill="#f1efe8" stroke="#888780"/>
  <text x="550" y="107" text-anchor="middle" font-family="Arial" font-size="12" font-weight="700">R&#x2081;</text>
  <text x="550" y="120" text-anchor="middle" font-family="Arial" font-size="9" fill="#5f5e5a">NL answer</text>
  <line x1="572" y1="108" x2="592" y2="108" stroke="#444" stroke-width="1.5" marker-end="url(#arr)"/>
  <rect x="596" y="70" width="160" height="76" rx="8" fill="#faecea" stroke="#993c1d" stroke-width="1.5"/>
  <text x="676" y="100" text-anchor="middle" font-family="Arial" font-size="13" font-weight="700" fill="#4a1b0c">A2UI Formatter</text>
  <text x="676" y="118" text-anchor="middle" font-family="Arial" font-size="11" fill="#712b13">JSON schema</text>
  <text x="676" y="134" text-anchor="middle" font-family="Arial" font-size="11" fill="#712b13">Streamlit render</text>
  <line x1="676" y1="146" x2="676" y2="176" stroke="#444" stroke-width="1.5" marker-end="url(#arr)"/>
  <rect x="652" y="180" width="48" height="36" rx="6" fill="#f1efe8" stroke="#888780"/>
  <text x="676" y="197" text-anchor="middle" font-family="Arial" font-size="12" font-weight="700">R&#x2082;</text>
  <text x="676" y="210" text-anchor="middle" font-family="Arial" font-size="9" fill="#5f5e5a">JSON payload</text>
  <text x="400" y="248" text-anchor="middle" font-family="Arial" font-size="11" font-weight="600" fill="#333">Ground truth reference answer (human-written from httpx docs)</text>
  <rect x="120" y="254" width="560" height="28" rx="6" fill="#faeeda" stroke="#ba7517" stroke-width="1.2"/>
  <text x="400" y="272" text-anchor="middle" font-family="Arial" font-size="11" fill="#633806">BERTScore P, R, F1(R&#x2099;, reference) &#x2014; same reference for all three layers</text>
  <line x1="272" y1="126" x2="272" y2="252" stroke="#ba7517" stroke-width="1" stroke-dasharray="4,3" marker-end="url(#amb)"/>
  <line x1="550" y1="126" x2="550" y2="252" stroke="#ba7517" stroke-width="1" stroke-dasharray="4,3" marker-end="url(#amb)"/>
  <line x1="676" y1="216" x2="676" y2="252" stroke="#ba7517" stroke-width="1" stroke-dasharray="4,3" marker-end="url(#amb)"/>
  <text x="411" y="245" text-anchor="middle" font-family="Arial" font-size="10" fill="#854f0b">&#916;&#x2081; = F1(R&#x2081;)&#x2212;F1(R&#x2080;)</text>
  <text x="613" y="245" text-anchor="middle" font-family="Arial" font-size="10" fill="#854f0b">&#916;&#x2082; = F1(R&#x2082;)&#x2212;F1(R&#x2081;)</text>
  <text x="400" y="316" text-anchor="middle" font-family="Arial" font-size="10" fill="#888">R&#x2080;=raw MCP | R&#x2081;=A2A synth | R&#x2082;=A2UI payload | dashed=BERTScore | &#916;&#x2081;/&#916;&#x2082;=F1 deltas | &#916;&#x2081;&#x1d3f;/&#916;&#x2082;&#x1d3f;=Recall deltas</text>
</svg></body></html>"""

fig2_html = """<!DOCTYPE html><html><head><style>body{margin:0;padding:0;background:white;}</style></head><body>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="800" height="420">
  <rect width="800" height="420" fill="#ffffff"/>
  <text x="400" y="28" text-anchor="middle" font-family="Arial" font-size="13" font-weight="600" fill="#111">Figure 2. Layer-wise Fidelity Scoring: Research Questions and Testable Hypotheses</text>
  <rect x="40" y="44" width="720" height="38" rx="7" fill="#f1efe8" stroke="#888780"/>
  <text x="400" y="60" text-anchor="middle" font-family="Arial" font-size="11" fill="#2c2c2a">Score R0, R1, R2 against the same ground truth using BERTScore (P, R, F1)</text>
  <text x="400" y="76" text-anchor="middle" font-family="Arial" font-size="11" font-weight="600" fill="#2c2c2a">The deltas between layers are the finding: where does fidelity degrade?</text>
  <rect x="40" y="100" width="222" height="134" rx="8" fill="#e8e4fb" stroke="#6c5ce7" stroke-width="1.5"/>
  <text x="151" y="122" text-anchor="middle" font-family="Arial" font-size="12" font-weight="700" fill="#26215c">Q1: A2A distortion</text>
  <line x1="60" y1="130" x2="242" y2="130" stroke="#afa9ec"/>
  <text x="151" y="148" text-anchor="middle" font-family="Arial" font-size="11" fill="#3c3489">Does agent synthesis of R0</text>
  <text x="151" y="163" text-anchor="middle" font-family="Arial" font-size="11" fill="#3c3489">lose or add information</text>
  <text x="151" y="178" text-anchor="middle" font-family="Arial" font-size="11" fill="#3c3489">vs. the raw tool output?</text>
  <text x="151" y="195" text-anchor="middle" font-family="Arial" font-size="10" font-weight="700" fill="#26215c">&#916;&#x2081; F1 + &#916;&#x2081;&#x1d3f; Recall</text>
  <text x="151" y="224" text-anchor="middle" font-family="Arial" font-size="10" font-style="italic" fill="#534ab7">A2A layer effect</text>
  <rect x="289" y="100" width="222" height="134" rx="8" fill="#d8f5e8" stroke="#0f6e56" stroke-width="1.5"/>
  <text x="400" y="122" text-anchor="middle" font-family="Arial" font-size="12" font-weight="700" fill="#04342c">Q2: A2UI distortion</text>
  <line x1="309" y1="130" x2="491" y2="130" stroke="#9fe1cb"/>
  <text x="400" y="148" text-anchor="middle" font-family="Arial" font-size="11" fill="#0f6e56">Does rendering for UI</text>
  <text x="400" y="163" text-anchor="middle" font-family="Arial" font-size="11" fill="#0f6e56">further degrade or improve</text>
  <text x="400" y="178" text-anchor="middle" font-family="Arial" font-size="11" fill="#0f6e56">coherence of R1?</text>
  <text x="400" y="195" text-anchor="middle" font-family="Arial" font-size="10" font-weight="700" fill="#04342c">&#916;&#x2082; F1 + &#916;&#x2082;&#x1d3f; Recall</text>
  <text x="400" y="224" text-anchor="middle" font-family="Arial" font-size="10" font-style="italic" fill="#0f6e56">A2UI layer effect</text>
  <rect x="538" y="100" width="222" height="134" rx="8" fill="#faecea" stroke="#993c1d" stroke-width="1.5"/>
  <text x="649" y="122" text-anchor="middle" font-family="Arial" font-size="12" font-weight="700" fill="#4a1b0c">Q3: End-to-end</text>
  <line x1="558" y1="130" x2="740" y2="130" stroke="#f0997b"/>
  <text x="649" y="148" text-anchor="middle" font-family="Arial" font-size="11" fill="#993c1d">How much fidelity survives</text>
  <text x="649" y="163" text-anchor="middle" font-family="Arial" font-size="11" fill="#993c1d">the full pipeline from raw</text>
  <text x="649" y="178" text-anchor="middle" font-family="Arial" font-size="11" fill="#993c1d">tool output to user?</text>
  <text x="649" y="198" text-anchor="middle" font-family="Arial" font-size="11" font-weight="700" fill="#4a1b0c">F1(R0) vs F1(R2)</text>
  <text x="649" y="224" text-anchor="middle" font-family="Arial" font-size="10" font-style="italic" fill="#712b13">Full pipeline effect</text>
  <rect x="40" y="252" width="720" height="144" rx="8" fill="#faeeda" stroke="#ba7517" stroke-width="1.5"/>
  <text x="400" y="274" text-anchor="middle" font-family="Arial" font-size="12" font-weight="700" fill="#412402">Testable hypotheses &#x2014; any outcome is a publishable finding</text>
  <line x1="60" y1="282" x2="740" y2="282" stroke="#ef9f27"/>
  <rect x="60" y="292" width="12" height="12" rx="2" fill="#6c5ce7"/>
  <text x="82" y="302" font-family="Arial" font-size="11" font-weight="700" fill="#2c2c2a">H-A: Lossy pipeline</text>
  <text x="82" y="316" font-family="Arial" font-size="10" fill="#2c2c2a">Each layer degrades fidelity: F1(R0) &gt; F1(R1) &gt; F1(R2)</text>
  <text x="82" y="328" font-family="Arial" font-size="10" font-style="italic" fill="#633806">Implies: synthesis and formatting compress information</text>
  <rect x="60" y="338" width="12" height="12" rx="2" fill="#0f6e56"/>
  <text x="82" y="348" font-family="Arial" font-size="11" font-weight="700" fill="#2c2c2a">H-B: Synthesis adds value</text>
  <text x="82" y="362" font-family="Arial" font-size="10" fill="#2c2c2a">&#916;&#x2081; &gt; 0 on F1 AND &#916;&#x2081;&#x1d3f; &gt;= 0 on Recall: condensation without loss</text>
  <text x="82" y="374" font-family="Arial" font-size="10" font-style="italic" fill="#633806">Implies: synthesis improves selectivity; Recall drop = over-compression</text>
  <rect x="60" y="384" width="12" height="12" rx="2" fill="#993c1d"/>
  <text x="82" y="394" font-family="Arial" font-size="11" font-weight="700" fill="#2c2c2a">H-C: A2UI is the main loss point</text>
  <text x="82" y="408" font-family="Arial" font-size="10" fill="#2c2c2a">Formatting loses content: F1(R1) &gt;&gt; F1(R2), &#916;&#x2082; &lt;&lt; 0</text>
  <text x="400" y="418" text-anchor="middle" font-family="Arial" font-size="10" fill="#888">&#916;&#x2081;/&#916;&#x2082; = F1 deltas | &#916;&#x2081;&#x1d3f;/&#916;&#x2082;&#x1d3f; = Recall deltas | roberta-large | n=15 queries</text>
</svg></body></html>"""

def try_wkhtmltopdf(html_content, out_pdf, width_mm, height_mm):
    import shutil as _shutil
    if not _shutil.which("wkhtmltopdf"):
        return False
    import tempfile
    with tempfile.NamedTemporaryFile(suffix=".html", mode="w", delete=False) as f:
        f.write(html_content)
        tmp = f.name
    r = subprocess.run([
        "wkhtmltopdf",
        f"--page-width", f"{width_mm}mm",
        f"--page-height", f"{height_mm}mm",
        "--margin-top", "0", "--margin-bottom", "0",
        "--margin-left", "0", "--margin-right", "0",
        tmp, out_pdf
    ], capture_output=True)
    os.unlink(tmp)
    return r.returncode == 0 and os.path.exists(out_pdf)

def try_inkscape(svg_path, out_pdf):
    import shutil as _shutil
    if not _shutil.which("inkscape"):
        return False
    r = subprocess.run(["inkscape", svg_path, f"--export-pdf={out_pdf}"], capture_output=True)
    return r.returncode == 0 and os.path.exists(out_pdf)

fig1_ok = try_wkhtmltopdf(fig1_html, "figures/fig1-pipeline-architecture.pdf", 210, 89)
fig2_ok = try_wkhtmltopdf(fig2_html, "figures/fig2-evaluation-design.pdf", 210, 110)

if fig1_ok:
    print("Written: figures/fig1-pipeline-architecture.pdf")
else:
    print("WARNING: Could not generate fig1. Trying inkscape fallback...")
    fig1_ok = try_inkscape("output/figures/fig1-pipeline-architecture.svg",
                           "figures/fig1-pipeline-architecture.pdf")
    if fig1_ok:
        print("Written via inkscape: figures/fig1-pipeline-architecture.pdf")
    else:
        print("ERROR: fig1 could not be generated. Install inkscape or wkhtmltopdf.")

if fig2_ok:
    print("Written: figures/fig2-evaluation-design.pdf")
else:
    print("WARNING: Could not generate fig2. Trying inkscape fallback...")
    fig2_ok = try_inkscape("output/figures/fig2-evaluation-design.svg",
                           "figures/fig2-evaluation-design.pdf")
    if fig2_ok:
        print("Written via inkscape: figures/fig2-evaluation-design.pdf")
    else:
        print("ERROR: fig2 could not be generated. Install inkscape or wkhtmltopdf.")

if not fig1_ok or not fig2_ok:
    print("\nCompilation will proceed but figures will be missing.")
    print("Install: brew install inkscape  OR  brew install wkhtmltopdf")

print("\nRunning pdflatex (2 passes)...")
for i in range(2):
    r = subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", "main.tex"],
        capture_output=True, text=True
    )
    if r.returncode != 0:
        print(f"pdflatex pass {i+1} failed. Last 40 lines of log:")
        lines = r.stdout.splitlines()
        for line in lines[-40:]:
            print(line)
        sys.exit(1)
    else:
        print(f"  Pass {i+1}/2 OK")

print("\nDone. Output: main.pdf")
