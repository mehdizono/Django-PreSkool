# 🎓 PreSkool : School Management System


**PreSkool** est une application web de gestion scolaire complète développée avec le framework **Django**. Ce projet a été réalisé dans le cadre du module *Développement Web Avancé (Back-end Python)* au sein de la **LST IDAI** (Faculté des Sciences et Techniques de Tanger).

L'application permet de centraliser la gestion des étudiants, des enseignants, des départements, des emplois du temps et des résultats académiques via une interface intuitive et sécurisée.

---

## 📑 Table des Matières
1. [✨ Fonctionnalités](#-fonctionnalités)
2. [🏗️ Architecture du Projet](#️-architecture-du-projet)
3. [🛠️ Technologies Utilisées](#️-technologies-utilisées)
4. [🚀 Installation et Lancement](#-installation-et-lancement)
5. [👥 Authentification et Rôles](#-authentification-et-rôles)
6. [📐 Modèle de Données](#-modèle-de-données)
7. [📂 Structure du Dépôt](#-structure-du-dépôt)
8. [🎥 Démonstration](#-démonstration)

---

## ✨ Fonctionnalités

### 👨‍💼 Administration
*   **Gestion CRUD complète** : Étudiants, Enseignants, Parents, Départements et Matières.
*   **Affectation** : Liaison des enseignants aux départements et des matières aux enseignants.
*   **Interface d'administration** : Utilisation de l'admin Django personnalisé pour une gestion rapide des données.

### 👩‍🏫 Espace Enseignant
*   **Consultation** : Visualisation de l'emploi du temps et des matières assignées.
*   **Examens** : Planification des examens et saisie des notes des étudiants.

### 🎓 Espace Étudiant
*   **Tableau de bord** : Vue d'ensemble des statistiques personnelles.
*   **Scolarité** : Consultation des notes d'examen et de l'emploi du temps.
*   **Calendrier** : Accès aux jours fériés et événements de l'école.

---

## 🏗️ Architecture du Projet

Le projet respecte l'architecture **MVT (Model-View-Template)** de Django et est divisé en trois applications modulaires :

1.  **`home_auth`** : Gestion du modèle utilisateur personnalisé (`CustomUser`), inscription, connexion et gestion des permissions par rôles.
2.  **`student`** : Gestion du cycle de vie des étudiants et de leurs relations avec les parents.
3.  **`faculty`** : Cœur académique (Enseignants, Départements, Matières, Examens, Emplois du temps).

---

## 🛠️ Technologies Utilisées

| Secteur | Technologie |
| :--- | :--- |
| **Backend** | Python 3.11+ / Django 4.x |
| **Frontend** | HTML5, CSS3 (Bootstrap 5), JavaScript |
| **Base de données** | SQLite (par défaut) |
| **Traitement Image** | Pillow (pour les profils étudiants/enseignants) |
| **Versionnage** | Git / GitHub |

---

## 🚀 Installation et Lancement

### Prérequis
*   Python 3.10 ou supérieur installé.
*   `pip` (gestionnaire de paquets Python).

### Étapes d'installation
1.  **Cloner le projet** :
    ```bash
    git clone https://github.com/votre-username/PFM__Python.git
    cd PFM__Python
    ```

2.  **Créer un environnement virtuel** :
    ```bash
    python -m venv monenv
    # Activation (Windows)
    monenv\Scripts\activate
    # Activation (Linux/Mac)
    source monenv/bin/activate
    ```

3.  **Installer les dépendances** :
    ```bash
    pip install -r requirements.txt
    ```

4.  **Appliquer les migrations** :
    ```bash
    cd school
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Lancer le serveur** :
    ```bash
    python manage.py runserver
    ```
    Accédez à l'application via : `http://127.0.0.1:8000/`

---

## 👥 Authentification et Rôles

Le système utilise un modèle **RBAC (Role-Based Access Control)**. Voici les comptes de test configurés :

| Rôle | Email / Login | Mot de passe |
| :--- | :--- | :--- |
| **Administrateur** | `admin@gmail.com` | `admin` |
| **Enseignant** | `teacher@gmail.com` | `teacher` |
| **Étudiant** | `student@gmail.com` | `student` |

---

## 📐 Modèle de Données

Le projet s'appuie sur des relations SQL complexes pour garantir l'intégrité des données :
*   **OneToOneField** : Entre `Student` et `Parent`.
*   **ForeignKey** : Entre `Subject` et `Teacher`, ou `ExamResult` et `Student`.
*   **AbstractUser** : Extension du modèle Django pour inclure les booléens `is_admin`, `is_teacher`, `is_student`.

---

## 📂 Structure du Dépôt

```text
PFM__Python/
├── school/                 # Projet Django Principal
│   ├── faculty/            # App : Gestion académique
│   ├── student/            # App : Gestion des élèves
│   ├── home_auth/          # App : Sécurité & Utilisateurs
│   ├── static/             # Assets (CSS, JS, Images)
│   ├── templates/          # Fichiers HTML (Base & Modules)
│   └── manage.py           # CLI Django
├── requirements.txt        # Dépendances du projet
└── README.md               # Documentation principale
```
---

##🎥 Démonstration Vidéo

https://github.com/user-attachments/assets/e6c94e1e-59ef-46aa-9f23-38a64d6b9042





