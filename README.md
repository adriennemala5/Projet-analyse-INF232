# 📊 StudyFlow Analytics - INF232 EC2

## Présentation du projet

**StudyFlow Analytics** est une application web développée dans le cadre du programme **INF232 EC2**. Elle permet de collecter et d'analyser les données des étudiants afin d'étudier la corrélation entre :

- Les heures d'étude par jour
- Les heures de sommeil par nuit
- Les notes moyennes obtenues
- Le niveau de satisfaction des étudiants

## 🎯 Objectifs pédagogiques

- Collecter des données anonymes sur les habitudes d'étude
- Calculer des statistiques descriptives (moyenne, médiane, écart-type, etc.)
- Analyser les corrélations linéaires (coefficient de Pearson)
- Visualiser les données avec des graphiques interactifs
- Interpréter les relations entre les variables

## 🛠️ Technologies utilisées

| Technologie | Rôle |
|-------------|------|
| **Python 3.11+** | Langage principal |
| **Flask** | Framework web |
| **SQLite** | Base de données |
| **Chart.js** | Graphiques interactifs |
| **Matplotlib** | Génération de graphiques |
| **SciPy** | Calculs statistiques |
| **HTML5/CSS3** | Interface utilisateur |

## 📦 Installation

### Prérequis

- Python 3.11 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Ouvrir le terminal dans le dossier du projet**

```bash
cd Projet_Analyse_Academique

2. creer un environnement virtuel
python -m venv venv

3. Activer l'environnement virtuel
venv\Scripts\activate

4. installer les dependances
pip install -r exigences.txt

5. Lancer l'application
python app.py

6. acceder a l'application
http://127.0.0.1:5000

structure de l'application
Projet_Analyse_Academique/
├── app.py                 # Point d'entrée de l'application
├── config.py              # Configuration
├── exigences.txt          # Dépendances Python
├── base_de_donnees.db     # Base de données SQLite
├── README.md              # Documentation
│
├── modeles/                # Modèles de données
│   └── donnees_academiques.py
│
├── routes/                # Routes de l'application
│   ├── donnees_routes.py
│   └── statistiques_routes.py
│
├── services/              # Services métier
│   ├── service_analyse.py
│   └── service_base_de_donnees.py
│
├── templates/             # Templates HTML
│   ├── base.html
│   ├── accueil.html
│   ├── formulaire.html
│   ├── analyse.html
│   ├── index.html
│   ├── liste_avis.html
│   └── success.html
│
└── static/                # Fichiers statiques
    └── style.css

 Fonctionnalités
1. Page d'accueil
Présentation du projet

Navigation vers les différentes sections

2. Collecte de données (Formulaire)
Filière d'étude

Âge

Niveau d'étude

Heures d'étude par jour

Heures de sommeil par nuit

Note moyenne (sur 20)

Niveau de satisfaction (1 à 5)

Commentaire optionnel

3. Résultats statistiques
Cartes récapitulatives

Statistiques des notes (moyenne, médiane, écart-type, min, max, étendue)

Statistiques des heures d'étude

Statistiques des heures de sommeil

Statistiques de satisfaction

4. Analyse des corrélations
Nuages de points (Étude vs Notes, Sommeil vs Notes)

Histogramme de distribution des notes

Camembert de répartition par filière

Diagramme en barres (Note moyenne par filière)

Tableau des corrélations de Pearson

5. Liste des avis
Tableau complet des participants

Affichage anonyme
tri par date

