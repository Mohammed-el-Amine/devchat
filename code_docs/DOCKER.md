# Docker cheat sheet

## Commandes Docker

```sh
$ docker ps # Visualiser les conteneurs actifs
$ docker ps -a # Visualiser tous les conteneurs
$ docker rm [container] # Supprimer un conteneur inactif
$ docker rm -f [container] # Forcer la suppression d'un conteneur actif
$ docker images # Lister les images existantes
$ docker rmi [image] # Supprimer une image docker
$ docker exec -t -i [container] /bin/bash # Exécuter des commandes dans un conteneur actif
$ docker inspect [container] # Inspecter la configuration d'un conteneur
$ docker build -t [image] . # Construire une image à partir d'un Dockerfile
$ docker history [image] # Visualiser l'ensemble des couches d'une image
$ docker logs --tail 5 [container] # Visualiser les logs d'un conteneur (les 5 dernières lignes)

# Intéractions avec le registry
$ docker login # Se connecter au registry
$ docker search [name] # Rechercher une image
$ docker pull [image] # Récupérer une image
$ docker push [image] # Pouser une image du cache local au registry
$ docker tag [UUID] [image]:[tag] # Tagger une image
```

## Commandes Docker Compose

```sh
$ docker-compose up -d # Démarre un ensemble de conteneurs en arrière-plan
$ docker-compose down # Stoppe un ensemble de conteneurs
$ docker-compose exec [service] [command] # Exécute une commande au sein d'un service
```

## Instructions Dockerfile

|Ordre|Instruction|Description|
|-----|-----------|-----------|
|1|FROM|Image parente|
|2|MAINTAINER|Auteur|
|3|ARG|Variables passées comme paramètres à la construction de l'image|
|4|ENV|Variable d'environnement|
|4|LABEL|Ajout de métadonnées|
|5|VOLUME|Crée un point de montage|
|6|RUN|Commande(s) utilisée(s) pour construire l'image|
|(6)|(ADD)|(Ajoute un fichier dans l'image \*[ADD vs COPY](https://nickjanetakis.com/blog/docker-tip-2-the-difference-between-copy-and-add-in-a-dockerile))|
|6|COPY|Ajoute un fichier dans l'image|
|6|WORKDIR|Permet de changer le chemin courant|
|7|EXPOSE|Port(s) écouté(s) par le conteneur|
|8|USER|Nom d'utilisateur ou UID à utiliser|
|9|ONBUILD|Instructions exécutées lors de la construction d'images enfants|
|10|CMD|Exécuter une commande au démarrage du conteneur|
|10|ENTRYPOINT|Exécuter une commande au démarrage du conteneur|

## Documentation officielle

- [Dockerfile reference](https://docs.docker.com/engine/reference/builder/#/dockerfile-reference)
- [The Docker commands](https://docs.docker.com/engine/reference/commandline)
- [Docker Compose](https://docs.docker.com/compose/)

## Autres ressources

- [Understanding Docker in sketchnotes](https://dev.to/aurelievache/understanding-docker-part-1-retrieve-pull-images-3ccn)

## Outils

- [dockly](https://github.com/lirantal/dockly) - Immersive terminal interface for managing docker containers and services