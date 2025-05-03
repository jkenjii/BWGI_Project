from pprint import pprint
from bwgi_project.core.reconcile import reconcile_accounts
from bwgi_project.data_utils.csv_utils import CSVTransactions
from bwgi_project.strategies.task_strategy import TaskStrategy

class ReconcileStrategy(TaskStrategy):
    def executar(self):
        arq1 = CSVTransactions('data/transactions1.csv')
        arq2 = CSVTransactions('data/transactions2.csv')
        r1, r2 = reconcile_accounts(arq1.get_transacoes(), arq2.get_transacoes())
        pprint(r1)
        pprint(r2)
