class Player:
    def __init__(self, name):
        self.name = name
        self.metal = 100
        self.energy = 100
        self.naquadah = 50
        self.fleet = 0
        self.turn = 0

    def build_mine(self):
        cost = 20
        if self.metal >= cost:
            self.metal -= cost
            self.energy += 10
            print(f"Mine construite. Energie +10. Metal restant: {self.metal}")
        else:
            print("Pas assez de metal pour construire une mine.")

    def build_ship(self):
        cost_metal = 30
        cost_naquadah = 10
        if self.metal >= cost_metal and self.naquadah >= cost_naquadah:
            self.metal -= cost_metal
            self.naquadah -= cost_naquadah
            self.fleet += 1
            print(f"Vaisseau construit. Flotte totale: {self.fleet}")
        else:
            print("Ressources insuffisantes pour construire un vaisseau.")

    def next_turn(self):
        self.turn += 1
        self.metal += 10
        self.energy += 5
        self.naquadah += 2
        print(f"-- Tour {self.turn} --")
        print(f"Ressources: metal={self.metal}, energie={self.energy}, naquadah={self.naquadah}")


def main():
    name = input("Nom du joueur: ")
    player = Player(name)
    while True:
        print("\nActions: [1] Construire mine [2] Construire vaisseau [3] Tour suivant [4] Quitter")
        choice = input("Choix: ")
        if choice == '1':
            player.build_mine()
        elif choice == '2':
            player.build_ship()
        elif choice == '3':
            player.next_turn()
        elif choice == '4':
            print("Fin du jeu.")
            break
        else:
            print("Choix invalide")

if __name__ == '__main__':
    main()
