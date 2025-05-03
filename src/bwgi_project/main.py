from bwgi_project.facade import Facade
from bwgi_project.strategies.reconcile_strategy import ReconcileStrategy
from bwgi_project.strategies.last_lines_strategy import LastLinesStrategy
from bwgi_project.strategies.computed_property_strategy import ComputedPropertyStrategy

if __name__ == "__main__":
    print("\nExecutando Reconciliação:")
    Facade(ReconcileStrategy()).executar_task()
    print("\n\nExecutando Linhas Invertidas:")
    Facade(LastLinesStrategy()).executar_task()
    print("\n\nExecutando Computed Property:")
    Facade(ComputedPropertyStrategy()).executar_task()
