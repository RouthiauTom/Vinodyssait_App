# Audit de l’application originale

> **État actuel après réception de `QuestionsId.csv` :** les métadonnées des 673 questions sont désormais disponibles et raccordées exactement au CSV FR/EN. Les mentions de métadonnées manquantes dans les étapes antérieures ci-dessous décrivent leur état à cette date et sont remplacées par le complément final. Les 300 questions Domaines n’ont pas de niveau : banque commune par région confirmée par le porteur [VALIDÉ], B7 résolu. Aucun code de jeu ni conversion JSON créé.

Date : 11 octobre 2026. Phase 0, analyse statique en lecture seule.

## Périmètre et preuves

Source : `/Users/tomrouthiau/Documents/Vinodyssait_App/VinodysSait_Game.zip`.
Références lues intégralement : `AGENTS.md` et `CAHIER_DES_CHARGES_VINODYSSAIT.md` dans ce même dossier. Les chemins ci-dessous sont internes au ZIP, sous `VinodysSait_Game/`.

L’archive a été consultée directement en mémoire, sans extraction, installation, lancement de l’application, connexion à PostgreSQL ou exécution de migration. Les `.env`, secrets et le contenu du dépôt `.git` n’ont pas été consultés ou transférés. L’absence de données est établie dans les fichiers livrés hors historique Git ; celui-ci n’a pas été fouillé. La présence d’un code ne prouve pas son fonctionnement en production. Aucun test applicatif historique n’a été exécuté.

Le ZIP comporte 401 entrées, dont 97 fichiers hors répertoires, métadonnées `__MACOSX`, `.git` et `.env`. Les dépendances ci-dessous sont celles déclarées dans les manifests historiques ; aucune validation de leurs versions actuelles n’a été réalisée.

## Architecture réellement présente

- Frontend JavaScript React 19.1.1 déclaré, Create React App (`react-scripts` 5.0.1), React Router 6.30.1, i18next/react-i18next. CSS par composant, avec règles globales répétées et styles inline.
- Backend Express 4.18.2 déclaré dans `server/package.json`, Prisma 6.16.1, PostgreSQL, JWT et sessions en base, bcrypt, envoi d’emails via Resend. Le package racine déclare séparément Express 5.1.0 : ce sont deux manifests distincts.
- `server/src/index.js` monte les routes auth, profils, jeu, extensions. Socket.IO ne gère que connexion/déconnexion ; aucun multijoueur de jeu n’est établi par ce code.
- `src/api/api.js` utilise `REACT_APP_API_URL` et un jeton Bearer. Plusieurs composants font aussi leurs propres appels fetch.
- Pas de moteur de plateau séparé, TypeScript, sauvegarde de partie, IndexedDB ou service worker trouvé dans les fichiers audités. Un manifest existe, mais ne rend pas les questions disponibles hors ligne.

## Écrans et navigation

Preuve principale : `vinodys-sait-frontend/src/App.js`.

| Route / composant | Fonction présente | Traitement proposé V2 |
| --- | --- | --- |
| `/` — Home | Connexion, inscription, mot de passe oublié, FR/EN, lien achat | Remplacer par nouvelle partie/reprise, conserver identité et langue |
| `/profiles` — Profiles | CRUD de profils via API, pseudo, avatar, langue ; limite de 4 | Configuration locale de 2 à 10 joueurs ; avatars candidats |
| `/gameChoice` — GameChoice | France, miniature du plateau, accès par code | Accès direct au plateau France |
| `/menu` — Menu | Jouer, règles, paramètres avec images FR/EN | Conserver ces entrées utiles |
| `/game` — GamePlay | Tirage de questions, choix catégorie/niveau ou région, timer, réponse | Réutiliser le parcours comme référence ; créer jeu complet |
| `/rules` — Rules | Texte des règles via i18next/Trans | Conserver et compléter après validation |
| `/settings` — Settings | Sons boutons/timer via API, mot de passe, avertissement, lien légal | Réglages locaux ; texte légal disponible localement à prévoir |
| `/verify/:token`, `/verify` — VerifyPage | Vérification email | Hors périmètre V2 |
| `/reset-password/:token`, `/change-password` | Gestion mots de passe | Hors périmètre V2 |

Le jeton de garde des routes est conservé dans l’état React de `App`, alors que d’autres composants utilisent localStorage : une réouverture ne reconstitue pas uniformément ce parcours. `/game` est ouvert directement ; l’ancienne condition profil/jeu est commentée. Les profils et jeux passent surtout dans `location.state`, sans état de partie durable.

## Jeu réellement codé et règles seulement décrites

`GamePlay.js:70–95` définit cinq catégories, dix régions et trois niveaux. Le parcours codé est : catégorie → niveau (catégories 1–4) ou région (catégorie 5) → tirage API → 60 secondes → affichage de la réponse → nouvelle question.

`GamePlay.js:97` charge `/api/game/play`. Le timer démarre après réception de la question ; le tic-tac commence avant la requête. À zéro, la réponse est révélée. Aucun statut bonne/mauvaise réponse, pénalité, score, pion ou tour n’est enregistré. Le bouton « Voir la réponse » arrête le timer. Aucun choix interactif de QCM/vrai-faux n’est implémenté : question et réponse sont affichées comme texte. `imageUrl`, renvoyée par l’API, n’est pas affichée par ce composant.

Le texte `src/i18n.js`, rendu par `Rules.js`, décrit dé, maintien après réussite, retour à la position précédente après échec, passage de tour, échelles, tapis et victoire en Corse. Ces règles ne sont pas exécutées par le code audité. Aucun ordre de cases ni paire d’extrémités d’effet n’a été trouvé.

## Questions : localisation et structure

Source d’exécution : `server/src/routes/game.js`, GET `/play`, authentifié. Prisma lit `Question` et ses `QuestionTranslation`, filtre puis tire aléatoirement une question en mémoire.

Schéma actuel `server/prisma/schema.prisma` :

- Question : `id`, `categoryId`, `domainId?`, `difficulty?` (String), `imageUrl?`, `createdAt`.
- QuestionTranslation : `id`, `questionId`, `language`, `question`, `answer`, `createdAt` ; unicité question/langue.
- Category : liée à Game ; Domain : lié à Category. Dans l’UI, « Domain » désigne les régions viticoles, pas une liste de propriétés individuelles.

Aucun champ structuré de type de question, choix, réponse correcte ou explication séparée n’existe dans ce schéma. Des QCM pourraient être inclus dans le texte des données, mais cela ne peut être établi sans les enregistrements.

Aucun fichier CSV, XLS/XLSX, dump de base, JSON de questions, seed ou document de banque de questions n’a été trouvé dans les fichiers livrés hors `.git`. Les sept migrations SQL ne contiennent pas d’INSERT/COPY. L’exemple de question dans le texte des règles n’est pas une banque exploitable. Dans le ZIP seul, le volume, la couverture FR/EN, les types et les images sont inconnus. Le CSV ajouté après cet audit précise volume et présence FR/EN : voir le complément ci-dessous.

IDs UI à vérifier face aux données réelles :

| Catégorie | ID | Couleur historique |
| --- | --- | --- |
| Histoire | 1 | #5AA5B0 |
| Géographie | 2 | #0B7C5A |
| Accords / Crus / Dégustation | 3 | #2B303A |
| Métiers / Vinification | 4 | #d74933 |
| Domaines | 5 | #b157b0ff |

Niveaux : 1 Primeur, 2 Grand Cru, 3 Millésime. Leur encodage réel en base reste inconnu. Régions UI : 1 Val de Loire, 2 Champagne, 3 Alsace, 4 Bourgogne, 5 Beaujolais, 6 Vallée du Rhône, 7 Provence, 8 Languedoc-Roussillon, 9 Bordeaux, 10 Corse. Aucune association à une case n’est établie.

La route accepte `excludedIds`, mais le frontend ne l’envoie pas et ne tient pas de registre de questions tirées. Pour la catégorie 5, le niveau est ignoré : seul le domaine/région est filtré. Le serveur revient au français si la traduction demandée manque ; la sélection ne garantit pas la présence de cette traduction.

## Traductions

`src/i18n.js` embarque des textes d’interface et de règles FR/EN. Les niveaux utilisent « Vintage » en anglais ; les régions gardent majoritairement leur nom français. Les cartes de menu existent en deux langues. `server/src/i18n/{fr,en}.js` concerne les emails et messages de compte, pas les questions. Certains messages frontend sont codés directement en français, notamment l’erreur de tirage. La complétude des traductions de questions ne peut pas être vérifiée.

## Ressources réutilisables candidates

Aucune ressource n’a été transférée. Réutilisation soumise à confirmation des droits et à validation du choix des fichiers.

- `src/components/assets/Plateau_france.png` : 1000 × 1000, 578180 octets. Inspection visuelle effectuée en mémoire : France, parcours coloré, régions jusqu’à la Corse, deux illustrations d’échelles et un tapis. Les cases ne sont pas numérotées ; ne pas déduire automatiquement leurs IDs/extrémités. Résolution à évaluer pour le zoom ; demander un original haute définition s’il existe.
- `logo.png` : 3613 × 2118, 92626 octets.
- `jouerFR/EN.png` : 330 × 455 ; `reglesFR/EN.png`, `paramFR/EN.png` : 330 × 443. Ce sont les visuels d’entrée du menu, pas des fichiers de questions ni une preuve autonome des règles.
- Drapeaux `fr.png` : 275 × 183 ; `en.png` : 1200 × 600.
- 12 avatars `avatar1.png` à `avatar12.png` : environ 110 × 110 (5 et 10 : 110 × 111). Aucun système de pions mobiles de plateau trouvé ; adéquation à ce rôle à valider.
- Sons : `click.mp3` (28416 octets), `tic-tac.mp3` (1550235), réellement importés ; `click_Tom.mp3` (11702), `tic-tac_Tom.mp3` (174707), variantes présentes. Aucun test d’écoute ou d’autoplay mobile exécuté.
- Icônes publiques/favicon et `src/logo.svg`. Les `logo192.png` et `logo512.png` mesurent tous deux 1724 × 1725, contrairement au manifest ; variantes `_2` aux tailles 192 et 512. Ne pas retenir des icônes sans contrôle visuel.
- Police Jost appelée depuis Google Fonts dans les CSS ; aucun fichier local de police trouvé. Prévoir une police locale autorisée ou une police système après validation esthétique.

## Anomalies statiques et limites

- Schéma Prisma actuel et migrations divergent : la migration initiale crée `questionText/answerText` dans Question ; aucune migration livrée ne crée QuestionTranslation ni Session. Une reconstruction fidèle de la base n’est pas démontrée.
- `routes/extensions.js` utilise `usedById`, absent du schéma (`usedBy`) ; `routes/game.js` utilise `usedBy`.
- Erreur réseau de tirage : `hasDrawn` reste vrai et aucun bouton dédié de relance n’est rendu ; le tic-tac peut continuer.
- `handleBack` depuis l’étape question ne nettoie pas systématiquement l’intervalle ; le nettoyage au démontage et au reset existe.
- `Settings.js` écrit le jeton en console. Ne transférer ni authentification ni journalisation de données sensibles.
- `App.test.js` est encore le test modèle « learn react » ; le script test racine annonce qu’aucun test n’est défini. Aucun test métier identifié. Ces tests n’ont pas été lancés.
- Aucun résultat de build, d’exécution, de navigateur, d’accessibilité ou de sécurité exhaustive n’est revendiqué.

## Conclusion

Conserver les contenus réels, l’identité, les catégories/niveaux, le plateau et les sons utiles. Remplacer les dépendances serveur par des données et réglages locaux. Créer le moteur, les joueurs/tours, la correction interactive, le plateau superposé, la sauvegarde et le hors ligne. La banque CSV reçue a été auditée dans le complément ci-dessous ; les métadonnées de catégorie, région et niveau restent nécessaires.

## Inventaire exhaustif des fichiers hors secrets/historique Git

Chemins internes au ZIP et taille non compressée. Aucun fichier de cette liste n’a été copié.

| Fichier | Octets |
| --- | ---: |
| `README.md` | 18 |
| `.gitignore` | 292 |
| `package-lock.json` | 61922 |
| `package.json` | 541 |
| `server/test-jwt.js` | 508 |
| `server/.gitignore` | 93 |
| `server/package-lock.json` | 83041 |
| `server/package.json` | 715 |
| `vinodys-sait-frontend/README.md` | 3359 |
| `vinodys-sait-frontend/.gitignore` | 310 |
| `vinodys-sait-frontend/package-lock.json` | 669097 |
| `vinodys-sait-frontend/package.json` | 979 |
| `server/prisma/schema.prisma` | 3734 |
| `server/src/db.js` | 113 |
| `server/src/index.js` | 1553 |
| `vinodys-sait-frontend/public/favicon.ico` | 9662 |
| `vinodys-sait-frontend/public/index.html` | 1767 |
| `vinodys-sait-frontend/public/logo512.png` | 59965 |
| `vinodys-sait-frontend/public/logo192_2.png` | 5347 |
| `vinodys-sait-frontend/public/manifest.json` | 484 |
| `vinodys-sait-frontend/public/robots.txt` | 67 |
| `vinodys-sait-frontend/public/logo512_2.png` | 9664 |
| `vinodys-sait-frontend/public/favicon_2.ico` | 3870 |
| `vinodys-sait-frontend/public/logo192.png` | 59965 |
| `vinodys-sait-frontend/src/reportWebVitals.js` | 362 |
| `vinodys-sait-frontend/src/App.css` | 977 |
| `vinodys-sait-frontend/src/index.js` | 271 |
| `vinodys-sait-frontend/src/index.css` | 279 |
| `vinodys-sait-frontend/src/App.test.js` | 246 |
| `vinodys-sait-frontend/src/setupTests.js` | 241 |
| `vinodys-sait-frontend/src/logo.svg` | 2632 |
| `vinodys-sait-frontend/src/i18n.js` | 13885 |
| `vinodys-sait-frontend/src/App.js` | 2440 |
| `server/prisma/migrations/migration_lock.toml` | 128 |
| `server/src/middleware/auth.js` | 1481 |
| `server/src/i18n/index.js` | 180 |
| `server/src/i18n/en.js` | 1471 |
| `server/src/i18n/fr.js` | 2623 |
| `server/src/routes/game.js` | 5217 |
| `server/src/routes/auth.js` | 10039 |
| `server/src/routes/profiles.js` | 2297 |
| `server/src/routes/extensions.js` | 1547 |
| `vinodys-sait-frontend/src/components/Home.css` | 2807 |
| `vinodys-sait-frontend/src/components/ChangePassword.css` | 1589 |
| `vinodys-sait-frontend/src/components/Rules.js` | 1833 |
| `vinodys-sait-frontend/src/components/GamePlay.css` | 3466 |
| `vinodys-sait-frontend/src/components/Rules.css` | 832 |
| `vinodys-sait-frontend/src/components/VerifyPage.js` | 2750 |
| `vinodys-sait-frontend/src/components/Settings.css` | 1040 |
| `vinodys-sait-frontend/src/components/Home.js` | 7027 |
| `vinodys-sait-frontend/src/components/GameChoice.js` | 4586 |
| `vinodys-sait-frontend/src/components/ResetPassword.js` | 2479 |
| `vinodys-sait-frontend/src/components/VerifyPage.css` | 1049 |
| `vinodys-sait-frontend/src/components/Profiles.css` | 3003 |
| `vinodys-sait-frontend/src/components/Profiles.js` | 8621 |
| `vinodys-sait-frontend/src/components/GameChoice.css` | 2401 |
| `vinodys-sait-frontend/src/components/Menu.js` | 3059 |
| `vinodys-sait-frontend/src/components/GamePlay.js` | 12083 |
| `vinodys-sait-frontend/src/components/Menu.css` | 1694 |
| `vinodys-sait-frontend/src/components/ChangePassword.js` | 3130 |
| `vinodys-sait-frontend/src/components/ResetPassword.css` | 1822 |
| `vinodys-sait-frontend/src/components/Settings.js` | 4250 |
| `vinodys-sait-frontend/src/api/api.js` | 665 |
| `server/prisma/migrations/20250923165730_add_reset_password_token/migration.sql` | 124 |
| `server/prisma/migrations/20250913133914_add_domain_id_to_question/migration.sql` | 87 |
| `server/prisma/migrations/20250921122527_add_email_verification/migration.sql` | 309 |
| `server/prisma/migrations/20250913131215_add_domains/migration.sql` | 646 |
| `server/prisma/migrations/20251001175355_add_sound_preferences/migration.sql` | 169 |
| `server/prisma/migrations/20250918195514_test/migration.sql` | 1285 |
| `server/prisma/migrations/20250913115303_init/migration.sql` | 3017 |
| `vinodys-sait-frontend/src/components/hooks/usePreferences.js` | 935 |
| `vinodys-sait-frontend/src/components/assets/reglesFR.png` | 131662 |
| `vinodys-sait-frontend/src/components/assets/reglesEN.png` | 128250 |
| `vinodys-sait-frontend/src/components/assets/paramEN.png` | 123681 |
| `vinodys-sait-frontend/src/components/assets/en.png` | 5254 |
| `vinodys-sait-frontend/src/components/assets/paramFR.png` | 125245 |
| `vinodys-sait-frontend/src/components/assets/fr.png` | 398 |
| `vinodys-sait-frontend/src/components/assets/logo.png` | 92626 |
| `vinodys-sait-frontend/src/components/assets/Plateau_france.png` | 578180 |
| `vinodys-sait-frontend/src/components/assets/jouerEN.png` | 147648 |
| `vinodys-sait-frontend/src/components/assets/jouerFR.png` | 149891 |
| `vinodys-sait-frontend/src/components/assets/sounds/click_Tom.mp3` | 11702 |
| `vinodys-sait-frontend/src/components/assets/sounds/click.mp3` | 28416 |
| `vinodys-sait-frontend/src/components/assets/sounds/tic-tac.mp3` | 1550235 |
| `vinodys-sait-frontend/src/components/assets/sounds/tic-tac_Tom.mp3` | 174707 |
| `vinodys-sait-frontend/src/components/assets/avatars/avatar9.png` | 5692 |
| `vinodys-sait-frontend/src/components/assets/avatars/avatar8.png` | 4468 |
| `vinodys-sait-frontend/src/components/assets/avatars/avatar5.png` | 5024 |
| `vinodys-sait-frontend/src/components/assets/avatars/avatar4.png` | 7826 |
| `vinodys-sait-frontend/src/components/assets/avatars/avatar6.png` | 3832 |
| `vinodys-sait-frontend/src/components/assets/avatars/avatar7.png` | 4478 |
| `vinodys-sait-frontend/src/components/assets/avatars/avatar3.png` | 3481 |
| `vinodys-sait-frontend/src/components/assets/avatars/avatar12.png` | 4621 |
| `vinodys-sait-frontend/src/components/assets/avatars/avatar2.png` | 8829 |
| `vinodys-sait-frontend/src/components/assets/avatars/avatar10.png` | 5183 |
| `vinodys-sait-frontend/src/components/assets/avatars/avatar11.png` | 6280 |
| `vinodys-sait-frontend/src/components/assets/avatars/avatar1.png` | 6935 |

## Vérifications effectivement exécutées en phase 0

- Lecture des références et sources indiquées, recherche de données et contrôle des dimensions PNG : réalisés.
- Présence des cinq documents Markdown non vides : contrôlée.
- Empreintes SHA-256 avant/après identiques pour archive et références (voir ci-dessous).
- Aucun test métier, build, installation ou test navigateur exécuté ; aucune migration ni connexion base.

| Référence | SHA-256 avant et après |
| --- | --- |
| `AGENTS.md` | `be1869374c6ba186748188f73574c672725f9ae803dbd4b4c576193f8551771c` |
| `CAHIER_DES_CHARGES_VINODYSSAIT.md` | `52967649240491ea40edbf5f3d7f96b376fb85995f8022e64306b39f36906f33` |
| `VinodysSait_Game.zip` | `49178f502be2a27448fd01ed50608f8f24d9a06ebb2104b3fc8d9ba21317a7c3` |

## Complément — CSV reçu et périmètre de travail corrigé

Le porteur demande désormais de travailler exclusivement dans `Vinodyssait_App`. Le nouveau projet et ses rapports sont placés dans `Vinodyssait_App/`, dans un dépôt local distinct. Les cinq rapports précédemment produits ont été rapatriés comme documents ; aucun code, secret, asset ou Git historique n’a été transféré. Le dossier créé précédemment à l’extérieur n’a pas été supprimé : aucune opération destructive n’a été effectuée. Les rapports du présent sous-dossier font foi pour cette mise à jour.

L’inventaire ZIP ci-dessus reste exact pour l’archive. Ses constats « questions non trouvées » ne s’appliquent pas au nouveau CSV externe, analysé séparément ici.

### Source et contrôles exécutés

Fichier : `2026-QUESTIONS TOUTES LES LANGUES - TAB 2 (2).csv`, 526483 octets, UTF-8 lisible, séparateur virgule. Lecture avec le parseur CSV, sans modification du fichier. En-têtes exacts : `quel ` (avec espace final), `questionId`, `language`, `question`, `answer`, `createdAt`.

- 1346 enregistrements de données, tous à six colonnes ; 673 IDs de question, de 1 à 673, sans trou.
- 673 lignes `fr` et 673 lignes `en` : chaque ID dispose exactement d’une ligne dans chaque langue.
- Aucun couple `(questionId, language)` dupliqué ; aucun champ vide après suppression des espaces périphériques.
- La colonne `quel ` comporte 1346 valeurs distinctes. Son nom est atypique ; son rôle d’identifiant de traduction est plausible, non confirmé. Ne pas la renommer dans la source.
- Aucun URL HTTP(S) détecté dans les questions ou réponses. Cela ne démontre pas l’absence d’images associées ailleurs.
- Une question anglaise identique après retrait des espaces périphériques apparaît aux IDs 337 et 368 ; les formulations françaises diffèrent (`vin doux` / `vin sucré`). Ne pas fusionner ces IDs sans accord.

La présence des deux langues est établie, mais la fidélité des traductions, l’exactitude œnologique et l’exhaustivité par rapport à la banque originale ne sont pas certifiées par ce contrôle structurel. Aucune recherche factuelle externe ni correction éditoriale n’a été effectuée.

### Métadonnées absentes

Le CSV ressemble à un export de QuestionTranslation, mais ne contient pas `categoryId`, `domainId`, `difficulty`, `imageUrl`, ni type explicite, liste structurée de choix, IDs de réponses correctes ou explication séparée. Le texte `answer` combine fréquemment réponse et commentaire. Le rapprochement avec les tables Question, Category et Domain est nécessaire pour filtrer fidèlement les questions selon une case et un niveau.

Ne pas déduire la catégorie, région ou difficulté du rang des IDs, du vocabulaire ou des blocs thématiques. Les niveaux des questions Domaines restent inconnus. Impossible de calculer actuellement une couverture catégorie × région × niveau × langue.

### Types et anomalies de normalisation

Repérage heuristique uniquement : une question est candidate QCM si les marqueurs A et B sont détectés après un début de texte ou saut de ligne réel/littéral ; candidate vrai/faux si `Vrai ou Faux` / `True or False` est détecté ; sinon elle reste à qualifier. Ces chiffres ne sont pas une classification validée :

| Langue | QCM candidats | Vrai/faux candidats | Autres à qualifier |
| --- | ---: | ---: | ---: |
| FR | 441 | 84 | 148 |
| EN | 442 | 84 | 147 |

La différence provient de l’ID 532 FR : le séparateur avant B est mal formé (barres obliques inverses sans `n`), alors que A/C et EN ont des séparateurs de ligne. Cette question est candidate à une correction de format dans une future copie dérivée, après validation, jamais dans le CSV source.

Les textes utilisent des sauts de ligne échappés de plusieurs formes ; 889 champs question contiennent la séquence littérale barre oblique inverse + n, 457 n’en contiennent pas. Normaliser seulement dans les données dérivées, avec conservation du texte source et contrôle des choix obtenus.

Exemples nécessitant un traitement structuré et une revue humaine :

- ID 111 : réponse listant A, B et C ; ID 152 : `B et C` ; ID 480 : A, D et E. Les QCM à plusieurs réponses sont réellement présents textuellement. Définir la règle de sélection et de correction avant leur intégration.
- ID 203 : réponse `Les deux` sans lettre au début ; ID 108 : `B` sans ponctuation standard ; IDs 500–507 : préfixe `Réponse X`. Une extraction fondée uniquement sur la première lettre suivie de deux-points serait insuffisante.
- 26 lignes parmi les QCM candidats ne commencent pas par une lettre suivie de `:`, `.` ou `)` ; ce contrôle étroit est un signal de revue, pas une liste exhaustive des cas complexes.
- ID 2 : formulation `Dom Pérignon a inventé…` alors que l’explication nuance cette attribution ; la traduction anglaise du choix C diffère du français. Consigner pour revue éditoriale, sans modifier ou certifier la réponse.
- Exemples de formulation EN `Corsen` et `Corse` dans les dernières questions : revue linguistique à prévoir sans inventer de traduction.

### Suite autorisée après validation

Obtenir les métadonnées rattachées aux 673 IDs, confirmer le rôle de `quel `, vérifier que ce CSV est la banque complète et recueillir la politique de QCM multiples. Préparer ensuite un rapport d’import avec provenance, types et choix approuvés, puis des JSON locaux uniquement après validation du rapport d’audit. Aucun import de jeu ou code applicatif réalisé à cette étape.

### Intégrité vérifiée après le complément

| Fichier source | SHA-256 avant/après identique |
| --- | --- |
| `AGENTS.md` | `be1869374c6ba186748188f73574c672725f9ae803dbd4b4c576193f8551771c` |
| `CAHIER_DES_CHARGES_VINODYSSAIT.md` | `52967649240491ea40edbf5f3d7f96b376fb85995f8022e64306b39f36906f33` |
| `VinodysSait_Game.zip` | `49178f502be2a27448fd01ed50608f8f24d9a06ebb2104b3fc8d9ba21317a7c3` |
| `2026-QUESTIONS TOUTES LES LANGUES - TAB 2 (2).csv` | `1c21f3e66a98b0beb40cb4a7ec1a9d9ceb150a4b2b1704d0fd3f0795cfd945e0` |

## Complément — métadonnées `QuestionsId.csv`

Source lue uniquement, UTF-8, virgule, 673 lignes de données à sept colonnes : `id`, `categoryId`, `difficulty`, `domainId`, `translations`, `imageUrl`, `createdAt`.

Contrôles exécutés : aucun ID dupliqué, aucune ligne de largeur incorrecte, aucune traduction sans métadonnée et aucune métadonnée sans traduction. Le rapprochement par `QuestionsId.id = questionId` fournit exactement une traduction FR et EN pour chacun des 673 IDs.

### Répartition des questions

Les libellés ci-dessous sont ceux associés aux IDs dans l’UI historique ; aucun export des tables Category/Domain n’a été fourni pour les confirmer indépendamment. Les valeurs 1/2/3 correspondent au mapping de niveaux de cette UI.

| Catégorie UI | Primeur (1) | Grand Cru (2) | Millésime (3) | Niveau absent | Total |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 — Histoire | 30 | 30 | 30 | 0 | 90 |
| 2 — Géographie | 30 | 30 | 30 | 0 | 90 |
| 3 — Accords / Crus / Dégustation | 30 | 30 | 30 | 0 | 90 |
| 4 — Métiers / Vinification | 43 | 30 | 30 | 0 | 103 |
| 5 — Domaines | 0 | 0 | 0 | 300 | 300 |
| Total | 133 | 120 | 120 | 300 | 673 |

Chacune de ces questions a ses textes FR/EN. Les 300 questions de catégorie 5 disposent d’un `domainId` de 1 à 10, avec exactement 30 questions pour chaque ID. Selon les libellés de la V1 : Val de Loire, Champagne, Alsace, Bourgogne, Beaujolais, Vallée du Rhône, Provence, Languedoc-Roussillon, Bordeaux, Corse. Aucun `domainId` n’est présent dans les autres catégories. Les 373 questions des catégories 1–4 ont toutes un niveau de 1 à 3 ; les 300 Domaines n’en ont aucun.

Les 673 `imageUrl` sont vides : cet export ne référence donc aucune image de question. Cela ne remplace pas une confirmation de l’exhaustivité des ressources disponibles.

La colonne `translations` contient exactement la même valeur que `id` pour chaque ligne ; ce n’est pas une liste des deux IDs de traduction et sa sémantique reste à confirmer. Utiliser le rapprochement explicite par `questionId`, sans déduire des relations à partir de cette colonne. La colonne `quel ` du CSV de traductions reste également à identifier.

### Conséquences

Le blocage de localisation et de raccordement des métadonnées est résolu pour les fichiers fournis. Leur correspondance aux libellés historiques est documentée ; demander confirmation de ces mappings plutôt qu’inventer des catégories. Aucune banque locale dérivée n’a encore été produite.

Le manque de niveau des Domaines confirme le comportement constaté en V1. Ne pas attribuer des niveaux, répartir ces questions en trois groupes ou ignorer un choix de niveau sans décision explicite du porteur. La couverture par région est de 30 questions bilingues, mais la couverture par région ET niveau ne peut pas être établie.

La complétude structurelle des deux CSV ne certifie ni leur exhaustivité par rapport à toutes les questions du jeu, ni la qualité des traductions, ni l’exactitude scientifique. Les cas de QCM multiples et formats signalés précédemment restent à traiter après validation.

### Contrôle d’intégrité après ce complément

Les cinq sources ci-dessous ont des empreintes identiques avant/après.

| Fichier | SHA-256 |
| --- | --- |
| `AGENTS.md` | `be1869374c6ba186748188f73574c672725f9ae803dbd4b4c576193f8551771c` |
| `CAHIER_DES_CHARGES_VINODYSSAIT.md` | `52967649240491ea40edbf5f3d7f96b376fb85995f8022e64306b39f36906f33` |
| `VinodysSait_Game.zip` | `49178f502be2a27448fd01ed50608f8f24d9a06ebb2104b3fc8d9ba21317a7c3` |
| `QuestionsId.csv` | `162406a68392cd2a5cf436d73f9c87e4c0414858cc164a63e3bb26327eda3b8d` |
| `2026-QUESTIONS TOUTES LES LANGUES - TAB 2 (2).csv` | `1c21f3e66a98b0beb40cb4a7ec1a9d9ceb150a4b2b1704d0fd3f0795cfd945e0` |

## Décision du porteur — Domaines sans niveau [VALIDÉ]

Le porteur confirme : « Il n'y pas de niveaux pour les domaines donc une banque commune ». Les 300 questions Domaines constituent une banque commune aux niveaux, avec sélection par région (`domainId`), puis langue. Aucun niveau ne sera attribué à ces questions et leur champ `difficulty` absent sera conservé. La présence des 30 questions FR/EN pour chacune des dix régions a été contrôlée précédemment. Cette décision résout B7 ; les choix de niveaux restent pertinents pour les catégories 1–4. Elle ne tranche pas les autres règles en attente et n’autorise pas à commencer le code avant validation de l’audit.

## Validation et organisation actuelles [VALIDÉ]

Le porteur a validé l’audit et l’architecture et autorise le travail directement dans `Vinodyssait_App`, sans sous-projet V2. Le dépôt de la racine est le dépôt de travail, distinct du dépôt historique contenu dans le ZIP. Les passages antérieurs demandant la validation de l’audit sont clos ; les décisions métier encore ouvertes restent à recueillir.

Organisation actuelle : `docs/` pour les rapports ; `sources/questions/` pour les deux CSV inchangés ; `sources/audit-initial/` préserve uniquement les métadonnées Git du dépôt local créé pendant l’audit. Le ZIP historique et les deux références restent à leur emplacement d’origine, strictement inchangés. Aucun développement n’est effectué dans les dossiers de sources.

Prochaine phase autorisée : préparation des données et du plateau. Ne pas inventer les coordonnées, effets spéciaux, réponses correctes structurées ou traductions. Les Domaines utilisent la banque commune sans niveau déjà validée.
