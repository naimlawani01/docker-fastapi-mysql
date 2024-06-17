# Projet FastAPI MySQL Docker

## Description

Ce projet est une application FastAPI basique qui utilise SQLAlchemy pour l'ORM et MySQL comme base de données, le tout containerisé avec Docker. L'application permet de réaliser des opérations CRUD (Create, Read, Update, Delete) sur un modèle Item.

## Installation

### Prérequis

Étapes
Clonez le dépôt :

```

git 
````

```
cd 

```

Construisez les images Docker :

```

docker-compose build

```

```

docker-compose up

````

## Endpoints de l'API

- #### POST /items/ : Créer un nouvel item

- #### GET /items/ : Récupérer tous les items

- #### GET /items/{item_id} : Récupérer un item spécifique par ID.

- #### PUT /items/{item_id} : Mettre à jour un item spécifique par ID

- #### DELETE /items/{item_id} : Supprimer un item spécifique par ID

## Difficultés rencontrées

- Problèmes d'importation de modules : Gérer les erreurs d'importation de modules, en particulier pour les modèles SQLAlchemy.
- Configuration de la base de données : Configurer la base de données dans Docker et s'assurer que l'application peut se connecter à MySQL.
- Réseau Docker : Gérer le réseau entre l'application FastAPI et le conteneur MySQL.
- j'ai rencontré des difficultés à configurer correctement MySQL via Docker Compose
