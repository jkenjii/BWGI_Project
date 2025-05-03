from math import sqrt
from bwgi_project.core.computed_property import computed_property
from bwgi_project.strategies.task_strategy import TaskStrategy

class ComputedPropertyStrategy(TaskStrategy):
    def executar(self):
        class Vetor:
            def __init__(self, x, y, z): self.x, self.y, self.z = x, y, z
            @computed_property('x', 'y', 'z')
            def magnitude(self): return sqrt(self.x**2 + self.y**2 + self.z**2)
            @magnitude.setter
            def magnitude(self, valor): pass
            @magnitude.deleter
            def magnitude(self): self.x = self.y = self.z = 0

        v = Vetor(3, 4, 12)
        print(v.magnitude)
        v.x = 6
        print(v.magnitude)
        del v.magnitude
        print(v.magnitude)
