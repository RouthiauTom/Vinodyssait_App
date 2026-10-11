# Vinodys’Sait

Application locale React/TypeScript : 2 à 10 joueurs sur un appareil partagé, plateau original, 673 questions FR/EN, moteur indépendant et reprise IndexedDB.

## Lancer

Avec Node 22.12+ installé : `npm ci`, puis `npm run dev`. Ouvrir l’URL locale affichée. Vous pouvez aussi lancer `./scripts/dev.sh`, qui utilise Node installé ou le runtime local du projet. Dans cet environnement, ce runtime est local au projet :

```sh
export PATH="$PWD/.tools/node-v22.23.3-darwin-arm64/bin:$PATH"
npm run dev
```

## Vérifier

```sh
npm test
npm run build
python3 -B -m unittest discover -s tests/data -v
```

Parcours Chromium : `PLAYWRIGHT_BROWSERS_PATH="$PWD/.tools/browsers" npm run test:e2e` (Chromium doit être installé dans ce dossier). Les tests de l’interface jouent des parties déterministes pour vérifier les transitions ; en utilisation normale, le dé et les questions sont tirés aléatoirement.

## État

L’interface, les questions, le moteur, la sauvegarde locale et le cache PWA sont présents. Le rechargement hors ligne est testé après un premier chargement complet. La publication GitHub Pages et les essais sur appareils physiques restent à réaliser.

Les réglages sonores emploient de courts sons synthétiques, désactivés par défaut. Le logo et les cartes du menu historiques sont repris à la demande de l’utilisateur. La police Jost est embarquée localement avec sa licence OFL. Les pions numérotés distinguent les joueurs autrement que par couleur ; les messages ne donnent plus de numéro de case. Les sons historiques et avatars ne sont pas intégrés.

Références et ZIP historique restent intacts. Sources CSV en `sources/questions/`, données dérivées en `data/`, documentation en `docs/`.

## Installer et tester le mode hors ligne

Le cache PWA est activé sur la version compilée, pas sur le serveur de développement. Le raccourci `./scripts/preview.sh` compile puis démarre cette version, avec le Node local si nécessaire. Avec Node accessible :

```sh
npm run build
npm run preview
```

Ouvrir l’URL affichée et attendre « Prêt à jouer hors ligne sur cet appareil. ». Ensuite, l’application peut se recharger et reprendre une partie sans connexion. Sur Android, utiliser l’option d’installation du navigateur ; sur iPhone/iPad, Safari → Partager → Sur l’écran d’accueil. La disponibilité de cette option dépend du navigateur. Le déploiement doit utiliser HTTPS ; localhost convient aux tests locaux.

Les nouvelles versions se téléchargent en arrière-plan et s’activent après fermeture de tous les onglets/fenêtres du jeu. Elles conservent IndexedDB et les préférences. Un téléchargement incomplet conserve la version précédente. Pour le test automatisé production/hors ligne/sous-chemin : `npm run test:pwa` après compilation (Chromium Playwright requis).

## GitHub Pages

Le workflow `.github/workflows/pages.yml` publie uniquement `dist/` après réussite des tests. Activer **Settings → Pages → Source: GitHub Actions**, puis pousser `main`. Les étapes de publication et le protocole de test sur téléphone sont décrits dans [docs/GITHUB_PAGES.md](docs/GITHUB_PAGES.md).

Les contrôles Python de préparation des données nécessitent les CSV de `sources/questions/`, conservés localement et exclus du dépôt publié. La CI valide la banque jouable avec les tests du moteur et les parcours navigateur.
