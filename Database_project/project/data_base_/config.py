import os
import smtplib


class Config:
    SECRET_KEY='FABIENCLASSIC'
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:12345@localhost/amexpert"
    #SQLALCHEMY_DATABASE_URI =  "postgresql+psycopg2://postgres:1234@localhost/amexpert" 
    MAIL_SERVER ='smtp.infomaniak.com'#'mail.infomaniak.ch'
    MAIL_PORT = 587
    MAIL_USE_TLS =True
    BABEL_DEFAULT_LOCALE='fr'
    MAIL_USERNAME = 'info@resilion.eu'
    MAIL_PASSWORD = 'Vincent123$'
    RECAPTCHA_PUBLIC_KEY ='6LcghOIZAAAAAE3zgcS-maNClYmtLTqICZtmHvWi'
    RECAPTCHA_PRIVATE_KEY='6LcghOIZAAAAAFiTeOmn_gN6xW_sGIFTDcVdIO0x'
    SUIV=['Client','Responsable','Commentaire','Date Creation','Date Modification']
    UPLOAD_FOLDER=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'files')#os, 'files'.getcwd()+'/data_base_/static/files'
    UPLOAD_Export=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static','export')
    WKHTMLTOPDF_BIN_PATH =r"/usr/local/bin"
    #WKHTMLTOPDF_BIN_PATH =r"C:\Program Files\wkhtmltopdf\bin"
    WKHTMLTOPDF_USE_CELERY = True
    PDF_DIR_PATH =  os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'pdf')
    DEBUG = True
    CACHE_TYPE= "simple" # Flask-Caching related configs
    CACHE_DEFAULT_TIMEOUT= 300
    MISS=["REF BAILLEUR	SOCIETE BAILLEUR",	"TITRE BAILLEUR","NOM BAILLEUR","ADRESSE1 BAILLEUR",
    	"ADRESSE2 BAILLEUR","CP BAILLEUR","VILLE BAILLEUR","NRO FACTURE","ABONNEMENT",
        "TITRE CONCESS","NOM CONCESS","DATE REALISE EDL","PRIX HT EDL","TVA EDL","PRIX TTC EDL",
        "TITRE INTERV","NOM INTERV","REF LOCATAIRE","TITRE LOCATAIRE","NOM LOCATAIRE",
        "ADRESSE1 BIEN","ADRESSE2 BIEN","CP BIEN","	VILLE BIEN","CA HT AS","TVA AS",
        "CA TTC AS","CA HT AC","CA TTC AC","CA HT TRUST","TVA TRUST","Date chiffrage regle",
        "Prix ht chiffrage","% suiveur chiffrage","% AS chiffrage","% manager chiffrage",
    	"Nom manager chiffrage","% agent chiffrage","Nom agent chiffrage","TYPE EDL","DATE FACTURE",
        "TITRE PROPRIO",'NOMPROPRIO',"DATE FACT REGLEE","DATE COM REGLEE AS","MONTANT COM REGLEE AS",
        "DATE COM REGLEE AC","MONTANT COM REGLEE AC","TYPE LOGEMENT","NBRE EDL ABOONEMENT","MAIL CONTACT ENVOI FACT",
        "DATE saisie enregistrement","CODE AMEXPERT","COMMENTAIRE FACTURE","TYPE PAIEMENT","N° REMISE DE CHEQUE",
    	"SAISIE TRAITE PAR	infos / TRAITEMENT","LOGEMENT MEUBLE","CODE FACTURATION","TYPE DE BIEN","surface logement1"
        "ETAGE	POINTAGE","DATE POINTAGE","DEVEL","DATE EXTRACTION COMPTABLE","% COM AS DU CLIENT","Nom Respon Cell Dev",
        "%Respon Cell Dev","Nom agent Cell Dev","% Agent Cell Dev","Nom Agent CellTech","% Agent Cell Tech","Nom Respon Cell Tech"
        ,"% Respon Cell Tech","Nom Suiveur Cell Tech","% Suiveur Cell Tech","Nom Respon Cell Planif","% Respon Cell Planif",	
        "Nom Suiveur Cell Planif","% Suiveur Cell Planif","Nom Agent saisie Cell Planif","% Agent saisie CEll planif"]
    EXPS=["ID","identité agent","Trigramme","date entrée","Actif  Parti""AS AC AP","secteur activité","secteur intervnention","SIRET","Adresse 1","Adresse 2","CP",
        "Ville","Code Tva","Taux Tva","Téléphone","email groupe","email perso","Login backof","PWD backof","Login tablette",
    	"PWD backof","Login extranet","Pwd extranet","Pwd Gsuite","Pwd Samsung","Observations de suivi"] #,"Date certification initiale","date renouv certification","Type certification",    
    CLI=['ID','Reference','Type','P/C','Societe','Enseigne','Titre','Nom','email',"Numero","Siret","Date entree","Adresse1","Adresse2",
    'Etat_client','CP','Ville','Pays',"Login Extranet","MPD Extranet","Abonnement"]
    NEG=['Client','Genre','Nom','Email','Numero',"Date entree","Adresse",'Etat_client','CP','Ville','Pays',"Abonnement"]
    TARIFS=["Client","Edl Prix STD","Edl Appt prix F1","Edl Appt prix F2","Edl Appt prix F3","Edl Appt prix F4","Edl Appt prix F5"
    ,"Edl Appt prix F6","Edl pav Villa prix t1","Edl pav Villa prix t2","Edl pav Villa prix t3","Edl pav Villa prix t4","Edl pav Villa prix t5"
    ,"Edl pav Villa prix t6","Edl pav Villa prix t7","Edl pav Villa prix t8","Chif appt prix std","Chif appt prix f1","Chif appt prix f2"
    ,"Chif appt prix f3","Chif appt prix f4","Chif appt prix f5","Chif appt prix f6","Chif pav villa prix T1","Chif pav villa prix T2",
    "Chif pav villa prix T3","Chif pav villa prix T4","Chif pav villa prix T5","Chif pav villa prix T6","Chif pav villa prix T7"
    ,"Chif pav villa prix T8","Chif appt prix  stu","Chif appt prix F1","Chif appt prix F2","Chif appt prix F3","Chif appt prix F4"
    ,"Chif appt prix F5","Chif appt prix F6","Chif pav villa prix T1","Chif pav villa prix T2","Chif pav villa prix T3","Chif pav villa prix T4"
    ,"Chif pav villa prix T5","Chif pav villa prix T6","Chif pav villa prix T7","Chif pav villa prix T8","Code tva","Taux meuble","Referent as client",
    "Com as sur ca client","Cell dev ref responsable","Com cell dev ref responsable","Cell dev ref agent","Com cell dev ref agent","Cell tech ref agent",
    "Com cell tech Ref agent","Cell tech ref responsable","Com cell tech ref responsable","Cell tech ref suiveur","Com cell tech ref suiveur",
    "Cell planif ref responsable","Com cell planif ref responsable","Cell planif ref suiveur","Com cell planif ref suiveur","Cell planif ref agent saisie",
    "Com cell planif ref agent saisie","Prix autre","Commentaire libre"]

    
    
    
    
