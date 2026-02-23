# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is an academic paper on the **Model Context Protocol (MCP)** written in LaTeX, formatted for IEEE Computer Society journals using the `IEEEtran` class.

## Building the Paper

```bash
# Full build with bibliography
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex

# Or with latexmk (recommended)
latexmk -pdf main.tex

# Clean build artifacts
latexmk -C
```

The output is `main.pdf`.

## Regenerating the Architecture Diagram

The figure is pre-rendered (`figures/mcp_architecture.pdf` / `.png`). To regenerate it:

```bash
python3 figures/generate_architecture.py
```

Requires `matplotlib`. To also rebuild from TikZ source:

```bash
pdflatex figures/mcp_architecture.tex
```

## Repository Structure

- `main.tex` — the paper; single-file, all sections inline
- `source.tex` — the original unmodified IEEE IEEEtran template (`bare_jrnl_compsoc.tex v1.4b`), kept for reference
- `figures/` — diagram assets and their sources
  - `mcp_architecture.pdf/.png` — figure included in the paper
  - `mcp_architecture.tex` — standalone TikZ source for the same diagram
  - `generate_architecture.py` — matplotlib script that produces the PDF/PNG
- `papers/` — reference PDFs and notes

## LaTeX Conventions

- Document class: `\documentclass[10pt,journal,compsoc]{IEEEtran}`
- Graphics path is set to `./figures/` — reference figures by name only (e.g., `\includegraphics{mcp_architecture}`)
- Bibliography is inline (`thebibliography` environment), not a separate `.bib` file
- The abstract and keywords must be placed inside `\IEEEtitleabstractindextext{}` before `\maketitle` — this is a `compsoc` journal requirement
- The first section heading uses `\IEEEraisesectionheading{\section{...}}` per IEEE CS style
