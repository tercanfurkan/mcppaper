#!/usr/bin/env python3
"""Generate Figure 1: Pipeline Architecture with Layer-wise Fidelity Capture Points."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import matplotlib.patheffects as pe

fig, ax = plt.subplots(figsize=(7.0, 3.4))
ax.set_xlim(0, 10)
ax.set_ylim(0, 4.6)
ax.axis('off')
fig.patch.set_facecolor('white')

# Professional palette — muted fills, strong borders
colors = {
    'mcp':    ('#e8e8f4', '#5555a0'),
    'a2a':    ('#e2f0ec', '#2a7a6a'),
    'a2ui':   ('#f4e4e4', '#993333'),
    'r_box':  ('#f0f0ea', '#888888'),
    'score':  ('#fdf6e3', '#c89000'),
    'ref':    ('#f5f5f5', '#aaaaaa'),
}

def box(x, y, w, h, key, lw=1.8, radius=0.08):
    fc, ec = colors[key]
    b = FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad={radius}",
                       facecolor=fc, edgecolor=ec, linewidth=lw)
    ax.add_patch(b)

def arrow(x1, y1, x2, y2, style='->', color='#555555', lw=1.5, ls='-'):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle=style, color=color, lw=lw,
                                linestyle=ls, mutation_scale=14))

# Row y-positions
row_main = 2.9   # main pipeline boxes
row_r = 3.05     # R boxes (slightly raised center)
row_score = 0.65 # scoring box
row_ref = 1.55   # reference text
row_r2 = 1.6     # R2 box

# ── Main pipeline: 3 boxes + 3 R-intermediates, all horizontal ──

# MCP Server
box(0.15, row_main - 0.15, 1.9, 1.3, 'mcp')
ax.text(1.1, row_main + 0.85, 'MCP Server', ha='center', fontsize=9,
        fontweight='bold', color=colors['mcp'][1])
ax.text(1.1, row_main + 0.48, 'FastMCP + FAISS', ha='center', fontsize=7,
        color='#555555')
ax.text(1.1, row_main + 0.18, 'retrieve(query, k=3)', ha='center', fontsize=6.5,
        color='#555555', family='monospace')

# R0
box(2.4, row_r, 0.65, 0.65, 'r_box', lw=1.2, radius=0.06)
ax.text(2.725, row_r + 0.42, r'$R_0$', ha='center', fontsize=9.5, fontweight='bold')
ax.text(2.725, row_r + 0.14, 'raw chunks', ha='center', fontsize=5.5, color='#777')

# A2A Orchestrator
box(3.4, row_main - 0.15, 2.1, 1.3, 'a2a')
ax.text(4.45, row_main + 0.85, 'A2A Orchestrator', ha='center', fontsize=9,
        fontweight='bold', color=colors['a2a'][1])
ax.text(4.45, row_main + 0.48, 'LangGraph 2-node', ha='center', fontsize=7,
        color='#555555')
ax.text(4.45, row_main + 0.18, 'synthesise answer', ha='center', fontsize=7,
        color='#555555')

# R1
box(5.85, row_r, 0.65, 0.65, 'r_box', lw=1.2, radius=0.06)
ax.text(6.175, row_r + 0.42, r'$R_1$', ha='center', fontsize=9.5, fontweight='bold')
ax.text(6.175, row_r + 0.14, 'NL answer', ha='center', fontsize=5.5, color='#777')

# A2UI Formatter
box(6.85, row_main - 0.15, 1.85, 1.3, 'a2ui')
ax.text(7.775, row_main + 0.85, 'A2UI Formatter', ha='center', fontsize=9,
        fontweight='bold', color=colors['a2ui'][1])
ax.text(7.775, row_main + 0.48, 'JSON schema', ha='center', fontsize=7,
        color='#555555')
ax.text(7.775, row_main + 0.18, 'Streamlit render', ha='center', fontsize=7,
        color='#555555')

# R2 — placed below A2UI to show output drops down
box(9.05, row_r, 0.65, 0.65, 'r_box', lw=1.2, radius=0.06)
ax.text(9.375, row_r + 0.42, r'$R_2$', ha='center', fontsize=9.5, fontweight='bold')
ax.text(9.375, row_r + 0.14, 'JSON payload', ha='center', fontsize=5.5, color='#777')

# ── Horizontal arrows ──
arrow(2.05, row_r + 0.33, 2.4, row_r + 0.33)
arrow(3.05, row_r + 0.33, 3.4, row_r + 0.33)
arrow(5.5, row_r + 0.33, 5.85, row_r + 0.33)
arrow(6.5, row_r + 0.33, 6.85, row_r + 0.33)
arrow(8.7, row_r + 0.33, 9.05, row_r + 0.33)

# ── Dashed scoring arrows (down from each R to scoring box) ──
dash_color = '#c89000'
for x in [2.725, 6.175, 9.375]:
    arrow(x, row_r - 0.02, x, row_score + 0.45, style='->', color=dash_color,
          lw=1.0, ls='--')

# ── Reference answer line ──
ax.text(5.0, row_ref, 'Ground-truth reference (human-written)',
        ha='center', fontsize=7, color='#999999', fontstyle='italic')

# ── BERTScore box ──
box(1.2, row_score - 0.1, 7.6, 0.48, 'score', lw=1.5, radius=0.06)
ax.text(5.0, row_score + 0.14,
        r'BERTScore  P, R, F1($R_n$, reference)  —  same reference for all three layers',
        ha='center', fontsize=7.5, color='#665500')

# ── Delta labels ──
ax.text(4.45, 2.15, r'$\Delta_1 = F1(R_1) - F1(R_0)$',
        ha='center', fontsize=7, color='#777777',
        bbox=dict(boxstyle='round,pad=0.15', fc='white', ec='#dddddd', lw=0.5))
ax.text(7.8, 2.15, r'$\Delta_2 = F1(R_2) - F1(R_1)$',
        ha='center', fontsize=7, color='#777777',
        bbox=dict(boxstyle='round,pad=0.15', fc='white', ec='#dddddd', lw=0.5))

plt.tight_layout(pad=0.05)
plt.savefig('figures/fig1-pipeline-architecture.png', bbox_inches='tight',
            pad_inches=0.03, dpi=300, facecolor='white')
plt.savefig('figures/fig1-pipeline-architecture.pdf', bbox_inches='tight',
            pad_inches=0.03, facecolor='white')
print("Figure 1 saved.")
