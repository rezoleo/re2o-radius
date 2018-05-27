# Re2o-Radius

Ce projet sert de connecteur entre un serveur Radius et l'API de Re2o.

Il se connecte à l'API, récupère la liste des MAC enregistrées, et filtre pour vérifier que la MAC demandée est bien dedans.

## Installation

1. Cloner ce dépôt dans `/etc/raddb/scripts`
1. Copier `config.example.ini` en `config.ini`, insérer l'URL de Re2o et les informations de login d'un compte ayant les droits "serveur" (ancien système de droits, à vérifier avec le nouveau système d'ACL)
1. Installer les dépendances avec `pip3 install -r requirements.txt`
1. Tester que ça marche en lançant le script avec `./main.py swa1 01:23:45:67:89:00 fa0/12` (remplacer la MAC par une adresse acceptée puis une adresse non enregistrée)
1. Configurer Radius pour qu'il interroge le script à chaque nouvelle MAC détectée. Créer un fichier `/etc/raddb/users` avec ce contenu :
```
DEFAULT Auth-Type:=Accept
	Exec-Program-Wait = "/usr/bin/python3 /etc/raddb/scripts/re2o-radius/main.py %n %u %p"
```

## TODO list

* [ ] Gérer le cas si Re2o ne répond pas ➡ autoriser par défaut (VLAN 128)
* [ ] Trouver un endpoint de l'API Re2o qui permet de demander si *une* MAC est validée (plutôt que de lister l'intégralité des MAC à chaque fois, ce qui est un peu lourd pour le serveur Re2o)