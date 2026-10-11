# Analyse des écarts

> **État actuel après réception de `QuestionsId.csv` :** les métadonnées des 673 questions sont désormais disponibles et raccordées exactement au CSV FR/EN. Les mentions de métadonnées manquantes dans les étapes antérieures ci-dessous décrivent leur état à cette date et sont remplacées par le complément final. Les 300 questions Domaines n’ont pas de niveau : banque commune par région confirmée par le porteur [VALIDÉ], B7 résolu. Aucun code de jeu ni conversion JSON créé.

Référence : cahier des charges 1.0, 11 octobre 2026. « Présent » signifie identifié statiquement, sans test d’exécution. Preuves détaillées dans AUDIT_APPLICATION_ORIGINALE.md.

| Exigence / statut du cahier | V1 constatée | Travail V2 |
| --- | --- | --- |
| [VALIDÉ] 2–10 joueurs sur un appareil | Un profil actif, maximum 4 profils de compte ; aucun tour | Configuration locale et moteur multi-joueurs |
| [VALIDÉ] Plateau fidèle et tactile | Image affichée dans GameChoice ; aucun plateau jouable | Couche pions, zoom/déplacement, coordonnées validées |
| [VALIDÉ] Dé 1–6, progression | Dé décrit dans règles seulement | Implémenter et tester |
| [VALIDÉ] Niveau avant chaque question | Niveau pour catégories 1–4 ; région seule pour Domaines | Clarifier couverture de niveaux Domaines ; région dérivée de case |
| [VALIDÉ] Bonne réponse / retour après échec | Texte des règles ; aucun verdict ni déplacement | Résolution après correction, tests et garde de phases |
| [VALIDÉ] Timer 60 s, expiration incorrecte | Révélation à 60 s, sans verdict/pénalité | Échec et pénalité uniques, échéance persistée selon décision |
| [VALIDÉ] QCM/vrai-faux automatiques | Affichage textuel uniquement | Structurer les données et corriger les choix |
| [VALIDÉ] Ouvertes : réponse puis validation | Réponse révélée, sans validation | Boutons de validation du groupe ; confirmer le sens de « auto » |
| [VALIDÉ] Échelles et tapis | Texte et illustration ; aucune règle exécutée | Extrémités, ordre et cas validés avant codage |
| [VALIDÉ] Victoire atteint ou dépasse Corse | Texte « atteindre », aucun calcul | Priorité victoire/question/effets à décider |
| [VALIDÉ] Joueur suivant explicite | Nouvelle question, sans joueur | Transition manuelle protégée contre double clic |
| [VALIDÉ] Banque locale réelle | Question/Translation dans PostgreSQL ; CSV de traductions désormais fourni | Fournir fichiers, analyser puis importer sans inventer |
| [VALIDÉ] FR/EN | UI/règles bilingues ; questions non vérifiables | Audit couverture ; traductions manquantes fournies/validées |
| [VALIDÉ] Sons configurables | Deux préférences en base, quatre fichiers sons | Réglages locaux, audio centralisé |
| [VALIDÉ] Sauvegarde/reprise | token/lang en localStorage ; pas de partie | État versionné et récupération d’erreurs |
| [VALIDÉ] Hors ligne après chargement | API, comptes, Google Fonts ; aucun service worker | Précache complet, données embarquées, police locale/système |
| [VALIDÉ] GitHub Pages | Backend Express indispensable au tirage | Application statique, base et chemins testés |
| [RECOMMANDÉ] Capacitor | Aucun code mobile identifié | Adaptateurs indépendants ; évaluation après web stable |

## Contradictions et ambiguïtés à résoudre

1. Le cahier présente la catégorie et la région comme à vérifier : les IDs et libellés UI sont désormais identifiés, mais la banque et leur association aux cases restent inconnues. Aucune modification du document de référence n’a été faite.
2. Le niveau pour chaque question, validé en V2, s’oppose au parcours Domaines de la V1 et à son niveau facultatif en base. Ne pas attribuer arbitrairement un niveau aux questions historiques.
3. « Échelle automatique » ne précise pas si la question se pose avant/après la montée, à quelle catégorie/région, ni où revenir après échec. L’illustration ne tranche pas.
4. « Atteint ou dépasse » ne dit pas si la victoire est immédiate ou conditionnée à la dernière réponse. Une priorité explicite est nécessaire.
5. « Le processus fait marche arrière » dans le texte historique du tapis ne fixe pas destination ni effets successifs. Le cahier valide l’évitement du recul après réussite Millésime, mais laisse les autres cas ouverts.
6. Choix d’une région manuel en V1, automatique par case en V2 : conserver les régions, remplacer la sélection dans le parcours normal.
7. L’anglais retombe silencieusement sur le français en V1 ; cela ne prouve pas un jeu totalement bilingue. Décider du comportement en l’absence d’une traduction.
8. « Tout conserver » doit se lire dans le périmètre V2 : comptes, mots de passe, déblocages, modèles Purchase/AdminUser et emails ne sont pas à reproduire. Aucun système complet de paiement/admin n’est démontré par leur seule présence en base.

## Détails manquants nécessaires

- Cases : départ/position initiale, ordre total, couleurs/catégories, régions, destinations d’effets ; correspondance image/données approuvée.
- Questions : types réels, simple ou multiple choix, IDs de choix corrects, explications, images et fichiers locaux, encodage des niveaux, volumes par filtre et langue.
- Tour : méthode de détermination de l’ordre initial ; boutons entre lecture de correction, recul et joueur suivant.
- Temps : événement qui clôt une réponse ouverte avant révélation, délai d’auto-validation et expiration pendant cette validation ; arrière-plan et fermeture.
- Tirage : non-répétition, épuisement, filtre vide ; aucune règle de secours ne sera choisie implicitement.
- Langue : globale à la partie ou réglable par joueur ; changement autorisé en question et conservation de l’identifiant tiré.
- Persistance : version du jeu/banque/plateau référencée, mise à jour compatible, erreur d’écriture et stockage indisponible.
- Ressources : droits, visuel HD si disponible, identité des pions/sons à garder, texte légal à rendre lisible hors ligne.

Ces points complètent des besoins déjà mentionnés ; ce ne sont pas de nouvelles règles. L’ordre initial, le comportement QCM et la fermeture d’une réponse ouverte sont des décisions fonctionnelles à recueillir, pas des hypothèses à coder.

## Priorité

Bloquants de réalisation fidèle : données des questions, définition des cases/effets, résolution d’un tour/victoire, règles de réponse et de tirage. Bloquants de publication : droits des ressources, couverture bilingue, parcours hors ligne et sauvegarde vérifiés. Le projet peut documenter ses propositions maintenant ; aucune implémentation de jeu avant validation du rapport.

## Mise à jour après réception du CSV

La présence de 673 questions avec textes et réponses FR/EN est désormais vérifiée : 1346 traductions, aucune paire question/langue dupliquée, aucun champ vide. Les constats d’absence de banque concernent le ZIP seul. Le manque actuel porte sur les métadonnées `categoryId`, `domainId`, `difficulty` et `imageUrl`, et la structuration des types/choix/corrections. La couverture FR/EN par ID est complète dans ce fichier ; qualité linguistique, couverture par filtre et exhaustivité de la banque restent à valider.

QCM multiples attestés textuellement (111, 152, 480), réponse sans lettre (203), format FR mal formé (532), texte EN identique pour 337/368 : voir le complément d’audit. Aucun de ces points n’a été corrigé dans la source. La correction automatique impose un import revu humainement, et non l’extraction naïve d’une première lettre.

## Mise à jour — métadonnées raccordées

`QuestionsId.csv` résout l’absence de catégorie/région/niveau pour les 673 IDs, sous réserve de confirmer les libellés correspondant aux IDs historiques. Répartition : catégories 1, 2 et 3, 90 chacune (30 par niveau) ; catégorie 4, 103 (43 Primeur, 30 Grand Cru, 30 Millésime) ; catégorie 5, 300 (30 par région, aucun niveau). Aucun ID orphelin ou dupliqué ; chaque question a FR/EN. Tous les `imageUrl` sont vides.

L’écart principal de données restant est désormais précis : le niveau obligatoire avant chaque question en V2 ne dispose d’aucune valeur dans les 300 questions Domaines. Ce point nécessite une décision fonctionnelle, aucune classification automatique ne sera inventée. Les associations cases/catégories/régions restent inconnues même si les métadonnées de questions sont disponibles.

## Écart Domaines résolu [VALIDÉ]

Décision explicite du porteur : les Domaines n’ont pas de niveaux et utilisent une banque commune, filtrée par région et langue. L’absence de difficulté dans les 300 lignes Domaines est conforme à cette règle et ne constitue plus un manque de données. L’exigence générale de niveau avant chaque question reçoit donc cette exception pour les Domaines ; aucune classification artificielle n’est nécessaire. Les références originales restent inchangées, leur éventuelle actualisation nécessite une autorisation distincte.

## Validation et organisation actuelles [VALIDÉ]

Le porteur a validé l’audit et l’architecture et autorise le travail directement dans `Vinodyssait_App`, sans sous-projet V2. Le dépôt de la racine est le dépôt de travail, distinct du dépôt historique contenu dans le ZIP. Les passages antérieurs demandant la validation de l’audit sont clos ; les décisions métier encore ouvertes restent à recueillir.

Organisation actuelle : `docs/` pour les rapports ; `sources/questions/` pour les deux CSV inchangés ; `sources/audit-initial/` préserve uniquement les métadonnées Git du dépôt local créé pendant l’audit. Le ZIP historique et les deux références restent à leur emplacement d’origine, strictement inchangés. Aucun développement n’est effectué dans les dossiers de sources.

Prochaine phase autorisée : préparation des données et du plateau. Ne pas inventer les coordonnées, effets spéciaux, réponses correctes structurées ou traductions. Les Domaines utilisent la banque commune sans niveau déjà validée.
