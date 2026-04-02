🎓 Preskool - Système de Gestion Scolaire (Django)
📌 Présentation du Projet
Preskool (PFM-PYTHON) est une application web complète de gestion scolaire développée avec le framework Django. Ce projet suit l'architecture MVT (Model-View-Template) et propose une gestion dynamique des étudiants, des enseignants et de l'administration via un système de rôles .
Ce projet a été réalisé dans le cadre du module Développement Web Avancé (Licence Génie Informatique - FST Tanger).
<video src="static/assets/demo.webm" controls width="100%"></video>
✨ Matrice des Droits & Fonctionnalités
Module / Action	🔑 Administrateur	👨‍🏫 Enseignant	🎓 Étudiant
Tableau de Bord (Dashboard)	📊 Vue Globale	📈 Vue Partielle	👤 Vue Profil
Gestion Étudiants & Parents	✅ CRUD Complet	👁️ Lecture	❌ Aucun
Gestion Enseignants	✅ CRUD Complet	❌ Aucun	❌ Aucun
Saisie des Notes & Examens	✅ Configuration	📝 Saisie / Edit	👁️ Lecture Seule
Emploi du temps & Matières	✅ Gestion Totale	👁️ Consultation	👁️ Consultation
Calendrier & Jours Fériés	✅ Gestion	👁️ Lecture	👁️ Lecture
Redirection après Login	🚀 Vers Admin	🏫 Vers Faculty	📖 Vers Student
Légende :
✅ CRUD (Créer, Lire, Modifier, Supprimer) | 📝 Saisie autorisée | 👁️ Lecture seule | ❌ Accès refusé
✅ Accès complet | 👁️ Lecture seule | ❌ Pas d'accès

🗂️ Architecture & Modules
Le projet est découpé en 3 applications Django indépendantes pour une meilleure modularité :
home_auth : Gestion de l'authentification personnalisée (CustomUser), des rôles et de la sécurité.
faculty : Gestion des Enseignants, Départements, Matières, Examens et Emplois du temps.
student : Gestion des Étudiants et de la relation avec les Parents.

📐 Modèle de Données (Relations Clés)
CustomUser : Étend AbstractUser pour inclure les booléens is_admin, is_teacher, is_student.
Student & Parent : Relation OneToOne (un étudiant possède un profil parent).
Teacher & Department : Relations ForeignKey et ManyToMany pour l'attribution des chefs de département.
Timetable : Relie les matières (Subject) et les enseignants (Teacher).

🚀 Installation et Configuration
1. Prérequis
Python 3.10+
Git
2. Installation
code
Bash
# Cloner le dépôt
git clone https://github.com/aymanam12/PFM-PYTHON.git
cd PFM-PYTHON

# Créer un environnement virtuel
python -m venv venv

# Activer l'environnement
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Installer Django et les dépendances
pip install django Pillow
3. Base de données et Serveur
code
Bash
# Appliquer les migrations
python manage.py makemigrations
python manage.py migrate

# Créer un compte administrateur
python manage.py createsuperuser

# Lancer le serveur
python manage.py runserver
Accès à l'application : http://127.0.0.1:8000
🛠️ Technologies Utilisées
Back-end : Python 3, Django 5+
Front-end : HTML5, CSS3 (Bootstrap 5), JavaScript
Base de données : SQLite (par défaut)
Gestion d'images : Pillow (pour les photos de profil)
📁 Structure du Projet
code
Text
PFM-PYTHON/
├── school/                 # Configuration principale (settings, urls)
├── home_auth/              # Application Authentification
├── faculty/                # Application Enseignants & Académique
├── student/                # Application Étudiants
├── static/                 # Assets (CSS, JS, Images)
├── templates/              # Fichiers HTML
│   ├── Home/               # Base et Dashboard
│   ├── teachers/           # Vues Enseignants
│   ├── students/           # Vues Étudiants
│   └── authentification/   # Login / Register
└── manage.py

💡 Améliorations Spécifiques (UI/UX)
Barre latérale optimisée : Le bouton Logout est fixé en bas de la sidebar via Flexbox pour une navigation plus ferme et ergonomique.
Routage Dynamique : Utilisation systématique de la balise {% url %} pour éviter les erreurs de chemins relatifs.
Interface Responsive : Adaptation du tableau de bord pour mobile et tablettes.

👥 Comptes de Test
Admin : admin@gmail.com / admin123
Enseignant : teacher@teacher.com / teacher123
Étudiant : student@student.com / student123

### 📥 Importation des données de test
Si vous souhaitez charger des données de démonstration (comptes, étudiants, matières) :
1. Assurez-vous d'avoir fait les migrations : `python manage.py migrate`
2. Chargez les données : `python manage.py loaddata initial_data.json`
