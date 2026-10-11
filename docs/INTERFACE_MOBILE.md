# Interface mobile — bilan de la tranche

## Résultat

Une interface React/TypeScript locale utilise le moteur validé et les 673 questions bilingues. Parcours : accueil, configuration de 2–10 joueurs, plateau original, dé, niveau, tirage, QCM simples/multiples, vrai/faux, questions orales, correction, conséquence, joueur suivant et victoire. Les noms suivent l’ordre de saisie. Les pions numérotés et colorés sont alignés sur les centres validés et regroupés autour d’une case lorsqu’ils la partagent.

Le plateau propose des boutons de zoom, un déplacement au pointeur/tactile et un zoom à deux pointeurs. Le clavier peut déplacer la vue avec les flèches. Le respect de la réduction des animations est prévu. Les dialogues retiennent le focus, se ferment avec Échap et rendent le focus au déclencheur.

Les questions et réponses FR/EN proviennent de la banque fournie. Les libellés des nouveaux écrans et les résumés de règles dans `src/i18n/ui.ts` sont des propositions éditoriales d’interface à relire ; ils ne modifient aucune question historique ni règle du moteur. La langue d’une partie est choisie à la configuration ; le sélecteur est désactivé dans la partie pour conserver sa langue.

## Sauvegarde locale incluse

IndexedDB conserve une seule partie, avec validation de forme et IDs de questions à la lecture. Les écritures sont séquentielles. La fermeture/réouverture retrouve la phase et la question, et l’échéance absolue continue à s’écouler ; une question ouverte déjà révélée ne redémarre pas son chronomètre. Une erreur de stockage est affichée sans promettre une sauvegarde réussie. Remplacer une partie ou effacer la sauvegarde exige une confirmation. Les paramètres langue/sons sont locaux.

Ce socle anticipe la phase 4 : il ne constitue pas une migration complète des versions de contenu, une synchronisation entre onglets, ni une qualification du stockage sur tous les appareils. Le numéro de schéma est contrôlé ; une version inconnue est refusée.

## Visuel et sons

Le plateau public est une copie exacte de l’image autorisée, seule ressource historique transférée dans cette tranche. Marque en texte, pions numérotés, couleurs bordeaux/crème et polices système : aucun logo/avatar/police non autorisé transféré. Les sons de boutons et des dix dernières secondes sont des signaux synthétiques facultatifs, désactivés par défaut. Les sons historiques attendent la confirmation de leurs droits avant transfert.

## Fichiers principaux

- `src/App.tsx` : écrans et orchestration des actions du moteur.
- `src/components/Board.tsx` : plateau, pions, zoom et déplacement.
- `src/storage/save.ts` : reprise et écritures IndexedDB.
- `src/i18n/ui.ts`, `src/styles.css` : libellés FR/EN et responsive.
- `index.html`, `src/main.tsx`, `vite.config.ts` : entrée et build statique (base relative).
- `tests/e2e/ui.pw.ts`, `tests/game/save.test.ts` : parcours et validation des sauvegardes.
- `scripts/dev.sh`, README : lancement local.

Les dépendances de développement ont été mises à jour : Vitest 5, React, Vite, types et Playwright, avec lockfile. L’installation finale ne signale aucune vulnérabilité npm. Les outils restent dans le projet, sans modification de l’archive historique. Mise en place manuelle conforme aux [instructions Vite](https://vite.dev/guide/), cycle de vie conforme à la [documentation React useEffect](https://react.dev/reference/react/useEffect).

## Vérifications exécutées

- 34 tests Vitest réussis (29 moteur, 5 validation de sauvegarde).
- 14 tests de données Python réussis et contrôle du brouillon réussi.
- 4 parcours Playwright Chromium réussis : mobile 390 × 844 (configuration, zoom, reprise, réglages), partie complète à 2 joueurs, partie complète à 10 joueurs, langue anglaise et confirmation avant remplacement.
- TypeScript et compilation Vite réussis ; `dist/` produit. Le bundle principal est d’environ 1 Mo non compressé (242 Ko gzip), banque locale comprise ; optimisation ultérieure possible.
- Captures desktop et mobile inspectées : `interface-accueil.png`, `interface-mobile.png`.
- Références, ZIP et deux CSV : SHA-256 inchangés. Plateau public identique à la copie originale.

Les tests de partie utilisent des tirages déterministes. Un premier test repérait les questions par leur intitulé ; des intitulés identiques peuvent désigner des IDs et choix différents. Il utilise désormais l’ID réel affiché par l’interface. Le navigateur de test utilise le canal Chromium complet, le headless-shell téléchargé ayant montré une instabilité GPU/ICU dans cet environnement.

Aucun essai sur téléphone/tablette physique, test exhaustif du geste de pincement, test audio matériel ou certification d’accessibilité effectué. Aucun test de rechargement hors ligne effectué : le service worker PWA n’existe pas encore.

## Lancer et poursuivre

À la racine, exécuter `./scripts/dev.sh`, puis ouvrir l’URL locale affichée (normalement http://127.0.0.1:5173/). Rien n’est publié ; seul `dist/` est destiné à une publication future, jamais le dossier contenant les références/CSV/ZIP.

La prochaine tranche porte sur PWA/cache, mises à jour et récupération de sauvegarde plus approfondie, puis essais physiques et GitHub Pages. La définition de terminé web du cahier n’est pas encore atteinte : le rechargement hors ligne et la publication restent à réaliser.

## Identité visuelle historique — 11 octobre 2026

À la demande de l’utilisateur : retour au fond noir, texte blanc, boutons violets et couleurs historiques des niveaux. Le logo et les six cartes de menu FR/EN sont copiés depuis l’archive en lecture seule. Jost est embarquée localement, avec sa licence OFL dans `public/fonts/OFL.txt` (source : dépôt Google Fonts, `ofl/jost`). Aucun chargement distant de police n’est nécessaire.

Les messages de correction sont désormais complets, sans numéro : « Tu restes sur ta case. », « Tu reviens à ta position avant le lancer. », « Tu descends au bas du tapis. ». Les indications de position utilisent le nom de la région ou de la catégorie ; les numéros de pions désignent toujours les joueurs. Les règles et le moteur ne changent pas.

Compilation TypeScript/Vite et quatre parcours Chromium exécutés avec succès. Les parcours de partie complète vérifient aussi le texte exact « Tu restes sur ta case. ». Captures accueil et mobile actualisées et inspectées. Empreinte SHA-256 de l’archive historique inchangée.
