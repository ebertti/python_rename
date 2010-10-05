import os, sys
from datetime import datetime
temp = 'tempname'
raiz = '\\\\10.0.0.102\\hdd1\\'
pastas = ['Filmes', 'series',]
ignora = ['Thumbs.db']
qtd = 0
qtdArquivos = 0

def caminharPasta(pasta) :
	global qtd, qtdArquivos, temp
	tempname = pasta + '\\' + temp
	for item in os.listdir(pasta) :
		qtdArquivos += 1
		atual = pasta + '\\' + item
		if os.path.isdir(atual) :
			caminharPasta(atual)
		if not item in ignora and os.path.isfile(atual) and not item[:-4].istitle() and len(item) > 5 :
			novoNome = item[:-4].title() + item[-4:].lower()
			atualNovoNome = pasta + '\\' + novoNome
			qtd += 1
			os.rename(atual, tempname)
			os.rename(tempname, atualNovoNome)

def main() :
	agora = datetime.now()
	for pasta in pastas :
		caminhoPastaCompleto = raiz + pasta
		caminharPasta(caminhoPastaCompleto)

	print 'quantidade renomiados: ' + str(qtd) + ' de: ' + str(qtdArquivos)
	print 'tempo: ' + str(datetime.now() - agora)
	raw_input("fim")
	
if __name__ == "__main__":
    main()
