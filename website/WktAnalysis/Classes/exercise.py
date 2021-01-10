class Exercise(object):
    def __init__(self, name, targetedIntensity):
        self.name = name
        self.targetedIntensity = targetedIntensity
    def print(self):
        print(f"\n{self.name}", end="")
        for n in self.targetedIntensity.items():
            print(str(n) + "1111")