import unittest
import sys
import os

# Adiciona o caminho src ao sys.path para poder importar bwgi_project
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from bwgi_project.core.file_utils import last_lines

class TestLastLines(unittest.TestCase):
    def test_reverse_lines_with_newline(self):
        # Cria o arquivo temporário
        with open('data/test.txt', 'w', newline='') as f:
            f.write('linha1\nlinha2\nlinha3\n')

        # Chama a função que estamos testando
        result = last_lines('data/test.txt')

        # Verifica se é um iterator
        self.assertIs(result, iter(result), "A função não está retornando um iterator")

        # Converte o resultado para lista e normaliza as quebras de linha
        linhas = list(result)
        linhas = [linha.replace('\r\n', '\n') for linha in linhas]

        # Filtra linhas vazias (para ignorar linhas só com \n que aparecem se o arquivo termina com \n)
        linhas = [linha for linha in linhas if linha.strip()]

        # Verifica se as linhas estão invertidas corretamente
        self.assertEqual(linhas, ['linha3\n', 'linha2\n', 'linha1\n'])

        # (Boa prática) Remove o arquivo de teste para não deixar lixo
        os.remove('data/test.txt')
