import pandas as pd
from collections import defaultdict
from datetime import datetime

class Transform:
    
    def transformDados(jsonCarrinho, jsonProduto):

        categoriaProduto = {produto['id']: produto['category'] for produto in jsonProduto}

        dadosUsuario = defaultdict(lambda: {'DataUltimaCarrinho' : None,
                                             'MaiorCategoria' : defaultdict(int)})
        
        for carrinho in jsonCarrinho:
            idUsuario = carrinho['userId']
            dataCarrinho = datetime.strptime(carrinho['date'],  "%Y-%m-%dT%H:%M:%S.%fZ")

            if not dadosUsuario[idUsuario]['DataUltimaCarrinho'] or dataCarrinho > dadosUsuario[idUsuario]['DataUltimaCarrinho']:
                dadosUsuario[idUsuario]['DataUltimaCarrinho'] = dataCarrinho

            for produto in carrinho['products']:
                categoria = categoriaProduto[produto['productId']]
                dadosUsuario[idUsuario]['MaiorCategoria'][categoria] += produto['quantity']

        final = []
        
        for idUsuario, dado in dadosUsuario.items():
            maxCategoria = max(dado['MaiorCategoria'], key=dado['MaiorCategoria'].get)
            final.append({
                'idUsuario' : idUsuario,
                'DataUltimoCarrinho' : dado['DataUltimaCarrinho'],
                'MaiorCategoria' : maxCategoria
            })
        
        df =  pd.DataFrame(final)
        return df

            


