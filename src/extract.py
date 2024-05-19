import requests

class FakeStoreAPI:
        urlBase = r'https://fakestoreapi.com'

        def busca_carrinho():
            resposta = requests.get(f"{FakeStoreAPI.urlBase}/carts")
            resposta.raise_for_status()
            return resposta.json()
        
        def busca_produto():
            resposta = requests.get(f"{FakeStoreAPI.urlBase}/products")
            resposta.raise_for_status
            return resposta.json()