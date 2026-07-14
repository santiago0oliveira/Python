""" programa para contar palavras em um arquivo de texto:
1 - peça ao usuario o caminho para um arquivo de texto;
2 - leia o conteudo do arquivo;
3 - separe as palavras;
4 = conte o numero total de palavras;
5 - (opcional) exibe as 10 palavras mais frequentes;
"""
arquivo = input("Digite o caminho para o arquivo de texto: ")
try:
    with open(arquivo, "r", encoding="utf-8") as f:
        texto = f.read()
except FileNotFoundError:
    print("O arquivo especificado não existe")
    exit(1)

import re

palavras = re.findall(r"\w+", texto.lower())

palavras_total = len(palavras)

print(f"\nO Numero total de palavras: {palavras_total}")

from collections import Counter

contador: Counter[str] = Counter(palavras)

mais_comum = contador.most_common(10)

print("\nPalavras mais frequentes: ")
print("\n")

for palavra, freq in mais_comum:
    print(f"{palavra}: {freq}\n")
print("\n")