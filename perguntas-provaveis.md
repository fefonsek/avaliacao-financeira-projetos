# Perguntas prováveis e sugestões de resposta

Apresentação de Abensur (2012), *Um modelo multiobjetivo de otimização aplicado ao processo de orçamento de capital*. Avaliação Financeira de Projetos, Prof. Cleiton Martins Duarte Silva, 21/10/2026.

## 1. O modelo deixou dois terços do orçamento sem uso. Isso é bom ou ruim?

Depende do que a empresa faria com esse dinheiro. Pela teoria clássica, se há capital disponível e projetos com VPL positivo, aceitar esses projetos cria valor. Pela Tabela 2, a carteira só pelo IL gera R$ 62.047 a mais de VPL que a carteira do modelo. A "economia" de R$ 205.980 só é vantagem se a empresa tiver um uso melhor para o caixa, acima da TMA, ou se houver uma restrição de liquidez que o artigo não mostra. O autor trata a sobra como reforço de caixa ou dividendos, mas não compara com o valor que deixa de ser criado.

## 2. Por que usar o IL na função objetivo, e não o VPL?

Porque o artigo parte de capital racionado, e nesse caso os manuais (Ross, Westerfield e Jaffe, 2002; Samanez, 2009) recomendam ordenar pelo IL, que mede valor por real investido e permite comparar projetos de portes muito diferentes. A contrapartida é que o IL ignora a escala: um projeto de R$ 5 com IL de 321% pesa mais que um de R$ 150 mil com IL de 35%. A alternativa clássica, de Weingartner (1963), é maximizar o VPL total sujeito à restrição orçamentária, o que já resolve o racionamento sem perder a escala.

## 3. O GA_FT é mesmo uma medida de risco?

A ideia é boa: é uma análise de sensibilidade a dois choques, nas entradas de caixa e na TMA, sem supor distribuição de probabilidade. O problema é empírico: nos 45 projetos, a correlação entre GA_FT e IL é de 0,99. Ou seja, nesses dados a medida de risco quase repete a rentabilidade e não traz informação nova. O artigo também não deixa totalmente claro qual valor presente serve de base na Equação 6, e essa escolha pode explicar por que a medida acompanha a escala do IL. Uma alternativa seria simulação de Monte Carlo ou cenários, que o próprio autor menciona na seção 2.

## 4. Dá para generalizar os resultados, já que a amostra é de livros-texto?

Não no sentido estatístico. São 45 exemplos didáticos escolhidos "a esmo", o que evita viés de escolha do autor, mas não torna a amostra representativa de projetos reais, e o estudo não faz inferência. O artigo funciona como prova de conceito: mostra que o modelo roda e o que ele escolhe. O próprio autor coloca casos reais, com a opinião dos gestores, como próximo passo.

## 5. Como os pesos influenciam o resultado? Como você definiria os pesos?

No artigo, todos os pesos são iguais a 1. Como a função objetivo vira uma nota por projeto (1,4896 × IL − PBD − GA_FT), qualquer mudança de peso muda diretamente quem passa do zero. O projeto 35, por exemplo, entra com nota de apenas 0,93: um pequeno aumento no peso do risco o tiraria da carteira. Eu definiria os pesos com os gestores, por um método como o AHP, e depois faria uma análise de sensibilidade para ver quais projetos são estáveis e quais dependem de um peso específico. O script `scripts/verificacoes.py` permite testar isso rapidamente.

## Se perguntarem algo mais técnico

- **O IL da Tabela 2 é o mesmo da Equação 2?** Não exatamente. Na Equação 2, IL = VP / DI. Na Tabela 2, a coluna IL é VPL / DI, em %. Exemplo: projeto 1, 39 / 1.000 = 3,91%. Por isso aparecem valores negativos.
- **A Tabela 4 é coerente com a restrição de liquidez?** Há um ponto a checar: na avaliação grupo a grupo, o modelo aparece escolhendo os projetos 2 (grupo A) e 38 (grupo N), que têm PBD maior que a vida útil (4,70 > 4 e 4,50 > 4). Na carteira conjunta da Tabela 3 eles não entram.
- **Por que tantos projetos ficam de fora?** 22 dos 45 projetos violam a regra PBD ≤ vida útil.
