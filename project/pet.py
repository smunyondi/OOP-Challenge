# pet.py

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5        # 0 = full, 10 = starving
        self.energy = 5        # 0 = exhausted, 10 = fully rested
        self.happiness = 5     # 0 = sad, 10 = super happy
        self.tricks = []       # List of learned tricks
        self.health = 10       # 0 = very sick, 10 = perfectly healthy
        self.age = 0           # Increases with actions

    def eat(self):
        self.hunger = max(self.hunger - 3, 0)
        self.happiness = min(self.happiness + 1, 10)
        self.age += 1
        print(f"{self.name} ate some food. 🥩")

    def sleep(self):
        self.energy = min(self.energy + 5, 10)
        self.age += 1
        print(f"{self.name} had a nice nap. 😴")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(self.happiness + 2, 10)
            self.hunger = min(self.hunger + 1, 10)
            self.age += 1
            print(f"{self.name} played and had a blast! 🎾")
        else:
            print(f"{self.name} is too tired to play. 😓")

    def train(self, trick):
        self.tricks.append(trick)
        self.age += 1
        print(f"{self.name} learned a new trick: {trick}! 🧠")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} doesn't know any tricks yet.")

    def update_health(self):
        # Health decreases if hunger is too high or energy is too low
        if self.hunger >= 8 or self.energy <= 2:
            self.health = max(self.health - 1, 0)
        else:
            self.health = min(self.health + 1, 10)  # Regain health when conditions are good

    def get_mood(self):
        # Mood is based on happiness and energy
        if self.happiness > 7 and self.energy > 7:
            return "😊 Happy"
        elif self.happiness < 4 or self.energy < 3:
            return "😞 Grumpy"
        elif self.health < 5:
            return "🤒 Sick"
        else:
            return "😐 Okay"

    def get_status(self):
        self.update_health()  # Adjust health based on conditions
        mood = self.get_mood()
        print(f"\n📊 {self.name}'s Current Status:")
        print(f"  Age: {self.age}")
        print(f"  Hunger: {self.hunger}/10")
        print(f"  Energy: {self.energy}/10")
        print(f"  Happiness: {self.happiness}/10")
        print(f"  Health: {self.health}/10")
        print(f"  Mood: {mood}")
        print("-" * 30)
