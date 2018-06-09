from functools import reduce

text = "Na minha familia somos em 4 pessoas, meu pai {pai}, minha mãe {mae}, minha irmã {irma},e eu {eu} .".format(pai="Henrique", mae="Sandra", irma="Pamela", eu="Gustavo")
print(text)

if"pai" in text:
    print("A palavra 'pai' está no texto")

if "mãe" in text:
    print("A palavra 'mae' está no texto")

if "irmã" in text:
    print("A palavra 'irma' está no texto")

if "eu" in text:
    print("A palavra 'eu' está no texto")


splittedSentence = list(text.replace('.', '').replace(',', '').strip().split(' '))

print('Quantidade de espaços: ' + str(len((splittedSentence)) -1))
print('Quantidade de palavras: ' + str(len((splittedSentence))))

charsAmount = 0

for x in splittedSentence:
    charsAmount += len(x)

print('Quantidade de caracteres: ' + str(charsAmount))


res = text.replace('mãe', 'mamãe')

print('Replace: ' + res)
