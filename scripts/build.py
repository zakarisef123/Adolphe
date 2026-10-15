#!/usr/bin/env python3
"""Génère les pages métiers (élagage, espaces verts)
et injecte l'en-tête / le pied de page communs dans index.html.

Usage : python3 scripts/build.py   (depuis la racine du dépôt)
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMG = "https://adolphe-elagage.fr/wp-content/uploads/2026/03/"
TEL = "07 59 78 18 06"
TEL_HREF = "tel:+33759781806"
WA = "https://wa.me/33759781806?text=Bonjour%2C%20je%20souhaite%20un%20devis%20gratuit."
SITE = "https://adolphe-elagage.fr/"

P = {  # photos disponibles sur le site
    "elagage": "upload-elagage-arbre9-standard.webp",
    "intervention": "upload-file_0000000043a4720c84b86cc79fb821f6-high-shaxqh.webp",
    "abattage": "upload-screenshot_20260105_143100_maps-standard-x3u90i.webp",
    "apres_abattage": "upload-whatsapp-image-2025-11-16-at-17-55-57-2-standard.webp",
    "diagnostic": "upload-whatsapp-image-2025-11-16-at-17-55-57-1-standard.webp",
    "haie": "upload-20260112_102818-high-v8261e.webp",
    "haie_finie": "upload-20260112_111946-standard.webp",
    "jardin": "upload-whatsapp-image-2025-11-13-at-14-33-44-2-standard-nrb06h.webp",
    "jardin_chantier": "upload-whatsapp-image-2025-11-13-at-14-33-44-1-standard-m2r13n.webp",
    "exterieur": "upload-jardinier-paysagiste-a-cosnes-et-romain01-standard-ykts2k.webp",
    "debroussaillage": "upload-screenshot_20260112_213015_google-standard-wiutoq.webp",
    "pelouse": "upload-20260306_171259-standard.webp",
    "lierre": "upload-20260112_110128-standard.webp",
    "chantier1": "upload-20260214_123913-high-0pxaeo.webp",
    "chantier2": "upload-20260305_150656-high-rhqik4.webp",
    # Photos de chantier ajoutées au site (dossier assets/photos)
    "haie_thuyas": "assets/photos/taille-haie-thuyas.jpg",
    "platanes_avant": "assets/photos/platanes-avant.jpg",
    "platanes_apres": "assets/photos/platanes-apres.jpg",
    "jardin_avant": "assets/photos/jardin-tonte-avant.jpg",
    "jardin_apres": "assets/photos/jardin-tonte-apres.jpg",
    "massif_avant": "assets/photos/massif-avant.jpg",
    "massif_apres": "assets/photos/massif-apres.jpg",
    "peupliers_avant": "assets/photos/elagage-peupliers-avant.jpg",
    "peupliers_apres": "assets/photos/elagage-peupliers-apres.jpg",
}


def img(key):
    return P[key] if P[key].startswith("assets/") else IMG + P[key]


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def ic(name):
    return f'<svg><use href="#i-{name}"/></svg>'


# --------------------------------------------------------------------------
# Contenu des pages métiers
# --------------------------------------------------------------------------
TRADES = [
    {
        "slug": "elagage",
        "file": "elagage.html",
        "trade": "Élagueur",
        "menu": "Élagage & abattage",
        "icon": "tree",
        "roof": False,
        "card_img": "elagage",
        "short": "Élagage, abattage et mise en sécurité de vos arbres.",
        "title": "Élagage & abattage d'arbres dans le Val-d'Oise (95) | Adolphe",
        "desc": "Élagueur dans le Val-d'Oise (95) : élagage, taille douce, réduction de couronne, abattage par démontage, urgence après tempête. Devis gratuit au 07 59 78 18 06.",
        "h1": "Élagage & abattage <em>dans le Val-d'Oise</em>",
        "lead": "Un arbre trop proche de la maison, qui fait de l'ombre, frotte la toiture ou devient dangereux ? Nous l'élaguons ou l'abattons proprement, en toute sécurité, partout dans le 95.",
        "hero": ("img", "elagage"),
        "default": "Élagage d'arbres",
        "intro": [
            "L'élagage est un vrai métier : <strong>une coupe mal placée affaiblit un arbre pour des années</strong>, alors qu'une taille raisonnée l'allège, l'équilibre et prolonge sa vie. Avec deux générations de savoir-faire, nous regardons d'abord l'arbre, son environnement et votre besoin réel avant de sortir la tronçonneuse.",
            "Toiture, clôture, voisins, véhicules, lignes électriques, accès étroits : les jardins du Val-d'Oise sont rarement simples. Nous organisons chaque chantier pour travailler en sécurité, protéger les abords et repartir en laissant un terrain propre.",
        ],
        "services": [
            {
                "id": "elagage-arbres",
                "name": "Élagage d'arbres",
                "kicker": "Taille raisonnée",
                "media": ("duo", "elagage", "platanes_apres"),
                "paras": [
                    "L'élagage est la bonne solution quand un arbre est <strong>sain mais trop envahissant</strong> : il cache la lumière, s'approche de la toiture, déborde chez le voisin ou au-dessus d'un passage. Nous adaptons la coupe à l'essence et à la configuration pour alléger sans dénaturer.",
                    "Selon les cas, nous réalisons une taille douce d'entretien, une réduction de couronne, un éclaircissage pour laisser passer la lumière et le vent, ou la suppression du bois mort qui risque de tomber. Le travail se fait en grimpe ou depuis le sol selon la hauteur et l'accès.",
                ],
                "incl": ["Taille douce & d'entretien", "Réduction de couronne", "Suppression du bois mort", "Dégagement toiture & façade", "Éclaircissage", "Broyage & évacuation des branches"],
                "tip": "Un arbre régulièrement entretenu coûte moins cher sur la durée qu'un arbre repris tous les 10 ans : les coupes sont plus petites et cicatrisent mieux.",
                "service": "Élagage d'arbres",
            },
            {
                "id": "abattage",
                "name": "Abattage d'arbres",
                "kicker": "En toute sécurité",
                "media": ("duo", "abattage", "apres_abattage"),
                "paras": [
                    "L'abattage devient nécessaire quand un arbre est <strong>malade, mort, instable ou trop proche d'une construction</strong>, ou quand son maintien n'est plus souhaité. C'est une intervention qui ne s'improvise pas, surtout en milieu urbain.",
                    "Quand la place manque pour un abattage direct, nous procédons par <strong>démontage</strong> : l'arbre est découpé par tronçons depuis le haut, et chaque morceau est descendu de façon contrôlée. Nous tenons compte des clôtures, toitures, voisins et véhicules, puis nous évacuons ou débitons le bois selon votre choix.",
                ],
                "incl": ["Diagnostic avant intervention", "Abattage direct ou par démontage", "Accès étroits & jardins de ville", "Protection des abords", "Débitage du bois sur demande", "Évacuation & nettoyage"],
                "tip": "Selon la commune ou le PLU, un abattage peut nécessiter une autorisation. Nous vous indiquons les points à vérifier avant d'intervenir.",
                "service": "Abattage d'arbres",
            },
            {
                "id": "urgence",
                "name": "Urgence après tempête",
                "kicker": "Intervention rapide",
                "media": ("duo", "diagnostic", "chantier1"),
                "paras": [
                    "Après un coup de vent, une branche cassée peut rester suspendue au-dessus d'un toit, d'une voiture ou d'un passage. Un arbre peut aussi pencher dangereusement ou tomber sur une clôture. Dans ces cas-là, <strong>il faut agir vite et sans prendre de risque</strong>.",
                    "Nous faisons le maximum pour intervenir rapidement dans le Val-d'Oise : mise en sécurité, dégagement des branches, découpe et évacuation de l'arbre tombé.",
                ],
                "incl": ["Mise en sécurité", "Branches cassées ou suspendues", "Arbre tombé ou penché", "Dégagement des accès", "Évacuation des déchets verts", "Photos pour votre assurance"],
                "tip": "Ne montez jamais sur un toit ou dans un arbre fragilisé après une tempête. Prenez des photos pour votre assurance et appelez-nous.",
                "service": "Urgence / mise en sécurité",
                "urgent": True,
            },
        ],
        "signs": [
            "Des branches touchent ou surplombent la toiture",
            "Les gouttières se remplissent de feuilles chaque automne",
            "L'arbre fait trop d'ombre à la maison ou au jardin",
            "Du bois mort ou des branches cassées sont visibles",
            "L'arbre penche, son tronc est creux ou fendu",
            "Les branches débordent chez le voisin ou sur la voie publique",
        ],
        "gallery": [("platanes_apres", "Taille en têtes de chat de platanes"), ("elagage", "Élagage d'arbre en hauteur"), ("intervention", "Intervention d'élagage"), ("abattage", "Abattage sécurisé près d'une habitation"), ("diagnostic", "Diagnostic avant intervention"), ("apres_abattage", "Après abattage et nettoyage du chantier"), ("chantier1", "Chantier dans le Val-d'Oise"), ("chantier2", "Intervention dans le 95")],
        "faq": [
            ("Combien coûte un élagage dans le Val-d'Oise ?", "Le prix dépend de la hauteur de l'arbre, de son accessibilité, du volume à couper et des contraintes autour (toiture, voisins, lignes). C'est pourquoi nous nous déplaçons gratuitement pour établir un devis précis et sans engagement."),
            ("Quelle est la meilleure période pour élaguer ?", "Pour beaucoup d'essences, la période de repos végétatif (de novembre à mars, hors gel) est favorable. Certaines tailles légères se font aussi en été. Nous vous conseillons selon l'arbre et l'objectif."),
            ("Faut-il une autorisation pour abattre un arbre ?", "Cela dépend de la commune, du PLU, de l'emplacement de l'arbre et d'éventuelles protections. Nous vous indiquons les démarches à vérifier avant l'intervention."),
            ("Quelle différence entre élagage et abattage ?", "L'élagage consiste à tailler l'arbre pour l'entretenir, l'alléger ou le dégager. L'abattage est la coupe complète de l'arbre, lorsque son maintien n'est plus possible ou plus souhaité."),
            ("Que faites-vous des branches et du bois ?", "Les branches sont broyées ou évacuées, et le chantier est nettoyé. Le bois peut être débité en bûches et laissé sur place si vous le souhaitez."),
        ],
    },
    {
        "slug": "espaces-verts",
        "file": "espaces-verts.html",
        "trade": "Paysagiste",
        "menu": "Jardin & espaces verts",
        "icon": "broom",
        "roof": False,
        "card_img": "haie_thuyas",
        "short": "Haies, entretien de jardin, débroussaillage, pelouse, lierre.",
        "title": "Entretien de jardin, taille de haies & débroussaillage (95) | Adolphe",
        "desc": "Paysagiste dans le Val-d'Oise (95) : taille de haies, entretien de jardin, débroussaillage, pose de pelouse synthétique, enlèvement de lierre. Devis gratuit au 07 59 78 18 06.",
        "h1": "Jardin & espaces verts <em>toujours nets</em>",
        "lead": "Haies, pelouse, massifs, terrain envahi ou façade couverte de lierre : nous remettons votre extérieur en état et l'entretenons toute l'année dans le Val-d'Oise.",
        "hero": ("img", "jardin"),
        "default": "Entretien de jardins",
        "intro": [
            "Un jardin agréable, c'est avant tout un jardin <strong>suivi régulièrement</strong>. Quand on laisse filer, la haie ferme la vue, les ronces gagnent du terrain et le lierre s'accroche partout : le rattrapage devient long et coûteux.",
            "Nous intervenons ponctuellement pour une remise en propre, ou de façon régulière pour que vous n'ayez plus à y penser. Particuliers, copropriétés ou professionnels : même exigence de finition et de chantier propre.",
        ],
        "services": [
            {
                "id": "taille-de-haies",
                "name": "Taille de haies",
                "kicker": "Lignes nettes",
                "media": ("duo", "haie_thuyas", "haie_finie"),
                "paras": [
                    "Une haie bien taillée change tout dans un jardin : elle protège des regards sans étouffer l'espace. Nous réalisons des <strong>tailles d'entretien régulières</strong> comme des <strong>remises en forme</strong> plus importantes sur des haies laissées à l'abandon.",
                    "Faces, dessus, hauteur : nous travaillons au cordeau pour une silhouette homogène, en réglant au passage les problèmes de passage, de lumière ou de voisinage. Thuyas, lauriers, troènes, photinias, charmilles… chaque essence a sa bonne période et sa bonne technique.",
                ],
                "incl": ["Taille des faces & du dessus", "Remise en forme / réduction", "Haies hautes & longues", "Toutes essences", "Ramassage des déchets", "Évacuation des végétaux"],
                "tip": "Évitez les grosses tailles pendant la période de nidification des oiseaux (printemps - début d'été). Deux tailles légères par an valent mieux qu'une taille sévère.",
                "service": "Taille de haies",
            },
            {
                "id": "entretien-de-jardin",
                "name": "Entretien de jardin",
                "kicker": "Toute l'année",
                "media": ("duo", "jardin_apres", "jardin"),
                "paras": [
                    "Un jardin demande de la régularité. Nous proposons des <strong>remises en propre ponctuelles</strong> (avant une vente, un événement, au retour de vacances) ou un <strong>entretien suivi</strong> à la fréquence qui vous convient.",
                    "Tonte, désherbage des allées et massifs, taille des arbustes, ramassage des feuilles, nettoyage des terrasses : nous gardons votre extérieur présentable en toute saison, ce qui valorise la maison et évite les gros travaux de rattrapage.",
                ],
                "incl": ["Tonte & bordures", "Désherbage allées & massifs", "Taille d'arbustes", "Ramassage des feuilles", "Entretien ponctuel ou régulier", "Évacuation des déchets verts"],
                "tip": "Un passage régulier, même court, coûte bien moins cher qu'une grosse remise en état une fois par an.",
                "service": "Entretien de jardins",
            },
            {
                "id": "debroussaillage",
                "name": "Débroussaillage",
                "kicker": "Terrain dégagé",
                "media": ("duo", "debroussaillage", "massif_apres"),
                "paras": [
                    "Herbes hautes, ronces, repousses d'arbustes, accès masqués : nous remettons vos terrains en état pour retrouver des <strong>zones claires, accessibles et faciles à entretenir</strong>.",
                    "Le débroussaillage est très utile avant une vente ou une location, après une longue absence, avant des travaux ou simplement pour sécuriser un terrain. Nous adaptons le matériel (débroussailleuse, broyeur) à la densité de la végétation et évacuons tout.",
                ],
                "incl": ["Ronces & herbes hautes", "Jeunes repousses & arbustes", "Terrains en pente ou en friche", "Dégagement des accès", "Broyage ou évacuation", "Avant vente ou travaux"],
                "tip": "Un terrain débroussaillé puis entretenu une à deux fois par an reste propre sans effort.",
                "service": "Débroussaillage",
            },
            {
                "id": "pelouse-synthetique",
                "name": "Pose de pelouse synthétique",
                "kicker": "Zéro tonte",
                "media": ("img", "pelouse"),
                "paras": [
                    "La pelouse synthétique répond à une demande concrète : un <strong>extérieur vert et net toute l'année</strong>, sans tonte, sans arrosage et sans plaques jaunies. Idéal pour les petits jardins, les terrasses, les zones ombragées ou les espaces de jeux.",
                    "Le rendu dépend surtout de la préparation : décaissement, nivellement, compactage, géotextile anti-repousse, puis pose et jonction soignées des lés. C'est cette base qui garantit une pelouse plane et durable.",
                ],
                "incl": ["Préparation & décaissement", "Nivellement & compactage", "Géotextile anti-repousse", "Pose & jonction des lés", "Découpes & bordures", "Finitions soignées"],
                "tip": "Un simple coup de brosse et un rinçage de temps en temps suffisent à garder une pelouse synthétique comme neuve.",
                "service": "Pelouse synthétique",
            },
            {
                "id": "lierre",
                "name": "Enlèvement de lierre",
                "kicker": "Murs libérés",
                "media": ("img", "lierre"),
                "paras": [
                    "Le lierre envahit vite une façade, un mur, une clôture ou un tronc d'arbre. Il <strong>retient l'humidité, abîme les joints et alourdit les clôtures</strong>, et peut masquer des dégâts sur le support.",
                    "Nous l'enlevons avec précaution, en coupant à la base puis en décrochant les tiges sans arracher l'enduit, pour retrouver un support lisible et une base saine. Souvent réalisé en complément d'un débroussaillage ou d'une reprise de haie.",
                ],
                "incl": ["Façades & murs", "Clôtures & grillages", "Troncs d'arbres", "Coupe à la base", "Décrochage soigneux", "Évacuation complète"],
                "tip": "Plus le lierre est ancien, plus il est difficile à retirer sans abîmer le support : n'attendez pas qu'il atteigne la toiture.",
                "service": "Enlèvement de lierre",
            },
        ],
        "signs": [
            "La haie a perdu sa forme et ferme la vue",
            "Les ronces gagnent du terrain",
            "Vous n'avez plus le temps d'entretenir le jardin",
            "Le lierre grimpe sur la façade ou la clôture",
            "Vous préparez une vente ou une location",
            "La pelouse est abîmée et demande trop d'entretien",
        ],
        "gallery": [("haie_thuyas", "Taille d'une haie de thuyas"), ("jardin_apres", "Jardin remis en état et tondu"), ("massif_apres", "Massif couvre-sol taillé"), ("haie", "Taille de haie en cours de reprise"), ("haie_finie", "Taille de haies finalisée"), ("jardin", "Extérieur remis en propre"), ("jardin_chantier", "Entretien de jardin en cours"), ("debroussaillage", "Débroussaillage de terrain"), ("pelouse", "Pose de pelouse synthétique"), ("lierre", "Façade dégagée du lierre"), ("exterieur", "Travaux d'entretien extérieur")],
        "faq": [
            ("Proposez-vous un entretien régulier ?", "Oui, nous intervenons à la fréquence que vous choisissez (mensuelle, saisonnière…) ou ponctuellement pour une remise en propre."),
            ("Quand faut-il tailler sa haie ?", "En général à la fin de l'hiver et à la fin de l'été, en évitant la période de nidification. Le bon moment dépend aussi de l'essence : nous vous conseillons."),
            ("Évacuez-vous les déchets verts ?", "Oui, les déchets verts sont ramassés et évacués. Le chantier est laissé propre à la fin de chaque intervention."),
            ("La pelouse synthétique est-elle adaptée à mon jardin ?", "Elle convient à la plupart des surfaces planes ou légèrement en pente, y compris à l'ombre. Nous vérifions le sol et l'écoulement de l'eau lors du devis."),
        ],
    },
]

BY_SLUG = {t["slug"]: t for t in TRADES}

# Balises Google (Tag Manager + Google Analytics + Google Ads), reprises à l'identique de l'ancien site
TRACKING = """<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-TVZLCH2X');</script>
<!-- End Google Tag Manager -->
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-N3K3Y19X9H"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-N3K3Y19X9H');
  gtag('config', 'AW-17854390149');
</script>
"""

# Logo d'origine du site (repli sur le nom en texte si l'image ne charge pas)
LOGO = (f'<img class="brand-logo" src="{IMG}upload-logo-site.png" alt="Logo Élagage Adolphe" '
        'width="180" height="44" decoding="async" '
        'onerror="this.parentNode.classList.add(\'no-logo\')">'
        '<span class="brand-fallback"><span class="brand-mark"><svg><use href="#i-logo"/></svg></span>'
        '<span><span class="brand-name">Adolphe</span><span class="brand-sub">Élagueur · Paysagiste</span></span></span>')

# Comparaisons avant / après. Chaque bloc ne s'affiche que si ses deux photos sont chargées
# (les peupliers restent masqués tant que leurs fichiers ne sont pas dans assets/photos/).
COMPARISONS = [
    {"key": "platanes", "trade": "elagage", "title": "Taille en têtes de chat de platanes",
     "text": "Couronnes réduites et branches ramenées sur les têtes de chat : arbres allégés et abords dégagés."},
    {"key": "peupliers", "trade": "elagage", "title": "Réduction de grands peupliers",
     "text": "Près d'un immeuble : hauteur réduite, bois débité et chantier nettoyé."},
    {"key": "jardin", "trade": "espaces-verts", "title": "Remise en état d'un jardin",
     "text": "Herbes hautes fauchées, pelouse tondue en bandes : le terrain redevient praticable."},
    {"key": "massif", "trade": "espaces-verts", "title": "Taille d'un massif couvre-sol",
     "text": "Massif recadré, bordures nettes le long de l'allée et volumes harmonisés."},
]


def before_after(trade=None):
    cards = ""
    for c in COMPARISONS:
        if trade and c["trade"] != trade:
            continue
        k = c["key"]
        cards += f'''<div class="ba">
  <figure><img src="{img(k + "_avant")}" alt="{esc(c["title"])} : avant" decoding="async"><figcaption>Avant</figcaption></figure>
  <figure><img src="{img(k + "_apres")}" alt="{esc(c["title"])} : après" decoding="async"><figcaption class="after">Après</figcaption></figure>
  <p><b>{esc(c["title"])}</b> {esc(c["text"])}</p>
</div>
'''
    return f'''<div class="ba-wrap">
  <div class="ba-head"><span class="eyebrow copper">Avant / Après</span><h3>Le résultat <span class="accent">se voit</span></h3></div>
  <div class="ba-grid">
{cards}  </div>
</div>
'''


GTM_NOSCRIPT = """<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-TVZLCH2X"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
"""


# --------------------------------------------------------------------------
# Blocs communs
# --------------------------------------------------------------------------
def header(home):
    h = "" if home else "index.html"
    menu_cols = ""
    for group, roof, slugs in (("Élagueur", False, ["elagage"]), ("Paysagiste", False, ["espaces-verts"])):
        links = ""
        for s in slugs:
            t = BY_SLUG[s]
            links += f'<a href="{t["file"]}">{ic(t["icon"])} {esc(t["menu"])}</a>'
            for sv in t["services"]:
                links += f'<a href="{t["file"]}#{sv["id"]}" style="padding-left:38px;font-weight:500;font-size:13.5px;color:var(--muted)">{esc(sv["name"])}</a>'
        menu_cols += f'<div{" class=\"roof\"" if roof else ""}><h5>{group}</h5>{links}</div>'
    mobile = ""
    for t in TRADES:
        mobile += f'<a href="{t["file"]}">{esc(t["menu"])}</a>'
    return f'''<!-- Topbar -->
<div class="topbar">
  <div class="container">
    <div class="tb-left">
      <span><i class="dot"></i> Disponible cette semaine dans le 95</span>
      <span>Devis gratuit sous 48h</span>
      <span>Urgence tempête : arbres tombés</span>
    </div>
    <a href="{TEL_HREF}">{TEL}</a>
  </div>
</div>

<!-- Header -->
<header class="header" id="header">
  <div class="container">
    <a href="{h or '#accueil'}" class="brand" aria-label="Adolphe – accueil">
      {LOGO}
    </a>
    <nav class="nav" aria-label="Navigation principale">
      <div class="dd"><button aria-expanded="false" aria-haspopup="true">Nos métiers {ic("right")}</button><div class="dd-menu">{menu_cols}</div></div>
      <a href="elagage.html">Élagage</a>
      <a href="espaces-verts.html">Paysagiste</a>
      <a href="{h}#realisations">Réalisations</a>
      <a href="{h}#avis">Avis</a>
      <a href="#contact">Contact</a>
    </nav>
    <div class="header-cta">
      <a class="header-phone" href="{TEL_HREF}">
        <span class="ic">{ic("phone")}</span>
        <span><small>Appel gratuit</small>{TEL}</span>
      </a>
      <a href="#contact" class="btn btn-primary">Devis gratuit</a>
      <button class="burger" id="burger" aria-label="Ouvrir le menu" aria-expanded="false">{ic("menu")}</button>
    </div>
  </div>
</header>
<div class="mobile-nav" id="mobileNav">
  <a href="{h or '#accueil'}">Accueil</a>
  <div class="m-group">Nos métiers</div>
  {mobile}
  <a href="{h}#realisations">Nos réalisations</a>
  <a href="{h}#avis">Avis clients</a>
  <a href="#contact">Contact</a>
  <a href="{TEL_HREF}" class="btn btn-primary">{ic("phone")} Appeler le {TEL}</a>
</div>
'''


def footer(home):
    h = "" if home else "index.html"
    cols = ""
    for t in TRADES:
        items = "".join(f'<li><a href="{t["file"]}#{s["id"]}">{esc(s["name"])}</a></li>' for s in t["services"])
        cols += f'<div class="f-trade"><h4><a href="{t["file"]}">{esc(t["menu"])}</a></h4><ul>{items}</ul></div>'
    return f'''<!-- FOOTER -->
<footer class="footer">
  <div class="container footer-grid">
    <div>
      <a href="{h or '#accueil'}" class="brand brand-footer" aria-label="Adolphe – accueil">
        {LOGO}
      </a>
      <p>Élagage, abattage, taille de haies et entretien de jardins dans tout le Val-d'Oise (95).</p>
      <ul>
        <li><a href="{TEL_HREF}">{TEL}</a></li>
        <li><a href="mailto:barryadolphe9@gmail.com">barryadolphe9@gmail.com</a></li>
      </ul>
      <a href="#contact" class="btn btn-primary" style="margin-top:20px">Devis gratuit {ic("arrow")}</a>
    </div>
    {cols}
    <div><h4>Liens rapides</h4><ul><li><a href="{h or '#accueil'}">Accueil</a></li><li><a href="{h}#realisations">Nos réalisations</a></li><li><a href="{h}#avis">Avis clients</a></li><li><a href="{h}#faq">Questions fréquentes</a></li><li><a href="#contact">Contact &amp; devis</a></li></ul></div>
  </div>
  <div class="footer-bottom">
    <div class="container">
      <span>© <span id="year">2026</span> Élagage Adolphe – Élagueur &amp; paysagiste dans le Val-d'Oise (95)</span>
      <span>Cergy · Pontoise · Argenteuil · Taverny · Franconville · Ermont et alentours</span>
    </div>
  </div>
</footer>

<!-- Floating actions -->
<a class="fab-wa" href="{WA}" target="_blank" rel="noopener" aria-label="Nous écrire sur WhatsApp">{ic("wa")}</a>
<div class="mobile-bar">
  <a href="{TEL_HREF}" class="btn btn-dark">{ic("phone")} Appeler</a>
  <a href="#contact" class="btn btn-primary">Devis gratuit</a>
</div>
'''


def media(m, alt, cls="pb-media", badge=""):
    kind = m[0]
    if kind == "img":
        return f'<div class="{cls}"><img src="{img(m[1])}" alt="{esc(alt)}" loading="lazy">{badge}</div>'
    if kind == "duo":
        return f'<div class="{cls} duo"><img src="{img(m[1])}" alt="{esc(alt)}" loading="lazy"><img src="{img(m[2])}" alt="{esc(alt)} – chantier dans le Val-d\'Oise" loading="lazy"></div>'
    # art
    return f'<div class="{cls} roof-art {m[1]}" role="img" aria-label="{esc(alt)}"><span class="ic-big">{ic(m[2])}</span>{badge}</div>'


def trade_card(t):
    if t["roof"]:
        bg = f'<div class="roof-art {t["card_art"]}"></div>'
    else:
        bg = f'<img src="{img(t["card_img"])}" alt="" loading="lazy">'
    return f'<a class="trade reveal" href="{t["file"]}">{bg}<div class="t"><small>{esc(t["trade"])}</small><b>{esc(t["menu"])} {ic("arrow")}</b><span class="d">{esc(t["short"])}</span></div></a>'


def page(t, contact_html, lightbox_html, sprite, reviews):
    url = SITE + t["file"]
    rating = '<div class="ph-badge"><span class="score">4,9</span><span><span class="stars">★★★★★</span><small>8 avis Google</small></span></div>'
    hero_media = media(t["hero"], t["menu"] + " dans le Val-d'Oise", "ph-media", rating)

    chips = "".join(f'<a href="#{s["id"]}">{esc(s["name"])}</a>' for s in t["services"])
    chips += '<a href="#contact" class="cta">Devis gratuit</a>'

    blocks = ""
    for i, s in enumerate(t["services"], 1):
        paras = "".join(f"<p>{p}</p>" for p in s["paras"])
        incl = "".join(f"<div>{ic('check')} {esc(x)}</div>" for x in s["incl"])
        num = f'<span class="pb-num">{i:02d}</span>'
        m = media(s["media"], s["name"] + " dans le Val-d'Oise", "pb-media", num)
        primary = "Intervention urgente" if s.get("urgent") else f"Devis gratuit – {s['name'].split(' :')[0].lower()}"
        blocks += f'''
      <article class="pblock reveal" id="{s["id"]}">
        {m}
        <div class="pb-text">
          <span class="eyebrow{' copper' if t['roof'] else ''}">{esc(s["kicker"])}</span>
          <h2>{esc(s["name"])}</h2>
          {paras}
          <div class="incl">{incl}</div>
          <p style="font-size:15px;background:var(--leaf-soft);border-radius:14px;padding:14px 16px;color:var(--forest-3)"><strong style="color:var(--forest)">Bon à savoir :</strong> {esc(s["tip"])}</p>
          <div class="pb-ctas">
            <button class="btn btn-primary" data-service="{esc(s["service"])}">{esc(primary)} {ic("arrow")}</button>
            <a href="{TEL_HREF}" class="btn btn-outline">{ic("phone")} {TEL}</a>
          </div>
        </div>
      </article>'''

    signs = "".join(f"<li>{ic('tarp')} {esc(x)}</li>" for x in t["signs"])
    intro = "".join(f"<p>{p}</p>" for p in t["intro"])

    combo = ""
    if t.get("combo"):
        c = t["combo"]
        combo = f'''<div class="combo reveal"><img src="{img(c["img"])}" alt="Élagage d'arbre près d'une maison" loading="lazy"><div><b>{esc(c["title"])}</b><p>{esc(c["text"])}</p><a href="{c["href"]}" class="btn btn-dark">{esc(c["cta"])} {ic("arrow")}</a></div></div>'''

    gallery = ""
    if t.get("gallery"):
        items = "".join(f'<button><img src="{img(k)}" alt="{esc(a)} dans le Val-d\'Oise" loading="lazy"><span>{esc(a)}</span></button>' for k, a in t["gallery"])
        gallery = f'''
<section class="section gallery-section" id="realisations">
  <div class="container">
    <div class="gallery-head reveal">
      <div class="section-head">
        <span class="eyebrow">Nos réalisations</span>
        <h2 style="margin-top:14px">Des chantiers <span class="accent">réels</span> dans le 95</h2>
      </div>
      <a href="#contact" class="btn btn-dark">Je veux le même résultat {ic("arrow")}</a>
    </div>
    {before_after(t["slug"])}
    <div class="gallery reveal">{items}</div>
  </div>
</section>
{lightbox_html}'''

    faq = "".join(f'<details><summary>{esc(q)} <span class="pm">{ic("plus")}</span></summary><div class="ans">{esc(a)}</div></details>' for q, a in t["faq"])
    faq_ld = ",".join('{"@type":"Question","name":%s,"acceptedAnswer":{"@type":"Answer","text":%s}}' % (jstr(q), jstr(a)) for q, a in t["faq"])

    others = "".join(trade_card(o) for o in TRADES if o is not t)

    contact = contact_html.replace('<form id="quoteForm" novalidate>', f'<form id="quoteForm" novalidate data-default-service="{esc(t["default"])}">')

    services_ld = ",".join('{"@type":"Offer","itemOffered":{"@type":"Service","name":%s}}' % jstr(s["name"]) for s in t["services"])

    return f'''<!DOCTYPE html>
<html lang="fr-FR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="index, follow, max-image-preview:large">
{TRACKING}<title>{esc(t["title"])}</title>
<meta name="description" content="{esc(t["desc"])}">
<link rel="canonical" href="{url}">
<meta property="og:locale" content="fr_FR">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(t["title"])}">
<meta property="og:description" content="{esc(t["desc"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{img("elagage")}">
<meta name="theme-color" content="#0f2a1f">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
<script type="application/ld+json">
{{"@context":"https://schema.org","@graph":[
{{"@type":"Service","name":{jstr(t["menu"])},"serviceType":{jstr(t["trade"])},"areaServed":{{"@type":"AdministrativeArea","name":"Val-d'Oise (95)"}},"provider":{{"@type":"LandscapingBusiness","name":"Élagage Adolphe","telephone":"+33759781806","url":"{SITE}"}},"hasOfferCatalog":{{"@type":"OfferCatalog","name":{jstr(t["menu"])},"itemListElement":[{services_ld}]}}}},
{{"@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Accueil","item":"{SITE}"}},{{"@type":"ListItem","position":2,"name":{jstr(t["menu"])},"item":"{url}"}}]}},
{{"@type":"FAQPage","mainEntity":[{faq_ld}]}}
]}}
</script>
</head>
<body>
{GTM_NOSCRIPT}{sprite}
{header(False)}
<main>

<section class="page-hero{' roof-hero' if t['roof'] else ''}">
  <div class="hero-grain"></div>
  <div class="container">
    <div>
      <nav class="crumbs" aria-label="Fil d'Ariane"><a href="index.html">Accueil</a><span>/</span><span>Nos métiers</span><span>/</span><span aria-current="page">{esc(t["menu"])}</span></nav>
      <span class="hero-badge"><b>{esc(t["trade"])}</b> Val-d'Oise (95)</span>
      <h1>{t["h1"]}</h1>
      <p class="hero-lead">{esc(t["lead"])}</p>
      <div class="hero-ctas">
        <a href="#contact" class="btn btn-primary btn-lg pulse">Obtenir mon devis gratuit {ic("arrow")}</a>
        <a href="{TEL_HREF}" class="btn btn-ghost btn-lg">{ic("phone")} {TEL}</a>
      </div>
      <div class="hero-trust">
        <span>{ic("check")} Devis &amp; déplacement gratuits</span>
        <span>{ic("check")} Chantier laissé propre</span>
        <span>{ic("check")} Satisfait ou on revient</span>
      </div>
    </div>
    {hero_media}
  </div>
</section>

<nav class="chips-nav" aria-label="Prestations"><div class="container">{chips}</div></nav>

<section class="section">
  <div class="container svc-layout">
    <div class="prose reveal">
      <span class="eyebrow{' copper' if t['roof'] else ''}">Notre métier</span>
      <h2 style="margin-top:14px">{esc(t["trade"])} dans le Val-d'Oise : <span class="accent">ce que nous faisons</span></h2>
      {intro}
      <h2>Quand faire appel à nous&nbsp;?</h2>
      <ul class="signs">{signs}</ul>
      {combo}
    </div>
    <aside class="side reveal">
      <div class="side-cta">
        <h3>Devis gratuit sous 48h</h3>
        <p>Décrivez votre besoin, nous vous rappelons rapidement avec une proposition claire.</p>
        <a href="#contact" class="btn btn-primary">Demander mon devis {ic("arrow")}</a>
        <a href="{TEL_HREF}" class="btn btn-ghost">{ic("phone")} {TEL}</a>
        <a href="{WA}" class="btn wa" target="_blank" rel="noopener">{ic("wa")} WhatsApp</a>
        <ul>
          <li>{ic("check")} Déplacement gratuit dans le 95</li>
          <li>{ic("check")} Sans engagement</li>
          <li>{ic("check")} Suivi après travaux offert</li>
        </ul>
      </div>
      <div class="side-box">
        <h4>Nos prestations</h4>
        {"".join(f'<a href="#{s["id"]}">{esc(s["name"])} {ic("right")}</a>' for s in t["services"])}
      </div>
    </aside>
  </div>
</section>

<section class="section" style="background:#fff">
  <div class="container">
    <div class="section-head center reveal">
      <span class="eyebrow{' copper' if t['roof'] else ''}">Nos prestations en détail</span>
      <h2 style="margin-top:14px">{esc(t["menu"])} : <span class="accent">tout ce que nous prenons en charge</span></h2>
    </div>
    <div class="pblocks">{blocks}
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head center reveal">
      <span class="eyebrow">Comment ça se passe ?</span>
      <h2 style="margin-top:14px">3 étapes, <span class="accent">zéro mauvaise surprise</span></h2>
    </div>
    <div class="mini-steps reveal">
      <div><b><span>1</span> Vous nous contactez</b><p>Par téléphone, WhatsApp ou formulaire. Envoyez quelques photos si vous le pouvez.</p></div>
      <div><b><span>2</span> Devis gratuit</b><p>Nous passons voir sur place et vous remettons une proposition claire sous 48h.</p></div>
      <div><b><span>3</span> Intervention</b><p>Travaux réalisés proprement, chantier nettoyé, suivi après travaux offert.</p></div>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <div class="cta-box reveal">
      <div style="position:relative;z-index:1">
        <h2>Besoin d'un {esc(t["trade"].lower())} dans le 95&nbsp;?</h2>
        <p>Un appel suffit : nous vous orientons tout de suite vers la bonne intervention.</p>
      </div>
      <div class="cta-actions">
        <a href="#contact" class="btn btn-white btn-lg">Demander mon devis gratuit {ic("arrow")}</a>
        <a href="{TEL_HREF}" class="btn btn-ghost btn-lg">{ic("phone")} {TEL}</a>
      </div>
    </div>
  </div>
</section>
<div style="height:110px"></div>
{gallery}

{reviews}
<section class="section faq">
  <div class="container">
    <div class="faq-side reveal">
      <span class="eyebrow">Questions fréquentes</span>
      <h2 style="margin-top:14px">{esc(t["menu"])} : <span class="accent">vos questions</span></h2>
      <div class="faq-help">
        <b>Une autre question&nbsp;?</b>
        <p>Appelez-nous, nous vous répondons directement.</p>
        <a href="{TEL_HREF}" class="btn btn-dark">{ic("phone")} {TEL}</a>
      </div>
    </div>
    <div class="reveal">{faq}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head center reveal">
      <span class="eyebrow">Notre autre métier</span>
      <h2 style="margin-top:14px">Un seul interlocuteur, <span class="accent">de l'arbre au jardin</span></h2>
    </div>
    <div class="trades" style="grid-template-columns:1fr;max-width:760px;margin:0 auto">{others}</div>
  </div>
</section>

{contact}
</main>

{footer(False)}
<script src="assets/main.js"></script>
</body>
</html>
'''


def jstr(s):
    import json
    return json.dumps(s, ensure_ascii=False)


def replace_block(s, name, content):
    return re.sub(rf"<!--{name}-->.*?<!--/{name}-->", lambda _: f"<!--{name}-->\n{content}<!--/{name}-->", s, flags=re.S)


def main():
    index_path = ROOT / "index.html"
    index = index_path.read_text()
    sprite = (ROOT / "scripts" / "sprite.html").read_text()
    contact = re.search(r'<!-- CONTACT -->\n<section class="section contact" id="contact">.*?</section>\n', index, re.S).group(0)
    reviews = re.search(r'<!-- REVIEWS -->\n<section.*?</section>\n', index, re.S).group(0)
    lightbox = re.search(r'<div class="lightbox" id="lightbox".*?</div>\n', index, re.S).group(0)

    index = replace_block(index, "TRACKING", TRACKING)
    index = replace_block(index, "GTM-NOSCRIPT", GTM_NOSCRIPT)
    index = replace_block(index, "SPRITE", sprite)
    index = replace_block(index, "AVANT-APRES", before_after())
    index = replace_block(index, "HEADER", header(True))
    index = replace_block(index, "FOOTER", footer(True))
    index = replace_block(index, "TRADES", "".join(trade_card(t) for t in TRADES) + "\n")
    index_path.write_text(index)

    for t in TRADES:
        (ROOT / t["file"]).write_text(page(t, contact, lightbox, sprite, reviews))
        print("écrit", t["file"])

    urls = [SITE] + [SITE + t["file"] for t in TRADES]
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls) + "</urlset>\n")


if __name__ == "__main__":
    main()
