
from tabulate import tabulate
from estoque import Estoque
import uuid
from datetime import datetime


class Venda:
    def __init__(self):
        self.estoque = Estoque()
        self.estoque.carregar_estoque()
        self.itens_venda = {

        }
        self.total_venda = 0
        self.ID_venda = None
        self.data_venda = None

    def adicionar_item(self, nome, quantidade):

        estoque_disponivel = self.estoque.produtos[nome]["Quantidade"]
        preco = self.estoque.produtos[nome]["Preco"]

        if nome not in self.estoque.produtos:
            return f"Venda não autorizada. Produto '{nome}' não está disponível no estoque."
        
        if estoque_disponivel < quantidade:
            return f"Erro: Quantidade insuficiente no estoque. \n Estoque disponível: {estoque_disponivel} unidades \n Quantidade solicitada: {quantidade} unidades"
    

        self.itens_venda[nome] = {
            "Quantidade": quantidade,
            "Preco": preco
        }
        self.total_venda += quantidade * preco
        nova_quantidade = estoque_disponivel - quantidade
        return f"\n\nProduto '{nome}' adicionado a venda. Unidades compradas: {quantidade} unidades.\nNova quantidade no estoque: {nova_quantidade}"

    
    def remover_item(self, nome):

        if nome not in self.itens_venda:
            return f"O produto '{nome}' não está na lista de vendas."
        
        del self.itens_venda[nome]
        return f"Produto '{nome}' removido da venda."
    
    def atualizar_quantidade_item(self, nome, quantidade):
        estoque_disponivel = self.estoque.produtos[nome]["Quantidade"]
        

        if nome not in self.itens_venda:
            return f"Erro: O produto '{nome}' não está na lista de venda."
        
        if quantidade > estoque_disponivel:
            return f"Erro. Estoque indisponível. Há apenas {estoque_disponivel} unidades"
        
        self.itens_venda[nome]['Quantidade'] += quantidade
        estoque_disponivel -= quantidade
        return f"Quantidade compradas de '{nome}' atualizada: {self.itens_venda[nome]['Quantidade']} unidades\n"\
               f"Quantidade restante de '{nome}': {estoque_disponivel} unidades"
    

    def finalizar_compra(self):
        if not self.itens_venda:
           return "Não houve compras"
    
        self.ID_venda = str(uuid.uuid4())
        self.data_venda = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        total = 0
        tabela_itens = []

    
        for nome, dados_item in self.itens_venda.items():
            quantidade = dados_item["Quantidade"]
            preco = dados_item["Preco"]
            total_item = quantidade * preco
            total += total_item
            tabela_itens.append([nome, quantidade, f"R${preco:.2f}", f"R${total_item:.2f}"])

        self.total_venda = total
        


    
        recibo = f"\n{'='*40}\n"
        recibo += f"{'RECIBO DA VENDA':^40}\n"
        recibo += f"{'='*40}\n"
        recibo += f"ID da Venda: {self.ID_venda}\n"
        recibo += f"Data e Hora: {self.data_venda}\n"
        recibo += f"{'-'*40}\n"
        recibo += tabulate(
            tabela_itens,
            headers=["Produto", "Quantidade", "Preço Unitário", "Total"],
            tablefmt="grid",
            numalign="right",
            floatfmt=".2f"
        )
        recibo += f"\n{'-'*40}\n"
        recibo += f"{'TOTAL GERAL':<30} R${self.total_venda:.2f}\n"
        recibo += f"{'='*40}\n"
        recibo += "Agradecemos pela sua compra!\n"

    
        self.itens_venda.clear()

        return recibo





venda = Venda()


print(venda.adicionar_item("Morango", 30))
print(venda.adicionar_item("Maca", 20))

print(venda.atualizar_quantidade_item("Morango", 10))
print(venda.finalizar_compra())