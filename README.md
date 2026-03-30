# Laboratório 6 - Tokenização BPE e WordPiece

Este repositório contém a implementação do motor básico do algoritmo Byte Pair Encoding (BPE) e a exploração do tokenizador WordPiece utilizado pelo BERT.

## Funcionamento do WordPiece

No tokenizador do BERT, os sinais de cerquilha (`##`) indicam que o token é uma continuação de uma sub-palavra anterior (ex: `##mente`). O uso dessas sub-palavras permite que o modelo mantenha um vocabulário fixo e otimizado, impedindo o travamento ou a ocorrência de tokens "out-of-vocabulary" (OOV). Ao decompor palavras complexas em fragmentos menores conhecidos, o modelo consegue processar qualquer sequência de texto, mesmo que a palavra original nunca tenha sido vista durante o treinamento.

## Citação de IA

> **Nota:** A lógica de manipulação de strings e expressões regulares utilizada na função `merge_vocab` para garantir a substituição exata dos pares no tokenizador BPE foi gerada por IA.
