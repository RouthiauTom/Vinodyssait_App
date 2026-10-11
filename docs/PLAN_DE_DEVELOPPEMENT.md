# Plan de développement

> **État actuel après réception de `QuestionsId.csv` :** les métadonnées des 673 questions sont désormais disponibles et raccordées exactement au CSV FR/EN. Les mentions de métadonnées manquantes dans les étapes antérieures ci-dessous décrivent leur état à cette date et sont remplacées par le complément final. Les 300 questions Domaines n’ont pas de niveau : banque commune par région confirmée par le porteur [VALIDÉ], B7 résolu. Aucun code de jeu ni conversion JSON créé.

Statut : proposition [RECOMMANDÉ]. Aucune phase de code n’est autorisée avant validation du rapport. Objectif prioritaire : une partie complète avec les vraies données, puis fiabilité hors ligne et publication ; pas de comptes, administration ou extensions supplémentaires.

## Phase 0 — Audit et validation

- Objectif : établir l’existant et les inconnues sans toucher à l’historique.
- Livrables : les cinq documents de `docs/`, inventaire, comparaison et registre des décisions.
- Dépendances : ZIP et références ; CSV de traductions reçu ; métadonnées Question/Category/Domain encore manquantes.
- Vérifications : lecture statique, dimensions PNG, recherche données/migrations, empreintes source et références, existence des documents.
- Acceptation : provenance et limites explicites, aucun test fictivement annoncé, historique intact.
- Validation attendue : rapport, architecture et réponses initiales. L’audit des questions sera complété à réception de leurs fichiers avant l’import.

## Phase 1 — Données réelles et plateau

- Objectif : disposer d’un modèle fidèle avant d’implémenter les règles.
- Fonctionnalités : analyser fichiers de questions et traductions, normaliser sans perte, inventorier images ; relever toutes les cases et associations, extrémités d’effets et ordre.
- Modules futurs : `src/data/`, `scripts/`, `tests/data/`, assets autorisés et documentation de provenance.
- Dépendances : fichiers/export ciblé fourni par le porteur, réponses B1–B7 du registre et droits de transfert.
- Tests : IDs uniques, références existantes, niveaux/types attestés, couverture FR/EN, filtres atteignables, coordonnées bornées et cohérentes, assets locaux.
- Acceptation : chaque donnée tracée à sa source ; aucune coordonnée, question ou traduction inventée ; liste des trous à zéro pour la configuration jouable retenue ou politique approuvée.
- Validation : carte annotée/numérotée, associations et effets, rapport d’import, règles de trous/non-répétition. Aucun transfert d’assets tant que choix et droits ne sont pas confirmés.

## Phase 2 — Moteur indépendant

- Objectif : rendre une partie complète simulable sans interface.
- Fonctionnalités : configuration 2–10, ordre, phases, dé et déplacements, région/catégorie, niveau, sélection, correction QCM/vrai-faux/ouvertes, expiration, échelles/tapis, fin de tour et victoire.
- Modules : `src/game/`, interfaces `platform/`, `tests/game/`.
- Dépendances : données et règles approuvées en phase 1 ; Vitest proposé.
- Tests écrits avant ou avec chaque règle : joueurs 1/2/10/11, dé 0/1/6/7, déplacement exact, maintien, retour après lecture, expiration unique, chaque paire d’échelle, tous cas tapis validés, région dérivée, fin atteinte/dépassée selon priorité retenue, question vide/épuisée, choix corrects, validation ouverte, actions hors phase et doubles clics.
- Acceptation : règles validées couvertes ; simulation déterministe jusqu’à la victoire à 2 et 10 joueurs ; aucune ambiguïté encodée par défaut.
- Validation : matrice de règles et transitions. Pas de refonte de règle pour simplifier les tests.

## Phase 3 — Interface mobile jouable

- Objectif : partie complète sur un appareil partagé, avec identité originale.
- Fonctionnalités : accueil, configuration, plateau zoomable, pions identifiables, dé, joueur actif, niveau, question/correction et continuation, victoire, règles/réglages, FR/EN et sons.
- Modules : `screens/`, `components/`, `styles/`, `i18n/`, adaptateurs audio/clock.
- Dépendances : moteur et assets approuvés ; React/TypeScript/Vite, Testing Library et Playwright proposés.
- Tests : parcours complets 2/10, affichage de correction avant recul, clics répétés, noms longs, pions groupés, position conservée au zoom, langue et sons, focus, réduction d’animations ; essais tactiles smartphone/tablette.
- Acceptation : progression exacte, aucun lancer pendant une question, fin de tour manuelle, contenus réels lisibles dans les deux langues.
- Validation : fidélité au plateau et ergonomie ; choix final des pions et des sons. Cette tranche précède les améliorations secondaires.

## Phase 4 — Sauvegarde et PWA

- Objectif : jouer et reprendre sans réseau après premier chargement complet.
- Fonctionnalités : IndexedDB versionnée, réglages, confirmation de remplacement, suppression locale, reprise toutes phases stables, timer en arrière-plan, précache et mise à jour compatible.
- Modules : `storage/`, orchestration `app/`, configuration PWA, `tests/storage/`, `tests/e2e/`.
- Dépendances : état moteur stable, politique temps et version de contenu validées ; choix du plugin PWA lors de l’implémentation.
- Tests : fermeture/reprise pendant question et correction, expiration à la limite, sauvegarde corrompue/version inconnue, écriture refusée, mise à jour en partie, cache incomplet, partie 2/10 sans requête serveur, sons/images/police hors ligne. Vérification navigateur hors ligne puis mode avion sur appareils réels.
- Acceptation : partie complète hors ligne et reprise cohérente ; erreur explicite si le stockage échoue ; aucun écrasement silencieux.
- Validation : expérience de reprise, gestion des erreurs et notification de disponibilité/mise à jour.

## Phase 5 — GitHub Pages

- Objectif : première livraison web reproductible.
- Fonctionnalités : checks CI, compilation, déploiement statique, base/paths/service worker ajustés, documentation installation/reprise.
- Modules : `.github/workflows/`, config Vite/PWA, tests E2E, documentation utilisateur.
- Dépendances : dépôt GitHub cible et stratégie publication confirmés ; phases précédentes acceptées.
- Tests : unité/données/E2E requis, build, navigation sous le chemin du dépôt, premier chargement, mise à jour, FR/EN, contrôles tactiles et accessibilité ; vérification finale de l’intégrité du ZIP.
- Acceptation : définition de terminé du cahier satisfaite avec données réelles et résultats consignés. Publication seulement dans la phase autorisée, après revue du résultat concret.
- Validation : URL/dépôt et recette utilisateur d’une partie complète ; droits et texte légal finalisés.

## Phase 6 — Android/iOS après stabilité web

- Objectif : évaluer puis empaqueter sans changer le moteur.
- Fonctionnalités : étude Capacitor, projets natifs isolés, icônes, lifecycle/stockage/audio, préparation boutiques.
- Modules : adaptateurs `platform/`, configuration Capacitor et projets natifs futurs.
- Dépendances : version web acceptée, environnement et comptes boutiques ; politiques à vérifier à ce moment-là.
- Tests : appareils Android/iOS réels, installation, mode avion, interruption/reprise, audio, écrans tactiles et migrations.
- Acceptation : parité des règles/données/sauvegarde, aucune API de jeu obligatoire ; conformité vérifiée sans supposer une acceptation automatique.
- Validation : choix Capacitor, périmètre mobile, identité et soumission. Aucun travail mobile requis pour la première version web.

## Compte rendu obligatoire de chaque phase

Lister fichiers créés/modifiés dans V2, tests effectivement exécutés et résultats, limites, décisions restantes et prochaine validation. Si un contrôle n’a pas été exécuté, le dire explicitement. Ne pas chiffrer de délai tant que volume et qualité de la banque/plateau ne sont pas connus.

## Mise à jour de la phase 0 et des prérequis de phase 1

Le CSV a été audité en lecture seule : 673 questions bilingues, 1346 lignes. Contrôles exécutés : parseur CSV, champs vides, IDs/langues, doublons, repérage heuristique des types et contrôle de formats signalés. Aucun test de jeu, import JSON ou développement effectué.

Phase 1 : remplacer le prérequis « obtenir les textes » par « confirmer l’exhaustivité du CSV et fournir les métadonnées des 673 IDs ». Ajouter à la recette d’import : sauts de ligne, choix simples/multiples, extraction non ambiguë des réponses et revue des cas 2, 108, 111, 152, 203, 480, 500–507, 532, 337/368. Ne pas prétendre certifier le contenu scientifique par des contrôles structurels.

Toutes les phases futures se dérouleront exclusivement dans `Vinodyssait_App`. La validation du rapport reste requise avant le code de jeu.

## Mise à jour — prérequis de données précisés

La phase 0 inclut désormais le rapprochement des deux CSV : 673 IDs uniques, 1346 traductions FR/EN raccordées, distribution catégorie/niveau/région contrôlée, absence d’imageUrl constatée. Contrôles réellement exécutés, sans développement de jeu.

La phase 1 ne nécessite plus de rechercher les métadonnées de ces 673 questions. Ses prérequis restants sont : confirmer l’exhaustivité et les mappings des IDs/libellés, trancher les 300 Domaines sans niveau, valider les types/choix/corrections et les cas éditoriaux signalés, puis fournir/valider la définition complète du plateau et de ses effets. La matrice de couverture détaillée figure dans l’audit. Aucune phase de code n’est commencée avant validation de la mission 1.

## Mise à jour du prérequis B7 [VALIDÉ]

La décision du porteur résout le traitement des 300 Domaines sans niveau : banque commune par région, sans filtre de difficulté. Supprimer la classification de ces questions des prérequis de phase 1. Prévoir en phase 2 des tests vérifiant ce tirage sans niveau, la région dérivée de la case, les traductions réelles et l’absence d’exclusion due à un champ difficulty vide. Les niveaux des autres catégories restent appliqués. La validation du rapport demeure requise avant développement.

## Validation et organisation actuelles [VALIDÉ]

Le porteur a validé l’audit et l’architecture et autorise le travail directement dans `Vinodyssait_App`, sans sous-projet V2. Le dépôt de la racine est le dépôt de travail, distinct du dépôt historique contenu dans le ZIP. Les passages antérieurs demandant la validation de l’audit sont clos ; les décisions métier encore ouvertes restent à recueillir.

Organisation actuelle : `docs/` pour les rapports ; `sources/questions/` pour les deux CSV inchangés ; `sources/audit-initial/` préserve uniquement les métadonnées Git du dépôt local créé pendant l’audit. Le ZIP historique et les deux références restent à leur emplacement d’origine, strictement inchangés. Aucun développement n’est effectué dans les dossiers de sources.

Prochaine phase autorisée : préparation des données et du plateau. Ne pas inventer les coordonnées, effets spéciaux, réponses correctes structurées ou traductions. Les Domaines utilisent la banque commune sans niveau déjà validée.

## Phase 1 démarrée après autorisation

Brouillon local lossless de 673 questions produit et contrôlé, avec six tests d’import passés. Voir PREPARATION_DONNEES.md. Les types/choix/corrections et le plateau restent en validation ; aucun moteur de jeu implémenté. La phase est en cours, pas terminée.

## Droits du plateau confirmés [VALIDÉ]

Le porteur a confirmé les droits de réutilisation du plateau. Une copie exacte de l’image a été produite dans `docs/plateau/Plateau_original.png` et un support quadrillé dans `docs/plateau/RELEVE_PLATEAU.svg`. Le ZIP est inchangé. Les mentions antérieures de droits en attente sont résolues pour le plateau ; les droits des autres ressources ne sont pas implicitement confirmés. Les cases et extrémités restent à relever et valider.

## Cercles de régions inclus dans le parcours [VALIDÉ]

En réponse à la question « les cercles portant les noms des régions comptent-ils comme des cases, au même titre que les segments colorés ? », le porteur confirme « Oui ». Chaque cercle de région compte donc comme une case dans le décompte des déplacements. Cette décision ne fixe pas encore le statut du point Départ, la position initiale, le nombre total de cases ou leurs coordonnées.

## Position initiale sur la case Départ [VALIDÉ]

Le porteur confirme que les joueurs commencent sur la case Départ, distincte du cercle Val de Loire. Le cercle Val de Loire reste une case du parcours, conformément à la décision précédente. Cette confirmation ne fixe pas de coordonnées ni d’identifiant numérique de case.

## Première case après le Départ [VALIDÉ]

Le porteur confirme qu’un lancer de 1 depuis la case Départ mène directement au cercle Val de Loire. L’adjacence Départ → Val de Loire est donc validée, et le Val de Loire est la première case atteinte en avançant. Aucun identifiant numérique ni coordonnée graphique n’est fixé par cette décision.

## Questions sur les cercles de régions [VALIDÉ]

Le porteur confirme que chaque cercle de région déclenche une question Domaines de cette région, sans choix de niveau. Le filtre utilise donc la catégorie Domaines et la région du cercle ; la banque commune sans niveau s’applique. Cette décision ne tranche pas la priorité de victoire à l’arrivée en Corse, qui reste à confirmer.

## Arrivée en Corse et dernière question [VALIDÉ]

Le porteur précise : « Il doit réussir la dernière question. S’il dépasse, il arrive tout de même sur la case Corse ». Un déplacement atteignant ou dépassant l’arrivée est donc limité à la case Corse, sans rebond. L’arrivée ne déclenche pas une victoire immédiate : le joueur doit réussir la question Domaines de Corse, sans niveau, conformément à la règle validée des cercles de régions. La victoire n’est acquise qu’après cette réussite. En cas de réponse incorrecte ou de temps écoulé, la règle générale déjà validée de retour à la position avant le lancer après lecture de correction s’applique. Aucun nombre de cases ni coordonnée n’est déduit de cette décision.

## Couleurs des segments et catégories [VALIDÉ]

Le porteur confirme la correspondance suivante : bleu → Histoire (categoryId 1), vert → Géographie (2), noir → Accords / Crus / Dégustation (3), rouge → Métiers / Vinification (4). Les cercles de régions relèvent de Domaines (5), sans niveau, conformément aux décisions précédentes. La correspondance des couleurs est validée ; les identifiants, centres et ordre de chaque segment restent à relever sur le plateau.

## Échelle : montée avant la question [VALIDÉ]

Le porteur confirme : « Monter immédiatement et répondre à la case d’arrivée ». La montée précède donc la question, dont la catégorie et la région éventuelle sont déterminées par la case d’arrivée de l’échelle. Cette décision ne fixe pas les extrémités des échelles, les effets en chaîne ou leur activation au passage. Le point de retour en cas d’échec après une échelle reste à confirmer explicitement.

## Échelle : retour en cas d’échec [VALIDÉ]

Le porteur confirme qu’une mauvaise réponse à la question de la case d’arrivée d’une échelle ramène le joueur à sa position avant le lancer, comme pour une case normale, après lecture de la correction. L’expiration du délai reste une réponse incorrecte conformément à la règle générale. La décision antérieure laissant ce point à confirmer est donc résolue. Les extrémités, l’activation au passage et les éventuels effets en chaîne restent à préciser.

## Déclenchement des cases spéciales à l’arrêt [VALIDÉ]

Le porteur confirme que les échelles et le tapis se déclenchent lorsque le joueur s’arrête sur leur case, et non lorsqu’il la traverse. La question antérieure sur l’activation au passage est résolue. Cette décision ne fixe pas les extrémités, les conséquences du tapis ni les éventuels effets en chaîne lorsqu’un déplacement spécial aboutit sur une autre case spéciale.

## Tapis : réussite aux niveaux Primeur et Grand Cru [VALIDÉ]

Le porteur confirme qu’une bonne réponse Primeur ou Grand Cru sur la case du tapis entraîne tout de même la descente jusqu’à l’extrémité inférieure du tapis. Une bonne réponse Millésime permet de rester sur la case, selon la règle déjà validée. Cette décision ne détermine ni la case exacte de destination ni le traitement d’une mauvaise réponse ou d’un délai expiré sur le tapis.

## Tapis : mauvaise réponse ou expiration [VALIDÉ]

Le porteur confirme qu’en cas de mauvaise réponse ou de temps écoulé sur le tapis, le joueur revient à sa position avant le lancer, après lecture de la correction conformément à la règle générale. Il ne descend pas à l’extrémité inférieure dans ce cas. Récapitulatif : réussite Millésime → maintien sur la case ; réussite Primeur/Grand Cru → descente à l’extrémité inférieure ; échec ou expiration, à tout niveau → retour à la position avant le lancer. Les extrémités exactes et les éventuels effets/questions après la descente restent à confirmer.

## Tapis : fin du tour après descente [VALIDÉ]

Le porteur confirme : « le tour s’arrête sans nouvelle question ». Après une bonne réponse Primeur ou Grand Cru et la descente à l’extrémité inférieure du tapis, aucune question n’est posée sur la case d’arrivée ; le tour se termine. Le passage au joueur suivant demeure déclenché par le bouton explicite, conformément à la règle générale déjà validée. Cette décision clôt la question de la nouvelle question après descente ; les coordonnées et extrémités exactes restent à relever.

## Nombre de cases après le Départ [VALIDÉ]

À la question du nombre total de cases après le Départ, cercles de régions et Corse inclus, le porteur répond « 60 ». Le parcours comporte donc 60 cases après la position initiale Départ ; Val de Loire est la première et Corse la dernière. Le nombre est confirmé, mais les centres, associations et extrémités restent à relever.

## Relevé visuel proposé — en attente de validation

Le porteur autorise la préparation du relevé. `PLATEAU_NUMEROTE_PROPOSE.svg` et `CASES_PROPOSEES.csv` présentent 60 cases après le Départ (repère technique proposé 0), relevées manuellement sur l’image. `data/preparation/board.proposal.json` contient cette proposition isolée, marquée non jouable et à vérifier. Le brouillon validé `board.pending.json` ne reçoit pas ces coordonnées : ses listes de cases/effets restent vides jusqu’à approbation.

Cercles proposés : Val de Loire 1 ; Champagne 7 ; Alsace 12 ; Bourgogne 17 ; Beaujolais 26 ; Vallée du Rhône 28 ; Provence 34 ; Languedoc-Roussillon 37 ; Bordeaux 44 ; Corse 60. Les autres segments reprennent les catégories des couleurs confirmées.

Extrémités interprétées visuellement, non validées : échelle 4 → 19 ; échelle 27 → 38 ; tapis 56 → 33. Les centres visibles sous les illustrations d’effets demandent une attention particulière ; aucune précision au pixel ni règle d’extrémité n’est garantie par le simple relevé.

Vérifications réellement exécutées : 60 IDs/ordres consécutifs uniques, coordonnées bornées, dix cercles/régions distincts, cohérence catégorie/région, extrémités référant à des cases existantes, échelles avançantes/tapis reculant dans la proposition, CSV de 61 lignes avec Départ, SVG XML valide avec 61 repères et référence image présente. Ces contrôles vérifient la structure, pas l’exactitude graphique ni la validité métier des extrémités. SHA-256 du ZIP, d’AGENTS.md et du cahier inchangés ; image originale inchangée. Aucun test du moteur ni rendu navigateur exécuté.

À valider par le porteur : numérotation complète, position des centres, correspondance des couleurs aux cases et les trois paires d’extrémités. Après approbation seulement, intégrer le relevé dans les données de plateau puis tester les déplacements.

## Relevé du plateau approuvé [VALIDÉ]

Le porteur valide la proposition complète par « C’est parfait », en réponse à la demande de validation de la numérotation, des coordonnées et des trois paires d’extrémités. Le relevé est intégré dans `data/board.json` : Départ 0, cases 1–60, échelles 4 → 19 et 27 → 38, tapis 56 → 33. Les centres et catégories/régions proposés sont désormais validés. Les fichiers de proposition et le brouillon antérieur sont conservés comme traces de préparation ; `data/board.json` est la référence structurée actuelle.

Contrôles exécutés à l’intégration : 60 cases présentes et trois paires d’effets conformes à la proposition approuvée. Aucune modification des sources historiques. Les règles de réponses, répétition et minuterie encore ouvertes ne sont pas tranchées par cette validation du plateau.

## Correction des QCM multiples [VALIDÉ]

Le porteur confirme qu’un QCM à plusieurs bonnes réponses est réussi uniquement si toutes les bonnes réponses et aucune mauvaise sont sélectionnées. La comparaison porte sur l’ensemble exact des choix corrects ; aucune réussite partielle. Cette règle est consignée dans `data/rules.json`. Les choix corrects de chaque question restent à structurer et vérifier depuis les réponses originales ; la décision ne valide pas une extraction automatique des textes.

## Questions ouvertes : validation orale par le groupe [VALIDÉ]

Le porteur confirme le parcours : réponse orale, affichage de la réponse attendue, puis validation par le groupe avec « Correct » ou « Incorrect ». Aucune évaluation automatique de la parole n’est requise. La règle est consignée dans `data/rules.json`. Le moment de clôture de la réponse et l’arrêt du chronomètre lors de la révélation restent à confirmer ; la validation du groupe ne doit pas permettre de transformer une expiration déjà survenue en réussite.

## Questions ouvertes : arrêt du chronomètre à la révélation [VALIDÉ]

Le porteur confirme que le bouton « Voir la réponse » arrête le chronomètre lorsqu’il est pressé avant les 60 secondes. La réponse orale est alors clôturée ; le groupe lit la réponse attendue puis valide « Correct » ou « Incorrect ». Si les 60 secondes sont atteintes ou dépassées, l’expiration vaut échec conformément à la règle générale, et une validation tardive ne peut pas la transformer en réussite. Cette décision est consignée dans `data/rules.json` ; la politique en arrière-plan ou à la fermeture reste à confirmer.

## Chronomètre en arrière-plan et après fermeture [VALIDÉ]

Le porteur confirme que les 60 secondes continuent à s’écouler si l’application passe en arrière-plan ou est fermée pendant une question. À la reprise, un délai atteint ou dépassé entraîne une réponse incorrecte. L’implémentation devra persister l’échéance absolue et traiter l’expiration une seule fois. Cette règle concerne une question encore en cours : elle ne redémarre pas le chronomètre arrêté par « Voir la réponse » avant expiration pour une question ouverte. La décision est consignée dans `data/rules.json` et résout la politique de temps en arrière-plan/reprise.

## Tirage : non-répétition puis filtre épuisé [VALIDÉ]

Le porteur confirme qu’une question déjà utilisée est évitée pendant toute la partie, tous joueurs confondus. Le suivi utilise l’identifiant de question, commun aux traductions FR/EN. Lorsque toutes les questions compatibles avec le filtre demandé ont été utilisées, les répétitions sont autorisées dans ce même filtre ; aucun autre niveau, catégorie ou région n’est substitué. Cette décision est consignée dans `data/rules.json`. Elle ne fixe pas un mécanisme particulier de cycles ou de réinitialisation de l’historique, ni un comportement pour un filtre initialement vide.

## Ordre des joueurs [VALIDÉ]

Le porteur confirme que les joueurs jouent dans leur ordre de saisie lors de la configuration. Le premier joueur saisi commence ; les tours suivent cet ordre de façon cyclique. Aucun tirage aléatoire de l’ordre n’est ajouté. Cette décision est consignée dans `data/rules.json` et résout la détermination de l’ordre initial.

## Structuration et moteur réalisés

668 questions structurées, cinq cas de format isolés pour validation (QUESTIONS_A_VALIDER.md). Moteur TypeScript indépendant dans src/game/engine.ts : 29 tests Vitest et 11 tests Python réussis, contrôle TypeScript réussi. Voir MOTEUR_DE_JEU.md pour le périmètre, les résultats et limites. Les demandes métier déjà résolues dans les décisions successives ne sont pas à redemander ; les cinq corrections de format et les éléments éditoriaux/restants ne sont pas validés implicitement.

## Cinq corrections approuvées et banque complète

Le porteur confirme « Oui, je valide » pour les cinq corrections proposées (108, 166, 511, 532, 564). Elles sont intégrées uniquement dans les fichiers dérivés et dans le script reproductible de structuration, avec provenance par langue. La banque contient 673 questions bilingues et aucun cas de format en attente. Les signalements éditoriaux distincts de l’audit ne sont pas déclarés vérifiés par cette validation. Tests exécutés après intégration : 14 tests Python, 29 tests Vitest, contrôle TypeScript et contrôle du brouillon réussis. Les références, ZIP et CSV restent inchangés.

## Interface locale implémentée

Parcours mobile FR/EN branché sur le moteur et les 673 questions, avec reprise IndexedDB, confirmation avant remplacement, plateau zoomable, pions numérotés et sons synthétiques locaux. Bilan et limites : INTERFACE_MOBILE.md. Vérifications finales : 34 tests Vitest, 14 tests Python, 4 tests Chromium et compilation réussis. Aucun déploiement ni service worker PWA ; pas encore de garantie de rechargement hors ligne. Les nouveaux libellés/résumés d’interface restent proposés à relecture.
