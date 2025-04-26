class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5   # Default mid-level hunger
        self.energy = 5   # Default mid-level energy
        self.happiness = 5  # Default mid-level happiness
        self.tricks = []  # Bonus: List to store learned tricks

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate some food! 🍖")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} had a good nap! 😴")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} played and had fun! 🎾")
        else:
            print(f"{self.name} is too tired to play. 🥱")

    def get_status(self):
        print(f"🐾 {self.name}'s Status:")
        print(f"  Hunger: {self.hunger}/10")
        print(f"  Energy: {self.energy}/10")
        print(f"  Happiness: {self.happiness}/10")
        print()

    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 2)
        print(f"{self.name} learned a new trick: {trick}! 🎓")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)} 🎉")
        else:
            print(f"{self.name} hasn't learned any tricks yet. 🐶")



