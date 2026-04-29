import sqlite3
from config import Config
from modeles.donnees_academiques import DonneesAcademiques

class ServiceBaseDeDonnees:
    
    @staticmethod
    def get_donnees_pour_analyse():
        return DonneesAcademiques.charger_tous_avis()
    
    @staticmethod
    def get_valeurs_numeriques():
        avis = DonneesAcademiques.charger_tous_avis()
        
        print(f"DEBUG get_valeurs_numeriques - Nombre d'avis: {len(avis)}")
        
        if not avis:
            print("DEBUG - Aucun avis trouvé")
            return [], [], [], []
        
        heures_etude = []
        heures_sommeil = []
        notes = []
        satisfaction = []
        
        for a in avis:
            print(f"DEBUG - Avis: {a}")  # Voir la structure
            heures_etude.append(float(a['heures_etude']))
            heures_sommeil.append(float(a['heures_sommeil']))
            notes.append(float(a['note_moyenne']))
            satisfaction.append(int(a['satisfaction']))
        
        print(f"DEBUG - Données extraites: étude={heures_etude}, notes={notes}")
        
        return heures_etude, heures_sommeil, notes, satisfaction
    
    @staticmethod
    def ajouter_avis(donnees):
        return DonneesAcademiques.sauvegarder_avis(donnees)
    
    @staticmethod
    def get_statistiques():
        return DonneesAcademiques.get_statistiques_globales()