L'objectif de ce TD est de reprendre les développements réalisés dans le TD sur Docker et d'étendre cela à une API Rest.
Ceci n'est qu'une introduction aux API Rest et vous ne traiterez pas l'asynchronisme ni les aspects liés à la sécurité / authentification / autorisation.

# Exercice 1 - API Rest avec FastAPI

Faites une API Rest avec FASTAPI qui accède à une base de donnée mongodb afin de fournir les endpoits suivants :

- [GET] personnes
- [POST] personnes
- [GET] personnes/ssn
- [DELETE] personnes/ssn
- [UPDATE] personnes/ssn

Le modèle utilisé, nommé `ModelPersonne`, doit être composé d'un `nom`, `prenom` et `ssn`.

**Indications** : vous utiliserez deux conteneurs, le premier remplira la base de donnée (cf. précédent TD), le second exposera l'API Rest sur le port 3000. Il est attendu que votre modèle soit défini dans une fichier `model_personne.py`, votre application RestAPI soit définie dans un fichier `app.py`, la logique associée au parsing de ssn soit contenu dans un fichier `ssn_parser.py`.

**Note** : utilisez des `validator` pour vous assurer que le ssn du modèle est valide (https://pydantic-docs.helpmanual.io/usage/validators/).

# Exercice 2 - Utilisation d'API tierces

Retravaillez l'endpoint `[GET] personnes` pour qu'il affiche plus d'informations.

Celui-ci devra permettre d'afficher (si spécifié) les informations suivantes :

- le sex de la personne,
- la date de naissance de la personne (mois calendaire + année);
- le lieu de naissance;
- la position.

Dans le cas du lieu de naissance, utilisez le service HTTP et le parsing de fichier :

- Lorsque la personne vient de France, utilisez l'API https://api.gouv.fr/les-api/api-geo afin d'afficher le vrai nom du département de naissance et le vrai nom de la commune.
- Lorsque la personne vient de l'étrager, utilisez le fichier `pays.json`

**Note** : il serait bon de tester votre parsing de ssn afin de vous assurer que les informations extraites sont cohérentes.
