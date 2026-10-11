# Validation du plateau — phase 1 en cours

## Établi par les sources

Le plateau de référence est dans le ZIP, à `VinodysSait_Game/vinodys-sait-frontend/src/components/assets/Plateau_france.png`, 1000 × 1000 pixels. Il montre le départ au Val de Loire, l’arrivée en Corse, un parcours coloré, deux illustrations d’échelles et un tapis. L’image a été examinée pendant l’audit ; aucun fichier de numérotation ou coordonnées n’a été trouvé. Ces observations visuelles ne déterminent pas les cases exactes de déclenchement.

Aucun asset n’a été transféré : la confirmation des droits reste ouverte. Le fichier `data/preparation/board.pending.json` référence uniquement cette source et conserve les valeurs inconnues à null ou en listes vides ; il n’est pas utilisable pour jouer.

## Données à valider

Pour chaque case réelle : identifiant, ordre, centre normalisé x/y, catégorie, région éventuelle, effet éventuel. Distinguer le point de départ, les cases de régions et les segments colorés : leur fonction dans le parcours doit être confirmée, pas déduite automatiquement du dessin.

La fiche de relevé `docs/CASE_PLATEAU_A_COMPLETER.csv` contient uniquement les colonnes nécessaires, sans ligne fictive. La coordonnée x est le centre horizontal en pixels divisé par 1000, y le centre vertical divisé par 1000 ; origine en haut à gauche. Ces formules ne fixent aucune coordonnée à la place du porteur.

À fournir ou confirmer :

1. Nombre et ordre des cases, départ et arrivée, inclusion des cases de région dans le décompte des déplacements.
2. Association officielle couleurs/catégories et régions/cases ; les couleurs et IDs UI de la V1 sont documentés dans l’audit mais ne constituent pas cette correspondance.
3. Extrémités de chacune des échelles et du tapis, activation à l’arrêt ou au passage, effets successifs éventuels.
4. Ordre question/effet, catégorie de la question après une montée, position de retour en cas d’échec et priorité de victoire.
5. Ressource haute définition si disponible, et confirmation des droits de transfert pour produire un relevé visuel annoté dans le projet.

Un plateau déjà numéroté ou une photo annotée du jeu physique serait une référence utile. En son absence, un relevé visuel pourra être préparé comme proposition à vérifier, mais aucun ordre ou point proposé ne sera adopté comme règle sans validation.

## Règles connues et décisions encore ouvertes

[VALIDÉ] Dé 1–6, bonne réponse maintien, mauvaise réponse retour à la position avant lancer après lecture de correction, délai 60 secondes, choix explicite du joueur suivant, arrivée ou dépassement en Corse, Domaines sans niveau et banque commune par région.

[À VÉRIFIER] Destination exacte du tapis dans tous les cas, extrémités des échelles, ordre des effets et de la victoire, effets en chaîne, passage sans arrêt et éventuelle association tapis/Domaines. Ne pas résoudre ces questions au moyen d’une approximation de la carte.

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
