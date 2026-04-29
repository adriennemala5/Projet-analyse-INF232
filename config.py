import os
from pathlib import Path
class Config:
    """Configuration principale de l'application"""

    #Chemins des dossiers
    BASE_DIR = Path(__file__).resolve().parent
    BASE_DE_DONNEES = os.path.join(BASE_DIR, 'base_de_donnees.db')
    DOSSIER_STATIQUES = os.path.join(BASE_DIR, 'static')
    DOSSIER_TEMPLATES = os.path.join(BASE_DIR, 'templates')

    #Configuration Flask
    SECRET_KEY = os.environ.get('SECRET_KEY', 'cle-secrete-projet-academique')
    DEBUG = False
    JSON_AS_ASCII = False

    #Configuration base de donnees
    DATABASE = BASE_DE_DONNEES
    @classmethod
    def init_application(cls):
        """Initialise les dossiers necessaires"""
        #Creation des dossiers
        for dossier in [cls.DOSSIER_STATIQUES, cls.DOSSIER_TEMPLATES]:
            if not os.path.exists(dossier):
                os.makedirs(dossier)
    
        # Creation du dossier .vscode
        vscode_dir = os.path.join(cls.BASE_DIR, '.vscode')
        if not os.path.exists(vscode_dir):
            os.makedirs(vscode_dir)