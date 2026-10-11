# Support de relevé du plateau

[VALIDÉ] Le porteur confirme les droits en réponse à la demande concernant le plateau. Cette confirmation est consignée pour le plateau ; elle n’est pas étendue implicitement à des sons, polices ou autres ressources.

`Plateau_original.png` est une copie exacte de l’entrée `VinodysSait_Game/vinodys-sait-frontend/src/components/assets/Plateau_france.png` dans le ZIP. SHA-256 de l’image : `77c5f48c3a3a9e2ea610c82af0f256151145f617aae21cd070b1b5ad4c95e946`. SHA-256 du ZIP avant/après : `49178f502be2a27448fd01ed50608f8f24d9a06ebb2104b3fc8d9ba21317a7c3`.

Ouvrir `RELEVE_PLATEAU.svg` en conservant le PNG dans le même dossier. Le quadrillage et les axes sont des repères de mesure, pas des coordonnées de cases. Le dessin original n’a pas été modifié. Aucune numérotation du parcours, catégorie de case ou paire d’extrémités d’effet n’a été inventée. La fiche CSV de relevé reste dans `docs/CASE_PLATEAU_A_COMPLETER.csv`.

Il reste à confirmer ce qui compte comme une case : segments colorés, cercles de région, point de départ et arrivée. Une fois l’ordre confirmé, relever les centres sur ce support et soumettre le tableau complet à validation avant toute utilisation par le moteur.

## Relevé visuel proposé — en attente de validation

Le porteur autorise la préparation du relevé. `PLATEAU_NUMEROTE_PROPOSE.svg` et `CASES_PROPOSEES.csv` présentent 60 cases après le Départ (repère technique proposé 0), relevées manuellement sur l’image. `data/preparation/board.proposal.json` contient cette proposition isolée, marquée non jouable et à vérifier. Le brouillon validé `board.pending.json` ne reçoit pas ces coordonnées : ses listes de cases/effets restent vides jusqu’à approbation.

Cercles proposés : Val de Loire 1 ; Champagne 7 ; Alsace 12 ; Bourgogne 17 ; Beaujolais 26 ; Vallée du Rhône 28 ; Provence 34 ; Languedoc-Roussillon 37 ; Bordeaux 44 ; Corse 60. Les autres segments reprennent les catégories des couleurs confirmées.

Extrémités interprétées visuellement, non validées : échelle 4 → 19 ; échelle 27 → 38 ; tapis 56 → 33. Les centres visibles sous les illustrations d’effets demandent une attention particulière ; aucune précision au pixel ni règle d’extrémité n’est garantie par le simple relevé.

Vérifications réellement exécutées : 60 IDs/ordres consécutifs uniques, coordonnées bornées, dix cercles/régions distincts, cohérence catégorie/région, extrémités référant à des cases existantes, échelles avançantes/tapis reculant dans la proposition, CSV de 61 lignes avec Départ, SVG XML valide avec 61 repères et référence image présente. Ces contrôles vérifient la structure, pas l’exactitude graphique ni la validité métier des extrémités. SHA-256 du ZIP, d’AGENTS.md et du cahier inchangés ; image originale inchangée. Aucun test du moteur ni rendu navigateur exécuté.

À valider par le porteur : numérotation complète, position des centres, correspondance des couleurs aux cases et les trois paires d’extrémités. Après approbation seulement, intégrer le relevé dans les données de plateau puis tester les déplacements.
