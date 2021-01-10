class Exercise(object):
    def __init__(self, name, intensity ,target):
        self.__dict__.update({k: v for k, v in locals().items() if k != 'self'})