import pandas as pd
import os

class Load:
    outputPath = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Resultado\\DadosUsuario')

    def toCsv(df):
        df.to_csv(f'{Load.outputPath}.csv', sep = ';', index = None)