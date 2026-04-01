# Layer-Wise Fidelity Evaluation of Multi-Layer Agentic AI Pipelines: MCP, A2A, and A2UI

IEEE Computer Society journal paper proposing **layer-wise fidelity scoring** for multi-layer agentic pipelines built on MCP, A2A, and A2UI protocols.

The evaluation prototype, annotated test set (n=30), and scoring harness live in the companion repository: **[fidelity-agentic-stack](https://github.com/tercanfurkan/fidelity-agentic-stack)**.

## Building

```bash
latexmk -pdf main.tex    # or: pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
```

Requires a LaTeX distribution ([MacTeX](https://www.tug.org/mactex/), TeX Live, or MiKTeX).

## Regenerating Figures

```bash
python3 figures/generate_fig1.py   # Pipeline architecture
python3 figures/generate_fig2.py   # Evaluation design
```

Requires `matplotlib`.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
