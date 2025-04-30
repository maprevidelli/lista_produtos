# Lista de compras simples
lista = []
def cabecalho_inicial():
	print('\n\033[1;31;44m=============>>> Lista de compras simples! <<<=============\033[0m ')
	print("-" * 60)
	print('\nA. Adicionar produto')
	print('B. Remover produto')
	print('C. Pesquiar produto')
	print('D. Sair do programa')

def cabecalho_lista ():
	print(f"\n{'Indice':<10} | {'NOME':<10} | {'QUANTIDADE':>10} | {'UNIDADE':<10} | {'DESCRIÇÃO':<20}")
	print("-" * 60)
	
def unidade_medida ():
	while True:
		print('\nA. Quilograma')
		print('B. Grama')
		print('C. Litro')
		print('D. Mililitro')
		print('E. Unidade')
		print('F. Metro')
		print('G. Centímetro')
		opcao = input('\n(?) - Entre com a letra referente á unidade de medida: ').lower()
		if opcao not in	['a', 'b', 'c', 'd', 'e', 'f', 'g']:
			print('\n\033[1;31;40m(!) - Opção inexistente, tente novamente.\033[0m')
			continue
		if opcao == 'a':
			unidade = 'Quilos'
		if opcao == 'b':
			unidade = 'Gramas'
		if opcao == 'c':
			unidade = 'Litros'
		if opcao == 'd':
			unidade = 'Mililitros'
		if opcao == 'e':
			unidade = 'Unidades'
		if opcao == 'f':
			unidade = 'Metros'
		if opcao == 'g':
			unidade = 'Centímetros'
		return unidade				
		break

def pesquisar_por_nome(lista):
    termo = input("(?) - Digite o nome (ou parte do nome) do produto que deseja pesquisar: ").lower()
    encontrados = [(i, item) for i, item in enumerate(lista) if termo in item["Nome"].lower()]
    
    if encontrados:
        print("\n=====>> Resultados da Pesquisa <<=====")
        print("Idx | Nome       | Quantidade | Unidade    | Descrição")
        print("-" * 60)
        for i, item in encontrados:
            print(
                f'{i:<3} | '
                f'{item["Nome"]:<10} | '
                f'{item["Quantidade"]:>10} | '
                f'{item["Unidade"]:<10} | '
                f'{item["Descrição"]:<20}'
            )
    else:
        print("\n\033[1;31;40m(!) - Nenhum produto encontrado com esse nome.\033[0m")

	
		
while True:
	cabecalho_inicial()
	opcao = input('\n(?) - Digite a opção desejada: ').lower()
	if opcao not in ['a', 'b', 'c', 'd']:
		print('\n\033[1;31;40m(!) - Opção inválida, tente novamente\033[0m')
		continue
	if opcao == 'd':
		print(f'\n\033[1;33;40m=====> Grato por usar a lista de compras simples <<=====\033[0m ')
		break
		
	if opcao == 'a':
		try:
			print('\n\033[1;31;44m =============>> Adicionar Produto\033[0m ')
			nome = input('\n(?) - Entre com o nome do produto: ')
			if nome.isalpha() == False:
				print("\n\033[1;31;40m(!) - Digite apenas letras, sem números, espaços ou símbolos.\033[0m")
				continue
					
			unidade = unidade_medida()
			qtd = int(input('(?) - Entre com a quantidade deste produto: '))
			desc = input('(?) - Entre com uma breve descrição deste produto: ')
			lista.append({
			"Nome" : nome,
			"Quantidade" : qtd,
			"Unidade" : unidade,
			"Descrição" : desc
			})
			print('\n\033[1;36;42m============================>> Item computado com sucesso\033[0m ')
			cabecalho_lista()
			for i, item in enumerate(lista):
				print(
					f'{i:<10} | '
					f'{item['Nome']:<10} | '
					f'{item['Quantidade']:>10} | '
					f'{item['Unidade']:<10} | '
					f'{item['Descrição']:<20}'
				)
		except ValueError:
			print('\n\033[1;31;40m(!) -  Valor deve ser númerico\033[0m') 		
			continue
	if opcao == 'b':
		if len(lista) == 0:
			print('\n\033[1;31;40m(!) - Não há intens para serem removidos\033[0m')
			continue
		try:
			apaga = int(input('(?) - Digite o item que deseja apagar: '))
			del lista[apaga]
			print('===' * 20)
			print('\n\033[1;33;40m===>> Lista alterada <<===\033[0m')
			cabecalho_lista()
			for i, item in enumerate(lista):
				print(
					f'{i:<10} | '
					f'{item['Nome']:<10} | '
					f'{item['Quantidade']:>10} | '
					f'{item['Unidade']:<10} | '
					f'{item['Descrição']:<20}'
				)
		except IndexError:
			print('\n\033[1;31;40m(!) - Item não consta na lista\033[0m')
			continue
	# Pesquisar produto
	if opcao == 'c':
		contagem = len(lista)
		if contagem == 0:
			print('\n\033[1;31;40m(!) - A lista não possuí itens.\033[0m')
			continue
		if contagem >= 1:
			pesquisar_por_nome(lista)
			
# aplicação desenvolvida por maprevidelli - em construção - Abril 30