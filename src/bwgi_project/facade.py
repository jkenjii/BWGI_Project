class Facade:
    def __init__(self, strategy):
        self.strategy = strategy
    def executar_task(self):
        self.strategy.executar()
