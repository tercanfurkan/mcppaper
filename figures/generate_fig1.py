#!/usr/bin/env python3
"""Generate Figure 1: Pipeline Architecture with Layer-wise Fidelity Capture Points."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(7.5, 4.2))
ax.set_xlim(0, 10)
ax.set_ylim(0, 5.5)
ax.axis('off')

# Colors
mcp_bg = '#d5d5f5'
mcp_border = '#6666bb'
a2a_bg = '#c5ede5'
a2a_border = '#22887a'
a2ui_bg = '#f5d5d5'
a2ui_border = '#8b3333'
r_bg = '#e8e8e0'
r_border = '#999999'
score_bg = '#fff3d0'
score_border = '#dda800'

def rounded_box(x, y, w, h, fc, ec, lw=1.5):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.12",
                         facecolor=fc, edgecolor=ec, linewidth=lw)
    ax.add_patch(box)
    return box

# --- Main pipeline boxes ---
# MCP Server
rounded_box(0.2, 3.2, 2.0, 1.5, mcp_bg, mcp_border, 2)
ax.text(1.2, 4.25, 'MCP Server', ha='center', va='center', fontsize=9, fontweight='bold', color=mcp_border)
ax.text(1.2, 3.85, 'FastMCP + FAISS', ha='center', va='center', fontsize=7, color='#444444')
ax.text(1.2, 3.55, 'retrieve(query, k=3)', ha='center', va='center', fontsize=7, color='#444444', family='monospace')

# R0 box
rounded_box(2.7, 3.55, 0.75, 0.8, r_bg, r_border)
ax.text(3.075, 4.05, r'$R_0$', ha='center', va='center', fontsize=10, fontweight='bold')
ax.text(3.075, 3.75, 'raw chunks', ha='center', va='center', fontsize=6, color='#777777')

# A2A Orchestrator
rounded_box(4.0, 3.2, 2.2, 1.5, a2a_bg, a2a_border, 2)
ax.text(5.1, 4.25, 'A2A Orchestrator', ha='center', va='center', fontsize=9, fontweight='bold', color='#1a6b60')
ax.text(5.1, 3.85, 'LangGraph 2-node', ha='center', va='center', fontsize=7, color='#444444')
ax.text(5.1, 3.55, 'synthesise answer', ha='center', va='center', fontsize=7, color='#444444')

# R1 box
rounded_box(6.7, 3.55, 0.75, 0.8, r_bg, r_border)
ax.text(7.075, 4.05, r'$R_1$', ha='center', va='center', fontsize=10, fontweight='bold')
ax.text(7.075, 3.75, 'NL answer', ha='center', va='center', fontsize=6, color='#777777')

# A2UI Formatter
rounded_box(7.9, 3.2, 1.9, 1.5, a2ui_bg, a2ui_border, 2)
ax.text(8.85, 4.25, 'A2UI Formatter', ha='center', va='center', fontsize=9, fontweight='bold', color=a2ui_border)
ax.text(8.85, 3.85, 'JSON schema', ha='center', va='center', fontsize=7, color='#444444')
ax.text(8.85, 3.55, 'Streamlit render', ha='center', va='center', fontsize=7, color='#444444')

# R2 box (below A2UI)
rounded_box(8.5, 2.05, 0.75, 0.8, r_bg, r_border)
ax.text(8.875, 2.55, r'$R_2$', ha='center', va='center', fontsize=10, fontweight='bold')
ax.text(8.875, 2.25, 'JSON payload', ha='center', va='center', fontsize=6, color='#777777')

# --- Arrows ---
arrow_kw = dict(arrowstyle='->', color='#666666', lw=1.5, mutation_scale=15)
# MCP -> R0
ax.annotate('', xy=(2.7, 3.95), xytext=(2.2, 3.95), arrowprops=arrow_kw)
# R0 -> A2A
ax.annotate('', xy=(4.0, 3.95), xytext=(3.45, 3.95), arrowprops=arrow_kw)
# A2A -> R1
ax.annotate('', xy=(6.7, 3.95), xytext=(6.2, 3.95), arrowprops=arrow_kw)
# R1 -> A2UI
ax.annotate('', xy=(7.9, 3.95), xytext=(7.45, 3.95), arrowprops=arrow_kw)
# A2UI -> R2 (downward)
ax.annotate('', xy=(8.875, 2.85), xytext=(8.875, 3.2), arrowprops=arrow_kw)

# --- Dashed scoring arrows (amber) ---
dash_kw = dict(arrowstyle='->', color='#dda800', lw=1.2, linestyle='dashed', mutation_scale=12)

# R0 dashed down
ax.annotate('', xy=(3.075, 1.45), xytext=(3.075, 3.55), arrowprops=dash_kw)
# R1 dashed down
ax.annotate('', xy=(7.075, 1.45), xytext=(7.075, 3.55), arrowprops=dash_kw)
# R2 dashed down
ax.annotate('', xy=(8.875, 1.45), xytext=(8.875, 2.05), arrowprops=dash_kw)

# --- Ground truth + BERTScore box ---
ax.text(5.5, 1.85, 'Ground truth reference answer (human-written from httpx docs)',
        ha='center', va='center', fontsize=6.5, color='#666666')

rounded_box(1.5, 0.9, 7.5, 0.55, score_bg, score_border, 1.5)
ax.text(5.25, 1.18, r'BERTScore P, R, F1($R_n$, reference) — same reference for all three layers',
        ha='center', va='center', fontsize=7.5)

# --- Delta labels ---
ax.text(5.1, 2.6, r'$\Delta_1 = F1(R_1) - F1(R_0)$',
        ha='center', va='center', fontsize=7, color='#666666')
ax.text(9.6, 2.6, r'$\Delta_2 = F1(R_2) - F1(R_1)$',
        ha='left', va='center', fontsize=7, color='#666666')

# --- Legend ---
ax.text(5.0, 0.35,
        r'$R_0$=raw MCP | $R_1$=A2A synth | $R_2$=A2UI payload | dashed=BERTScore | $\Delta_1/\Delta_2$=F1 deltas | $\Delta_1^R/\Delta_2^R$=Recall deltas',
        ha='center', va='center', fontsize=5.5, color='#aaaaaa')

plt.tight_layout(pad=0.1)
plt.savefig('figures/fig1-pipeline-architecture.pdf', bbox_inches='tight', pad_inches=0.05)
plt.savefig('figures/fig1-pipeline-architecture.png', bbox_inches='tight', pad_inches=0.05, dpi=200)
print("Figure 1 saved.")
