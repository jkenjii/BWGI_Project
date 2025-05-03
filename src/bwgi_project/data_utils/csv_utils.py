
import csv
import os

class CSVTransactions:
    def __init__(self, caminho):
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
        caminho_absoluto = os.path.join(base_dir, caminho)
        self.caminho = caminho_absoluto
        self.transacoes = []
        self._ler_arquivo()

    def _ler_arquivo(self):
        with open(self.caminho, newline='', encoding='utf-8') as f:
            self.transacoes = list(csv.reader(f))

    def get_transacoes(self):
        return self.transacoes
