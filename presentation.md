---
# to compile you need xelatex and pandoc
# run pandoc -t beamer -o file.pdf -is --latex-engine=xelatex monero.md
author: "joão carabetta, lucas carneiro, bruno cuconato"
title: "NER in Brazilian Portuguese"
subtitle: "training a NER tagger for use in DOs"
institute: "EMAp"
header-includes: 
    - \usepackage{polyglossia} 
    - \setmainlanguage{portuges}
    - \usepackage{hyperref}
    - \hypersetup{colorlinks=true, linkcolor=blue, linkbordercolor=blue}
---

# monero

![logo da monero](img/monero-logo.png){width=50%}

# fatos básicos

- baseado no protocolo CryptoNote[^cryptonote] (originalmente Bytecoin)

	- "correções" ao protocolo Bitcoin: PoW, emissão, constantes,
  scripts, anonimidade

- monero altera o protocolo cryptonote para ser ainda mais anônimo

  - busca ser moeda totalmente anônima $\implies$ fungível

- top 10 em market capitalization

- 1 XMR = $10^{12}$ "monoshis"

[^cryptonote]: https://cryptonote.org/
