#!/usr/bin/env python3
"""Generate Figure 2: Layer-wise Fidelity Scoring — Research Questions and Testable Hypotheses."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig, ax = plt.subplots(figsize=(7.0, 5.2))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6.8)
ax.axis('off')
fig.patch.set_facecolor('white')

# Professional palette
colors = {
    'top':    ('#f5f5f0', '#aaaaaa'),
    'q1':     ('#e8e8f4', '#5555a0'),
    'q2':     ('#e2f0ec', '#2a7a6a'),
    'q3':     ('#f4e4e4', '#993333'),
    'hyp':    ('#fdf6e3', '#c89000'),
    'ha':     '#6666a0',
    'hb':     '#2a7a6a',
    'hc':     '#884422',
}

def box(x, y, w, h, key, lw=1.8, radius=0.12):
    fc, ec = colors[key]
    b = FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad={radius}",
                       facecolor=fc, edgecolor=ec, linewidth=lw)
    ax.add_patch(b)

# ═══ Top banner ═══
box(0.5, 5.8, 9.0, 0.8, 'top', lw=1.2)
ax.text(5.0, 6.38, 'Score $R_0$, $R_1$, $R_2$ against the same ground truth using BERTScore (P, R, F1)',
        ha='center', fontsize=8.5, fontweight='bold', color='#444444')
ax.text(5.0, 6.02, 'The deltas between layers are the finding: where does fidelity degrade?',
        ha='center', fontsize=8, color='#777777')

# ═══ Three research question boxes ═══
qw, qh = 2.7, 2.15
qy = 3.3
gap = 0.3

# Q1
q1x = 0.35
box(q1x, qy, qw, qh, 'q1')
ax.text(q1x + qw/2, qy + qh - 0.3, 'Q1: A2A distortion', ha='center',
        fontsize=9.5, fontweight='bold', color='#444444')
ax.plot([q1x + 0.2, q1x + qw - 0.2], [qy + qh - 0.48, qy + qh - 0.48],
        color=colors['q1'][1], lw=0.8, alpha=0.5)
ax.text(q1x + qw/2, qy + qh - 0.78, 'Does agent synthesis of $R_0$',
        ha='center', fontsize=8, color='#555555')
ax.text(q1x + qw/2, qy + qh - 1.05, 'lose or add information',
        ha='center', fontsize=8, color='#555555')
ax.text(q1x + qw/2, qy + qh - 1.32, 'vs. the raw tool output?',
        ha='center', fontsize=8, color='#555555')
ax.text(q1x + qw/2, qy + 0.48, r'$\Delta_1$ F1  +  $\Delta_1^R$ Recall',
        ha='center', fontsize=9, fontweight='bold', color='#333333')
ax.text(q1x + qw/2, qy + 0.15, 'A2A layer effect',
        ha='center', fontsize=7.5, fontstyle='italic', color='#999999')

# Q2
q2x = q1x + qw + gap
box(q2x, qy, qw, qh, 'q2')
ax.text(q2x + qw/2, qy + qh - 0.3, 'Q2: A2UI distortion', ha='center',
        fontsize=9.5, fontweight='bold', color='#444444')
ax.plot([q2x + 0.2, q2x + qw - 0.2], [qy + qh - 0.48, qy + qh - 0.48],
        color=colors['q2'][1], lw=0.8, alpha=0.5)
ax.text(q2x + qw/2, qy + qh - 0.78, 'Does rendering for UI',
        ha='center', fontsize=8, color='#555555')
ax.text(q2x + qw/2, qy + qh - 1.05, 'further degrade or improve',
        ha='center', fontsize=8, color='#555555')
ax.text(q2x + qw/2, qy + qh - 1.32, 'coherence of $R_1$?',
        ha='center', fontsize=8, color='#555555')
ax.text(q2x + qw/2, qy + 0.48, r'$\Delta_2$ F1  +  $\Delta_2^R$ Recall',
        ha='center', fontsize=9, fontweight='bold', color='#333333')
ax.text(q2x + qw/2, qy + 0.15, 'A2UI layer effect',
        ha='center', fontsize=7.5, fontstyle='italic', color='#999999')

# Q3
q3x = q2x + qw + gap
box(q3x, qy, qw, qh, 'q3')
ax.text(q3x + qw/2, qy + qh - 0.3, 'Q3: End-to-end', ha='center',
        fontsize=9.5, fontweight='bold', color='#444444')
ax.plot([q3x + 0.2, q3x + qw - 0.2], [qy + qh - 0.48, qy + qh - 0.48],
        color=colors['q3'][1], lw=0.8, alpha=0.5)
ax.text(q3x + qw/2, qy + qh - 0.78, 'How much fidelity survives',
        ha='center', fontsize=8, color='#555555')
ax.text(q3x + qw/2, qy + qh - 1.05, 'the full pipeline from raw',
        ha='center', fontsize=8, color='#555555')
ax.text(q3x + qw/2, qy + qh - 1.32, 'tool output to user?',
        ha='center', fontsize=8, color='#555555')
ax.text(q3x + qw/2, qy + 0.48, 'F1($R_0$) vs F1($R_2$)',
        ha='center', fontsize=9, fontweight='bold', color='#333333')
ax.text(q3x + qw/2, qy + 0.15, 'Full pipeline effect',
        ha='center', fontsize=7.5, fontstyle='italic', color='#999999')

# ═══ Hypotheses box ═══
hy = 0.15
hh = 2.85
box(0.35, hy, 9.3, hh, 'hyp')

ax.text(5.0, hy + hh - 0.3,
        'Testable hypotheses — any outcome is a publishable finding',
        ha='center', fontsize=9.5, fontweight='bold', color='#8a6d00')
ax.plot([0.6, 9.4], [hy + hh - 0.52, hy + hh - 0.52],
        color=colors['hyp'][1], lw=1.0, alpha=0.6)

# H-A
ya = hy + hh - 0.85
sq = FancyBboxPatch((0.7, ya - 0.05), 0.3, 0.3, boxstyle="round,pad=0.02",
                     facecolor=colors['ha'], edgecolor='none')
ax.add_patch(sq)
ax.text(1.25, ya + 0.15, 'H-A: Lossy pipeline', fontsize=8.5, fontweight='bold',
        va='center', color='#333333')
ax.text(1.25, ya - 0.12, 'Each layer degrades fidelity:  F1($R_0$) > F1($R_1$) > F1($R_2$)',
        fontsize=7.5, va='center', color='#555555')
ax.text(1.25, ya - 0.38, 'Implies: synthesis and formatting compress information',
        fontsize=7.5, va='center', fontstyle='italic', color='#999999')

# H-B
yb = ya - 0.95
sq2 = FancyBboxPatch((0.7, yb - 0.05), 0.3, 0.3, boxstyle="round,pad=0.02",
                      facecolor=colors['hb'], edgecolor='none')
ax.add_patch(sq2)
ax.text(1.25, yb + 0.15, 'H-B: Synthesis adds value', fontsize=8.5,
        fontweight='bold', va='center', color='#333333')
ax.text(1.25, yb - 0.12,
        r'$\Delta_1 > 0$ on F1 AND $\Delta_1^R \geq 0$ on Recall: condensation without loss',
        fontsize=7.5, va='center', color='#555555')
ax.text(1.25, yb - 0.38,
        'Implies: synthesis improves selectivity; Recall drop = over-compression',
        fontsize=7.5, va='center', fontstyle='italic', color='#999999')

# H-C
yc = yb - 0.95
sq3 = FancyBboxPatch((0.7, yc - 0.05), 0.3, 0.3, boxstyle="round,pad=0.02",
                      facecolor=colors['hc'], edgecolor='none')
ax.add_patch(sq3)
ax.text(1.25, yc + 0.15, 'H-C: A2UI is the main loss point', fontsize=8.5,
        fontweight='bold', va='center', color='#333333')
ax.text(1.25, yc - 0.12,
        r'Formatting loses content:  F1($R_1$) $\gg$ F1($R_2$),  $\Delta_2 \ll 0$',
        fontsize=7.5, va='center', color='#555555')

plt.tight_layout(pad=0.05)
plt.savefig('figures/fig2-evaluation-design.png', bbox_inches='tight',
            pad_inches=0.03, dpi=300, facecolor='white')
plt.savefig('figures/fig2-evaluation-design.pdf', bbox_inches='tight',
            pad_inches=0.03, facecolor='white')
print("Figure 2 saved.")
