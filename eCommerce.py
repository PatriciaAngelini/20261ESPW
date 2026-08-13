#Teste de matriz
#revendo matriz
#catalogo é uma matriz
# catalogo = [
#     ["Camiseta Azul", 59.90, 120, [38, 40, 42, 44]],
#     ["Tênis Runner", 199.90, 40],
# ]
# print(f'produto: {catalogo[0]}')
# print(f'nome produto: {catalogo[0][0]}')
# print(f'estoque: {catalogo[0][2]}')
# print(f'tamanho: {catalogo[0][3][2]}')

def cadastrar_produto(catalogo, nome, preco, estoque):
    #exemplo produto = ["Tênis Runner", 199.90, 40]
    produto = [nome, preco, estoque]
    #exemplo catalogo = [["Tênis Runner", 199.90, 40]]
    catalogo.append(produto)
    return catalogo

def exibir_catalogo(catalogo):
    for produto in catalogo:
        #print(produto)
        print(f'{produto[0]} - R$ {produto[1]:.2f} (estoque: {produto[2]})')


if __name__ == '__main__':
    novos_produtos = []
    novos_produtos = cadastrar_produto(novos_produtos,
                                       'Camiseta Azul',
                                       89.90, 120)
    novos_produtos = cadastrar_produto(novos_produtos,
                                       'Tenis Runner',
                                       199.90, 40)
    novos_produtos = cadastrar_produto(novos_produtos,
                                       'Boné Preto',
                                       39.90, 50)
    #print(novos_produtos)
    exibir_catalogo(novos_produtos)