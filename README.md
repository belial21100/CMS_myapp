# Stargate OGame Clone

Ce projet propose deux versions d'un jeu minimal inspiré d'OGame sur le thème de Stargate :

- Une version en ligne de commande écrite en Python.
- Une version web développée avec Next.js.

## Lancement du jeu en ligne de commande

```bash
python3 -m stargate_game.game
```

Le joueur gère ses ressources (métal, énergie, naquadah, cristal) et peut construire des mines, des vaisseaux ainsi que des tourelles de défense. À chaque tour, une attaque ennemie peut survenir.

## Lancement de la version Next.js

```bash
cd stargate_nextjs
npm install
npm run dev
```

Ouvrez ensuite http://localhost:3000 dans votre navigateur pour jouer.
Cette version web reprend les mêmes mécaniques avec l'ajout des tourelles et des attaques aléatoires.
