class Player:
    def __init__(self, name):
        self.name = name
        self.metal = 100
        self.energy = 100
        self.naquadah = 50
        self.crystal = 50
        self.fleet = 0
        self.defense = 0
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

    def enemy_attack(self):
        import random
        if random.random() < 0.3:
            print("Attaque ennemie !")
            if self.defense + self.fleet > 0:
                print("Vous repoussez l'ennemi grâce à votre défense.")
            else:
                perte = min(self.metal, 20)
                self.metal -= perte
                print(f"Vous perdez {perte} metal.")

    def build_turret(self):
        cost_metal = 40
        cost_crystal = 20
        if self.metal >= cost_metal and self.crystal >= cost_crystal:
            self.metal -= cost_metal
            self.crystal -= cost_crystal
            self.defense += 1
            print(f"Tourelle construite. Défense totale: {self.defense}")
        else:
            print("Ressources insuffisantes pour construire une tourelle.")

    def next_turn(self):
        self.turn += 1
        self.metal += 10
        self.energy += 5
        self.naquadah += 2
        self.crystal += 3
        self.enemy_attack()
        print(f"-- Tour {self.turn} --")
        print(
            f"Ressources: metal={self.metal}, energie={self.energy}, naquadah={self.naquadah}, crystal={self.crystal}"
        )
        print(f"Flotte={self.fleet} | Défense={self.defense}")


def main():
    name = input("Nom du joueur: ")
    player = Player(name)
    while True:
        print("\nActions: [1] Construire mine [2] Construire vaisseau [3] Construire tourelle [4] Tour suivant [5] Quitter")
        choice = input("Choix: ")
        if choice == '1':
            player.build_mine()
        elif choice == '2':
            player.build_ship()
        elif choice == '3':
            player.build_turret()
        elif choice == '4':
            player.next_turn()
        elif choice == '5':
            print("Fin du jeu.")
            break
        else:
            print("Choix invalide")

if __name__ == '__main__':
    main()
