# Projet de prise de rendez-vous en ligne

## Contexte
Un coach en développement personnel souhaite un système de prise de rendez-vous automatique en ligne. Votre mission est d'aider ce coach en développant un site web qui répondra à ses besoins

## Fonctionnalités souhaitées 
- Une page d'accueil qui présente son travail
- Un système d'authentification pour permettre au coach et aux utilisateurs de se connecter au site
- Un système de prise de rendez-vous
- Un historique des séances précédentes avec chaque client, avec la possibilité pour le coach de conserver des notes sur chacune des séances

## Prise de rendez-vous
- Le coach ne peut être dans deux rendez-vous en même temps.
- Il doit y avoir au moins 10 minutes entre deux rendez-vous. ( enlever car pas nécessaire et rendez vous predéfini)
- Les rendez-vous ne peuvent être pris que de 9h à 12h30 et de 13h30 à 17h. (modifier pour ma part 9h à 12h et de 13h à 17h)
- Lors de la prise de rendez-vous, le client peut remplir un formulaire indiquant l'objet de la séance.

## Installation du projet

1. Téléchargez ou clonez ce dépôt sur votre ordinateur.
2. Créez un environnement virtuel et activez-le.
3. Installez les dépendances requises en exécutant la commande suivante dans votre terminal : `pip install -r requirements.txt`

### Mettre en place la base de données :
Exécutez les commandes suivantes dans votre terminal pour créer les tables nécessaires dans votre base de données : `python manage.py makemigrations` puis `python manage.py migrate`

### Lancer le serveur de développement :
Exécutez la commande suivante pour démarrer le serveur de développement : `python manage.py runserver`

Accédez à l'application en entrant http://localhost:8000/ dans votre navigateur web.

## Le compte Coach Admin est déjà créé dans la base de données

- Il dispose d'un email `CoachAdmin@outlook.fr` et d'un mot de passe `Admin`.
- Surtout ne pas le supprimer de la base de données et ne pas modifier son mot de passe car il est le seul compte Admin Coach.
- Car son id est utilisé dans le code et le changement de son id dans la base de données peut causer des erreurs.

## Docstrings et commentaires
Les docstrings et les commentaires sont présents dans le code pour vous aider à comprendre le fonctionnement de l'application.

## Les clients
Vous pouvez créer des clients avec le formulaire d'inscription .

## Les rendez-vous
Vous pouvez créer des rendez-vous avec le formulaire de prise de rendez-vous.

## Les notes
Vous pouvez créer des notes avec le formulaire de création de note.


## Auteurs
* **Thomas.l59** _alias_ [@DonzerHD](https://github.com/DonzerHD)

## Contact
Si vous avez des questions ou trouver des bugs, vous pouvez me contacter à l'adresse suivante : `thomas.lemay59@outlook.fr`.
N'hésitez pas à me faire part de vos remarques et suggestions.

## Licence
Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
