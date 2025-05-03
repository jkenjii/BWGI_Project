from bwgi_project.core.file_utils import last_lines
from bwgi_project.strategies.task_strategy import TaskStrategy

class LastLinesStrategy(TaskStrategy):
    def executar(self):
        for linha in last_lines('data/my_file.txt'):
            print(linha, end='')
