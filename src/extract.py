import requests

class FakeStoreAPI:
        urlBase = r'https://fakestoreapi.com'

        def buscaCarrinho():
            resposta = requests.get(f"{FakeStoreAPI.urlBase}/carts")
            resposta.raise_for_status()
            return resposta.json()
        
        def buscaProduto():
            resposta = requests.get(f"{FakeStoreAPI.urlBase}/products")
            resposta.raise_for_status()
            return resposta.json()