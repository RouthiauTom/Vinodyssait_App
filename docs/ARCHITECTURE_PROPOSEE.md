# Architecture proposée

> **État actuel après réception de `QuestionsId.csv` :** les métadonnées des 673 questions sont désormais disponibles et raccordées exactement au CSV FR/EN. Les mentions de métadonnées manquantes dans les étapes antérieures ci-dessous décrivent leur état à cette date et sont remplacées par le complément final. Les 300 questions Domaines n’ont pas de niveau : banque commune par région confirmée par le porteur [VALIDÉ], B7 résolu. Aucun code de jeu ni conversion JSON créé.

Toutes les propositions techniques de ce document sont [RECOMMANDÉ], à valider. Aucune arborescence de code ci-dessous n’a été créée. Les exigences [VALIDÉ] restent celles du cahier des charges.

## Choix

React + TypeScript + Vite, application statique mobile-first. Questions et plateau en données locales ; IndexedDB pour une seule partie et ses réglages ; service worker pour ressources essentielles. Vitest pour données/moteur, Testing Library pour interactions pertinentes, Playwright pour parcours et hors ligne. Versions et éventuels plugins à vérifier dans leurs documentations officielles au moment de l’implémentation ; aucune dépendance installée pendant l’audit.

Préférer une navigation pilotée par les phases et quelques écrans sans URLs profondes ; si des URLs deviennent utiles, un routage par fragment peut être proposé pour GitHub Pages. Ne pas reprendre les gardes JWT ni les routes de comptes.

## Arborescence cible

```text
Vinodyssait_V2/
├── docs/                         # cinq documents de phase 0
├── public/
│   ├── assets/                   # plateau, visuels, sons, police autorisés
│   └── icons/                    # icônes PWA contrôlées
├── src/
│   ├── app/                      # orchestration, navigation, adaptateurs
│   ├── game/
│   │   ├── types.ts              # états, actions, résultats
│   │   ├── reducer.ts            # transitions pures et gardes
│   │   ├── movement.ts           # parcours et effets validés
│   │   ├── answers.ts            # correction structurée
│   │   ├── questions.ts          # filtres, tirage, disponibilité
│   │   └── invariants.ts         # contrôles d’état
│   ├── data/
│   │   ├── board.json            # uniquement coordonnées/ordre validés
│   │   ├── categories.json
│   │   ├── regions.json
│   │   ├── questions.json        # banque réelle, aucun exemple fictif
│   │   └── schemas.ts            # validation et versions
│   ├── storage/                  # repository IndexedDB, migrations, erreurs
│   ├── platform/                 # clock, random, audio ; adaptables au mobile
│   ├── i18n/                     # textes FR/EN validés
│   ├── components/               # Board, Token, Dice, Timer, Answer, Dialog
│   ├── screens/                  # Home, Setup, Game, Settings, Rules, Victory
│   └── styles/                   # identité, responsive, accessibilité
├── scripts/                      # import/validation de données, aucun secret
├── tests/
│   ├── game/
│   ├── data/
│   ├── storage/
│   └── e2e/
├── .github/workflows/            # checks/build/Pages après validation
├── vite.config.ts
└── package.json
```

## Frontières du moteur

L’UI envoie une action ; le moteur calcule un nouvel état et les conséquences ; l’orchestrateur sauvegarde puis déclenche animation/audio. Aucun import React, DOM, IndexedDB, API, Audio ou horloge réelle dans `game/`. Valeur du dé, valeur aléatoire du tirage et instant courant sont fournis explicitement. Tests reproductibles sans attendre 60 secondes.

Phases proposées : setup, ready, moving, level_choice, question, correction, turn_end, finished. `level_choice` rend explicite le choix avant toute question, absent du modèle indicatif du cahier. La phase moving concerne un déplacement logique déterminé, pas une animation qui décide d’une règle. Le détail des transitions après effets/victoire demeure à valider.

Conserver : joueurs, joueur actif, phase, position avant lancer, dé, déplacement prévu, question sélectionnée, échéance/temps selon décision, réponse soumise, résultat, questions utilisées, gagnant et dates. Ajouter `schemaVersion`, `contentVersion` et un identifiant de transition pour permettre sauvegarde et reprise cohérentes. Le moteur rejette l’action hors phase et les validations répétées ; l’UI désactive aussi les boutons. Une reprise restaure une phase logique, jamais une animation indispensable au calcul.

La lecture de correction et l’application visible du recul auront une transition explicite ; ne pas décider ici si elle utilise un bouton séparé ou le bouton de continuation existant.

## Données

Plateau : image référencée, dimensions, parcours ordonné, identifiants stables, centres x/y normalisés, catégorie/région, effets et destinations. Validation des références, plages x/y, ordre et destinations ; validation humaine de la géométrie. Aucun nombre de cases ou point n’est fourni par cet audit.

Questions : IDs stables, provenance, catégorie, région si nécessaire, niveau réel, type réel, textes FR/EN, choix identifiés pour QCM, choix corrects ou réponse attendue, explication/image si présentes. Garder la correspondance des IDs historiques lors de l’import. Une absence de donnée est signalée ; jamais comblée par traduction ou classification inventée. Rapports de couverture par catégorie × région × niveau × langue et détection des doublons/références cassées. Les QCM à plusieurs réponses nécessitent une règle confirmée avant fixation du schéma.

## Sauvegarde et temps

Écrire aux transitions stables via un seul repository. Lire et valider les versions avant reprise. Écriture transactionnelle et file séquentielle pour éviter qu’une ancienne transition écrase la suivante. Exposer une erreur de sauvegarde intelligible, sans promettre une reprise garantie en cas d’échec de stockage. Prévoir confirmation avant remplacement et suppression locale.

Proposition à valider : persister une échéance absolue, calculer le temps à partir de l’horloge injectée et résoudre l’expiration une seule fois lors du retour. Cette solution empêche une simple fermeture de suspendre le compteur, mais une horloge système modifiée demande un traitement explicite ; elle ne constitue pas une protection antifraude. Aucune politique de reprise n’est encore adoptée.

## Plateau, audio et accessibilité

Même transformation de zoom/déplacement pour l’image et la couche des pions. Décalage déterministe des pions partageant une case, identité par nom/symbole/couleur. Boutons tactiles, focus clavier, texte lisible, annonce de joueur/résultat et réduction d’animations. Aucun changement de catégorie ne vient d’une approximation graphique.

Audio centralisé avec deux réglages historiques ; activation après interaction utilisateur, arrêt au changement de phase et gestion des refus de lecture. Sons embarqués, pas de chargement réseau requis en partie.

## Hors ligne et publication

Précacher bundle, questions, traductions, plateau, pions, sons utiles et polices locales. Vérifier les images de questions : pas d’URL distante indispensable. La première visite doit terminer le chargement/cache avant d’annoncer le jeu disponible hors ligne. Prévoir un message de disponibilité et une mise à jour différée pendant une partie pour ne pas remplacer sa banque/son plateau.

Pour Pages : définir base de déploiement, chemins relatifs et portée du service worker ; tester sous un sous-chemin, pas seulement localhost à la racine. Workflow de checks et build statique. Le dépôt GitHub distant et la publication restent à configurer dans une phase ultérieure ; rien n’est publié par cet audit.

Capacitor sera évalué après stabilisation : réutiliser UI/moteur/données, adapter stockage et cycle de vie par interfaces, empaqueter les assets. Tests Android/iOS réels requis ; aucune garantie d’acceptation en boutique n’est supposée.

## Ajustement au CSV et à l’emplacement imposé

Racine réelle du nouveau projet : `/Users/tomrouthiau/Documents/Vinodyssait_App`. L’arborescence proposée reste une proposition, seuls les documents et le dépôt local existent. L’archive, le CSV et les références restent à la racine parente en lecture seule.

L’import futur rapprochera les 1346 traductions du CSV avec les métadonnées Question/Category/Domain par `questionId`. Conserver les IDs 1–673 et le texte source. Les variantes de séparateurs de ligne et de réponse nécessitent un rapport de conversion et une revue. Les QCM multiples devront stocker un ensemble explicite de choix corrects ; règle de correction à confirmer. Ne pas construire de catégories ou niveaux à partir du texte.

## Ajustement — métadonnées maintenant disponibles

L’import futur peut joindre `QuestionsId.csv.id` au `questionId` du CSV FR/EN sans perte : 673 correspondances exactes. Ne pas utiliser la colonne `translations` comme une liste d’IDs de traduction ; elle répète `id`. Le rapport d’import devra vérifier les mappings de catégories 1–5, niveaux 1–3 et régions 1–10 avec le porteur.

Le schéma de données doit pouvoir représenter explicitement le niveau absent dans la source des Domaines, avant de décider du modèle jouable validé. Un filtre de niveau strict exclurait les 300 questions ; ce comportement n’est pas adopté. Aucun JSON dérivé ou moteur n’a été créé pendant ce complément d’audit.

## Règle de sélection Domaines [VALIDÉ]

Pour la catégorie Domaines, sélectionner dans la banque commune selon la région de la case et la langue, sans filtre de niveau. Représenter le niveau comme non applicable pour ces questions ; ne pas créer de difficulté fictive. Le choix de niveau ne conditionne pas ce tirage. Le parcours de choix de niveau concerne les catégories 1–4. La sélection/répétition et les cas de banque épuisée restent à confirmer. Si une case de tapis devait demander une question Domaines, la condition de réussite Millésime ne pourrait pas s’y appliquer sans précision supplémentaire ; vérifier l’association réelle des cases avant de conclure à ce cas.

## Validation et organisation actuelles [VALIDÉ]

Le porteur a validé l’audit et l’architecture et autorise le travail directement dans `Vinodyssait_App`, sans sous-projet V2. Le dépôt de la racine est le dépôt de travail, distinct du dépôt historique contenu dans le ZIP. Les passages antérieurs demandant la validation de l’audit sont clos ; les décisions métier encore ouvertes restent à recueillir.

Organisation actuelle : `docs/` pour les rapports ; `sources/questions/` pour les deux CSV inchangés ; `sources/audit-initial/` préserve uniquement les métadonnées Git du dépôt local créé pendant l’audit. Le ZIP historique et les deux références restent à leur emplacement d’origine, strictement inchangés. Aucun développement n’est effectué dans les dossiers de sources.

Prochaine phase autorisée : préparation des données et du plateau. Ne pas inventer les coordonnées, effets spéciaux, réponses correctes structurées ou traductions. Les Domaines utilisent la banque commune sans niveau déjà validée.

## Interface locale implémentée

Parcours mobile FR/EN branché sur le moteur et les 673 questions, avec reprise IndexedDB, confirmation avant remplacement, plateau zoomable, pions numérotés et sons synthétiques locaux. Bilan et limites : INTERFACE_MOBILE.md. Vérifications finales : 34 tests Vitest, 14 tests Python, 4 tests Chromium et compilation réussis. Aucun déploiement ni service worker PWA ; pas encore de garantie de rechargement hors ligne. Les nouveaux libellés/résumés d’interface restent proposés à relecture.
