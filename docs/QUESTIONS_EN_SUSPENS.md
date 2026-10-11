# Questions en suspens

> **État actuel après réception de `QuestionsId.csv` :** les métadonnées des 673 questions sont désormais disponibles et raccordées exactement au CSV FR/EN. Les mentions de métadonnées manquantes dans les étapes antérieures ci-dessous décrivent leur état à cette date et sont remplacées par le complément final. Les 300 questions Domaines n’ont pas de niveau : banque commune par région confirmée par le porteur [VALIDÉ], B7 résolu. Aucun code de jeu ni conversion JSON créé.

Aucune proposition ci-dessous n’est une règle adoptée. Les réponses sont à consigner après validation du porteur, sans modifier les documents de référence sans autorisation.

## Bloquants avant une implémentation fidèle

| ID | Question / élément à fournir | Pourquoi |
| --- | --- | --- |
| B1 | CSV de traductions reçu. Fournir les métadonnées Question (id/catégorie/région/niveau/image) et correspondances Category/Domain, sans comptes, sessions, secrets ou données personnelles. | 673 questions avec FR/EN identifiées dans le CSV ; catégories/régions/niveaux et types structurés manquent. Aucune connexion à la base historique effectuée. |
| B2 | Fournir ou valider le plateau numéroté : départ, arrivée, nombre/ordre de cases, centres et correspondances catégories/régions. Existe-t-il un plateau HD ? | L’image 1000 × 1000 n’a ni IDs ni coordonnées associées. |
| B3 | Quelles sont les cases départ/arrivée de chaque échelle et tapis ? Les effets se déclenchent-ils seulement en s’arrêtant, se chaînent-ils ? | Aucune paire codée ; illustration insuffisante pour une règle. |
| B4 | Dans quel ordre résoudre déplacement, échelle/tapis, question, échec et victoire ? Quelle case détermine la question après une échelle et où revient-on après échec ? | Plusieurs conséquences possibles, aucune à choisir implicitement. |
| B5 | Tapis : destination exacte si Primeur/Grand Cru, si Millésime incorrect ou expiré ; Millésime correct laisse-t-il sur la case du tapis ? | Seul l’évitement du recul après réussite Millésime est établi. |
| B6 | À l’arrivée ou au dépassement de la Corse, faut-il répondre avant de gagner ou la victoire est-elle immédiate ? | La priorité de victoire n’est pas fixée. |
| B7 | Les questions Domaines ont-elles des niveaux réels ? Comment appliquer le choix de niveau à chacune sans classifier arbitrairement les données ? | V1 ignore le niveau de cette catégorie, V2 le demande à chaque question. |
| B8 | Confirmer les réponses ouvertes : réponse orale, révélation de la référence puis validation du groupe. Quelle action ferme la réponse avant 60 s ? Que faire si le délai expire pendant la lecture/validation ? | La V1 révèle seulement la réponse, sans verdict. |
| B9 | Non-répétition : sur toute la partie ou autrement ? Quand un filtre est vide/épuisé, autoriser répétition, autre niveau/catégorie ou interrompre le tirage ? Que faire si EN manque ? | Aucun comportement de secours approuvé. |
| B10 | Autorisez-vous le transfert dans V2 des ressources retenues et confirmez-vous leurs droits (plateau, logo, avatars, sons, questions, traductions, police) ? | Condition avant copie et publication ; aucun asset transféré pendant l’audit. |

## Décisions complémentaires avant les phases concernées

| ID | Décision | Proposition éventuelle [RECOMMANDÉ] |
| --- | --- | --- |
| D1 | Ordre initial des joueurs | Ordre saisi/modifiable ; ne pas ajouter de tirage d’ordre sans accord |
| D2 | Timer en arrière-plan/fermeture | Échéance absolue ; fermeture ne suspend pas les 60 s ; à valider |
| D3 | Correction puis recul visible | Action explicite après lecture ; préciser si bouton séparé ou continuation enchaînée |
| D4 | QCM à une ou plusieurs réponses | Adapter aux données réelles ; définir comparaison/notation sans points partiels inventés |
| D5 | Langue globale ou par joueur, changement pendant une question | Choix à expliciter, question stable et traductions réelles |
| D6 | Avatars comme pions et variante sonore | Choisir parmi ressources après inspection/écoute ; aucun nouveau visuel nécessairement ajouté |
| D7 | Identité typographique et mentions légales hors ligne | Jost locale si droits/fichier fournis, sinon choix validé ; fournir le texte légal à embarquer |
| D8 | Architecture proposée | React/TypeScript/Vite, moteur pur, JSON, IndexedDB, PWA, Vitest/Playwright ; détails et versions à confirmer pendant mise en œuvre |
| D9 | Dépôt GitHub et publication | Dépôt distant distinct, Pages statique ; aucune création distante/publication effectuée |

## Validation de la mission 1

Valider le rapport et l’architecture avant tout code de jeu. La validation du rapport ne remplace pas les réponses aux règles ambiguës ni l’audit complémentaire des questions manquantes. La prochaine étape sera la préparation des données et du plateau, après autorisation ; aucun jeu ne sera commencé sur une numérotation ou une banque inventée.

## Mise à jour des questions après réception du CSV

B1 est partiellement résolu : textes et réponses FR/EN identifiés pour 673 IDs. Il reste à fournir les métadonnées `Question` (`id`, `categoryId`, `domainId`, `difficulty`, `imageUrl`) et les correspondances `Category`/`Domain`, ou une table équivalente approuvée. Aucun export de comptes/sessions/secrets n’est nécessaire. Confirmez-vous que les 673 questions représentent la totalité de la banque à conserver, et ce que signifie la colonne `quel ` ?

D4 n’est plus hypothétique : des réponses multiples sont présentes aux IDs 111, 152 et 480. Quelle règle souhaitez-vous pour leur validation (ensemble exact ou autre règle explicitement définie) ? Les choix multiples doivent être signalés au joueur.

Confirmer la procédure de revue avant correction dans les données dérivées des séparateurs (532 FR), formulations/traductions (exemples 2 et dernières questions EN), et du doublon de formulation EN 337/368. Aucun texte source ne sera changé.

L’emplacement du projet est fixé par votre nouvelle instruction : `Vinodyssait_App`. Aucun travail ultérieur n’est prévu dans le dossier externe créé précédemment. La mission 1 est désormais validée par le porteur.

## État courant — décisions restantes après `QuestionsId.csv`

B1 est résolu pour la disponibilité des textes et métadonnées des 673 IDs, ainsi que leur raccordement. Il reste seulement à confirmer : ces deux CSV représentent-ils toute la banque à conserver ? Les IDs catégories/niveaux/régions ont-ils exactement les libellés de la V1 ? Quel est le rôle des colonnes `quel ` et `translations` (cette dernière répète systématiquement `id`) ? Aucun nouvel export n’est nécessaire pour joindre les questions reçues.

**B7 reste bloquant : les 300 questions Domaines ont réellement un niveau vide, avec 30 questions par région.** Souhaitez-vous qu’elles constituent une banque commune quel que soit le niveau choisi, ou fournir une classification validée par niveau ? Une exception sans choix de niveau modifierait l’exigence validée du cahier et nécessiterait votre décision explicite. Aucune de ces options n’est adoptée.

Les questions de plateau, effets, priorité de victoire, réponses ouvertes, QCM multiples, épuisement/répétition, reprise du timer et droits restent en attente. L’audit et l’architecture sont désormais validés par le porteur ; les règles encore ambiguës doivent être tranchées avant leur implémentation.

## B7 résolu — décision explicite [VALIDÉ]

Réponse du porteur : « Il n'y pas de niveaux pour les domaines donc une banque commune ».

Conséquence : catégorie Domaines sans niveau, banque commune filtrée par région et langue. Aucun classement Primeur/Grand Cru/Millésime à demander ou inventer pour ces 300 questions. B7 est clôturé. La demande antérieure de choisir entre banque commune et classification est remplacée par cette décision.

Restent notamment : validation de l’audit, définition des cases et effets, priorité de victoire, réponse ouverte, QCM multiples, répétition/épuisement, reprise du timer et droits des ressources. L’interaction éventuelle entre tapis (condition Millésime) et une case Domaines devra être examinée avec les associations réelles du plateau ; aucune règle supplémentaire n’est décidée ici.

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
