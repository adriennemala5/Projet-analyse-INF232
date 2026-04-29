import sqlite3
import json
from datetime import datetime
from config import Config

class DonneesAcademiques:
    
    @classmethod
    def _get_connexion(cls):
        return sqlite3.connect(Config.DATABASE)
    
    @classmethod
    def initialiser_base(cls):
        with cls._get_connexion() as conn:
            curseur = conn.cursor()
            curseur.execute('''
                CREATE TABLE IF NOT EXISTS avis_etudiants (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    filiere TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    niveau TEXT NOT NULL,
                    heures_etude REAL NOT NULL,
                    heures_sommeil REAL NOT NULL,
                    note_moyenne REAL NOT NULL,
                    satisfaction INTEGER NOT NULL,
                    commentaire TEXT,
                    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()
    
    @classmethod
    def sauvegarder_avis(cls, donnees):
        with cls._get_connexion() as conn:
            curseur = conn.cursor()
            curseur.execute('''
                INSERT INTO avis_etudiants 
                (filiere, age, niveau, heures_etude, heures_sommeil, note_moyenne, satisfaction, commentaire)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                donnees.get('filiere'),
                int(donnees.get('age')),
                donnees.get('niveau'),
                float(donnees.get('heures_etude')),
                float(donnees.get('heures_sommeil')),
                float(donnees.get('note_moyenne')),
                int(donnees.get('satisfaction')),
                donnees.get('commentaire', '')
            ))
            conn.commit()
            return curseur.lastrowid
    
    @classmethod
    def charger_tous_avis(cls):
        with cls._get_connexion() as conn:
            curseur = conn.cursor()
            curseur.execute('SELECT * FROM avis_etudiants ORDER BY date_creation DESC')
            colonnes = [description[0] for description in curseur.description]
            avis = []
            for ligne in curseur.fetchall():
                avis_dict = dict(zip(colonnes, ligne))
                avis_dict['date_creation'] = str(avis_dict['date_creation'])
                avis.append(avis_dict)
            return avis
    
    @classmethod
    def get_statistiques_globales(cls):
        with cls._get_connexion() as conn:
            curseur = conn.cursor()
            curseur.execute('SELECT COUNT(*) FROM avis_etudiants')
            total = curseur.fetchone()[0]
            
            print(f"DEBUG - Total avis dans get_statistiques_globales: {total}")  # Pour debug
            
            if total == 0:
                return {}
            
            curseur.execute('''
                SELECT 
                    AVG(heures_etude) as moy_etude,
                    AVG(heures_sommeil) as moy_sommeil,
                    AVG(note_moyenne) as moy_note,
                    AVG(satisfaction) as moy_satisfaction,
                    MIN(heures_etude) as min_etude,
                    MAX(heures_etude) as max_etude,
                    MIN(heures_sommeil) as min_sommeil,
                    MAX(heures_sommeil) as max_sommeil,
                    MIN(note_moyenne) as min_note,
                    MAX(note_moyenne) as max_note
                FROM avis_etudiants
            ''')
            stats = curseur.fetchone()
            
            result = {
                'total_etudiants': total,
                'moyenne_heures_etude': round(stats[0] or 0, 2),
                'moyenne_heures_sommeil': round(stats[1] or 0, 2),
                'moyenne_notes': round(stats[2] or 0, 2),
                'moyenne_satisfaction': round(stats[3] or 0, 2),
                'min_heures_etude': stats[4] or 0,
                'max_heures_etude': stats[5] or 0,
                'min_sommeil': stats[6] or 0,
                'max_sommeil': stats[7] or 0,
                'min_note': stats[8] or 0,
                'max_note': stats[9] or 0
            }
            
            print(f"DEBUG - Statistiques calculées: {result}")  # Pour debug
            return result
