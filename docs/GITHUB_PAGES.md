# Publication GitHub Pages et tests téléphone

## Préparation

Le dépôt configuré est `RouthiauTom/Vinodyssait_App`, branche `main`. Le workflow `.github/workflows/pages.yml` lance les tests unitaires, compile, teste les parcours de jeu et le mode hors ligne, contrôle les fichiers publiables, puis déploie exclusivement `dist/`. L’archive historique et `sources/` sont exclus de Git. Les questions jouables restent dans la banque locale de l’application.

Cette configuration suit la [documentation officielle GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages). Aucun serveur de jeu n’est nécessaire.

## Actions à effectuer sur GitHub

1. Dans le dépôt, ouvrir **Settings → Pages**.
2. Dans **Build and deployment → Source**, sélectionner **GitHub Actions**.
3. Pousser la branche `main` préparée localement.
4. Dans **Actions**, ouvrir « Tests et publication GitHub Pages » et attendre que `build` puis `deploy` soient verts. En cas de besoin, relancer avec **Run workflow**.
5. Ouvrir l’adresse HTTPS affichée par GitHub dans **Settings → Pages** ou dans le job `deploy`.

Adresse attendue, à confirmer après un déploiement réussi :
`https://routhiautom.github.io/Vinodyssait_App/`

L’adresse ne constitue pas une preuve de publication. Le dépôt doit disposer de GitHub Pages selon son offre et ses paramètres. Le workflow n’a pas encore été exécuté sur GitHub au moment de cette préparation. Le push est effectué par l’utilisateur.

## Tests sur téléphone

Sur Android avec Chrome et sur iPhone/iPad avec Safari :

1. Ouvrir l’URL HTTPS et attendre « Prêt à jouer hors ligne sur cet appareil. ».
2. Installer via l’option du navigateur Android, ou Safari → Partager → Sur l’écran d’accueil. Ouvrir ensuite l’application installée et attendre à nouveau le message hors ligne : le stockage peut différer entre navigateur et application installée.
3. Faire une partie à deux : dé, choix de niveau, question, correction et joueur suivant. Vérifier aussi le français/anglais, le zoom/déplacement du plateau et les réglages sonores.
4. Activer le mode avion, fermer puis rouvrir l’application installée, reprendre la partie et répondre à une nouvelle question.
5. Fermer pendant une question, attendre plus de 60 secondes, rouvrir et vérifier la correction pour temps écoulé.
6. Tester une partie à dix joueurs et la lisibilité sur tablette. Vérifier une victoire en Corse avec dernière réponse correcte.

Noter le modèle, la version du système, le navigateur, l’utilisation en navigateur ou depuis l’écran d’accueil, et les étapes de chaque problème. Pour une nouvelle version, reconnecter l’appareil puis fermer toutes les fenêtres/onglets du jeu après téléchargement de la mise à jour. Aucune sauvegarde n’est partagée entre appareils.
