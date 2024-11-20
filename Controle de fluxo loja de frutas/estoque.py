import json

class Estoque:
    def __init__(self):
        self.produtos = {

        }
    
    def adicionar_produto(self, nome: str, quantidade: int, preco: float):
        if quantidade <= 0:
            return f"A quantidade do produto deve ser um valor maior que zero."
        if preco <= 0:
            return f"O preço do produto deve ser um valor maior que zero."
        
        self.produtos[nome] = {
            "Nome": nome, \
            "Quantidade": quantidade,\
            "Preco": preco
        }

        return f"O produto '{nome}' foi adicionado com sucesso."


    def atualizar_quantidade(self, nome, quantidade):
        if nome not in self.produtos:
            return f"O produto '{nome}' não está no estoque."
        
        self.produtos[nome]["Quantidade"] += quantidade

        return f"Produto '{nome}' atualizado. Agora há {self.produtos[nome]['Quantidade']} unidades."
    
    def listar_produtos(self):
        if not self.produtos:
            return f'Não há produtos no estoque'
        
        lista_produtos = "produtos no estoque:\n"

        for nome, valores in self.produtos.items():
            lista_produtos += f"- {nome:<10} {valores['Quantidade']} unidades--R${valores['Preco']:.2f} \n"

        return lista_produtos
    
    def consultar_produto(self, nome):
        if nome not in self.produtos:
            return f"O produto '{nome}' não está no estoque."
        
        listar_produto = f"produto '{nome}': \n"
        listar_produto += f"Quantidade: {self.produtos[nome]['Quantidade']}; Preço: R${self.produtos[nome]['Preco']:.2f}\n\n"

        return listar_produto
    
    def remover_produto(self, nome):
        if nome not in self.produtos:
            return f"Produto {nome} não está no estoque"

        del self.produtos[nome]
        return f"Produto '{nome}' removido com sucesso"
    
    def verificar_estoque_baixo(self, percentual_limite = 0.2):
        produto_estoque_baixo = []

        for nome, detalhes in self.produtos.items():
            limite = detalhes["Quantidade"] * percentual_limite
            if detalhes["Quantidade"] <= limite:
                produto_estoque_baixo.append(
                     f"O produto '{nome}' está abaixo do limite. Há apenas {detalhes['Quantidade']} unidades."
                )
        if produto_estoque_baixo:
            return "\n".join(produto_estoque_baixo)
        else:
            return f"Não há produtos abaixo do limite."

    def salvar_estoque(self, arquivo="estoque.json"):
        with open(arquivo, "w") as file:
             json.dump(self.produtos, file, indent = 4)
        return "Estoque salvo com sucesso."
    
    
    def carregar_estoque(self, arquivo="estoque.json"):
        try:
            with open(arquivo, "r") as file:
                self.produtos = json.load(file)
            return "Estoque carregado com sucesso."
        
        except FileNotFoundError:
            self.produtos = {}
            return "Arquivo de estoque não encontrado. Criando um novo."


    
estoque = Estoque()


print(estoque.adicionar_produto("Morango", 50, 3.5))
print(estoque.adicionar_produto("Maca", 30, 2.0))
print(estoque.adicionar_produto("Banana", 20, 1.2))
print(estoque.adicionar_produto("Abacaxi", 10, 4.0))
print(estoque.adicionar_produto("Laranja", 15, 1.8))



print(estoque.listar_produtos())


print(estoque.atualizar_quantidade("Morango", 20))
print(estoque.atualizar_quantidade("Banana", -5))

print(estoque.consultar_produto("Abacaxi"))


print(estoque.verificar_estoque_baixo())

print(estoque.remover_produto("Laranja"))


print(estoque.salvar_estoque())


print(estoque.carregar_estoque())


print(estoque.listar_produtos())

