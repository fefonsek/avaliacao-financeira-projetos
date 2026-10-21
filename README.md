# Apresentação: Abensur (2012), orçamento de capital multiobjetivo

Slides em Quarto (revealjs) para a disciplina **Avaliação Financeira de Projetos**, Prof. Cleiton Martins Duarte Silva, Mestrado Profissional em Administração, IFMG Campus Formiga.

**Artigo:** ABENSUR, E. O. Um modelo multiobjetivo de otimização aplicado ao processo de orçamento de capital. *Gestão & Produção*, São Carlos, v. 19, n. 4, p. 747-758, 2012.
DOI: <https://doi.org/10.1590/S0104-530X2012000400007>

**Apresentação:** Felipe Luiz Fonseca, 21/10/2026.

## Como usar os slides

- Abra `docs/index.html` no navegador. O arquivo é autocontido: funciona sem internet.
- Tecla **S**: abre a visão do apresentador, com as notas de fala e o cronômetro.
- Tecla **F**: tela cheia. Tecla **M**: menu de slides. Tecla **Esc**: visão geral.

## Estrutura

| Pasta ou arquivo | Conteúdo |
|---|---|
| `index.qmd` | Slides e notas de fala |
| `_apendice.qmd` | Tabela 2 completa (gerada por script) |
| `ifmg.scss`, `fonts.css`, `fonts/` | Tema visual (paleta PPGA IFMG, fonte Inter, licença OFL) |
| `dados/tabela2.csv` | Transcrição da Tabela 2 do artigo |
| `scripts/graficos.py` | Gera os gráficos em `img/` |
| `scripts/verificacoes.py` | Reproduz as conferências do slide "Um olhar estatístico" |
| `scripts/apendice.py` | Gera `_apendice.qmd` |
| `perguntas-provaveis.md` | 5 perguntas prováveis com sugestão de resposta |
| `docs/` | Versão renderizada, publicada pelo GitHub Pages |

## Renderizar de novo

```bash
python scripts/graficos.py
python scripts/apendice.py
quarto render
```

## Publicar no GitHub com link (GitHub Pages)

1. Em <https://github.com/new>, crie um repositório **público** chamado `avaliacao-financeira-projetos`, sem README, sem .gitignore e sem licença.
2. No PowerShell, dentro desta pasta:

   ```powershell
   cd D:\Projetos\mestrado\avaliacao-financeira-projetos
   git init
   git add .
   git commit -m "Apresentação Abensur (2012), Avaliação Financeira de Projetos"
   git branch -M main
   git remote add origin https://github.com/SEU-USUARIO/avaliacao-financeira-projetos.git
   git push -u origin main
   ```

3. No GitHub, abra **Settings > Pages**. Em *Build and deployment*, escolha **Deploy from a branch**, branch **main**, pasta **/docs**, e clique em **Save**.
4. Em um ou dois minutos o link fica ativo:
   `https://SEU-USUARIO.github.io/avaliacao-financeira-projetos/`

Para atualizar depois: edite, rode `quarto render`, e faça `git add .`, `git commit -m "..."` e `git push`.
