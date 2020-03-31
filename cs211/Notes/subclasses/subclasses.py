class Animal(object):
    def __init__(self, name):
        self.name = name
        self.cuteness_pct = 75

    def my_sound(self):
        raise NotImplementedError("No generic animals!")

    def rename(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        clazz = type(self).__name__
        return "{}({})".format(clazz, self.name)


class Goat(Animal):

    def my_sound(self):
        return "mmgammgammga"


class Dolphin(Animal):
    def __init__(self, name="Willy", iq=250):
        self.name = name
        self.iq = iq
        self.cuteness_pct = 100
    def my_sound(self):
        return "EEEkeeppppekeeek"
    def is_smart(self):
        return self.iq > 200



billy = Goat("Billy")
print(billy.my_sound())

willy = Dolphin()
print(willy.my_sound())
if willy.is_smart():
    print("So smart, you can't even comprehend")


class Spinner(Dolphin):
    def __init__(self, name="Silly"):
        self.iq = 300
        self.cuteness_pct = 125
        self.name = name
    def jump_style(self):
        return "Yes, I spin. Really."


my_pets = [Dolphin(), Goat("Marcie"), Spinner(), Goat("Billy")]

for pet in my_pets:
    print("{} says {}".format(pet.name, pet.my_sound()))

print(my_pets)

craig = willy
willy.rename("Marcia")
print(craig.name)
