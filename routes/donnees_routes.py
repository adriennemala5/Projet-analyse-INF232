from flask import Blueprint, request, render_template, jsonify
from services.service_base_de_donnees import ServiceBaseDeDonnees

donnees_bp = Blueprint('donnees', __name__)

@donnees_bp.route('/soumettre', methods=['POST'])
def soumettre_avis():
    try:
        donnees = request.form.to_dict()
        
        # Validation des champs requis (SANS le champ nom)
        required_fields = ['filiere', 'age', 'niveau', 'heures_etude', 'heures_sommeil', 'note_moyenne', 'satisfaction']
        for field in required_fields:
            if field not in donnees or not donnees[field]:
                return jsonify({'erreur': f'Le champ {field} est requis'}), 400
        
        # Validation des plages
        if float(donnees['heures_etude']) < 0 or float(donnees['heures_etude']) > 24:
            return jsonify({'erreur': 'Les heures d\'étude doivent être entre 0 et 24'}), 400
        
        if float(donnees['heures_sommeil']) < 0 or float(donnees['heures_sommeil']) > 24:
            return jsonify({'erreur': 'Les heures de sommeil doivent être entre 0 et 24'}), 400
        
        if float(donnees['note_moyenne']) < 0 or float(donnees['note_moyenne']) > 20:
            return jsonify({'erreur': 'La note moyenne doit être entre 0 et 20'}), 400
        
        if int(donnees['satisfaction']) < 1 or int(donnees['satisfaction']) > 5:
            return jsonify({'erreur': 'La satisfaction doit être entre 1 et 5'}), 400
        
        # Sauvegarde
        id_avis = ServiceBaseDeDonnees.ajouter_avis(donnees)
        
        return jsonify({
            'succes': True,
            'message': 'Avis soumis avec succès!',
            'id': id_avis
        })
    
    except Exception as e:
        return jsonify({'erreur': str(e)}), 500

@donnees_bp.route('/liste', methods=['GET'])
def liste_avis():
    try:
        avis = ServiceBaseDeDonnees.get_donnees_pour_analyse()
        return render_template('liste_avis.html', avis=avis)
    except Exception as e:
        return jsonify({'erreur': str(e)}), 500

@donnees_bp.route('/api/liste', methods=['GET'])
def api_liste_avis():
    try:
        avis = ServiceBaseDeDonnees.get_donnees_pour_analyse()
        return jsonify({'avis': avis, 'total': len(avis)})
    except Exception as e:
        return jsonify({'erreur': str(e)}), 500