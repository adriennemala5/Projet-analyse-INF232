from flask import Flask, render_template
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from routes.donnees_routes import donnees_bp
from routes.statistiques_routes import statistiques_bp
from modeles.donnees_academiques import DonneesAcademiques
from config import Config
import os

# Initialisation de l'application
app = Flask(__name__, 
           template_folder=Config.DOSSIER_TEMPLATES,
           static_folder=Config.DOSSIER_STATIQUES)

# Configuration
app.config['SECRET_KEY'] = Config.SECRET_KEY
app.config['JSON_AS_ASCII'] = Config.JSON_AS_ASCII

# Initialisation de la base de données
DonneesAcademiques.initialiser_base()

# Enregistrement des blueprints
app.register_blueprint(donnees_bp, url_prefix='/donnees')
app.register_blueprint(statistiques_bp, url_prefix='/statistiques')

# ============ ROUTES PRINCIPALES ============

# Page d'accueil
@app.route('/')
def accueil():
    return render_template('accueil.html')

# Page formulaire de collecte
@app.route('/formulaire')
def formulaire():
    return render_template('formulaire.html')

# Page de confirmation
@app.route('/success')
def success():
    return render_template('success.html')

# ============ LANCEMENT DE L'APPLICATION ============

if __name__ == '__main__':
    # Initialisation des dossiers
    Config.init_application()
    
    # Configuration du port (pour serveur en ligne)
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'False').lower() == 'true'
    
    # Lancement du serveur
    app.run(debug=debug, host='0.0.0.0', port=port)