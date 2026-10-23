#!/usr/bin/env python3
"""Construit le site droitautableau.fr (pages HTML statiques) à la racine du dépôt.

Pour ajouter une vidéo : ajouter une entrée dans COURS ou METHODES, puis relancer
    python3 construire_site.py
"""
from pathlib import Path
from html import escape

SORTIE = Path(__file__).resolve().parent.parent  # racine du dépôt = racine du site
DOMAINE = "https://droitautableau.fr"
YOUTUBE = "https://www.youtube.com/@DroitauTableau"
TIKTOK = "https://www.tiktok.com/@droitautableau"
INSTAGRAM = "https://www.instagram.com/droitautableau"
MAIL = "contact@droitautableau.fr"
# Jeton Cloudflare Web Analytics (tableau de bord Cloudflare > Web Analytics). Vide = pas de statistiques.
CLOUDFLARE_TOKEN = "dcc2d9e8d9ec4beea6d0b43680309280"

ICONES = {
    "youtube": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.6 12 3.6 12 3.6s-7.5 0-9.4.5A3 3 0 0 0 .5 6.2 31 31 0 0 0 0 12a31 31 0 0 0 .5 5.8 3 3 0 0 0 2.1 2.1c1.9.5 9.4.5 9.4.5s7.5 0 9.4-.5a3 3 0 0 0 2.1-2.1A31 31 0 0 0 24 12a31 31 0 0 0-.5-5.8zM9.6 15.6V8.4l6.2 3.6-6.2 3.6z"/></svg>',
    "tiktok": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12.53.02c1.31-.02 2.61-.01 3.91-.02.08 1.53.63 3.09 1.75 4.17 1.12 1.11 2.7 1.62 4.24 1.79v4.03c-1.44-.05-2.89-.35-4.2-.97-.57-.26-1.1-.59-1.62-.93-.01 2.92.01 5.84-.02 8.75-.08 1.4-.54 2.79-1.35 3.94-1.31 1.92-3.58 3.17-5.91 3.21-1.43.08-2.86-.31-4.08-1.03-2.02-1.19-3.44-3.37-3.65-5.71-.02-.5-.03-1-.01-1.49.18-1.9 1.12-3.72 2.58-4.96 1.66-1.44 3.98-2.13 6.15-1.72.02 1.48-.04 2.96-.04 4.44-.99-.32-2.15-.23-3.02.37-.63.41-1.11 1.04-1.36 1.75-.21.51-.15 1.07-.14 1.61.24 1.64 1.82 3.02 3.5 2.87 1.12-.01 2.19-.66 2.77-1.61.19-.33.4-.67.41-1.06.1-1.79.06-3.57.07-5.36.01-4.03-.01-8.05.02-12.07z"/></svg>',
    "livre": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 3h7a3 3 0 0 1 2 .8A3 3 0 0 1 15 3h5a1 1 0 0 1 1 1v14a1 1 0 0 1-1 1h-5a2 2 0 0 0-2 2h-2a2 2 0 0 0-2-2H4a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1zm1 2v12h4a4 4 0 0 1 2 .5V6a1 1 0 0 0-1-1H5zm10 0a1 1 0 0 0-1 1v11.5a4 4 0 0 1 2-.5h3V5h-4z"/></svg>',
    "stylo": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16.3 2.3a1 1 0 0 1 1.4 0l4 4a1 1 0 0 1 0 1.4l-12 12a1 1 0 0 1-.5.3l-5 1a1 1 0 0 1-1.2-1.2l1-5a1 1 0 0 1 .3-.5l12-12zM17 4.4 5.9 15.5l-.6 3.2 3.2-.6L19.6 7 17 4.4z"/></svg>',
    "instagram": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 2h10a5 5 0 0 1 5 5v10a5 5 0 0 1-5 5H7a5 5 0 0 1-5-5V7a5 5 0 0 1 5-5zm0 2a3 3 0 0 0-3 3v10a3 3 0 0 0 3 3h10a3 3 0 0 0 3-3V7a3 3 0 0 0-3-3H7zm5 3.5a4.5 4.5 0 1 1 0 9 4.5 4.5 0 0 1 0-9zm0 2a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5zM17.3 5.5a1.2 1.2 0 1 1 0 2.4 1.2 1.2 0 0 1 0-2.4z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 5h18a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1zm1 2.4V17h16V7.4l-7.4 5.4a1 1 0 0 1-1.2 0L4 7.4zM5.7 7l6.3 4.6L18.3 7H5.7z"/></svg>',
}

# Matières : nom affiché, classe CSS du badge, couleur du bandeau des miniatures
MATIERES = {
    "constit": ("Droit constitutionnel", "#F28C6B"),
}

# url = lien exact de la vidéo YouTube (en attendant : la page des vidéos de la chaîne)
COURS = [
    {
        "id": "etat",
        "matiere": "constit", "niveau": "L1",
        "titre": "L'État en droit constitutionnel : le cours complet",
        "image": "img/etat.jpg", "duree": "8:10", "date": "18 octobre 2026",
        "url": "https://youtu.be/wr3pwngFDDI",
        "resume": "Qu'est-ce qu'un État en droit ? Les trois éléments constitutifs, la reconnaissance et la personnalité morale, avec les auteurs à citer et les pièges classiques du partiel.",
        "notions": [
            "Les définitions de l'État : Carré de Malberg, Weber, Kelsen et la convention de Montevideo (1933)",
            "Pourquoi obéir à l'État : contrat social ou rapport de force",
            "Les trois éléments : la population, le territoire, la puissance publique et la souveraineté",
            "La reconnaissance : constitutive ou déclarative (avis n° 1 de la commission Badinter, 1991)",
            "La personnalité morale de l'État et sa continuité (l'affaire des emprunts russes)",
        ],
        "exemples": "Sealand, le Vatican, l'ordre de Malte, le Somaliland",
        "chapitres": [
            ("0:00", "Sealand est-il un État ?"), ("0:41", "Pourquoi commencer par l'État"),
            ("1:15", "Pourquoi obéir à l'État ?"), ("1:52", "Les définitions de l'État"),
            ("3:11", "La population"), ("3:50", "Le territoire"),
            ("4:26", "La puissance publique et la souveraineté"), ("5:11", "La reconnaissance"),
            ("6:00", "La personnalité morale"), ("6:40", "Verdict sur Sealand"),
            ("7:24", "Récap et conseil pour le partiel"),
        ],
    },
    {
        "id": "formes-etat",
        "matiere": "constit", "niveau": "L1",
        "titre": "État unitaire, fédéral, confédération : le cours complet",
        "image": "img/formes-etat.jpg", "duree": "8:13", "date": "25 octobre 2026",
        "url": "https://youtu.be/i01Q7joVDEY",
        "resume": "Tout le chapitre sur les formes de l'État à partir d'un seul critère, le nombre de centres de pouvoir politique, avec les trois pièges qui tombent chaque année.",
        "notions": [
            "L'État unitaire : centralisation, déconcentration, décentralisation (art. 72 de la Constitution, lois Defferre de 1982, révision de 2003)",
            "Déconcentration ou décentralisation : la seule question à se poser, « qui nomme ? »",
            "L'État régional : Italie, Espagne, Écosse",
            "La confédération : un traité, des États souverains, l'unanimité, le droit de retrait",
            "L'État fédéral et les trois principes de Georges Scelle : superposition, autonomie, participation",
            "L'Union européenne : fédération ou confédération ?",
        ],
        "exemples": "les États-Unis, l'Allemagne et ses Länder, la Suisse, la Belgique",
        "chapitres": [
            ("0:00", "Le critère"), ("0:17", "L'État unitaire"), ("0:48", "Déconcentration"),
            ("1:09", "Décentralisation"), ("1:53", "Piège n° 1 : déconcentration ou décentralisation"),
            ("2:10", "L'État régional"), ("2:31", "La confédération"), ("3:23", "L'État fédéral"),
            ("4:08", "Les 3 principes de Scelle"), ("5:31", "Pièges n° 2 et n° 3"),
            ("6:06", "L'Union européenne"), ("6:45", "4 exemples pour tout fixer"),
            ("7:03", "Récap"), ("7:25", "Conseil pour le partiel"),
        ],
    },
]

METHODES = [
    {
        "id": "fiche-arret", "url": "https://www.tiktok.com/@droitautableau/video/7698756874455289120", "titre": "La fiche d'arrêt", "niveau": "L1", "dispo": True,
        "resume": "La méthode étape par étape, sur un vrai arrêt de L1 : Ass. plén., 29 juin 2001 (l'enfant à naître).",
        "points": ["Les faits, la procédure, les thèses en présence", "Le problème de droit, là où on perd le plus de points", "La solution et la façon de la rédiger"],
    },
    {
        "id": "commentaire-arret", "url": "https://www.tiktok.com/@droitautableau/video/7699220762737003808", "titre": "Le commentaire d'arrêt", "niveau": "L1", "dispo": True,
        "resume": "Les quatre étapes du commentaire, sur un grand classique : Ass. plén., 31 mai 1991 (mères porteuses).",
        "points": ["La fiche d'arrêt, qui devient ton introduction", "Sens, valeur, portée : trouver tes idées", "Un plan qui sort de l'arrêt", "La rédaction : citer, expliquer, donner ton avis"],
    },
    {
        "id": "code-civil", "url": "https://www.tiktok.com/@droitautableau/video/7699490578131701025", "titre": "Utiliser ton code civil en examen", "niveau": "L1", "dispo": True,
        "resume": "Trois réflexes pour trouver le bon article en 30 secondes, sur un vrai sujet : le respect du corps humain.",
        "points": ["L'index alphabétique à la fin du code", "Le numéro d'article en haut des pages", "Le sommaire et les décisions résumées sous les articles", "Le piège des vieux arrêts : l'ancien article 1382 est devenu l'article 1240 en 2016"],
    },
    {
        "id": "dissertation", "titre": "La dissertation juridique", "niveau": "L1", "dispo": False,
        "resume": "La méthode complète sur un sujet de L1 : « La loi est-elle encore l'expression de la volonté générale ? »",
        "points": [],
    },
]

PAGES_NAV = [("./", "Accueil"), ("cours.html", "Les cours"), ("methodologie.html", "Méthodologie"), ("contact.html", "Contact")]


def page(fichier, titre, description, contenu, nav_actif=None):
    nav = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if label == nav_actif else ""}>{label}</a>'
        for href, label in PAGES_NAV
    )
    canon = DOMAINE + "/" + ("" if fichier == "index.html" else fichier)
    stats = (
        f'<script defer src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon=\'{{"token": "{CLOUDFLARE_TOKEN}"}}\'></script>'
        if CLOUDFLARE_TOKEN else ""
    )
    titre_complet = titre if fichier == "index.html" else f"{titre} · Droit au Tableau"
    html = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{escape(titre_complet)}</title>
<meta name="description" content="{escape(description)}">
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#1F3B33">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Droit au Tableau">
<meta property="og:title" content="{escape(titre_complet)}">
<meta property="og:description" content="{escape(description)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{DOMAINE}/img/partage.jpg">
<meta property="og:locale" content="fr_FR">
<link rel="icon" type="image/png" href="img/favicon.png">
<link rel="apple-touch-icon" href="img/apple-touch-icon.png">
<link rel="preload" href="fonts/poppins-600.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="./"><img class="brand-mark" src="img/balance.png" alt="" width="32" height="32">Droit au Tableau</a>
    <nav class="nav" aria-label="Menu principal">{nav}</nav>
  </div>
</header>
<main>
{contenu}
</main>
<footer class="site-footer">
  <div class="wrap">
    <p>© 2026 Droit au Tableau</p>
    <nav aria-label="Informations">
      <a href="mentions-legales.html">Mentions légales</a>
      <a href="confidentialite.html">Confidentialité</a>
      <a href="contact.html">Contact</a>
    </nav>
  </div>
</footer>
{stats}
</body>
</html>
"""
    (SORTIE / fichier).write_text(html, encoding="utf-8")


def badges(c):
    nom, _ = MATIERES[c["matiere"]]
    return f'<span class="badge {c["niveau"].lower()}">{c["niveau"]}</span><span class="badge matiere {c["matiere"]}">{nom}</span>'


def carte(c):
    return f"""<article class="card">
  <a class="thumb" href="{c['url']}" target="_blank" rel="noopener"><img src="{c['image']}" alt="Miniature : {escape(c['titre'])}" width="640" height="360" loading="lazy"></a>
  <div class="meta">{badges(c)}<span>{c['duree']}</span></div>
  <h3><a href="cours.html#{c['id']}">{escape(c['titre'])}</a></h3>
</article>"""


def liens_reseaux():
    return f"""<div class="links">
  <a class="link-btn primary" href="{YOUTUBE}" target="_blank" rel="noopener">{ICONES['youtube']}S'abonner sur YouTube</a>
  <a class="link-btn" href="{TIKTOK}" target="_blank" rel="noopener">{ICONES['tiktok']}Suivre sur TikTok</a>
  <a class="link-btn" href="{INSTAGRAM}" target="_blank" rel="noopener">{ICONES['instagram']}Suivre sur Instagram</a>
  <a class="link-btn" href="cours.html">{ICONES['livre']}Tous les cours</a>
  <a class="link-btn" href="methodologie.html">{ICONES['stylo']}Méthodologie</a>
  <a class="link-btn" href="contact.html">{ICONES['mail']}Contact</a>
</div>"""


def accueil():
    cartes = "\n".join(carte(c) for c in reversed(COURS))
    contenu = f"""<section class="hero">
  <div class="wrap">
    <img class="avatar" src="img/logo.png" alt="Logo Droit au Tableau : une balance de la justice" width="160" height="160">
    <h1>Droit au Tableau</h1>
    <p class="lead">Tes cours de droit, expliqués au tableau. De la L1 au master.</p>
    {liens_reseaux()}
  </div>
</section>
<section class="section">
  <div class="wrap home-courses">
    <div class="section-head">
      <h2>Derniers cours</h2>
    </div>
    <div class="grid">{cartes}</div>
    <p class="more"><a href="cours.html">Tous les cours</a></p>
  </div>
</section>"""
    page("index.html", "Droit au Tableau · Cours de droit en vidéo, de la L1 au master",
         "Tes cours de droit expliqués au tableau, de la L1 au master : vidéos complètes par chapitre, résumés, auteurs et arrêts à citer, méthodologie.",
         contenu, "Accueil")


def cours():
    blocs = []
    for cle, (nom, couleur) in MATIERES.items():
        items = [c for c in COURS if c["matiere"] == cle]
        fiches = []
        for c in items:
            notions = "".join(f"<li>{escape(n)}</li>" for n in c["notions"])
            chap = "".join(f"<li><time>{t}</time> {escape(n)}</li>" for t, n in c["chapitres"])
            fiches.append(f"""<article class="course" id="{c['id']}">
  <a class="course-thumb" href="{c['url']}" target="_blank" rel="noopener"><img src="{c['image']}" alt="Miniature : {escape(c['titre'])}" width="640" height="360" loading="lazy"></a>
  <div class="course-body">
    <div class="meta">{badges(c)}<span>{c['duree']}</span><span>{c['date']}</span></div>
    <h3>{escape(c['titre'])}</h3>
    <p>{escape(c['resume'])}</p>
    <details class="chapters"><summary>Ce qu'il faut retenir</summary><ul>{notions}</ul></details>
    <details class="chapters"><summary>Les chapitres</summary><ol>{chap}</ol></details>
    <p><a href="{c['url']}" target="_blank" rel="noopener">Regarder le cours sur YouTube</a></p>
  </div>
</article>""")
        blocs.append(f"""<h2 class="subject-title" style="--dot:{couleur}">{nom}</h2>
{''.join(fiches)}""")
    contenu = f"""<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h1>Les cours</h1>
      <p class="lead">Un nouveau chapitre chaque dimanche.</p>
    </div>
    {''.join(blocs)}
  </div>
</section>"""
    page("cours.html", "Les cours", "Tous les cours de droit de Droit au Tableau classés par matière et niveau, avec un résumé de ce qu'il faut retenir pour le partiel.", contenu, "Les cours")


def methodologie():
    items = []
    for m in METHODES:
        pts = "".join(f"<li>{escape(p)}</li>" for p in m["points"])
        etat = f'<a href="{m.get("url", TIKTOK)}" target="_blank" rel="noopener">Voir la vidéo sur TikTok</a>' if m["dispo"] else ""
        badge_dispo = "" if m["dispo"] else '<span class="badge soon">Bientôt</span>'
        items.append(f"""<article class="method" id="{m['id']}">
  <div class="meta"><span class="badge {m['niveau'].lower()}">{m['niveau']}</span><span class="badge methodo">Méthodologie</span>{badge_dispo}</div>
  <h3>{escape(m['titre'])}</h3>
  <p>{escape(m['resume'])}</p>
  {f'<p>{etat}</p>' if etat else ''}
</article>""")
    contenu = f"""<section class="section">
  <div class="wrap narrow">
    <div class="section-head">
      <h1>Méthodologie</h1>
      <p class="lead">Chaque méthode en deux minutes, sur un vrai arrêt.</p>
    </div>
    {''.join(items)}
  </div>
</section>"""
    page("methodologie.html", "Méthodologie", "Les méthodes de la fiche d'arrêt, du commentaire d'arrêt, de la dissertation et de l'utilisation du code civil en examen, montrées sur de vrais arrêts.", contenu, "Méthodologie")


def contact():
    contenu = f"""<section class="section">
  <div class="wrap narrow">
    <div class="section-head">
      <h1>Contact</h1>
      <p class="lead">Une question, un chapitre à proposer, une erreur repérée : écris-moi.</p>
    </div>
    <div class="contact-box">
      <div class="mail"><a id="mail" href="mailto:{MAIL}">{MAIL}</a><button class="copy" type="button" data-copy="{MAIL}">Copier</button></div>
      <p class="note">Partenariats : même adresse, objet « Partenariat ».</p>
    </div>
  </div>
</section>
<script>
document.querySelectorAll("button.copy").forEach(function (b) {{
  b.addEventListener("click", function () {{
    navigator.clipboard.writeText(b.dataset.copy).then(function () {{ b.textContent = "Copié"; }}, function () {{
      var r = document.createRange(); r.selectNodeContents(document.getElementById("mail"));
      var s = getSelection(); s.removeAllRanges(); s.addRange(r);
    }});
  }});
}});
</script>"""
    page("contact.html", "Contact", "Contacter Droit au Tableau : questions sur les cours, suggestions de chapitres, partenariats.", contenu, "Contact")


def mentions():
    contenu = f"""<section class="section">
  <div class="wrap">
    <div class="prose">
      <span class="eyebrow">Informations légales</span>
      <h1>Mentions légales</h1>
      <h2>Éditeur du site</h2>
      <p>Le site droitautableau.fr est édité à titre non professionnel par une personne physique. Conformément à la loi n° 2004-575 du 21 juin 2004 pour la confiance dans l'économie numérique (LCEN), l'éditeur a choisi de préserver son anonymat : ses éléments d'identification ont été communiqués à l'hébergeur du site.</p>
      <p>Contact : <a href="mailto:{MAIL}">{MAIL}</a></p>
      <h2>Hébergement</h2>
      <p>GitHub, Inc. (service GitHub Pages), 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis. Site : <a href="https://github.com" rel="noopener">github.com</a>.</p>
      <h2>Nom de domaine</h2>
      <p>Le nom de domaine droitautableau.fr est enregistré auprès d'Infomaniak Network SA, rue Eugène-Marziano 25, 1227 Genève, Suisse.</p>
      <h2>Propriété intellectuelle</h2>
      <p>Les textes, vidéos, miniatures, le logo et le nom « Droit au Tableau » sont protégés par le droit d'auteur. Toute reproduction sans autorisation est interdite, sauf les exceptions prévues par le Code de la propriété intellectuelle (courte citation avec la source, usage privé). Les textes de loi et les décisions de justice cités restent libres de droits.</p>
      <h2>Contenu pédagogique</h2>
      <p>Les vidéos et résumés sont des supports de révision. Ils ne remplacent ni ton cours ni les consignes de tes enseignants, et ne constituent pas un conseil juridique. Malgré le soin apporté, une erreur reste possible : signale-la à l'adresse ci-dessus.</p>
      <h2>Liens externes</h2>
      <p>Le site renvoie vers YouTube, TikTok et Instagram. Ces plateformes ont leurs propres conditions et leur propre politique de confidentialité.</p>
      <p class="note">Dernière mise à jour : 23 octobre 2026.</p>
    </div>
  </div>
</section>"""
    page("mentions-legales.html", "Mentions légales", "Mentions légales du site droitautableau.fr.", contenu)


def confidentialite():
    stats = ("Le site utilise Cloudflare Web Analytics pour compter les visites. Cet outil ne dépose aucun cookie, ne suit pas les visiteurs d'un site à l'autre et ne conserve pas ton adresse IP : il donne seulement des chiffres globaux (nombre de visites, pages vues, pays, type d'appareil)."
             if CLOUDFLARE_TOKEN else
             "Le site ne mesure pas l'audience et n'utilise aucun outil de statistiques.")
    contenu = f"""<section class="section">
  <div class="wrap">
    <div class="prose">
      <span class="eyebrow">Informations légales</span>
      <h1>Politique de confidentialité</h1>
      <p>En résumé : ce site ne dépose aucun cookie, n'a pas de compte utilisateur et ne te demande aucune donnée. Il n'y a donc pas de bandeau cookies.</p>
      <h2>Cookies</h2>
      <p>Aucun cookie n'est déposé. Les vidéos ne sont pas intégrées dans les pages : un clic sur une vidéo t'emmène sur YouTube ou TikTok, qui appliquent alors leurs propres règles.</p>
      <h2>Statistiques de visite</h2>
      <p>{stats}</p>
      <h2>Hébergement</h2>
      <p>Comme tout hébergeur, GitHub (GitHub Pages) enregistre des données techniques au moment de la visite (adresse IP, type de navigateur, page demandée) pour faire fonctionner et sécuriser le service. Voir la <a href="https://docs.github.com/fr/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener">déclaration de confidentialité de GitHub</a>.</p>
      <h2>Si tu m'écris</h2>
      <p>Quand tu écris à {MAIL}, ton adresse et ton message servent uniquement à te répondre. Ils ne sont ni revendus ni utilisés pour de la publicité, et sont supprimés quand ils ne sont plus utiles.</p>
      <h2>Tes droits</h2>
      <p>Selon le RGPD, tu peux demander l'accès, la rectification ou la suppression de tes données à {MAIL}. Tu peux aussi saisir la CNIL (<a href="https://www.cnil.fr" rel="noopener">cnil.fr</a>).</p>
      <p class="note">Dernière mise à jour : 23 octobre 2026.</p>
    </div>
  </div>
</section>"""
    page("confidentialite.html", "Confidentialité", "Politique de confidentialité de droitautableau.fr : aucun cookie, aucune donnée collectée.", contenu)


def introuvable():
    contenu = """<section class="section">
  <div class="wrap narrow">
    <div class="section-head">
      <span class="eyebrow">Erreur 404</span>
      <h1>Cette page n'existe pas</h1>
      <p class="lead">Le lien est peut-être ancien ou mal recopié.</p>
    </div>
    <p><a href="/">Retour à l'accueil</a> · <a href="/cours.html">Tous les cours</a></p>
  </div>
</section>"""
    page("404.html", "Page introuvable", "Cette page n'existe pas.", contenu)


def annexes():
    (SORTIE / "CNAME").write_text("droitautableau.fr\n", encoding="utf-8")
    (SORTIE / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {DOMAINE}/sitemap.xml\n", encoding="utf-8")
    urls = ["", "cours.html", "methodologie.html", "contact.html", "mentions-legales.html", "confidentialite.html"]
    plan = "".join(f"  <url><loc>{DOMAINE}/{u}</loc></url>\n" for u in urls)
    (SORTIE / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{plan}</urlset>\n',
        encoding="utf-8")


if __name__ == "__main__":
    SORTIE.mkdir(exist_ok=True)
    accueil(); cours(); methodologie(); contact(); mentions(); confidentialite(); introuvable(); annexes()
    print("Site construit dans", SORTIE)
