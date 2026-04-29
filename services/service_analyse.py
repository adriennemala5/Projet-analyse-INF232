import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr
import io
import base64
from services.service_base_de_donnees import ServiceBaseDeDonnees

class ServiceAnalyse:
    
    @classmethod
    def calculer_correlation(cls, x, y):
        if len(x) < 2 or len(y) < 2:
            return None
        corr, p_valeur = pearsonr(x, y)
        return [corr, p_valeur]
    
    @classmethod
    def calculer_statistiques_descriptives(cls, donnees):
        if not donnees or len(donnees) == 0:
            return {}
        return {
            'moyenne': round(np.mean(donnees), 2),
            'mediane': round(np.median(donnees), 2),
            'ecart_type': round(np.std(donnees), 2),
            'minimum': round(min(donnees), 2),
            'maximum': round(max(donnees), 2)
        }
    
    @classmethod
    def analyser_toutes_correlations(cls):
        heures_etude, heures_sommeil, notes, satisfaction = ServiceBaseDeDonnees.get_valeurs_numeriques()
        
        print(f"DEBUG Corrélations - étude: {heures_etude}, notes: {notes}")
        
        if len(heures_etude) < 2:
            print("DEBUG - Pas assez de données (moins de 2 avis)")
            return {}
        
        correlations = {
            'etude_vs_note': cls.calculer_correlation(heures_etude, notes),
            'sommeil_vs_note': cls.calculer_correlation(heures_sommeil, notes),
            'etude_vs_sommeil': cls.calculer_correlation(heures_etude, heures_sommeil),
            'satisfaction_vs_note': cls.calculer_correlation(satisfaction, notes)
        }
        
        print(f"DEBUG Corrélations calculées: {correlations}")
        return correlations
    
    @classmethod
    def get_analyse_complete(cls):
        heures_etude, heures_sommeil, notes, satisfaction = ServiceBaseDeDonnees.get_valeurs_numeriques()
        
        print(f"DEBUG get_analyse_complete - étude: {heures_etude}")
        
        if len(heures_etude) < 2:
            print("DEBUG - Renvoie None (pas assez de données)")
            return None
        
        avis = ServiceBaseDeDonnees.get_donnees_pour_analyse()
        noms = [a['filiere'] for a in avis]  # Utiliser filière au lieu de nom
        
        result = {
            'statistiques_etude': cls.calculer_statistiques_descriptives(heures_etude),
            'statistiques_sommeil': cls.calculer_statistiques_descriptives(heures_sommeil),
            'statistiques_notes': cls.calculer_statistiques_descriptives(notes),
            'statistiques_satisfaction': cls.calculer_statistiques_descriptives(satisfaction),
            'correlations': cls.analyser_toutes_correlations(),
            'toutes_etudes': heures_etude,
            'toutes_sommeils': heures_sommeil,
            'toutes_notes': notes,
            'etudiants_noms': noms,
            'nbr_etudiants': len(heures_etude)
        }
        
        print(f"DEBUG Résultat: {result}")
        return result