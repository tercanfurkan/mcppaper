#!/usr/bin/env python3
"""Generate Figure 2: Layer-wise Fidelity Scoring — Research Questions and Testable Hypotheses."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig, ax = plt.subplots(figsize=(7.5, 5.8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 7.2)
ax.axis('off')

# Colors
mcp_bg = '#ededf8'
mcp_border = '#9999cc'
a2a_bg = '#d8f5ef'
a2a_border = '#33aa99'
a2ui_bg = '#fde0e0'
a2ui_border = '#cc4444'
hyp_bg = '#fff6dc'
hyp_border = '#dda800'
top_bg = '#f5f5f0'
top_border = '#bbbbbb'

def rounded_box(x, y, w, h, fc, ec, lw=1.5):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.15",
                         facecolor=fc, edgecolor=ec, linewidth=lw)
    ax.add_patch(box)

# === Top banner ===
rounded_box(0.8, 6.0, 8.4, 0.9, top_bg, top_border, 1.2)
ax.text(5.0, 6.65, 'Score R0, R1, R2 against the same ground truth using BERTScore (P, R, F1)',
        ha='center', va='center', fontsize=7.5)
ax.text(5.0, 6.3, 'The deltas between layers are the finding: where does fidelity degrade?',
        ha='center', va='center', fontsize=7, color='#666666')

# === Three Q boxes ===
qw, qh = 2.6, 2.0

# Q1
rounded_box(0.3, 3.6, qw, qh, mcp_bg, mcp_border, 1.8)
ax.text(1.6, 5.25, 'Q1: A2A distortion', ha='center', va='center', fontsize=8.5, fontweight='bold', color='#444444')
ax.plot([0.55, 2.65], [5.08, 5.08], color=mcp_border, lw=0.8)
ax.text(1.6, 4.75, 'Does agent synthesis of R0', ha='center', va='center', fontsize=6.5, color='#555555')
ax.text(1.6, 4.48, 'lose or add information', ha='center', va='center', fontsize=6.5, color='#555555')
ax.text(1.6, 4.21, 'vs. the raw tool output?', ha='center', va='center', fontsize=6.5, color='#555555')
ax.text(1.6, 3.88, r'$\Delta_1$ F1 + $\Delta_1^R$ Recall', ha='center', va='center', fontsize=7.5, fontweight='bold')
ax.text(1.6, 3.58, 'A2A layer effect', ha='center', va='center', fontsize=6.5, fontstyle='italic', color='#888888')

# Q2
rounded_box(3.7, 3.6, qw, qh, a2a_bg, a2a_border, 1.8)
ax.text(5.0, 5.25, 'Q2: A2UI distortion', ha='center', va='center', fontsize=8.5, fontweight='bold', color='#444444')
ax.plot([3.95, 6.05], [5.08, 5.08], color=a2a_border, lw=0.8)
ax.text(5.0, 4.75, 'Does rendering for UI', ha='center', va='center', fontsize=6.5, color='#555555')
ax.text(5.0, 4.48, 'further degrade or improve', ha='center', va='center', fontsize=6.5, color='#555555')
ax.text(5.0, 4.21, 'coherence of R1?', ha='center', va='center', fontsize=6.5, color='#555555')
ax.text(5.0, 3.88, r'$\Delta_2$ F1 + $\Delta_2^R$ Recall', ha='center', va='center', fontsize=7.5, fontweight='bold')
ax.text(5.0, 3.58, 'A2UI layer effect', ha='center', va='center', fontsize=6.5, fontstyle='italic', color='#888888')

# Q3
rounded_box(7.1, 3.6, qw, qh, a2ui_bg, a2ui_border, 1.8)
ax.text(8.4, 5.25, 'Q3: End-to-end', ha='center', va='center', fontsize=8.5, fontweight='bold', color='#444444')
ax.plot([7.35, 9.45], [5.08, 5.08], color=a2ui_border, lw=0.8)
ax.text(8.4, 4.75, 'How much fidelity survives', ha='center', va='center', fontsize=6.5, color='#555555')
ax.text(8.4, 4.48, 'the full pipeline from raw', ha='center', va='center', fontsize=6.5, color='#555555')
ax.text(8.4, 4.21, 'tool output to user?', ha='center', va='center', fontsize=6.5, color='#555555')
ax.text(8.4, 3.88, 'F1(R0) vs F1(R2)', ha='center', va='center', fontsize=7.5, fontweight='bold')
ax.text(8.4, 3.58, 'Full pipeline effect', ha='center', va='center', fontsize=6.5, fontstyle='italic', color='#888888')

# === Hypotheses box ===
rounded_box(0.3, 0.35, 9.4, 2.9, hyp_bg, hyp_border, 1.8)

ax.text(5.0, 3.0, 'Testable hypotheses — any outcome is a publishable finding',
        ha='center', va='center', fontsize=8.5, fontweight='bold', color='#996600')
ax.plot([0.55, 9.45], [2.78, 2.78], color=hyp_border, lw=1.0)

# H-A
sq_ha = FancyBboxPatch((0.7, 2.28), 0.28, 0.28, boxstyle="round,pad=0.02",
                        facecolor=mcp_border, edgecolor='none')
ax.add_patch(sq_ha)
ax.text(1.2, 2.48, 'H-A: Lossy pipeline', va='center', fontsize=7.5, fontweight='bold')
ax.text(1.2, 2.2, 'Each layer degrades fidelity: F1(R0) > F1(R1) > F1(R2)', va='center', fontsize=6.5)
ax.text(1.2, 1.95, 'Implies: synthesis and formatting compress information',
        va='center', fontsize=6.5, fontstyle='italic', color='#888888')

# H-B
sq_hb = FancyBboxPatch((0.7, 1.45), 0.28, 0.28, boxstyle="round,pad=0.02",
                        facecolor=a2a_border, edgecolor='none')
ax.add_patch(sq_hb)
ax.text(1.2, 1.65, 'H-B: Synthesis adds value', va='center', fontsize=7.5, fontweight='bold')
ax.text(1.2, 1.38, r'$\Delta_1$ > 0 on F1 AND $\Delta_1^R$ >= 0 on Recall: condensation without loss',
        va='center', fontsize=6.5)
ax.text(1.2, 1.12, 'Implies: synthesis improves selectivity; Recall drop = over-compression',
        va='center', fontsize=6.5, fontstyle='italic', color='#888888')

# H-C
sq_hc = FancyBboxPatch((0.7, 0.65), 0.28, 0.28, boxstyle="round,pad=0.02",
                        facecolor='#8b4513', edgecolor='none')
ax.add_patch(sq_hc)
ax.text(1.2, 0.85, 'H-C: A2UI is the main loss point', va='center', fontsize=7.5, fontweight='bold')
ax.text(1.2, 0.58, r'Formatting loses content: F1(R1) >> F1(R2), $\Delta_2$ << 0',
        va='center', fontsize=6.5)

# Legend at bottom
ax.text(5.0, 0.1,
        r'$\Delta_1/\Delta_2$ = F1 deltas | $\Delta_1^R/\Delta_2^R$ = Recall deltas | roberta-large | n=15 queries',
        ha='center', va='center', fontsize=5.5, color='#aaaaaa')

plt.tight_layout(pad=0.1)
plt.savefig('figures/fig2-evaluation-design.pdf', bbox_inches='tight', pad_inches=0.05)
plt.savefig('figures/fig2-evaluation-design.png', bbox_inches='tight', pad_inches=0.05, dpi=200)
print("Figure 2 saved.")
