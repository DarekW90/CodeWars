class Human:
    def __init__(self, name):
        self.name = name


class Man(Human):
    def __init__(self,name):
        super().__init__(name)
        self.gender = "Male"


class Woman(Human):
    def __init__(self,name):
        super().__init__(name)
        self.gender = "Female"


def God():
    adam = Man("Adam")
    eve = Woman("Eve")
    return [adam, eve]



#
# paradise = God()
# test.assert_equals(isinstance(paradise[0], Man), True, "First object are a man")