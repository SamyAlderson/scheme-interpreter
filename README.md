# Scheme Interpreter
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/tonybalbinot/scheme-interpreter/actions/workflows/ci.yml/badge.svg)](https://github.com/tonybalbinot/scheme-interpreter/actions/workflows/ci.yml)

## Description

L'interpréteur Scheme est une implémentation du langage Scheme en Python. Il est conçu pour être flexible et extensible, permettant la définition de fonctions et de variables de manière dynamique. Le projet est structuré en plusieurs modules, chacun responsable d'une étape spécifique du processus d'exécution : le traitement du code Scheme en jetons, la compilation des jetons en abstrait syntaxique, et l'exécution réelle du code.

## Fonctionnalités

*   Interprétation de code Scheme
*   Définition de fonctions et de variables de manière dynamique
*   Traitement du code Scheme en jetons
*   Compilation des jetons en abstrait syntaxique
*   Exécution réelle du code

## Installation

Pour installer le projet, exécutez les commandes suivantes :

```bash
git clone https://github.com/tonybalbinot/scheme-interpreter.git
cd scheme-interpreter
pip install -r requirements.txt
```

## Usage

Pour exécuter le projet, utilisez la commande suivante :

```bash
python src/main.py
```

Vous pouvez également exécuter des fichiers Scheme spécifiques en utilisant l'option `-f` :

```bash
python src/main.py -f example.scheme
```

## Architecture du projet

Le projet est structuré en plusieurs modules :

*   `src/main.py` : Fichier principal, charge les fichiers Scheme et les exécute
*   `src/scheme.py` : Module contenant les classes et fonctions pour l'interpréteur Scheme
*   `src/tokenizer.py` : Module pour le traitement du code Scheme en jetons
*   `src/parser.py` : Module pour la compilation des jetons en abstrait syntaxique

## Contribuer

Pour contribuer à ce projet, vous pouvez suivre les étapes suivantes :

1.  Cloner le projet en utilisant `git clone https://github.com/tonybalbinot/scheme-interpreter.git`
2.  Créer une branche nouvelle pour votre contribution en utilisant `git branch nom_de_la_branche`
3.  Exécuter les tests en utilisant `python -m unittest discover`
4.  Lancer la CI en utilisant `python -m unittest discover`
5.  Soumettre votre Pull Request pour que les autres membres de l'équipe puissent la revue

## Licence

Ce projet est sous licence MIT. Vous pouvez trouver la licence dans le fichier [LICENSE](LICENSE).