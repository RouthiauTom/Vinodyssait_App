# Préparation des données — bilan de phase 1

## Résultat disponible

L’audit et l’architecture ont été validés, puis la préparation autorisée par le porteur. Le projet utilise directement `Vinodyssait_App`. Aucun changement des documents de référence, des CSV ou de l’archive historique.

`data/preparation/questions.draft.json` rapproche les 673 questions et leurs 1346 traductions FR/EN. Les champs source complets sont conservés dans `sourceMetadata` et `sourceTranslation`, en plus des champs structurés id/catégorie/région/niveau. Les textes et réponses ne subissent ni correction, ni traduction, ni normalisation des sauts de ligne. Le brouillon est explicitement `draft_not_playable` ; il ne contient aucun choix correct ou type de question inventé. Chaque question reste `reviewStatus: pending`.

Les catégories 1–4 gardent leurs difficultés 1/2/3. Les 300 Domaines conservent une difficulté null, conformément à la décision du porteur, et leur région 1–10. Les IDs sont rapprochés explicitement, sans employer la colonne `translations` comme lien vers les deux textes.

## Import reproductible sans dépendance installée

- Générer : `python3 -B scripts/prepare_questions.py`
- Contrôler sans écriture : `python3 -B scripts/prepare_questions.py --check`
- Tester : `python3 -B -m unittest discover -s tests/data -v`

Le script écrit seulement le brouillon dérivé ; il ne modifie pas les CSV. Les empreintes des deux sources sont incluses dans le JSON. Le mode check compare le brouillon aux sources actuelles sans le réécrire. Ces outils de préparation utilisent la bibliothèque standard Python ; le moteur et l’UI futurs restent prévus en TypeScript/React.

## Vérifications effectivement exécutées

Six tests passés : Domaines sans difficulté et conservation exacte des textes/champs sources, rejet de traduction dupliquée, de langue manquante, de traduction orpheline, de niveau attribué aux Domaines et de métadonnée dupliquée.

Génération réelle puis contrôle sans écriture réussis : 673 questions bilingues. Vérification des empreintes historiques et CSV réalisée après la préparation, voir INTEGRITE_PHASE_1.md. Aucun test de moteur, build frontend ou test navigateur n’a été exécuté : ces modules n’existent pas encore.

## Suite requise pour une banque jouable

Qualifier et valider les types, séparer les choix et réponses correctes, conserver les explications et normaliser les formats uniquement dans une copie dérivée approuvée. Les cas 2, 108, 111, 152, 203, 480, 500–507, 532, 337/368 signalés dans l’audit restent en revue. Confirmer la correction des QCM multiples et la validation orale des réponses ouvertes, ainsi que répétition/épuisement et exhaustivité des CSV. Une classification automatique n’est pas adoptée.

Le plateau reste à valider : voir VALIDATION_PLATEAU.md et sa fiche de relevé. `board.pending.json` n’ajoute aucun nombre de cases, coordonnée, association ou effet arbitraire. La phase 1 est donc en cours, pas déclarée terminée ; le moteur n’est pas implémenté sur des règles non établies.

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
