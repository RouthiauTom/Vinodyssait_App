# Moteur de jeu — résultat de phase 2

## Réalisé

`src/game/engine.ts` est un moteur TypeScript indépendant de React, du DOM, du réseau et du stockage. Il reçoit le plateau, la banque, les valeurs du dé/aléatoire et les instants en paramètres. Les transitions renvoient un nouvel état ; la révision de chaque action empêche la réapplication d’un clic devenu obsolète.

Règles implémentées : 2–10 joueurs, ordre de saisie, déplacement 1–6, montée des échelles 4→19 et 27→38 avant la question, activation à l’arrêt seulement, question correspondant à la case/région d’arrivée, choix de niveau des catégories 1–4, Domaines sans niveau, non-répétition par ID puis répétition du même filtre épuisé, QCM/vrai-faux par ensemble exact, réponses ouvertes révélées puis évaluées par le groupe, délai absolu de 60 secondes et expiration après reprise, correction avant application visible du recul, tapis 56→33 selon les résultats validés, victoire après réussite de la question finale avec dépassement limité à Corse, joueur suivant manuel.

L’arrêt du chronomètre oral se fait avant révélation/validation du groupe, et n’autorise pas de renverser une expiration. La lecture de correction se termine par l’action `continue`, qui applique la conséquence ; `next_player` est une action distincte. La victoire est affichable après la correction finale.

Les trois destinations d’effets du plateau validé ne sont pas des départs d’autres effets : aucune règle d’effets en chaîne n’a été ajoutée. Un filtre initialement vide provoque une erreur explicite et laisse l’état inchangé ; aucune catégorie/niveau de secours n’est inventée.

## Données

`data/questions.json` contient 673 questions structurées depuis les marqueurs explicites des sources, avec réponses/explications conservées. Les cinq corrections de format validées sont appliquées avec une trace par langue dans la provenance ; `data/preparation/questions.review.json` est désormais vide. Voir QUESTIONS_A_VALIDER.md. La provenance est marquée `source_extracted_not_editorially_verified`. Aucun contenu scientifique ou traduction n’a été corrigé. La source JSON complète de préparation conserve les champs CSV originaux.

Les états sont sérialisables en JSON. Une simulation de reprise vérifie le délai et la validation orale ; cela ne constitue pas une sauvegarde IndexedDB réelle, qui appartient à la prochaine tranche.

## Vérifications exécutées

- Vitest : 29 tests du moteur réussis, dont simulations de partie complète à 2 et 10 joueurs.
- Python unittest : 14 tests d’import/structuration réussis.
- TypeScript : `tsc --noEmit` réussi.
- Relecture du brouillon : `prepare_questions.py --check` réussi.
- SHA-256 du ZIP, des deux références et des deux CSV inchangés après le travail.

Aucun test navigateur, interface mobile, IndexedDB, mode avion ou build frontend n’est revendiqué. Cette tranche livre un moteur testé, pas encore l’application jouable avec interface.

## Exécution locale

Node était absent de l’environnement. Un runtime officiel Node 22 a été placé uniquement dans `.tools/`, après vérification de son SHA-256 publié par nodejs.org ; aucun outil système installé. Les dépendances de développement sont dans le projet et figées par package-lock.json. La configuration TypeScript emploie ESNext/Bundler pour la future UI, conformément à la [documentation TypeScript](https://www.typescriptlang.org/tsconfig/module.html).

Avec Node présent dans PATH : `npm test` puis `npm run typecheck`. Dans cet environnement, préfixer par `PATH="$PWD/.tools/node-v22.23.3-darwin-arm64/bin:$PATH"`. Tests de données : `python3 -B -m unittest discover -s tests/data -v`.

## Suite

Les cinq corrections de format sont validées et les 673 questions intégrées. La prochaine étape est de construire l’interface mobile et les adaptateurs. Les droits du logo, sons/police/autres visuels ne sont pas implicitement confirmés par ceux du plateau. La phase de préparation n’est pas déclarée entièrement close tant que la banque et ses signalements à examiner ne sont pas finalisés.
