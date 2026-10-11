# PWA et fonctionnement hors ligne

## Livraison

Le build crée un service worker avec un cache versionné par l’empreinte des fichiers compilés. Il précache les 17 fichiers publics et compilés : HTML, JavaScript (banque de questions et traductions incluse), CSS, plateau, logo, cartes FR/EN, police, manifeste, licence et icônes. Le serveur de développement ne l’enregistre pas.

L’accueil indique la disponibilité hors ligne seulement lorsque le service worker contrôle la page. Une installation incomplète échoue, supprime son cache partiel et conserve l’ancienne version. Les mises à jour attendent la fermeture de tous les onglets/fenêtres contrôlés ; aucun rechargement forcé pendant une partie. L’activation nettoie seulement les anciens caches de cette application et de ce sous-chemin. IndexedDB et les préférences ne sont pas supprimées. Le format de sauvegarde reste en version 1 : aucune migration nécessaire pour cette livraison. Une modification future du schéma demandera sa migration propre.

Le manifeste et les chemins relatifs permettent l’hébergement dans un sous-dossier GitHub Pages. Les icônes utilisent un monogramme VS sur fond violet/noir, défini en SVG et exporté en PNG. Le cycle installation/attente/activation suit la [documentation MDN des service workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API/Using_Service_Workers).

## Vérifications exécutées

- TypeScript et build Vite : réussis. Cache généré : 17 fichiers. Le bundle principal reste d’environ 1 Mo brut / 242 Ko gzip.
- 34 tests Vitest : réussis.
- 4 parcours Playwright existants : réussis (mobile, parties complètes à 2 et 10 joueurs, interface anglaise).
- Test Chromium de production sous `/vinodyssait/` : reprise après rechargement hors ligne, plateau/logo/police chargés, manifeste et icônes accessibles.
- Mise à jour : nouvelle version en attente, partie non interrompue ; fermeture/réouverture, nettoyage de l’ancien cache et reprise hors ligne réussis.
- Chronomètre expiré pendant la fermeture : correction et retour à la position précédente réussis hors ligne.
- Ressource indisponible pendant une mise à jour : installation rejetée, version précédente utilisable hors ligne.
- Premier téléchargement incomplet : aucun cache partiel conservé, aucun message de disponibilité hors ligne erroné.

Commandes : `npm test`, `npm run build`, puis `npm run test:pwa` avec Chromium Playwright installé. Les tests utilisent le navigateur local ; ils ne remplacent pas un essai physique.

## Essai utilisateur

1. Lancer `./scripts/preview.sh`, puis ouvrir l’URL affichée.
2. Attendre « Prêt à jouer hors ligne sur cet appareil. ».
3. Commencer une partie, couper la connexion dans les outils réseau du navigateur, recharger et reprendre.
4. Pour installer sur téléphone après hébergement HTTPS : option d’installation du navigateur Android ; Safari → Partager → Sur l’écran d’accueil sur iPhone/iPad.

Une première visite sans réseau ne fonctionne pas. Le navigateur peut évincer son stockage ; le cache local ne remplace pas une sauvegarde exportée. Aucun essai physique Android/iOS, installation depuis un écran d’accueil ou déploiement GitHub Pages effectué à ce stade.

## Suite

Essais sur téléphones et tablettes, puis préparation du dépôt et du déploiement GitHub Pages. Aucun blocage sur les règles pour cette étape. L’archive historique et les références sont restées inchangées.
