class Character():
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.health, self.power)

    def attack(self, other):
        other.health -= self.power
        print "%s does %d damage to %s." % (self.name, other.power, other.name)

    def alive(self):
        if self.health > 0:
            return True
        return False

hero = Character("hero", 10, 5)
goblin = Character("goblin", 6, 2)
options = """
        1. fight goblin
        2. do nothing
        3. flee
        """

def start():
    if goblin.alive() and hero.alive():
        goblin.print_status()
        hero.print_status()
        print options
        user_input = int(raw_input("What do you want to do? "))
        if user_input == 1:
            # Hero attacks goblin
            hero.attack(goblin)
            # conditional outcomes of attack    
            if not goblin.alive():
                print "The goblin is dead."
                win()
        elif user_input == 2:
            pass
        elif user_input == 3:
            print "Goodbye."   
        else:
            print "Invalid input %d" % user_input
            start()
    
    if hero.alive() and goblin.alive():
        goblin.attack(hero)     
        if not hero.alive():
            print "You are dead."
    
    if hero.alive() and goblin.alive():
        start()
def win():
    print "You win!"
start()   
