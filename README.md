# QR_Code_System
The QR code generator backend

## Guide
* Suivez l'exemple d'environnement .env.example
* Entrer principale de l'application : *run.py*
* Demmarage de l'API: `uvicorn run:app --reload`

## Description des fichiers

### api/v1
Il regrouper les fichier suivant:
* `routes` : Dossier qui contiendra toutes les routes de l'api 
* `app.py` : L'entree principale de l'api qui defini les configuration et les routes de l'api

### databases
Dossier contenant tous les fichiers sql de la base de donnees. Elle sera utiles pour des migrations de donnees

### models
Le dossier des models de l'application
* `engines` : Dossier qui regroupe de le gestion de base de donnees situe dans `db_storage.py`
* `base.py` : Model de base des modeles de l'app
Les autres fichiers representent chacune les models (tables) de donnees

### output
Ce dossier comporte toutes les images de qr_code qui seront generes. Il faut cree un dossier `qr_codes` dans celui ci

### src
Dossier comportant toutes les logiques internes du system

### tests
Dossier des test unitaires des codes

