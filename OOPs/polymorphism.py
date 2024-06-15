# the ability of the code, data or methods to behave differently depending on their circumstances and context
class Instrument:
    def play(self):
        print("Instrument is playing")


# Method Overriding
# subclass provides a different implementation of the method that is already defined in the parent class
class Piano(Instrument):
    def play(self):
        print("Piano is playing")


class Guitar(Instrument):
    def play(self):
        print("Strumming a Guitar")


class Violin(Instrument):
    def play(self):
        print("Violin is playing")


print("--Method Overloading Example--")
instruments = [Piano(), Guitar(), Violin()]
for instrument in instruments:
    instrument.play()
print()


# Method Overloading

class Drum(Instrument):
    def beat(self, *args):
        if len(args) == 0:
            print("drum is getting playing in default beat")
        else:
            for i in args:
                print(f"drum is getting played with {i} beat")


print(" -- Method Overloading --")
drum = Drum()
drum.beat()
drum.beat(1, 2, 3)
print()


# Operator Overloading

class Song:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def __str__(self):
        return f"{self.title}, ({self.duration} minutes) "

    def __add__(self, other):
        new_title = f"{self.title} & {other.title}"
        new_duration = self.duration + other.duration
        return Song(new_title, new_duration)


song1 = Song("Double Take", 2.50)
song2 = Song("Dandelions", 4)
combined_song = song1 + song2
print(" --Operator Overloading --")
print("Song 1 :", song1)
print("Song 2:", song2)
print(combined_song)
