import os
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','public')
TEL='06 03 50 82 30'; TELH='+33603508230'; MAIL='pro.ap.couverture@gmail.com'

def ic(p,s=28): return f'<svg class="i" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'
I={
 'roof':ic('<path d="M3 12 12 4l9 8"/><path d="M5 10.5V20h14v-9.5"/><path d="M9 20v-6h6v6"/>'),
 'zinc':ic('<path d="M3 7h18v3H3z"/><path d="M6 10v8a2 2 0 0 0 2 2h0"/><path d="M18 10v6"/><path d="M18 19v.01"/>'),
 'gable':ic('<path d="M12 3 4 12v9h16v-9z"/><path d="M12 3v18"/><path d="M4 12h16"/>'),
 'velux':ic('<path d="M3 18 9 6h12l-6 12z"/><path d="m6 12 12 0"/>'),
 'phone':ic('<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/>',22),
 'mail':ic('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',22),
 'pin':ic('<path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',22),
 'clock':ic('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',22),
 'check':ic('<path d="m5 12 5 5 9-10"/>',20),
 'arrow':ic('<path d="M5 12h14"/><path d="m13 6 6 6-6 6"/>',20),
 'file':ic('<path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5"/><path d="M10 13h6M10 17h6"/>'),
 'shield':ic('<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/><path d="m9 12 2 2 4-4"/>'),
 'user':ic('<circle cx="12" cy="8" r="4"/><path d="M4 21c1-4 4-6 8-6s7 2 8 6"/>'),
}
PAGES=[('index.html','Accueil'),('services.html','Services'),('realisations.html','Réalisations'),('a-propos.html','À propos'),('contact.html','Contact')]

def page(fn,title,desc,body,hero=None):
    nav=''.join(f'<a href="{f}"{" class=\"active\"" if f==fn else ""}>{n}</a>' for f,n in PAGES[:-1])
    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | P.A Couverture – Couvreur à Hautmont</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700&family=Barlow:wght@400;500;600&display=swap">
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="topbar"><div class="container"><span>{I['pin'].replace('width="22" height="22"','width="15" height="15"')} Hautmont (59330) et alentours</span><a href="tel:{TELH}">{I['phone'].replace('width="22" height="22"','width="15" height="15"')} {TEL}</a></div></div>
<header class="header">
<div class="container nav">
<a href="index.html" class="logo" aria-label="P.A Couverture, accueil"><img src="images/mascotte.png" alt="" width="59" height="34"><span>P.A <b>COUVERTURE</b></span></a>
<button class="burger" aria-label="Ouvrir le menu" aria-expanded="false"><span></span><span></span><span></span></button>
<nav class="menu">{nav}<a href="contact.html" class="btn btn-sm{' active' if fn=='contact.html' else ''}">Devis gratuit</a></nav>
</div>
</header>
<main>
{body}
</main>
<footer class="footer">
<div class="container fgrid">
<div><a href="index.html" class="logo"><img src="images/mascotte.png" alt="" width="59" height="34"><span>P.A <b>COUVERTURE</b></span></a>
<p>Couverture, zinguerie, pignon et velux.<br>Artisan couvreur à Hautmont.</p></div>
<div><h4>Navigation</h4>{''.join(f'<a href="{f}">{n}</a>' for f,n in PAGES)}</div>
<div><h4>Contact</h4><a href="tel:{TELH}">{TEL}</a><a href="mailto:{MAIL}">{MAIL}</a><span>59330 Hautmont</span></div>
</div>
<div class="container legal"><span>© <span id="year"></span> P.A Couverture – SIRET 000 000 000 00000</span><span class="legal-links"><a href="mentions-legales.html">Mentions légales</a><a href="confidentialite.html">Confidentialité</a><a href="/admin" class="adm-link" data-noedit>Administration</a></span></div>
</footer>
<script src="script.js"></script>
</body>
</html>'''

def banner(h,p,crumb):
    return f'<section class="banner"><div class="container"><p class="crumb"><a href="index.html">Accueil</a> / {crumb}</p><h1>{h}</h1><p>{p}</p></div></section>'

cta='''<section class="cta"><div class="container"><div><h2>Un projet de toiture ?</h2><p>Décrivez-nous vos travaux, nous vous répondons rapidement avec un devis gratuit.</p></div><div class="cta-btns"><a href="contact.html" class="btn btn-light">Demander un devis</a><a href="tel:%s" class="btn btn-ghost">%s</a></div></div></section>''' % (TELH,TEL)

SERV=[
('roof','Couverture','Réfection et rénovation complète de votre toiture, quel que soit le matériau.',
 ['Dépose et pose de tuiles, ardoises, bac acier','Remplacement de tuiles cassées ou déplacées','Recherche et réparation de fuites','Pose d\'écran sous-toiture et liteaux','Traitement et nettoyage de toiture']),
('zinc','Zinguerie','Évacuation des eaux pluviales et habillages en zinc, pour protéger durablement votre bâtiment.',
 ['Pose et remplacement de gouttières','Descentes d\'eaux pluviales','Noues, solins et faîtages','Bandes de rives et habillages','Création sur mesure en zinc']),
('gable','Pignon','Travaux de finition et d\'étanchéité sur les pignons, point sensible de toute toiture.',
 ['Réfection de rives et de pignons','Étanchéité et couvertines','Habillage et bardage de pignon','Reprise de maçonnerie en haut de pignon']),
('velux','Velux','Fourniture et pose de fenêtres de toit pour apporter lumière et volume à vos combles.',
 ['Pose de fenêtres de toit neuves','Remplacement de velux existants','Raccords d\'étanchéité soignés','Habillage intérieur et finitions']),
]

# ---------- INDEX
cards=''.join(f'<a class="scard" href="services.html#{t.lower()}"><span class="sico">{I[k]}</span><h3>{t}</h3><p>{d}</p><span class="more">En savoir plus {I["arrow"]}</span></a>' for k,t,d,_ in SERV)
why=[('file','Devis gratuit','Un chiffrage clair et détaillé, sans engagement et sans surprise.'),
     ('user','Un interlocuteur unique','Vous échangez directement avec l\'artisan, du devis à la fin du chantier.'),
     ('shield','Garantie décennale','Vos travaux sont couverts par notre garantie décennale, pour construire en toute sérénité.'),
     ('check','Travail soigné','Des finitions propres et un chantier laissé net à la fin des travaux.')]
whyh=''.join(f'<div class="why"><span class="sico">{I[k]}</span><div><h3>{t}</h3><p>{d}</p></div></div>' for k,t,d in why)
index=f'''<section class="hero"><div class="container hero-in"><div class="hero-txt">
<p class="eyebrow">Couverture · Zinguerie · Pignon · Velux</p>
<h1>Votre toiture<br>entre de bonnes mains.</h1>
<p class="lead">P.A Couverture réalise la couverture, la zinguerie, les pignons et la pose de velux à Hautmont et dans les environs.</p>
<div class="hero-btns"><a href="contact.html" class="btn">Demander un devis gratuit</a><a href="services.html" class="btn btn-ghost">Découvrir nos services</a></div><p class="hero-note">{I['shield']} Garantie décennale</p></div>
<div class="hero-logo"><div class="logo-shine"><img src="images/logo.png" alt="Logo P.A Couverture et Zinguerie"></div></div></div></section>
<section class="section"><div class="container"><div class="head"><p class="eyebrow">Nos métiers</p><h2>Ce que nous faisons</h2></div><div class="grid4">{cards}</div></div></section>
<section class="section alt"><div class="container"><div class="head"><p class="eyebrow">Notre engagement</p><h2>Pourquoi choisir P.A Couverture</h2></div><div class="grid2">{whyh}</div></div></section>
{cta}'''

# ---------- SERVICES
sec=''
for n,(k,t,d,l) in enumerate(SERV):
    lis=''.join(f'<li>{I["check"]}<span>{x}</span></li>' for x in l)
    rev=' rev' if n%2 else ''
    sec+=f'<section class="section{" alt" if n%2 else ""}" id="{t.lower()}"><div class="container srv{rev}"><div class="srv-ico">{I[k].replace("width=\"28\" height=\"28\"","width=\"90\" height=\"90\"")}</div><div><p class="eyebrow">0{n+1}</p><h2>{t}</h2><p class="lead2">{d}</p><ul class="list">{lis}</ul><a class="btn" href="contact.html">Devis pour {t.lower()}</a></div></div></section>'
services=banner('Nos services','Quatre savoir-faire pour une toiture complète, de la couverture aux finitions.','Services')+sec+cta

# ---------- REALISATIONS
ph=lambda t:f'<figure class="shot"><div class="ph">{I["roof"].replace("width=\"28\" height=\"28\"","width=\"56\" height=\"56\"")}<span>Photo à venir</span></div><figcaption><b>{t}</b></figcaption></figure>'
real=banner('Nos réalisations','Un aperçu de nos chantiers de couverture, zinguerie, pignon et velux.','Réalisations')+'<section class="section"><div class="container"><div class="gallery" id="gallery"></div></div></section>'+cta

# ---------- A PROPOS
infos=[('SIRET','000 000 000 00000'),('Activité','Couverture, zinguerie, pignon, velux'),('Garantie','Décennale'),('Zone','Hautmont (59330) et alentours'),('Contact',TEL)]
inf=''.join(f'<div class="irow"><span>{a}</span><b>{b}</b></div>' for a,b in infos)
about=banner('À propos','Une entreprise locale de couverture, à votre écoute.','À propos')+f'''<section class="section"><div class="container two"><div>
<p class="eyebrow">Qui sommes-nous</p><h2>P.A Couverture, artisan couvreur</h2>
<p class="para">Basée à Hautmont, P.A Couverture intervient auprès des particuliers et des professionnels pour tous les travaux de toiture : couverture, zinguerie, pignon et pose de velux.</p>
<p class="para">Notre approche est simple : un diagnostic honnête, un devis clair, des travaux réalisés dans les règles de l'art et un chantier laissé propre.</p>
<a class="btn" href="contact.html">Nous contacter</a></div>
<div class="panel"><h3>Informations</h3>{inf}</div></div></section>
<section class="section alt"><div class="container"><div class="head"><p class="eyebrow">Nos valeurs</p><h2>Notre façon de travailler</h2></div><div class="grid2">{whyh}</div></div></section>'''+cta

# ---------- CONTACT
def row(k,l,v,h=None):
    v=f'<a href="{h}">{v}</a>' if h else v
    return f'<div class="crow"><span class="sico">{I[k]}</span><div><small>{l}</small><b>{v}</b></div></div>'
contact=banner('Contact et devis gratuit','Décrivez votre projet, nous vous répondons rapidement.','Contact')+f'''<section class="section"><div class="container two">
<div><p class="eyebrow">Nos coordonnées</p><h2>Parlons de votre toiture</h2>
{row('phone','Téléphone',TEL,'tel:'+TELH)}{row('mail','E-mail',MAIL,'mailto:'+MAIL)}{row('pin','Adresse','59330 Hautmont')}
</div>
<form class="form" id="form"><h3>Demande de devis</h3>
<div class="frow"><label>Nom<input type="text" name="nom" required></label><label>Téléphone<input type="tel" name="tel" required></label></div>
<label>E-mail<input type="email" name="email" required></label>
<label>Type de travaux<select name="type"><option>Couverture</option><option>Zinguerie</option><option>Pignon</option><option>Velux</option><option>Réparation / fuite</option><option>Autre</option></select></label>
<label>Votre projet<textarea name="message" rows="5"></textarea></label>
<p class="fnote">Les informations saisies servent uniquement à répondre à votre demande. <a href="confidentialite.html">En savoir plus</a></p><button class="btn" type="submit">Envoyer la demande</button>
<p class="ok" hidden>Votre messagerie va s'ouvrir pour envoyer la demande.</p></form></div></section>'''


TODO='[à compléter]'
def doc(title, intro, blocks, crumb):
    out=''
    for h,items in blocks:
        out+=f'<h3>{h}</h3>'
        for it in items:
            if isinstance(it,list): out+='<ul>'+''.join(f'<li>{x}</li>' for x in it)+'</ul>'
            else: out+=f'<p>{it}</p>'
    return banner(title,intro,crumb)+f'<section class="section"><div class="container"><div class="prose">{out}<p class="upd">Dernière mise à jour : novembre 2026</p></div></div></section>'

mentions=doc('Mentions légales','Informations légales relatives au site et à son éditeur.',[
 ('Éditeur du site',[
  ['Nom commercial : P.A Couverture','Forme juridique : '+TODO,'SIRET : 000 000 000 00000','Adresse : 59330 Hautmont ('+TODO+' : numéro et rue)','Téléphone : '+TEL,'E-mail : '+MAIL,'N° de TVA intracommunautaire : '+TODO+' (si applicable)']]),
 ('Directeur de la publication',['Le directeur de la publication est '+TODO+'.']),
 ('Hébergeur',['Le site est hébergé par '+TODO+' (nom, adresse et téléphone de l\'hébergeur).']),
 ('Assurance',['Garantie décennale souscrite auprès de '+TODO+' (nom et coordonnées de l\'assureur), valable pour les travaux réalisés en France métropolitaine.']),
 ('Médiation de la consommation',['Conformément à la réglementation, en cas de litige non résolu avec un client particulier, celui-ci peut recourir gratuitement à un médiateur de la consommation : '+TODO+' (nom et coordonnées du médiateur).']),
 ('Propriété intellectuelle',['L\'ensemble des contenus du site (textes, photographies, logo, éléments graphiques) est la propriété de P.A Couverture, sauf mention contraire. Toute reproduction, représentation ou réutilisation, totale ou partielle, sans autorisation écrite préalable est interdite.']),
 ('Responsabilité',['Les informations présentées sur ce site sont données à titre indicatif. P.A Couverture s\'efforce de les maintenir exactes et à jour, mais ne saurait être tenue responsable d\'une erreur ou d\'une omission. Seul un devis signé engage l\'entreprise.','Le site peut contenir des liens vers des sites tiers dont P.A Couverture n\'a pas la maîtrise et dont elle ne peut garantir le contenu.']),
 ('Droit applicable',['Le présent site est soumis au droit français. En cas de litige, les tribunaux français sont seuls compétents.']),
],'Mentions légales')

confid=doc('Politique de confidentialité','Comment vos données personnelles sont utilisées et protégées.',[
 ('Responsable du traitement',['P.A Couverture, 59330 Hautmont, joignable à l\'adresse '+MAIL+'.']),
 ('Données collectées',['Lorsque vous utilisez le formulaire de demande de devis, nous collectons les informations que vous saisissez : nom, numéro de téléphone, adresse e-mail, type de travaux et message.']),
 ('Finalité et base légale',['Ces données sont utilisées uniquement pour répondre à votre demande de devis et vous contacter à ce sujet (mesures précontractuelles prises à votre demande). Elles ne sont ni vendues, ni cédées à des tiers à des fins commerciales.']),
 ('Durée de conservation',['Vos données sont conservées le temps nécessaire au traitement de votre demande, puis au maximum 3 ans après notre dernier échange, sauf obligation légale de conservation plus longue (par exemple en cas de contrat signé).']),
 ('Vos droits',['Conformément au RGPD, vous disposez d\'un droit d\'accès, de rectification, d\'effacement, d\'opposition, de limitation et de portabilité de vos données. Pour les exercer, écrivez à '+MAIL+'.','Si vous estimez, après nous avoir contactés, que vos droits ne sont pas respectés, vous pouvez introduire une réclamation auprès de la CNIL (www.cnil.fr).']),
 ('Cookies et polices',['Ce site n\'utilise aucun cookie publicitaire ni outil de mesure d\'audience. Un cookie technique strictement nécessaire n\'est déposé que pour la session de l\'administrateur du site.','Les polices de caractères sont chargées depuis le service Google Fonts, ce qui peut transmettre votre adresse IP à Google lors de l\'affichage des pages.']),
],'Confidentialité')

for fn,t,d,b in [
 ('index.html','Couvreur à Hautmont','P.A Couverture, couvreur à Hautmont : couverture, zinguerie, pignon et velux. Devis gratuit.',index),
 ('services.html','Services','Couverture, zinguerie, pignon et pose de velux à Hautmont et alentours.',services),
 ('realisations.html','Réalisations','Découvrez les chantiers de toiture réalisés par P.A Couverture.',real),
 ('a-propos.html','À propos','P.A Couverture, artisan couvreur à Hautmont (59330).',about),
 ('mentions-legales.html','Mentions légales','Mentions légales du site P.A Couverture.',mentions),
 ('confidentialite.html','Confidentialité','Politique de confidentialité du site P.A Couverture.',confid),
 ('contact.html','Contact','Contactez P.A Couverture pour un devis gratuit : 06 03 50 82 30.',contact)]:
    open(os.path.join(OUT,fn),'w').write(page(fn,t,d,b))
