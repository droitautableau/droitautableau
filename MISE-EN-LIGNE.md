# Mettre droitautableau.fr en ligne

Compte environ 30 minutes, plus jusqu'à quelques heures d'attente pour que le domaine s'active. Tu n'as rien à installer : tout se fait dans le navigateur.

Le site est hébergé gratuitement sur **GitHub Pages** (tu as déjà un compte GitHub). Le domaine et ta boîte mail restent chez Infomaniak : on ajoute juste quelques lignes, sans toucher au mail.

Le site est dans le dossier `droitautableau/` (sur ton PC : `09 Site droitautableau\droitautableau`).

---

## Étape 1 : créer le dépôt GitHub

1. Va sur github.com, connecte-toi, clique sur **+** en haut à droite, puis **New repository**.
2. Nom : `droitautableau`. Coche **Public** (GitHub Pages gratuit l'exige ; le dépôt ne contient que le site, rien de personnel).
3. Clique sur **Create repository**.
4. Sur la page du dépôt, clique sur **uploading an existing file**.
5. Ouvre le dossier `droitautableau` sur ton PC, sélectionne **tout son contenu** (pas le dossier lui-même : les fichiers `index.html`, `style.css`, `CNAME`… et les dossiers `img` et `fonts`) et glisse-le dans la page.
6. En bas, clique sur **Commit changes**.

## Étape 2 : activer GitHub Pages

1. Dans le dépôt : **Settings**, puis **Pages** dans le menu de gauche.
2. *Source* : **Deploy from a branch**. *Branch* : **main**, dossier **/ (root)**. **Save**.
3. Dans *Custom domain*, tu dois voir `droitautableau.fr` (il vient du fichier `CNAME`). Sinon, tape-le et clique sur **Save**.

## Étape 3 : relier le domaine chez Infomaniak

1. Manager Infomaniak : **Domaines**, puis `droitautableau.fr`, puis **Zone DNS**.
2. **Ne supprime aucune ligne MX, SPF ou autoconfig** : ce sont elles qui font marcher contact@droitautableau.fr.
3. Supprime seulement les éventuelles lignes **A** et **AAAA** déjà présentes pour `droitautableau.fr` (sans sous-domaine) et la ligne `www` si elle existe.
4. Ajoute ces lignes :

| Type | Source | Valeur |
|---|---|---|
| A | (vide / @) | 185.199.108.153 |
| A | (vide / @) | 185.199.109.153 |
| A | (vide / @) | 185.199.110.153 |
| A | (vide / @) | 185.199.111.153 |
| AAAA | (vide / @) | 2606:50c0:8000::153 |
| AAAA | (vide / @) | 2606:50c0:8001::153 |
| AAAA | (vide / @) | 2606:50c0:8002::153 |
| AAAA | (vide / @) | 2606:50c0:8003::153 |
| CNAME | www | TON-PSEUDO-GITHUB.github.io. |

5. Attends (de 10 minutes à quelques heures). Dans GitHub, **Settings > Pages** finit par afficher « DNS check successful ».
6. Coche alors **Enforce HTTPS**. Le site s'ouvre sur https://droitautableau.fr.

**Conseillé (protection) :** dans GitHub, clique sur ta photo > **Settings** > **Pages** > **Add a domain**, tape `droitautableau.fr`. GitHub te donne une ligne **TXT** à ajouter dans la zone DNS Infomaniak. Ça empêche quelqu'un d'autre d'utiliser ton domaine sur GitHub.

## Étape 4 : les statistiques (Cloudflare Web Analytics)

1. Crée un compte gratuit sur cloudflare.com (pas besoin d'y mettre ton domaine).
2. Menu **Analytics & Logs > Web Analytics > Add a site**, tape `droitautableau.fr`.
3. Cloudflare affiche un petit code avec `"token": "..."`. **Envoie-moi juste ce token** : je l'ajoute au site et je mets à jour la page Confidentialité. Tant qu'il n'y est pas, le site ne mesure rien (et la page Confidentialité le dit).

## Étape 5 : remplacer Linktree

Mets `droitautableau.fr` dans ta bio TikTok et dans les liens de ta chaîne YouTube (Personnalisation > Infos de base > Liens).

---

## Mettre le site à jour plus tard

Tu me dis quelle vidéo ajouter (avec son lien YouTube). Je régénère le site, puis tu remplaces les fichiers dans GitHub (**Add file > Upload files**, glisse les fichiers modifiés, **Commit changes**). Le site se met à jour en une minute.

## Point juridique sur l'anonymat

Les mentions légales disent que tu es une personne non professionnelle anonyme, ce que la loi (LCEN) permet **à condition que l'hébergeur ait ton identité**. GitHub ne vérifie pas les identités : pour être tranquille, utilise un compte GitHub relié à une adresse mail à ton nom, pour que l'hébergeur puisse t'identifier si un juge le demande. Ce n'est pas un conseil juridique : à faire confirmer si tu veux être sûr. Le jour où tu vendras le pack L1, il faudra de toute façon des mentions complètes (identité, statut, SIRET) et des CGV.
