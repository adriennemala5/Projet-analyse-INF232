from flask import Blueprint, render_template, jsonify
from services.service_base_de_donnees import ServiceBaseDeDonnees
from services.service_analyse import ServiceAnalyse
import traceback

statistiques_bp = Blueprint('statistiques', __name__)

@statistiques_bp.route('/')
def page_analyse():
    return render_template('analyse.html')

@statistiques_bp.route('/resultats')
def resultats():
    return render_template('index.html')

@statistiques_bp.route('/donnees')
def get_donnees():
    try:
        # Vérifier d'abord les statistiques globales
        stats = ServiceBaseDeDonnees.get_statistiques()
        print(f"DEBUG - Stats globales: {stats}")
        
        if not stats or stats.get('total_etudiants', 0) == 0:
            return jsonify({
                'donnees_existantes': False,
                'erreur': 'Aucune donnée disponible'
            }), 200  # Retourner 200 avec un flag
        
        # Récupérer l'analyse
        analyse = ServiceAnalyse.get_analyse_complete()
        print(f"DEBUG - Analyse: {analyse}")
        
        if analyse is None:
            return jsonify({
                'donnees_existantes': False,
                'erreur': 'Pas assez de données pour l\'analyse (minimum 2 avis requis)'
            }), 200
        
        return jsonify({
            'donnees_existantes': True,
            'statistiques_globales': stats,
            'analyse': analyse
        })
        
    except Exception as e:
        traceback.print_exc()
        return jsonify({
            'donnees_existantes': False,
            'erreur': str(e)
        }), 500