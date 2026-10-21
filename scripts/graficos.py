"""Gera os gráficos dos slides a partir da Tabela 2 de Abensur (2012).

Nenhum dado é criado aqui: tudo sai de dados/tabela2.csv (transcrição da
Tabela 2) ou das Tabelas 3 e 5 do artigo.

Uso: python scripts/graficos.py   (a partir da raiz do projeto)
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import font_manager

RAIZ = Path(__file__).resolve().parents[1]
IMG = RAIZ / "img"
IMG.mkdir(exist_ok=True)

for f in (RAIZ / "fonts").glob("*.otf"):
    font_manager.fontManager.addfont(str(f))

VERDE = "#2E7D3A"
VERDE_ESCURO = "#1E4D35"
CINZA = "#B8BDB9"
TINTA = "#1F2421"
TINTA_2 = "#5B635E"

plt.rcParams.update({
    "font.family": "Inter",
    "font.size": 13,
    "axes.edgecolor": "#C9CEC9",
    "axes.labelcolor": TINTA_2,
    "xtick.color": TINTA_2,
    "ytick.color": TINTA_2,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "svg.fonttype": "path",
})

d = pd.read_csv(RAIZ / "dados" / "tabela2.csv")
PROPOSTO = [10, 12, 28, 35, 45]


def br(x, casas=0):
    s = f"{x:,.{casas}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


# 1. Investimento das carteiras x orçamento (Tabela 3)
fig, ax = plt.subplots(figsize=(7.2, 3.0))
nomes = ["Só IL", "Modelo proposto"]
valores = [355_685, 149_705]
cores = [CINZA, VERDE]
y = np.arange(len(nomes))
ax.barh(y, valores, color=cores, height=0.52)
for yi, v, c in zip(y, valores, cores):
    ax.text(v + 6_000, yi, f"R$ {br(v)}", va="center", fontsize=14,
            color=TINTA, fontweight="semibold")
ax.axvline(452_000, color=TINTA_2, lw=1.4, ls=(0, (4, 3)))
ax.text(438_000, 1.62, "orçamento\nR$ 452.000", ha="right", va="bottom",
        fontsize=11.5, color=TINTA_2)
ax.set_yticks(y, nomes, fontsize=14, color=TINTA)
ax.set_xlim(0, 500_000)
ax.set_ylim(-0.5, 2.2)
ax.xaxis.set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.tick_params(left=False)
fig.tight_layout()
fig.savefig(IMG / "g1-investimento.svg", transparent=True)
plt.close(fig)

# 2. IL x GA_FT dos 45 projetos (Tabela 2)
r = d["il"].corr(d["gaft"])
fig, ax = plt.subplots(figsize=(6.4, 4.6))
outros = d[~d.projeto.isin(PROPOSTO)]
sel = d[d.projeto.isin(PROPOSTO)]
ax.scatter(outros.il, outros.gaft, s=46, color=CINZA, edgecolor="white",
           linewidth=1.2, zorder=2, label="demais projetos")
ax.scatter(sel.il, sel.gaft, s=70, color=VERDE, edgecolor="white",
           linewidth=1.2, zorder=3, label="escolhidos pelo modelo")
desloc = {10: (8, -14), 12: (-34, 6), 28: (-28, 8), 35: (8, -12), 45: (8, -10)}
for _, row in sel.iterrows():
    dx, dy = desloc[int(row.projeto)]
    ax.annotate(f"P{int(row.projeto)}", (row.il, row.gaft), xytext=(dx, dy),
                textcoords="offset points", fontsize=11.5, color=VERDE_ESCURO,
                fontweight="semibold")
ax.set_xlabel("IL (%)")
ax.set_ylabel("GA$_{FT}$ (%)")
ax.grid(color="#E6E9E6", lw=0.8, zorder=0)
ax.set_axisbelow(True)
ax.text(0.03, 0.95, f"r = {br(r, 2)}", transform=ax.transAxes, fontsize=17,
        fontweight="bold", color=TINTA, va="top")
ax.legend(loc="lower right", frameon=False, fontsize=11.5)
fig.tight_layout()
fig.savefig(IMG / "g2-il-gaft.svg", transparent=True)
plt.close(fig)

print(f"correlação IL x GA_FT = {r:.4f}")
