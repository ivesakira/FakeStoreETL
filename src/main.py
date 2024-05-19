from extract import FakeStoreAPI
from transform import Transform
from load import Load

def main():

    jsonCarrinho = FakeStoreAPI.busca_carrinho()
    jsonProduto = FakeStoreAPI.busca_produto()
    
    df = Transform.transformDados(jsonCarrinho, jsonProduto)

    Load.toCsv(df)

if __name__ == '__main__':
    main()