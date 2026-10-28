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
    "journal": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 4h13a1 1 0 0 1 1 1v3h2a1 1 0 0 1 1 1v9a3 3 0 0 1-3 3H6a3 3 0 0 1-3-3V5a1 1 0 0 1 1-1zm1 2v12a1 1 0 0 0 1 1h10.2a3 3 0 0 1-.2-1V6H5zm13 4v8a1 1 0 0 0 2 0v-8h-2zM7 8h7v2H7V8zm0 4h7v2H7v-2zm0 4h5v2H7v-2z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 5h18a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1zm1 2.4V17h16V7.4l-7.4 5.4a1 1 0 0 1-1.2 0L4 7.4zM5.7 7l6.3 4.6L18.3 7H5.7z"/></svg>',
}

# Matières : nom affiché, classe CSS du badge, couleur du bandeau des miniatures
MATIERES = {
    "constit": ("Droit constitutionnel", "#F28C6B"),
}

# publie = date et heure de mise en ligne (heure de Paris) : sert à afficher « il y a 3 heures » ou « hier »
# url = lien exact de la vidéo YouTube (en attendant : la page des vidéos de la chaîne)
COURS = [
    {
        "id": "etat",
        "matiere": "constit", "niveau": "L1",
        "titre": "L'État en droit constitutionnel : le cours complet",
        "image": "img/etat.jpg", "duree": "8:10", "date": "17 octobre 2026", "publie": "2026-10-17T12:00:00+02:00",
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
        "image": "img/formes-etat.jpg", "duree": "8:13", "date": "21 octobre 2026", "publie": "2026-10-21T12:00:00+02:00",
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
    {
        "id": "souverainete",
        "matiere": "constit", "niveau": "L1",
        "titre": "Souveraineté nationale et souveraineté populaire : le cours complet",
        "image": "img/souverainete.jpg", "duree": "8:16", "date": "25 octobre 2026", "publie": "2026-10-25T12:15:00+01:00",
        "url": "https://youtu.be/K6YmtPLtcwg",
        "resume": "À qui appartient la souveraineté ? Sieyès contre Rousseau, les conséquences de chaque théorie, et la synthèse de l'article 3 de la Constitution de 1958.",
        "notions": [
            "Le piège de départ : souveraineté de l'État ou souveraineté dans l'État",
            "La souveraineté nationale (Sieyès) : régime représentatif, électorat-fonction, mandat représentatif",
            "La souveraineté populaire (Rousseau) : démocratie directe, électorat-droit, mandat impératif, référendum",
            "Les Constitutions de 1791 et de 1793, et les limites de chaque théorie",
            "L'article 3 de la Constitution de 1958, l'article 27 et l'interdiction du mandat impératif",
            "Pour une copie excellente : CC 6 novembre 1962, décision Maastricht du 9 avril 1992, Carré de Malberg",
        ],
        "exemples": "le député de Lille, les Constitutions de 1791 et 1793",
        "chapitres": [
            ("0:00", "À qui appartient la souveraineté ?"), ("0:23", "Piège n° 1 : souveraineté de l'État ou dans l'État"),
            ("0:41", "Un peu d'histoire : Bodin, 1789"), ("1:01", "La souveraineté nationale (Sieyès)"),
            ("1:30", "Ses 4 conséquences"), ("2:24", "La souveraineté populaire (Rousseau)"),
            ("2:46", "Ses 4 conséquences"), ("3:29", "La Constitution de 1793"),
            ("3:49", "Les limites de chaque théorie"), ("4:26", "L'exemple du député de Lille"),
            ("4:43", "L'article 3 de la Constitution de 1958"), ("5:08", "Ce qui vient de chaque théorie"),
            ("6:04", "Le piège du partiel"), ("6:18", "Pour une copie excellente : 1962 et Maastricht"),
            ("6:59", "Carré de Malberg"), ("7:12", "Récap"), ("7:39", "Conseil pour le partiel"),
        ],
    },
    {
        "id": "constitution",
        "matiere": "constit", "niveau": "L1",
        "titre": "La constitution et la pyramide de Kelsen : le cours complet",
        "image": "img/constitution.jpg", "duree": "8:46", "date": "28 octobre 2026", "publie": "2026-10-28T14:00:00+01:00",
        "url": "https://youtu.be/5h3nESk6Ero",
        "resume": "Qu'est-ce qu'une constitution, comment la modifier, et pourquoi elle est au sommet de la hiérarchie des normes ? De l'article 16 de la DDHC à la pyramide de Kelsen.",
        "notions": [
            "La définition et les deux sens : constitution matérielle et constitution formelle",
            "Le piège du Royaume-Uni : constitution souple ou rigide",
            "L'article 16 de la DDHC et le bloc de constitutionnalité (CC, 16 juillet 1971)",
            "Le pouvoir constituant originaire et dérivé, l'article 89 et ses limites",
            "Kelsen et la pyramide des normes, avec l'exemple de l'arrêté du maire",
            "Le contrôle de constitutionnalité (a priori, QPC) et de conventionnalité (IVG 1975, Jacques Vabre, Nicolo)",
            "Le piège du partiel : traité ou constitution, qui est au sommet ? (art. 54, Sarran, Fraisse, Costa)",
        ],
        "exemples": "le Royaume-Uni, l'arrêté du maire",
        "chapitres": [
            ("0:00", "Une loi peut disparaître en une décision"), ("0:12", "Définition de la constitution"),
            ("0:22", "Les deux sens : matériel et formel"), ("0:51", "Piège n° 1 : le Royaume-Uni"),
            ("1:18", "Un peu d'histoire"), ("1:46", "L'article 16 de la DDHC"),
            ("2:02", "Une quinzaine de constitutions"), ("2:15", "Le bloc de constitutionnalité"),
            ("2:52", "Le pouvoir constituant"), ("3:23", "L'article 89"),
            ("4:02", "Les limites de la révision"), ("4:34", "Kelsen"),
            ("5:09", "La pyramide des normes"), ("5:46", "L'exemple de l'arrêté du maire"),
            ("6:04", "Qui contrôle ? Le Conseil constitutionnel"), ("6:40", "Et les traités ?"),
            ("6:59", "Le piège du partiel"), ("7:48", "Récap"), ("8:22", "Conseil pour le partiel"),
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
        "id": "dissertation", "url": "https://www.tiktok.com/@droitautableau/video/7700161151035821334", "titre": "La dissertation juridique", "niveau": "L1", "dispo": True,
        "resume": "La méthode complète en quatre étapes, sur un sujet de L1 : « La loi est-elle encore l'expression de la volonté générale ? »",
        "points": ["Analyser le sujet : définir chaque mot, sans oublier le petit mot « encore »", "Trouver la problématique : la tension entre 1789 et aujourd'hui", "Un plan en deux parties qui répond à la question", "L'introduction en cinq éléments, et pas de conclusion en droit (en général)"],
    },
    {
        "id": "cas-pratique", "url": "https://www.tiktok.com/@droitautableau/video/7700552377648303393", "titre": "Le cas pratique", "niveau": "L1", "dispo": True,
        "resume": "La méthode en quatre étapes, sur un cas de L1 : Léa, 16 ans, s'achète seule un scooter à 3 000 euros. Ses parents peuvent-ils faire annuler la vente ?",
        "points": ["Qualifier les faits avec les mots du droit", "Poser le problème de droit", "Énoncer la règle (la majeure) : articles 1146, 1148 et 1147 du code civil", "L'appliquer aux faits (la mineure) et conclure clairement"],
    },
    {
        "id": "introduction", "url": "https://www.tiktok.com/@droitautableau/video/7701385934968818977", "titre": "L'intro qui plaît au correcteur", "niveau": "L1", "dispo": True,
        "resume": "Les sept éléments d'une introduction de dissertation juridique, celle que le correcteur lit en premier.",
        "points": ["L'accroche, jamais « depuis la nuit des temps »", "Les définitions et la délimitation du sujet", "Le contexte et l'intérêt du sujet", "La problématique et l'annonce du plan"],
    },
]

# Annonce temporaire en haut de l'accueil et de la page des cours. Elle disparaît d'elle-même
# chez le visiteur à la date « fin » (heure de Paris). None = pas d'annonce.
ANNONCE = {
    "etiquette": "Spécial galops",
    "texte": "Cette semaine, une vidéo par jour sur YouTube pour préparer tes galops.",
    "lien": YOUTUBE,
    "fin": "2026-11-02T00:00:00+01:00",
}

# L'actu juridique de la semaine : une page par semaine (la plus récente en dernier).
# Chaque actu : matiere (clé de COULEURS_ACTU), jour (date ISO), verdict (le tampon sur la photo),
# photo (dans img/actu/, None = aplat de couleur avec le mot-clé), chapo, citation, corps (paragraphes ;
# une ligne qui commence par « ## » devient un intertitre), source.
COULEURS_ACTU = {
    "Libertés publiques": "#C7A8F4", "Droit constitutionnel": "#F28C6B", "Histoire du droit": "#F2A0C4",
    "Droit du travail": "#9EE0B8", "Institutions juridictionnelles": "#8FC7E8", "Procédure pénale": "#F5C26B",
}
ACTUS = [
    {
        "id": "2026-10-25", "numero": 1, "du": "19", "au": "25 octobre 2026", "lecture": 12,
        "chapo": "Le Conseil d'État recadre une annonce du Président, les mutuelles retrouvent le droit d'augmenter leurs tarifs, le Code noir disparaît enfin du droit français. Les six décisions de la semaine, expliquées.",
        "actus": [
            {
                "id": "manifestations", "matiere": "Libertés publiques", "jour": "2026-10-23", "verdict": "Recours rejetés",
                "mot": "Manifs", "photo": "img/actu/2026-10-25-manifestations.jpg",
                "legende": "Le 22 octobre, Emmanuel Macron annonçait l'interdiction des manifestations non syndicales.",
                "titre": "Une phrase de Macron n'interdit pas une manifestation",
                "chapo": "Sept recours contre l'annonce présidentielle ont été rejetés par le Conseil d'État. Ce n'est pas une victoire du gouvernement : pour le juge, cette annonce n'a tout simplement aucun effet juridique.",
                "citation": ("Ces propos ne révèlent pas l'existence d'une décision d'interdire toute manifestation, ni d'une instruction donnée en ce sens aux préfets.", "Conseil d'État, ordonnance du 23 octobre 2026"),
                "corps": [
                    "## Une annonce après les violences du 17 octobre",
                    "La manifestation nationale du 17 octobre a été marquée par de graves violences à Paris, suivies de nouveaux incidents le lendemain. Le 22 octobre, à l'issue d'un conseil de sécurité, Emmanuel Macron recommande qu'il n'y ait pas de manifestation « dans les jours à venir ». Il annonce surtout que les manifestations qui ne sont pas organisées par des syndicats seront interdites par les préfets, et que celles des syndicats seront examinées « conformément au droit ».",
                    "## Sept recours en urgence",
                    "L'annonce provoque une vague de recours. La Ligue des droits de l'Homme, le Syndicat des avocats de France, le Syndicat de la magistrature, plusieurs associations et sept partis politiques saisissent le juge des référés du Conseil d'État. Ils utilisent le référé-liberté, la procédure d'urgence qui permet d'obtenir en 48 heures la suspension d'une décision portant une atteinte grave et manifestement illégale à une liberté fondamentale.",
                    "## Pas de décision, donc rien à suspendre",
                    "Le juge rappelle d'abord le principe : la liberté de manifester est une liberté fondamentale, et une interdiction « ne peut être prise qu'en dernier recours ». Puis il constate que la déclaration du Président n'est ni une décision ni une instruction aux préfets. Elle n'est donc « pas susceptible d'avoir par elle-même des effets sur l'exercice de la liberté de manifester ». Les recours sont rejetés sans même d'audience, parce qu'ils étaient manifestement voués à l'échec.",
                    "## Ce que ça change pour les préfets",
                    "C'est le passage le plus important de l'ordonnance. Chaque préfet doit apprécier lui-même « la réalité et l'ampleur des risques de troubles à l'ordre public », manifestation par manifestation. Il ne peut pas justifier une interdiction « par la seule référence à la déclaration litigieuse ». Autrement dit, une interdiction générale des manifestations non syndicales serait illégale. Et chaque arrêté préfectoral d'interdiction pourra être attaqué, lui, devant le juge.",
                    "Retiens la leçon de contentieux administratif : on n'attaque pas des mots, on attaque des actes. Une déclaration politique ne fait pas grief tant qu'aucune mesure ne la traduit en droit.",
                ],
                "source": ("CE, ord. réf., 23 octobre 2026, n° 520729 et autres", "https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2026-10-23/520729"),
            },
            {
                "id": "mutuelles", "matiere": "Droit constitutionnel", "jour": "2026-10-23", "verdict": "Censuré",
                "mot": "Mutuelles", "photo": "img/actu/2026-10-25-mutuelles.jpg",
                "legende": "Les complémentaires santé retrouvent la liberté de fixer leurs tarifs.",
                "titre": "Le gel des cotisations de mutuelle est censuré",
                "chapo": "La loi interdisait toute hausse des cotisations de complémentaire santé en 2026. Saisi par les mutuelles et les assureurs, le Conseil constitutionnel juge ce gel trop brutal.",
                "citation": ("Une atteinte disproportionnée à la liberté d'entreprendre et à la liberté contractuelle.", "Conseil constitutionnel, décision du 23 octobre 2026"),
                "corps": [
                    "## Une taxe, et un gel pour l'accompagner",
                    "La loi de financement de la sécurité sociale pour 2026, votée fin 2025, crée une contribution exceptionnelle à la charge des organismes de complémentaire santé : mutuelles, assureurs, institutions de prévoyance. Pour éviter qu'ils ne fassent payer cette taxe à leurs assurés, le législateur ajoute une phrase à l'article 13 : « Pour l'année 2026, le montant de ces cotisations ne peut être augmenté par rapport à celui applicable pour l'année 2025. »",
                    "## Deux QPC venues du Conseil d'État",
                    "La Mutualité française, la Fédération française de l'assurance et une organisation patronale de l'alimentation contestent ce gel. Le Conseil d'État transmet leurs questions prioritaires de constitutionnalité en juillet. Leur argument principal : bloquer les tarifs empêche de suivre la hausse des dépenses de santé, alors même que les contrats de 2026 avaient déjà été signés.",
                    "## Un but légitime, un moyen excessif",
                    "Le Conseil raisonne en trois temps, comme toujours en matière de liberté d'entreprendre. Il y a bien une atteinte : les organismes ne peuvent plus fixer librement leurs prix. Le but est légitime : protéger les assurés est un objectif d'intérêt général. Mais le moyen va trop loin, parce que le gel s'oppose à toute augmentation « quelle qu'en soit la cause ». Même une hausse justifiée par l'augmentation structurelle du coût des soins devient impossible. D'où la censure.",
                    "## Une censure immédiate",
                    "Le Conseil aurait pu reporter les effets de sa décision pour laisser le temps au Parlement de corriger le texte. Il refuse : « aucun motif » ne le justifie. Le gel disparaît dès la publication de la décision et ne peut plus être appliqué dans les affaires en cours. Attention, seule la phrase sur le gel tombe : la contribution exceptionnelle, elle, reste due.",
                    "C'est un exemple parfait de contrôle de proportionnalité en QPC, et un rappel utile : la liberté d'entreprendre et la liberté contractuelle, toutes deux tirées de l'article 4 de la Déclaration de 1789, ne sont pas absolues, mais leurs limites doivent rester mesurées.",
                ],
                "source": ("Cons. const., déc. n° 2026-1230/1231 QPC du 23 octobre 2026", "https://www.conseil-constitutionnel.fr/decision/2026/20261230_1231QPC.htm"),
            },
            {
                "id": "code-noir", "matiere": "Histoire du droit", "jour": "2026-10-20", "verdict": "Abrogé",
                "mot": "Code noir", "photo": "img/actu/2026-10-25-code-noir.jpg", "fit": "contain",
                "legende": "Page de titre d'une édition du Code noir imprimée à Paris en 1718.",
                "titre": "Le Code noir est enfin abrogé, 341 ans après",
                "chapo": "Inapplicable depuis l'abolition de l'esclavage en 1848, le Code noir n'avait jamais été retiré du droit français. C'est chose faite avec le vote définitif du Sénat, le 20 octobre.",
                "citation": ("Le Code noir a organisé et légitimé l'esclavage. Il n'a plus sa place dans notre droit.", "Naïma Moutchou, ministre des Outre-mer"),
                "corps": [
                    "## Un texte qui faisait des êtres humains des biens",
                    "Le Code noir, c'est le nom donné à « l'édit du Roy sur les esclaves des îles de l'Amérique » de mars 1685, signé sous Louis XIV. Il encadrait l'esclavage dans les colonies françaises. Les personnes réduites en esclavage y étaient traitées comme des biens meubles, que l'on pouvait acheter, vendre ou transmettre. La fuite était punie de mutilations, du marquage au fer, voire de la mort.",
                    "## Caduc depuis 1848, mais jamais abrogé",
                    "Le décret du 27 avril 1848 abolit l'esclavage. À partir de là, le Code noir ne peut plus s'appliquer : une règle nouvelle incompatible avec l'ancienne la prive d'effet. C'est ce qu'on appelle une abrogation implicite. Mais aucun texte n'avait jamais visé expressément l'édit de 1685. Il restait donc, en théorie, dans l'ordre juridique français, sans aucun effet.",
                    "## Une loi votée à l'unanimité",
                    "La proposition de loi du député guadeloupéen Max Mathiasin a été adoptée à l'unanimité par l'Assemblée nationale en mai, puis votée dans les mêmes termes par le Sénat le 20 octobre. Elle abroge l'édit de 1685 ainsi que tous les textes pris pour son application. Elle ajoute que les textes qui ont réduit des êtres humains à l'état de biens meubles sont « indissociables du crime contre l'humanité constitué par la traite et l'esclavage », en écho à la loi Taubira du 21 mai 2001. Enfin, le Gouvernement devra remettre dans l'année un rapport sur le droit colonial encore en vigueur outre-mer et sur la place de l'esclavage dans les programmes scolaires.",
                    "## Une portée symbolique, mais pas seulement",
                    "Juridiquement, rien ne change : le texte ne s'appliquait plus. Mais l'abrogation expresse dit clairement ce que le droit pense de ce texte. Comme l'a résumé la ministre Aurore Bergé : « Reconnaître, ce n'est ni solder, ni tourner la page. » Il ne reste plus qu'à promulguer la loi.",
                    "Pour une introduction de dissertation sur l'abrogation, la hiérarchie des normes ou l'histoire du droit colonial, difficile de trouver meilleure accroche.",
                ],
                "source": ("Proposition de loi portant abrogation du « code noir », Sénat", "https://www.senat.fr/leg/ppl26-056.html"),
            },
            {
                "id": "harcelement", "matiere": "Droit du travail", "jour": "2026-10-21", "verdict": "Cassation",
                "mot": "Harcèlement", "photo": "img/actu/2026-10-25-harcelement.jpg",
                "legende": "La répétition d'un même comportement suffit à caractériser le harcèlement.",
                "titre": "Harcèlement moral : des faits identiques répétés suffisent",
                "chapo": "Une salariée avait été sollicitée 279 fois pendant ses congés et sa période de chômage partiel. La cour d'appel n'y avait pas vu de harcèlement. La Cour de cassation corrige.",
                "citation": ("L'existence d'un harcèlement n'implique pas que la répétition exigée par l'article L. 1152-1 s'attache à des agissements de nature différente.", "Cour de cassation, chambre sociale, 21 octobre 2026"),
                "corps": [
                    "## 279 messages pendant que le contrat était suspendu",
                    "Une responsable commerciale, en poste depuis 2010, est arrêtée pour maladie fin 2019, puis placée en activité partielle et en congés au printemps 2020. Entre octobre 2019 et mai 2020, elle relève 279 sollicitations de son employeur pendant ses congés et ses périodes d'activité partielle, c'est-à-dire à des moments où elle n'avait pas à travailler. En janvier 2021, pendant un nouvel arrêt, on lui propose même un séminaire commercial. Elle est finalement déclarée inapte, puis licenciée en octobre 2021.",
                    "## Pour la cour d'appel, un seul fait ne suffit pas",
                    "La salariée demande la reconnaissance d'un harcèlement moral et la nullité de son licenciement. La cour d'appel de Chambéry rejette sa demande : elle ne retient qu'un seul fait établi, les sollicitations, et estime que cela ne forme pas un ensemble d'éléments permettant de présumer un harcèlement. Implicitement, elle exige plusieurs types d'agissements.",
                    "## La répétition, pas la diversité",
                    "La Cour de cassation casse cet arrêt. L'article L. 1152-1 du code du travail définit le harcèlement moral comme des « agissements répétés » qui dégradent les conditions de travail. Rien n'impose que ces agissements soient de nature différente : le même comportement, répété des centaines de fois, peut suffire. La Cour reproche aussi aux juges d'appel de ne pas avoir examiné les certificats médicaux de la salariée, qui faisaient état de troubles anxiodépressifs.",
                    "## Comment se prouve un harcèlement",
                    "L'arrêt rappelle au passage le mécanisme de preuve de l'article L. 1154-1. Le salarié présente des éléments de fait qui, pris dans leur ensemble et avec les documents médicaux, laissent supposer un harcèlement. C'est ensuite à l'employeur de prouver que ses agissements sont étrangers à tout harcèlement. L'affaire est renvoyée devant la cour d'appel de Grenoble.",
                    "L'arrêt est publié au Bulletin, ce qui signale une solution de principe. À l'heure des messages professionnels envoyés à toute heure, il risque d'être souvent cité.",
                ],
                "source": ("Cass. soc., 21 octobre 2026, n° 25-10.793, publié au Bulletin", "https://www.courdecassation.fr/decision/6ad888927a1020213707fbe3"),
            },
            {
                "id": "ia", "matiere": "Institutions juridictionnelles", "jour": "2026-10-22", "verdict": "Charte adoptée",
                "mot": "IA", "photo": "img/actu/2026-10-25-ia.jpg",
                "legende": "La Cour de cassation, quai de l'Horloge, à Paris.",
                "titre": "Aucun jugement ne sera rendu par une IA",
                "chapo": "La plus haute juridiction judiciaire se dote d'une charte éthique sur l'intelligence artificielle. Le principe de départ est clair : l'IA peut aider le juge, jamais juger à sa place.",
                "citation": ("Aucune décision de justice ne peut être produite de manière automatisée, même sous contrôle du magistrat.", "Charte éthique de l'IA de la Cour de cassation"),
                "corps": [
                    "## Pourquoi une charte",
                    "La Cour de cassation utilise déjà l'intelligence artificielle, par exemple pour orienter les pourvois ou anonymiser les décisions. Un rapport de 2025 lui recommandait de se fixer un cadre éthique. La charte adoptée le 22 octobre va au-delà des règles imposées par la loi, « au nom de l'office propre du juge de cassation ». Elle nomme clairement les risques : l'appauvrissement du raisonnement juridique, la perte de diversité intellectuelle et la « fixité du droit ».",
                    "## Le juge reste aux commandes",
                    "Premier principe : la prééminence humaine. Aucune décision ne peut être produite automatiquement, même si un magistrat la relit ensuite. Dans le travail juridictionnel, l'IA est « cantonnée à des tâches d'appui » : chercher, trier, résumer. Aucun outil d'IA générative ne peut être imposé à un magistrat.",
                    "## Vérifier, et assumer",
                    "La charte demande de se méfier des biais, notamment le biais d'ancrage (se laisser influencer par la première réponse) et le biais de confirmation. Elle exige de vérifier tout ce que produit l'IA, en particulier « les références juridiques, dans leur existence, leur hiérarchie et leur portée ». Et elle pose une règle simple : « L'auteur d'un travail en répond seul, quel que soit l'outil utilisé. » Un nouvel arrivant doit d'ailleurs savoir faire son travail sans IA avant d'apprendre à s'en servir.",
                    "## Le secret du délibéré protégé",
                    "Aucun document contenant des données personnelles ou couvert par le secret du délibéré ne peut être envoyé à un outil externe. La Cour privilégie ses propres outils, qui doivent être « sécurisés, robustes, audités et documentés ». La charte sera revue au moins tous les deux ans.",
                    "Pourquoi la « fixité du droit » inquiète-t-elle ? Parce que la jurisprudence évolue quand des juges raisonnent à nouveau sur des situations nouvelles. Une machine nourrie des décisions passées tend à les reproduire. C'est un excellent sujet d'oral, et un conseil valable pour toi aussi : vérifie chaque article et chaque arrêt qu'une IA te propose.",
                ],
                "source": ("Cour de cassation, « IA : la Cour se dote d'une charte éthique », 22 octobre 2026", "https://www.courdecassation.fr/toutes-les-actualites/2026/10/22/ia-la-cour-se-dote-dune-charte-ethique"),
            },
            {
                "id": "rue-des-rosiers", "matiere": "Procédure pénale", "jour": "2026-10-21", "verdict": "Pourvoi rejeté",
                "mot": "Rue des Rosiers", "photo": "img/actu/2026-10-25-rue-des-rosiers.jpg",
                "legende": "La rue des Rosiers, dans le 4e arrondissement de Paris.",
                "titre": "Rue des Rosiers : le procès aura lieu",
                "chapo": "Plus de quarante ans après l'attentat, un des accusés contestait son renvoi devant la cour d'assises. La Cour de cassation juge son appel irrecevable : il était en fuite.",
                "citation": None,
                "corps": [
                    "## L'attentat du 9 août 1982",
                    "Ce jour-là, en plein Paris, un commando lance un engin explosif dans le restaurant Jo Goldenberg, rue des Rosiers, puis ouvre le feu à l'arme automatique sur les clients et les passants. Six personnes sont tuées, vingt blessées. L'enquête attribue l'attentat au Fatah-Conseil révolutionnaire, le groupe d'Abou Nidal.",
                    "## Un accusé remis à la France en 2026",
                    "Après plus de quarante ans d'instruction, le juge renvoie six personnes devant la cour d'assises de Paris spécialement composée, compétente en matière de terrorisme, le 31 juillet 2025. L'un des accusés, visé par un mandat d'arrêt depuis 2015, est remis à la France par les autorités palestiniennes le 16 avril 2026. Il fait aussitôt appel de l'ordonnance qui le renvoie aux assises. La chambre de l'instruction déclare cet appel irrecevable.",
                    "## Qu'est-ce qu'être « en fuite » ?",
                    "Pour l'accusé, vivre à l'étranger ne suffit pas à être en fuite : il faudrait des actes positifs pour se cacher, et la preuve qu'il savait être recherché. La Cour de cassation n'est pas d'accord. Il a vécu en Palestine pendant toute l'instruction, ne pouvait ignorer les poursuites vu la médiatisation de l'attentat et ses propres déclarations, et ne s'est jamais présenté à la justice française. Il a donc « entendu se soustraire aux poursuites ».",
                    "## Arrêté, mais toujours pas partie à l'instruction",
                    "L'accusé soutenait aussi qu'une fois arrêté et informé de l'ordonnance, il n'était plus en fuite et pouvait faire appel. La Cour répond que ni l'arrestation, ni la détention, ni la notification de l'ordonnance ne lui donnent la qualité de partie à l'information, qui ouvre le droit d'appel. Il n'est pas privé d'un procès équitable pour autant : il pouvait demander l'annulation de son extradition, et il exercera tous les droits de la défense devant la cour d'assises.",
                    "L'arrêt est publié au Bulletin. Il précise la notion de fuite, et rappelle qu'on ne peut pas se soustraire à la justice pendant des années puis contester la procédure menée sans soi. Le procès peut maintenant se tenir.",
                ],
                "source": ("Cass. crim., 21 octobre 2026, n° 26-85.257, publié au Bulletin", "https://www.courdecassation.fr/decision/6adb185d7a102021375ed345"),
            },
        ],
    },
]

PAGES_NAV = [("./", "Accueil"), ("cours.html", "Les cours"), ("methodologie.html", "Méthodologie"), ("actu.html", "L'actu"), ("contact.html", "Contact")]


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


def duree(c):
    return f'<span class="duration" aria-label="Durée {c["duree"]}">{c["duree"]}</span>'


def date_pub(c):
    return f'<time class="pub" datetime="{c["publie"]}">{c["date"]}</time>'


# Remplace la date par « il y a 3 heures » ou « hier », calculé chez le visiteur (rien à mettre à jour à la main)
SCRIPT_DATES = """<script>
(function () {
  var maintenant = new Date();
  function jour(d) { return new Date(d.getFullYear(), d.getMonth(), d.getDate()).getTime(); }
  document.querySelectorAll("time.pub").forEach(function (t) {
    var d = new Date(t.getAttribute("datetime"));
    if (isNaN(d) || d > maintenant) return;
    var ecart = Math.round((jour(maintenant) - jour(d)) / 86400000);
    if (ecart === 0) {
      var min = Math.floor((maintenant - d) / 60000), h = Math.floor(min / 60);
      t.textContent = h >= 1 ? "il y a " + h + (h > 1 ? " heures" : " heure") : min >= 1 ? "il y a " + min + " min" : "à l'instant";
    } else if (ecart === 1) {
      t.textContent = "hier";
    }
  });
})();
</script>"""


def annonce():
    if not ANNONCE:
        return ""
    a = ANNONCE
    return f"""<a class="annonce" href="{a['lien']}" target="_blank" rel="noopener" data-fin="{a['fin']}">
  <span class="annonce-tag">{escape(a['etiquette'])}</span>
  <span class="annonce-texte">{escape(a['texte'])}</span>
</a>
<script>
(function () {{
  var a = document.currentScript.previousElementSibling;
  if (new Date() >= new Date(a.dataset.fin)) a.remove();
}})();
</script>"""


def carte(c, nouveau=False):
    pastille = '<span class="new-tag">Nouveau</span>' if nouveau else ""
    return f"""<article class="card">
  <a class="thumb" href="{c['url']}" target="_blank" rel="noopener"><img src="{c['image']}" alt="{escape(c['titre'])}" width="640" height="360" loading="lazy">{duree(c)}</a>
  <div class="meta">{badges(c)}{pastille}</div>
  <div class="when">{date_pub(c)}</div>
</article>"""


def liens_reseaux():
    return f"""<div class="links">
  <a class="link-btn primary" href="{YOUTUBE}" target="_blank" rel="noopener">{ICONES['youtube']}S'abonner sur YouTube</a>
  <a class="link-btn" href="{TIKTOK}" target="_blank" rel="noopener">{ICONES['tiktok']}Suivre sur TikTok</a>
  <a class="link-btn" href="{INSTAGRAM}" target="_blank" rel="noopener">{ICONES['instagram']}Suivre sur Instagram</a>
  <a class="link-btn" href="cours.html">{ICONES['livre']}Tous les cours</a>
  <a class="link-btn" href="methodologie.html">{ICONES['stylo']}Méthodologie</a>
  <a class="link-btn" href="actu-{ACTUS[-1]['id']}.html">{ICONES['journal']}L'actu juridique de la semaine</a>
  <a class="link-btn" href="contact.html">{ICONES['mail']}Contact</a>
</div>"""


def accueil():
    cartes = "\n".join(carte(c, nouveau=(i == 0)) for i, c in enumerate(reversed(COURS)))
    contenu = f"""<section class="hero">
  <div class="wrap">
    <img class="avatar" src="img/logo.png" alt="Logo Droit au Tableau : une balance de la justice" width="160" height="160">
    <h1>Droit au Tableau</h1>
    <p class="lead">Tes cours de droit, expliqués au tableau. De la L1 au master.</p>
    {annonce()}
    {liens_reseaux()}
  </div>
</section>
<section class="section">
  <div class="wrap home-courses">
    <div class="section-head carousel-head">
      <h2>Derniers cours <span class="count">{len(COURS)} vidéos</span></h2>
      <div class="carousel-nav" hidden>
        <button type="button" data-dir="-1" aria-label="Vidéo précédente">‹</button>
        <button type="button" data-dir="1" aria-label="Vidéo suivante">›</button>
      </div>
    </div>
    <div class="carousel-frame">
      <div class="carousel" tabindex="0" aria-label="Derniers cours, du plus récent au plus ancien">{cartes}</div>
    </div>
    <div class="carousel-dots" hidden></div>
    <p class="more"><a class="more-btn" href="cours.html">{ICONES['livre']}Voir tous les cours<span class="arrow" aria-hidden="true">→</span></a></p>
  </div>
</section>
<script>
(function () {{
  var piste = document.querySelector(".carousel"), cadre = document.querySelector(".carousel-frame"),
      nav = document.querySelector(".carousel-nav"), points = document.querySelector(".carousel-dots");
  if (!piste || !nav) return;
  var cartes = Array.prototype.slice.call(piste.querySelectorAll(".card"));
  function pas() {{ return cartes.length > 1 ? cartes[1].offsetLeft - cartes[0].offsetLeft : piste.clientWidth; }}
  nav.hidden = false;
  nav.querySelectorAll("button").forEach(function (b) {{
    b.addEventListener("click", function () {{ piste.scrollBy({{ left: pas() * Number(b.dataset.dir), behavior: "smooth" }}); }});
  }});
  cartes.forEach(function (c, i) {{
    var d = document.createElement("button");
    d.type = "button";
    d.setAttribute("aria-label", "Vidéo " + (i + 1) + " sur " + cartes.length);
    d.addEventListener("click", function () {{ piste.scrollTo({{ left: c.offsetLeft - cartes[0].offsetLeft, behavior: "smooth" }}); }});
    points.appendChild(d);
  }});
  points.hidden = false;
  function maj() {{
    var max = piste.scrollWidth - piste.clientWidth - 2;
    var debut = piste.scrollLeft <= 2, fin = piste.scrollLeft >= max;
    nav.children[0].disabled = debut;
    nav.children[1].disabled = fin;
    cadre.classList.toggle("has-prev", !debut);
    cadre.classList.toggle("has-next", !fin);
    var actif = fin ? cartes.length - 1 : Math.round(piste.scrollLeft / pas());
    Array.prototype.forEach.call(points.children, function (d, i) {{ d.setAttribute("aria-current", i === actif ? "true" : "false"); }});
  }}
  piste.addEventListener("scroll", maj, {{ passive: true }});
  window.addEventListener("resize", maj);
  maj();
}})();
</script>""" + SCRIPT_DATES
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
  <a class="course-thumb" href="{c['url']}" target="_blank" rel="noopener"><img src="{c['image']}" alt="Miniature : {escape(c['titre'])}" width="640" height="360" loading="lazy">{duree(c)}</a>
  <div class="course-body">
    <div class="meta">{badges(c)}{date_pub(c)}</div>
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
      {annonce()}
    </div>
    {''.join(blocs)}
  </div>
</section>""" + SCRIPT_DATES
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
      <p class="lead">Chaque méthode en deux minutes, sur un vrai exemple.</p>
    </div>
    {''.join(items)}
  </div>
</section>"""
    page("methodologie.html", "Méthodologie", "Les méthodes de la fiche d'arrêt, du commentaire d'arrêt, de la dissertation et de son introduction, du cas pratique et de l'utilisation du code civil en examen, montrées sur de vrais exemples.", contenu, "Méthodologie")


def insec(t):
    """Échappe le texte et met des espaces insécables là où le français l'exige (avant : ; ? ! et dans « »)."""
    t = escape(t)
    for a, b in ((" :", "\u00a0:"), (" ;", "\u202f;"), (" ?", "\u202f?"), (" !", "\u202f!"), ("« ", "«\u00a0"), (" »", "\u00a0»"), ("n° ", "n°\u00a0")):
        t = t.replace(a, b)
    return t


MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]


def date_fr(iso):
    a, m, j = (int(x) for x in iso.split("-"))
    return f"{j} {MOIS[m - 1]}"


def visuel(a, classe):
    """La photo de l'actu, ou à défaut un aplat de la couleur de la matière avec le mot-clé."""
    tampon = f'<span class="stamp">{insec(a["verdict"])}</span>'
    if a["photo"]:
        contenir = f' contain" style="--c:{COULEURS_ACTU[a["matiere"]]}' if a.get("fit") == "contain" else ""
        return f'<div class="{classe}{contenir}"><img src="{a["photo"]}" alt="{insec(a["legende"])}" loading="lazy">{tampon}</div>'
    return f'<div class="{classe} plain" style="--c:{COULEURS_ACTU[a["matiere"]]}"><span class="word">{insec(a["mot"])}</span>{tampon}</div>'


def actu_semaine(s):
    titre = f"L'actu juridique du {s['du']} au {s['au']}"
    tuiles = "".join(f"""<a class="tile" href="#{a['id']}">{visuel(a, 'tile-img')}<span class="tile-t">{insec(a['titre'])}</span></a>""" for a in s["actus"])
    blocs = []
    for i, a in enumerate(s["actus"], 1):
        citation = ""
        if a["citation"]:
            citation = f'<blockquote><p>«\u00a0{insec(a["citation"][0])}\u00a0»</p><cite>{insec(a["citation"][1])}</cite></blockquote>'
        corps = []
        for k, para in enumerate(a["corps"]):
            if k == 2 and citation:
                corps.append(citation)
            corps.append(f"<h3>{insec(para[3:])}</h3>" if para.startswith("## ") else f"<p>{insec(para)}</p>")
        legende = f'<figcaption>{insec(a["legende"])}</figcaption>' if a["photo"] and a["legende"] else ""
        blocs.append(f"""<article class="news" id="{a['id']}">
  <figure>{visuel(a, 'news-img')}{legende}</figure>
  <div class="meta"><span class="news-num">{i}</span><span class="badge matiere" style="background:{COULEURS_ACTU[a['matiere']]}">{insec(a['matiere'])}</span><span>{date_fr(a['jour'])}</span></div>
  <h2>{insec(a['titre'])}</h2>
  <p class="chapo">{insec(a['chapo'])}</p>
  <div class="body">{''.join(corps)}</div>
  <p class="src">Source : <a href="{a['source'][1]}" target="_blank" rel="noopener">{insec(a['source'][0])}</a> <button type="button" class="cite-copy" data-copy="{insec(a['source'][0])}">Copier la référence</button></p>
</article>""")
    contenu = f"""<div class="read-progress" aria-hidden="true"><span></span></div>
<section class="section actu-page">
  <div class="wrap narrow">
    <header class="actu-head">
      <span class="eyebrow">L'actu juridique de la semaine · n° {s['numero']}</span>
      <h1>Du {s['du']} au {s['au']}</h1>
      <p class="lead">{insec(s['chapo'])}</p>
      <p class="note">{len(s['actus'])} actus · {s['lecture']} min de lecture</p>
    </header>
    <nav class="tiles" aria-label="Les actus de la semaine">{tuiles}</nav>
    {''.join(blocs)}
    <div class="actu-end">
      <p>Une nouvelle sélection chaque dimanche soir, en carrousel sur <a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a> et <a href="{TIKTOK}" target="_blank" rel="noopener">TikTok</a>.</p>
      <p><button type="button" class="share">Partager cette page</button> <a href="actu.html">Toutes les semaines</a></p>
    </div>
  </div>
</section>
<script>
(function () {{
  var barre = document.querySelector(".read-progress span");
  function lire() {{ var h = document.documentElement; barre.style.width = (100 * h.scrollTop / Math.max(1, h.scrollHeight - h.clientHeight)) + "%"; }}
  addEventListener("scroll", lire, {{ passive: true }}); lire();
  document.querySelectorAll(".cite-copy").forEach(function (b) {{
    b.addEventListener("click", function () {{
      navigator.clipboard.writeText(b.dataset.copy).then(function () {{ b.textContent = "Copiée"; setTimeout(function () {{ b.textContent = "Copier la référence"; }}, 1600); }});
    }});
  }});
  var partage = document.querySelector(".share");
  partage.addEventListener("click", function () {{
    if (navigator.share) navigator.share({{ title: document.title, url: location.href }}).catch(function () {{}});
    else navigator.clipboard.writeText(location.href).then(function () {{ partage.textContent = "Lien copié"; }});
  }});
}})();
</script>"""
    resume = "; ".join(a["titre"] for a in s["actus"])
    page(f"actu-{s['id']}.html", titre, f"{titre} : {resume}.", contenu, "L'actu")


def actu():
    items = "".join(f"""<li><a href="actu-{s['id']}.html">Du {s['du']} au {s['au']}</a>
  <span class="note">{insec(' · '.join(a['titre'] for a in s['actus'][:3]))}…</span></li>""" for s in reversed(ACTUS))
    contenu = f"""<section class="section">
  <div class="wrap narrow">
    <div class="section-head">
      <h1>L'actu juridique de la semaine</h1>
      <p class="lead">Chaque dimanche, les décisions et les lois de la semaine qui comptent pour tes copies et tes oraux.</p>
    </div>
    <ol class="weeks">{items}</ol>
  </div>
</section>"""
    page("actu.html", "L'actu juridique de la semaine", "Chaque dimanche, l'actualité juridique de la semaine expliquée aux étudiants en droit, avec les références à citer en copie.", contenu, "L'actu")
    for s in ACTUS:
        actu_semaine(s)


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
    urls = ["", "cours.html", "methodologie.html", "actu.html"] + [f"actu-{s['id']}.html" for s in ACTUS] + ["contact.html", "mentions-legales.html", "confidentialite.html"]
    plan = "".join(f"  <url><loc>{DOMAINE}/{u}</loc></url>\n" for u in urls)
    (SORTIE / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{plan}</urlset>\n',
        encoding="utf-8")


if __name__ == "__main__":
    SORTIE.mkdir(exist_ok=True)
    accueil(); cours(); methodologie(); actu(); contact(); mentions(); confidentialite(); introuvable(); annexes()
    print("Site construit dans", SORTIE)
