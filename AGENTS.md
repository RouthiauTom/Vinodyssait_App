# Instructions permanentes pour Codex — Vinodys'Sait

## Priorité absolue : protection du projet historique
Le projet source historique et son archive ZIP sont STRICTEMENT EN LECTURE SEULE. Ne jamais modifier, supprimer, renommer, reformater, installer des dépendances ou exécuter des migrations dans son répertoire. Ne jamais copier ses secrets, `.env` ou `.git`. Travailler exclusivement dans un NOUVEAU répertoire et un NOUVEAU dépôt. Demander confirmation avant toute action risquant de toucher à la source historique.

## Référence de spécification
Lire `CAHIER_DES_CHARGES_VINODYSSAIT.md` avant toute implémentation. Respecter les statuts [VALIDÉ], [RECOMMANDÉ], [À VÉRIFIER]. Ne jamais inventer une règle, une question, une traduction ou une coordonnée de case manquante.

## Méthode de travail
1. Commencer par un audit **en lecture seule** et un inventaire des écrans, règles, ressources et fichiers de questions.
2. Présenter un plan de développement par étapes et la liste des décisions bloquantes.
3. Implémenter un moteur de jeu indépendant de l'UI, testable par fonctions pures.
4. Écrire les tests des règles avant ou en même temps que leur implémentation.
5. Utiliser une banque de questions locale et une sauvegarde locale ; aucune API distante obligatoire pour jouer.
6. Construire une interface mobile-first fidèle au plateau original.
7. Après chaque étape, présenter : modifications dans le **nouveau** projet, tests exécutés, résultats et questions en attente.
8. Ne jamais déclarer un test réussi s'il n'a pas été exécuté.
9. Ne jamais lancer de commandes destructrices sans accord explicite.
10. Garder le dépôt GitHub Pages statique et préparer une migration mobile ultérieure sans refonte complète.

## Première mission demandée
Faire l'audit de la source historique en lecture seule ; retrouver les fichiers de questions ; lister les ressources réutilisables ; comparer les règles au cahier des charges ; proposer l'arborescence de la nouvelle application et les questions bloquantes. **Ne pas commencer à coder le jeu avant validation du rapport d'audit.**
