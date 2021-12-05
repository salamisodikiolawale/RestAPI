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
Note : utilisez des `validator` pour vous assurer que les ssn sont valides (https://pydantic-docs.helpmanual.io/usage/validators/), utilisez vos développements du TD précédent.

# Exercice 2 - Utilisation d'API tierces

Retravaillez l'appel `[GET] personnes` pour qu'il affiche des informations relatives au lieu de naissance.

Utilisez le service HTTP et le parsing de fichier :

- Lorsque la personne vient de France, utilisez l'API https://api.gouv.fr/les-api/api-geo afin d'afficher le vrai nom du département de naissance et le vrai nom de la commune.
- Lorsque la personne vient de l'étrager, utilisez le fichier `pays.json`

