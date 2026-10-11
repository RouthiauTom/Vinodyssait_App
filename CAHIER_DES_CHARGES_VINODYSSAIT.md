# VINODYS'SAIT — CAHIER DES CHARGES FONCTIONNEL ET TECHNIQUE
Version 1.0 — 11 octobre 2026 — Document destiné à Codex / VS Code

## Légende
- **[VALIDÉ]** Décision explicitement confirmée par le porteur du projet.
- **[RECOMMANDÉ]** Proposition technique à valider.
- **[À VÉRIFIER]** Point non établi, à contrôler dans les sources ou avec le porteur.

## 1. Objet et vision
**[VALIDÉ]** Dématérialiser entièrement Vinodys'Sait, jeu de société inspiré du jeu de l'oie sur le thème du vin. Préserver les aspects du jeu physique et de la première webapp : identité visuelle, catégories, niveaux, questions, règles et ressources pertinentes. Le code historique sert exclusivement de référence en lecture seule.

**[VALIDÉ]** Première publication GitHub Pages ; publication Android/Play Store et iOS/App Store envisagée après stabilisation. Projet personnel gratuit, sans publicité ni compte utilisateur.

## 2. Public et contraintes
- **[VALIDÉ]** 2 à 10 joueurs, individuels, sur un appareil partagé ; pas de multijoueur en ligne.
- **[VALIDÉ]** Priorité smartphone et tablette ; partie d'environ 45 minutes ; ton convivial ; public débutant à expert.
- **[VALIDÉ]** Français et anglais ; partie jouable hors ligne après première installation/chargement.
- **[VALIDÉ]** Une seule partie en cours, sauvegarde automatique, reprise sur le même navigateur et appareil.
- **[VALIDÉ]** Sons configurables ; conservation des sons historiques lorsque possible.

## 3. Inventaire de l'existant — éléments vérifiés dans l'archive
L'archive fournie `VinodysSait_Game.zip` contient notamment :
- `vinodys-sait-frontend/` avec React, dont `src/components/GamePlay.js` et `GamePlay.css` ;
- `server/` avec routes Express (`game.js`, `auth.js`, `profiles.js`, `extensions.js`) ;
- `server/prisma/schema.prisma` : modèles `User`, `Profile`, `Game`, `Category`, `Question`, `QuestionTranslation`, `Domain` et autres modèles associés ;
- des ressources graphiques et sonores ;
- un dépôt `.git` historique inclus dans l'archive.

**[À VÉRIFIER]** Faire un audit détaillé des composants, écrans, ressources et règles réellement codées avant de copier ou remplacer une fonctionnalité. Le schéma Prisma indique une base PostgreSQL, mais ne constitue pas une exportation des enregistrements de questions. Le porteur indique posséder les questions dans des fichiers : leur localisation et leur format exact restent à confirmer. Ne pas prétendre disposer de toutes les questions sans avoir identifié les fichiers.

## 4. Parcours d'une partie
1. Accueil, langue FR/EN et choix « Nouvelle partie » ou « Reprendre » si sauvegarde disponible.
2. Saisie de 2 à 10 joueurs, avec nom et pion/couleur identifiable ; ordre de jeu défini.
3. Plateau illustré avec position de chaque joueur et mise en évidence du joueur actif.
4. Le joueur actif lance un dé virtuel à six faces.
5. Son pion avance selon l'ordre réel des cases.
6. La case atteinte détermine le contexte de question et/ou un effet spécial.
7. Le joueur choisit son niveau **avant chaque question** : Primeur, Grand Cru, Millésime.
8. L'application présente une question compatible et un compte à rebours de 60 secondes.
9. La réponse est corrigée ; l'explication/réponse attendue s'affiche ; le déplacement définitif est résolu.
10. Le joueur lit la correction puis appuie sur « Joueur suivant ».
11. L'application sauvegarde l'état aux transitions significatives.
12. Le premier joueur qui atteint ou dépasse la dernière case en Corse gagne.

**[À VÉRIFIER]** Ordre exact des effets spéciaux par rapport à la question, aux pénalités et à la victoire ; ne pas figer le comportement avant validation des règles.

## 5. Règles métier confirmées
- **[VALIDÉ]** Dé classique de 1 à 6.
- **[VALIDÉ]** Bonne réponse : le joueur reste sur la case atteinte, sous réserve des effets spéciaux.
- **[VALIDÉ]** Mauvaise réponse : retour à la case occupée avant le lancer ; recul exécuté **après affichage de la correction**.
- **[VALIDÉ]** Temps écoulé à 60 s : réponse incorrecte et pénalité associée.
- **[VALIDÉ]** Échelles : déplacement ascendant automatique entre deux cases définies.
- **[VALIDÉ]** Tapis de levage : une bonne réponse **Millésime** permet d'éviter le recul.
- **[VALIDÉ]** Questions sur les domaines viticoles : région déterminée par la case du plateau.
- **[VALIDÉ]** Victoire lorsque le pion atteint **ou dépasse** la Corse.
- **[VALIDÉ]** Passage au joueur suivant par bouton, jamais automatique dès la correction.

**[À VÉRIFIER]** Les conséquences exactes du tapis de levage si le joueur choisit Primeur ou Grand Cru, s'il échoue au niveau Millésime, et la destination du recul ; les extrémités des échelles ; les éventuels effets en chaîne ; l'effet d'un passage sur une case spéciale sans s'y arrêter.

## 6. Plateau et représentation numérique
**[VALIDÉ]** Conserver fidèlement l'illustration fournie : carte de France, régions viticoles, parcours coloré, échelles, tapis de levage, arrivée en Corse. Plateau responsive, avec zoom et déplacement pour les écrans tactiles.

**[RECOMMANDÉ]** Utiliser l'image historique comme fond, avec couche interactive superposée ; stocker les centres de cases en coordonnées normalisées (x/y de 0 à 1) afin que les pions restent alignés à tous les niveaux de zoom. Gérer plusieurs pions sur la même case avec léger décalage ou regroupement.

**[À VÉRIFIER]** Relever manuellement et valider : nombre total de cases, numérotation et ordre de parcours, coordonnées exactes, catégories/couleurs, cases de régions, départ, arrivée, départ/fin de chaque échelle et tapis de levage. L'image seule ne doit pas conduire Codex à inventer une numérotation.

## 7. Joueurs et tours
**[VALIDÉ]** 2 à 10 joueurs individuels, localement, sans compte ni synchronisation cloud.

**[RECOMMANDÉ]** Chaque joueur possède `id`, `name`, `tokenId`, `color`, `position`. L'état de partie contient `currentPlayerIndex`, `phase`, `diceRoll`, `positionBeforeRoll`, `activeQuestionId`, `timeRemaining`, `answerStatus`, `usedQuestionIds`, `winnerId`, `updatedAt` et `schemaVersion`. Les phases doivent être explicites : `setup`, `ready`, `moving`, `question`, `correction`, `turn_end`, `finished`.

Prévenir les doubles validations, lancers multiples et actions hors phase. Un changement de joueur ne doit pas se produire deux fois sur double clic.

## 8. Banque de questions
**[VALIDÉ]** Réutiliser les questions existantes ; QCM, vrai/faux et questions ouvertes ; trois niveaux : Primeur (débutant), Grand Cru (amateur), Millésime (expert). Choix du niveau à chaque question. FR/EN.

**[À VÉRIFIER]** Catégories historiques à confirmer sur les données : histoire, géographie, accords/crus/dégustation, métiers/vinification, domaines viticoles. Confirmer les traductions réelles, les images, les explications, la proportion des types de questions et le volume disponible par catégorie/niveau/langue.

**[RECOMMANDÉ]** Transformer les fichiers de questions en JSON statique versionné, sans API requise. Schéma type : `id`, `categoryId`, `regionId?`, `difficulty`, `type`, `translations.fr`, `translations.en`, `choices?`, `correctChoiceIds?`, `expectedAnswer?`, `explanation?`, `imagePath?`. Adapter ce schéma aux données existantes, sans inventer des traductions. Ajouter un script de validation de cohérence et d'unicité.

**[À VÉRIFIER]** Règle de non-répétition des questions dans une partie ; comportement si aucune question n'existe pour le filtre ; éventuels types supplémentaires. Pas d'interface d'administration demandée.

## 9. Réponses et minuterie
- **[VALIDÉ]** QCM et vrai/faux corrigés automatiquement.
- **[VALIDÉ]** Questions ouvertes : afficher la réponse attendue, puis permettre au joueur/groupe de valider la réponse orale. **[À VÉRIFIER]** Le terme « auto » employé par le porteur désigne vraisemblablement l'affichage automatique de la réponse de référence, et non une évaluation automatique de la parole : confirmer avant implémentation.
- **[VALIDÉ]** 60 secondes ; expiration = mauvaise réponse.
- **[VALIDÉ]** La correction doit rester lisible avant application visible du recul et avant « Joueur suivant ».
- **[RECOMMANDÉ]** Définir précisément la reprise d'une question interrompue (horodatage et temps restant, sans pouvoir contourner le chronomètre par fermeture de l'app).

## 10. Écrans attendus
1. Accueil : nouvelle partie, reprendre, règles, paramètres, langue.
2. Configuration : joueurs, noms, pions/couleurs, ordre, validation.
3. Plateau : carte zoomable, positions, joueur actif, dé, tour, aide.
4. Choix du niveau : Primeur / Grand Cru / Millésime.
5. Question : catégorie/région, question, réponses, chronomètre, illustration éventuelle.
6. Correction : résultat, réponse de référence, conséquence, bouton de continuation.
7. Transition de tour : état mis à jour, « Joueur suivant ».
8. Victoire : gagnant « Grand Maître du Chai », rejouer, retour accueil.
9. Paramètres : son, langue, règles et informations.
10. Confirmation de nouvelle partie si une sauvegarde existe.

**[RECOMMANDÉ]** Navigation tactile accessible ; gros boutons, textes lisibles, contrastes suffisants, identification des pions autrement que par couleur ; respect de la préférence système de réduction des animations.

## 11. Sauvegarde et hors ligne
**[VALIDÉ]** Une seule partie en cours ; sauvegarde automatique sur le même appareil et navigateur ; aucune authentification.

**[RECOMMANDÉ]** IndexedDB pour l'état de partie, avec validation de schéma, migration et récupération d'erreur. Sauvegarder après chaque transition d'état stable. Afficher une confirmation avant écrasement/abandon de partie. Stocker les réglages localement.

**[RECOMMANDÉ]** PWA installable, service worker avec précache des fichiers indispensables (plateau, questions, sons, traductions), et stratégie de mise à jour évitant de casser les sauvegardes. Tester en mode avion **après le premier chargement réussi** ; GitHub Pages ne fournit pas de serveur d'application.

## 12. Architecture recommandée
- React + TypeScript + Vite.
- Moteur de jeu en fonctions pures, indépendant de React.
- Fichiers JSON locaux pour questions, régions et coordonnées des cases.
- IndexedDB pour la sauvegarde.
- PWA pour le fonctionnement hors ligne.
- Vitest pour tests unitaires ; Playwright pour tests de parcours.
- GitHub Actions pour tests, compilation et déploiement GitHub Pages.
- Capacitor à évaluer pour Android et iOS lorsque la version web est stable.

**[RECOMMANDÉ]** Organisation : `src/game/` (règles), `src/data/`, `src/storage/`, `src/components/`, `src/screens/`, `src/i18n/`, `src/assets/`, `tests/`, `docs/`. Aucune dépendance réseau obligatoire pour jouer. Vérifier le `base` Vite et les chemins d'assets sur GitHub Pages.

## 13. Protection absolue du projet historique
**[VALIDÉ — CONTRAINTE NON NÉGOCIABLE]** Le ZIP et tous les fichiers de l'application historique sont strictement en lecture seule. Codex ne doit jamais les modifier, renommer, supprimer, reformater, migrer ni écraser. Ne pas lancer `npm install`, scripts de build ou commandes Git dans le répertoire historique si elles peuvent écrire des fichiers. Ne pas copier les `.env`, secrets, clés ou le dossier `.git` historique. Construire la nouvelle application dans un dossier et dépôt distincts. Vérifier l'intégrité de l'archive de référence par empreinte SHA-256 avant/après si une copie de travail est créée.

**[RECOMMANDÉ]** Monter le dossier historique en lecture seule lorsque possible et placer la nouvelle application hors de celui-ci. Faire approuver tout transfert d'assets et vérifier les droits des visuels, sons et polices.

## 14. Qualité, sécurité et conformité
- Aucun secret côté client ; ne pas publier les secrets de l'ancienne application.
- Pas de compte, pas de télémétrie, pas de publicité sans nouvelle décision.
- Noms et parties stockés localement ; prévoir une suppression locale.
- Vérifier les droits sur le plateau, logo, illustrations, sons, questions et traductions.
- Thématique du vin : jeu culturel, sans mécanisme incitant à la consommation ; vérifier les classifications et politiques des boutiques avant soumission.
- Tests sur Android/iOS réels lors de la phase mobile ; ne pas supposer qu'un site PWA sera automatiquement accepté en boutique.

## 15. Plan de tests et critères d'acceptation
### Tests du moteur
- Refuser moins de 2 ou plus de 10 joueurs.
- Dé entre 1 et 6 ; avancer du nombre exact de cases.
- Bonne réponse : maintien ; mauvaise réponse : retour à la position d'avant lancer.
- Temps écoulé : échec ; pas de double application des pénalités.
- Échelles : chaque paire départ/arrivée validée.
- Tapis de levage : cas expert réussi, expert échoué et autres niveaux selon règles confirmées.
- Questions de domaine : région dérivée de la case.
- Victoire en atteignant ou dépassant la Corse.
- « Joueur suivant » ne change le joueur qu'une seule fois.

### Tests application
- Partie complète à 2 et 10 joueurs.
- Fermeture/réouverture et reprise sans perte d'état.
- Fonctionnement hors ligne après installation/chargement.
- Zoom et déplacement du plateau sur smartphone/tablette ; pions toujours alignés.
- Traductions FR/EN, affichage des questions, sons activés/désactivés.
- Sauvegarde corrompue, mise à jour d'application, cache PWA et chemins GitHub Pages.

### Conditions de livraison
Une version n'est acceptée que si les règles validées sont testées, que la banque de questions réelle est chargée, que la partie est jouable hors ligne, que la sauvegarde est fiable, et que le projet historique demeure intact.

## 16. Roadmap pour Codex
**Phase 0 — Audit lecture seule.** Inventorier les écrans, assets, questions, règles et dépendances ; produire un rapport des inconnues. Ne pas coder les règles ambiguës.

**Phase 1 — Modèle et plateau.** Définir le schéma des questions, exporter/valider les données, numéroter les cases et relever leurs coordonnées avec validation humaine.

**Phase 2 — Moteur de jeu.** Implémenter états, dé, déplacements, corrections, minuterie, cases spéciales et victoire avec tests unitaires.

**Phase 3 — UI mobile.** Intégrer le plateau historique responsive, pions, écrans, transitions, langue et sons.

**Phase 4 — Persistance/PWA.** Sauvegarde, reprise, cache hors ligne et tests mode avion.

**Phase 5 — GitHub Pages.** Tests de bout en bout, accessibilité, documentation et publication statique.

**Phase 6 — Boutiques.** Évaluer Capacitor, préparer Android/iOS, tester sur appareils réels, gérer conformité et publication.

À la fin de chaque phase : résumer les fichiers créés/modifiés **dans le nouveau projet**, tests exécutés, résultats, décisions en suspens et instructions pour l'étape suivante.

## 17. Registre des points bloquants ou à confirmer
1. Emplacement et export réel des fichiers de questions, réponses et traductions.
2. Nombre, ordre et coordonnées exacts de toutes les cases.
3. Association cases/couleurs/catégories/régions.
4. Extrémités exactes de chaque échelle.
5. Déclenchement et destination du tapis de levage, en particulier hors réussite Millésime.
6. Ordre des effets spéciaux et des questions ; activation en traversant une case.
7. Validation exacte des réponses ouvertes.
8. Règles de sélection et répétition des questions, gestion d'une catégorie vide.
9. Comportement de la minuterie en arrière-plan/reprise.
10. Droits de réutilisation des ressources.
11. Éventuelles autres fonctionnalités historiques couvertes par « tout conserver », à distinguer des comptes, paiements et administration explicitement exclus.

## 18. Définition de terminé
Vinodys'Sait est prêt pour la version web lorsque 2 à 10 joueurs peuvent réaliser une partie complète sur mobile/tablette, avec le plateau fidèle, les vraies questions, les règles validées, les langues FR/EN, les sons configurables, le fonctionnement hors ligne, la sauvegarde/reprise, une victoire correcte et un déploiement GitHub Pages reproductible, **sans aucune modification du projet historique**.
