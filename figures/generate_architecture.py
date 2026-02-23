"""
Generate the MCP architecture diagram for the IEEE paper.
Produces: mcp_architecture.pdf and mcp_architecture.png
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis("off")

# ── colour palette ──────────────────────────────────────────────────────────
C_HOST   = "#D6EAF8"   # light blue
C_CLIENT = "#D5F5E3"   # light green
C_SERVER = "#FDEBD0"   # light orange
C_BORDER = "#2C3E50"
C_ARROW  = "#5D6D7E"

def box(ax, x, y, w, h, label, sublabel=None, color="#FFFFFF", fontsize=10):
    rect = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.08",
        linewidth=1.4,
        edgecolor=C_BORDER,
        facecolor=color,
        zorder=2,
    )
    ax.add_patch(rect)
    cy = y + h / 2 + (0.15 if sublabel else 0)
    ax.text(x + w / 2, cy, label,
            ha="center", va="center", fontsize=fontsize,
            fontweight="bold", color=C_BORDER, zorder=3)
    if sublabel:
        ax.text(x + w / 2, y + h / 2 - 0.22, sublabel,
                ha="center", va="center", fontsize=7.5,
                color="#5D6D7E", style="italic", zorder=3)

def arrow(ax, x1, y1, x2, y2, label="", bidirectional=True):
    style = "<->" if bidirectional else "->"
    ax.annotate(
        "", xy=(x2, y2), xytext=(x1, y1),
        arrowprops=dict(
            arrowstyle=style,
            color=C_ARROW,
            lw=1.5,
            connectionstyle="arc3,rad=0.0",
        ),
        zorder=1,
    )
    if label:
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        ax.text(mx + 0.05, my + 0.18, label,
                fontsize=7.5, color=C_ARROW, ha="center", zorder=4)

# ── HOST outer boundary ──────────────────────────────────────────────────────
host_bg = FancyBboxPatch(
    (0.3, 0.4), 9.4, 5.3,
    boxstyle="round,pad=0.15",
    linewidth=2,
    edgecolor="#1A5276",
    facecolor=C_HOST,
    alpha=0.35,
    zorder=0,
)
ax.add_patch(host_bg)
ax.text(5.0, 5.55, "Host  (e.g. Claude Desktop, IDE Plugin, Agent Framework)",
        ha="center", va="center", fontsize=9, color="#1A5276", fontweight="bold")

# ── LLM box ──────────────────────────────────────────────────────────────────
box(ax, 3.8, 4.0, 2.4, 0.95, "LLM", "Large Language Model", color="#EBF5FB", fontsize=9)

# ── Client boxes ─────────────────────────────────────────────────────────────
box(ax, 1.0, 2.2, 2.2, 0.85, "MCP Client A", color=C_CLIENT, fontsize=9)
box(ax, 3.9, 2.2, 2.2, 0.85, "MCP Client B", color=C_CLIENT, fontsize=9)
box(ax, 6.8, 2.2, 2.2, 0.85, "MCP Client C", color=C_CLIENT, fontsize=9)

# ── LLM <-> Clients ──────────────────────────────────────────────────────────
arrow(ax, 5.0, 4.0,  2.1, 3.05, "tool calls / results")
arrow(ax, 5.0, 4.0,  5.0, 3.05)
arrow(ax, 5.0, 4.0,  7.9, 3.05)

# ── Server boxes ─────────────────────────────────────────────────────────────
box(ax, 0.5, 0.65, 2.2, 0.95, "MCP Server A", "Filesystem / Git", color=C_SERVER, fontsize=8.5)
box(ax, 3.4, 0.65, 2.2, 0.95, "MCP Server B", "Database / Search", color=C_SERVER, fontsize=8.5)
box(ax, 6.8, 0.65, 2.2, 0.95, "MCP Server C", "Cloud / API", color=C_SERVER, fontsize=8.5)

# ── Client <-> Server ────────────────────────────────────────────────────────
arrow(ax, 2.1, 2.2,  1.6, 1.60, "JSON-RPC 2.0\n(stdio / SSE)")
arrow(ax, 5.0, 2.2,  4.5, 1.60, "JSON-RPC 2.0\n(stdio / SSE)")
arrow(ax, 7.9, 2.2,  7.9, 1.60, "JSON-RPC 2.0\n(stdio / SSE)")

# ── Protocol label band ──────────────────────────────────────────────────────
band = FancyBboxPatch(
    (0.5, 1.62), 9.0, 0.52,
    boxstyle="round,pad=0.05",
    linewidth=0,
    facecolor="#F0F3F4",
    edgecolor="#BDC3C7",
    zorder=1,
    alpha=0.7,
)
ax.add_patch(band)
ax.text(5.0, 1.88,
        "MCP Protocol Layer  ·  JSON-RPC 2.0  ·  Transport: stdio  |  HTTP+SSE",
        ha="center", va="center", fontsize=8, color="#5D6D7E")

# ── Legend ───────────────────────────────────────────────────────────────────
legend_items = [
    mpatches.Patch(facecolor=C_HOST,   edgecolor=C_BORDER, label="Host environment"),
    mpatches.Patch(facecolor=C_CLIENT, edgecolor=C_BORDER, label="MCP Client"),
    mpatches.Patch(facecolor=C_SERVER, edgecolor=C_BORDER, label="MCP Server"),
]
ax.legend(handles=legend_items, loc="lower right",
          fontsize=8, framealpha=0.8, edgecolor=C_BORDER)

plt.tight_layout(pad=0.3)

out_dir = "/Users/furkan/mcppaper/figures"
plt.savefig(f"{out_dir}/mcp_architecture.pdf", dpi=300, bbox_inches="tight")
plt.savefig(f"{out_dir}/mcp_architecture.png", dpi=300, bbox_inches="tight")
print("Saved mcp_architecture.pdf and mcp_architecture.png")
