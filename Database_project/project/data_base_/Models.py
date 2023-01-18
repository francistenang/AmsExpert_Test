from flask import current_app
from Database_project.project.data_base_ import  db,login_manager
from itsdangerous import  TimedJSONWebSignatureSerializer as Serializer
from datetime import datetime
from sqlalchemy import ForeignKeyConstraint,ForeignKey,UniqueConstraint
from flask_login import UserMixin
from sqlalchemy import Float,DECIMAL
import json



@login_manager.user_loader
def load_user(user_id):
    return Expert.query.get(int(user_id))

class Client(db.Model):
    __table_args__ = {'extend_existing': True}


    __tablename__ = 'Client'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    reference = db.Column(db.Integer) 	
    TYPE = db.Column(db.String,default='') 
    societe = db.Column(db.String,default='') 	
    enseigne = db.Column(db.String,default='')
    titre = db.Column(db.String,default='') 	
    nom = db.Column(db.String,default='')
    prenom = db.Column(db.String,default='')
    email = db.Column(db.String,default='')
    numero = db.Column(db.String,default='')
    siret=db.Column(db.BigInteger,default=0)
    date_creation =db.Column(db.DateTime(),default=datetime.utcnow)
    anom= db.Column(db.Boolean,default=False) #you comment
    reason= db.Column(db.String,default='')
    visibility =db.Column(db.Boolean,default=True)
  


    #def __init__(self,TYPE,societe,sexe,nom,email,numero,siret):
      #  self.TYPE=TYPE
      #  self.societe= societe
       # self.sexe = sexe
       # self.nom = nom
       # self.email=email
       # self.numero=numero
       # self.siret=siret
     

    def __repr__(self):
        return '<Client %r>' %self.id

class Expert(db.Model,UserMixin):
    __table_args__ = {'extend_existing': True}

    __tablename__ = 'Expert'

    id = db.Column(db.Integer,primary_key=True)
    new= db.Column(db.String,default='')
    full=db.Column(db.String,default='')
    login = db.Column(db.String,default='')#refo unique
    genre  = db.Column(db.String,default='')	
    nom = db.Column(db.String,default='')
    prenom = db.Column(db.String,default='')
    trigramme=db.Column(db.String,default='')
    TYPE=db.Column(db.String,default='')
    date_entree=db.Column(db.DateTime,default=datetime.utcnow)
    siret=db.Column(db.BigInteger,default=0) 
    email = db.Column(db.String,default='')#unique
    email_perso = db.Column(db.String,default='')
    numero = db.Column(db.String)
    code_tva=db.Column(db.String,default='')
    taux_tva=db.Column(db.DECIMAL(65,2),default=0.00)
    anom= db.Column(db.Boolean,default=False)
    reason= db.Column(db.String,default='')
    password = db.Column(db.String(60))
    visibility =db.Column(db.Boolean,default=True)
    
    


    def get_reset_token(self,expire_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'],expire_sec)
        return s.dumps({'expert_id':self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            expert_id = s.loads(token) ['expert_id']
        except:
            return None
        return Expert.query.get(expert_id)

    def __repr__(self):
        return '<Expert %r>' %self.id
        
class Client_History(db.Model):
    __table_args__ = {'extend_existing': True}

    __tablename__ = 'Client_History'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    client_id = db.Column(db.Integer, ForeignKey('Client.id', onupdate="CASCADE", ondelete="CASCADE"))   	
    adresse1  = db.Column(db.String,default='')
    adresse2 = db.Column(db.String,default='')
    etat_client=db.Column(db.String,default='')
    cp 	 = db.Column(db.BigInteger,default=0)
    ville  = db.Column(db.String,default='')
    pays= db.Column(db.String,default='')
    login_extranet= db.Column(db.String,default='')
    mpd_extranet = db.Column(db.String,default='')
    abonnement=db.Column(db.String,default='')
    date =db.Column(db.DateTime(),default=datetime.utcnow)
    visibility =db.Column(db.Boolean,default=True)


 #adresse2

        

    def __repr__(self):
        return '<Client_History %r>' %self.id

class Client_negotiateur(db.Model):
    __table_args__ = {'extend_existing': True}

    __tablename__ = 'Client_negotiateur'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    client_id = db.Column(db.Integer, ForeignKey('Client.id', onupdate="CASCADE", ondelete="CASCADE"))   
    client__nego=db.relationship("Client", 
            primaryjoin=(client_id == Client.id),
            backref=db.backref('client__nego',  uselist=False),  uselist=False) 	
    sexe = db.Column(db.String,default='') 	
    nom = db.Column(db.String,default='')
    prenom = db.Column(db.String,default='')
    email = db.Column(db.String,default='')
    numero = db.Column(db.String,default='')
    date_creation =db.Column(db.DateTime(),default=datetime.utcnow)
    visibility =db.Column(db.Boolean,default=True)


    def __init__(self,client_id,sexe,nom,email,numero):
        self.client_id=client_id
        self.sexe = sexe
        self.nom = nom
        self.email=email
        self.numero=numero

    def __repr__(self):
        return '<Client_negotiateur %r>' %self.id

class Negotiateur_History(db.Model):
    __table_args__ = {'extend_existing': True}

    __tablename__ = 'Negotiateur_History'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    negotiateur_id = db.Column(db.Integer, ForeignKey('Client_negotiateur.id', onupdate="CASCADE", ondelete="CASCADE"))   	
    adresse  = db.Column(db.String,default='')	
    etat_client=db.Column(db.Boolean,default=True)
    cp 	 = db.Column(db.BigInteger)
    ville  = db.Column(db.String,default='')
    pays= db.Column(db.String,default='')
    abonnement=db.Column(db.String,default='')
    date =db.Column(db.DateTime(),default=datetime.utcnow)
    visibility =db.Column(db.Boolean,default=True)


        

    def __repr__(self):
        return '<Negotiateur_History %r>' %self.id

class suivi_client(db.Model):
    __table_args__ = {'extend_existing': True}

    __tablename__ = 'suivi_client'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    client = db.Column(db.Integer, ForeignKey('Client.id', onupdate="CASCADE", ondelete="CASCADE"))   
    suivi__data=db.relationship("Client", 
        primaryjoin=(client == Client.id),
        backref=db.backref('suivi__data',  uselist=False),  uselist=False)
    responsable=db.Column(db.Integer, db.ForeignKey('Expert.id'))
    responsable__data=db.relationship("Expert", 
        primaryjoin=(responsable == Expert.id),
        backref=db.backref('responsable__data',  uselist=False),  uselist=False)
    
    commentaire = db.Column(db.String,default='')
    date_creation=db.Column(db.DateTime(),default=datetime.utcnow)
    date_modif=db.Column(db.DateTime())
    visibility=visibility =db.Column(db.Boolean,default=True)

    def __init__(self,client,responsable,commentaire):
        self.client=client
        self.responsable=responsable
        self.commentaire= commentaire


    def __repr__(self):
        return '<suivi_client %r>' %self.id

class prospect(db.Model):
    __table_args__ = {'extend_existing': True}

    __tablename__ = 'prospect'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    reference = db.Column(db.Integer) 	
    TYPE = db.Column(db.String,default='') 
    societe = db.Column(db.String,default='') 	
    enseigne = db.Column(db.String,default='')
    titre = db.Column(db.String,default='') 	
    nom = db.Column(db.String,default='')
    prenom = db.Column(db.String,default='')
    email = db.Column(db.String,default='')
    numero = db.Column(db.String,default='')
    siret=db.Column(db.BigInteger)
    date_creation =db.Column(db.DateTime,default=datetime.utcnow)
    anom= db.Column(db.Boolean,default=False)
    reason= db.Column(db.String,default='')
    visibility =db.Column(db.Boolean,default=True)
  


    #def __init__(self,TYPE,societe,genre,nom,email,numero):
      #  self.TYPE=TYPE
      #  self.societe= societe
      #  self.genre = genre
      #  self.nom = nom
      #  self.email=email
      #  self.numero=numero
    

    def __repr__(self):
        return '<prospect %r>' %self.id

class prospect_History(db.Model):
    __table_args__ = {'extend_existing': True}

    __tablename__ = 'prospect_History'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    prospect = db.Column(db.Integer, ForeignKey('prospect.id', onupdate="CASCADE", ondelete="CASCADE"))   		
    adresse1  = db.Column(db.String,default='')
    adresse2 = db.Column(db.String,default='')
    cp 	 = db.Column(db.BigInteger)
    ville  = db.Column(db.String,default='')
    pays= db.Column(db.String,default='')
    etat_client=db.Column(db.String,default='')
    login_extranet= db.Column(db.String,default='')
    mpd_extranet = db.Column(db.String,default='')
    date =db.Column(db.DateTime(),default=datetime.utcnow)
    visibility =db.Column(db.Boolean,default=True)


    def __repr__(self):
        return '<prospect_History %r>' %self.id

class suivi_prospect(db.Model):
    __table_args__ = {'extend_existing': True}

    __tablename__ = 'suivi_prospect'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    prospect_id = db.Column(db.Integer, ForeignKey('prospect.id', onupdate="CASCADE", ondelete="CASCADE"))   
    responsable=db.Column(db.Integer, db.ForeignKey('Expert.id'))
    suivi__data=db.relationship("prospect", 
        primaryjoin=(prospect_id == prospect.id),
        backref=db.backref('prospect__data',  uselist=False),  uselist=False)
    responsable__data=db.relationship("Expert", 
        primaryjoin=(responsable == Expert.id),
        backref=db.backref('responsable___data',  uselist=False),  uselist=False)
    commentaire = db.Column(db.String,default='')
    date_creation=db.Column(db.DateTime(),default=datetime.utcnow)
    date_modif=db.Column(db.DateTime(),default=datetime.utcnow)
    visibility=db.Column(db.Boolean,default=True)

    def __init__(self,prospect,responsable,commentaire):
        self.prospect_id=prospect
        self.responsable=responsable
        self.commentaire= commentaire


    def __repr__(self):
        return '<suivi_prospect %r>' %self.id

class Expert_History(db.Model):
    __table_args__ = {'extend_existing': True}

    __tablename__ = 'Expert_History'

    id = db.Column(db.Integer,primary_key=True)
    expert_id= db.Column(db.Integer, ForeignKey('Expert.id'))
    actif_parti=db.Column(db.String,default='')
    secteur=db.Column(db.String,default='')
   # type_certification=db.Column(db.String,default='')
   # date_certification_initiale=db.Column(db.DateTime())#check this
   # date_renouv_certification=db.Column(db.DateTime())#check this
    adresse1 = db.Column(db.String,default='')
    adresse2 = db.Column(db.String,default='')
    cp=db.Column(db.Integer,default=0)
    login_backof=db.Column(db.String,default='')
    pwd_backof=db.Column(db.String,default='') 
    login_extranet=db.Column(db.String,default='')
    pwd_extranet=db.Column(db.String,default='') 
    pwd_gsuite=db.Column(db.String,default='')
    login_google=db.Column(db.String,default='')
    pwd_google=db.Column(db.String,default='')
    ville=db.Column(db.String,default='')
    observations_de_suivi=db.Column(db.String,default='')
    date_sortie=db.Column(db.DateTime)
    date=db.Column(db.DateTime(),default=datetime.utcnow)
    visibility =db.Column(db.Boolean,default=True)


    def __repr__(self):
        return '<Expert_History %r>' %self.id

class Tarif_base(db.Model):
    __table_args__ = {'extend_existing': True}

    __tablename__ = 'Tarif_base'

    id = db.Column(db.Integer,primary_key=True)
    pav_appartement=db.Column(db.String,default='') 
    Type  = db.Column(db.String,default='') 
    surface = db.Column(db.Integer) 
    Prix_EDL = db.Column(db.DECIMAL(65,2),default=0.00) 
    visibility =db.Column(db.Boolean,default=True)

    def __repr__(self):
        return '<Tarif_base %r>' %self.id

class Tarifs(db.Model):
    __table_args__ = {'extend_existing': True}

    __tablename__ = 'Tarifs'

    id = db.Column(db.Integer,primary_key=True)
    reference_client= db.Column(db.Integer, ForeignKey('Client.id', onupdate="CASCADE", ondelete="CASCADE"))   
    
    data_client=db.relationship("Client", 
        primaryjoin=(reference_client == Client.id),
        backref=db.backref('data_client',  uselist=False),  uselist=False)
    edl_prix_std=db.Column(db.DECIMAL(65,2),default=0.00)     
    edl_appt_prix_f1=db.Column(db.DECIMAL(65,2),default=0.00) 
    edl_appt_prix_f2=db.Column(db.DECIMAL(65,2),default=0.00) 
    edl_appt_prix_f3=db.Column(db.DECIMAL(65,2),default=0.00) 
    edl_appt_prix_f4=db.Column(db.DECIMAL(65,2),default=0.00) 
    edl_appt_prix_f5=db.Column(db.DECIMAL(65,2),default=0.00) 
    edl_appt_prix_f6=db.Column(db.DECIMAL(65,2),default=0.00) 
    edl_pav_villa_prix_t1=db.Column(db.DECIMAL(65,2),default=0.00) 
    edl_pav_villa_prix_t2=db.Column(db.DECIMAL(65,2),default=0.00) 
    edl_pav_villa_prix_t3=db.Column(db.DECIMAL(65,2),default=0.00) 
    edl_pav_villa_prix_t4=db.Column(db.DECIMAL(65,2),default=0.00) 
    edl_pav_villa_prix_t5=db.Column(db.DECIMAL(65,2),default=0.00) 
    edl_pav_villa_prix_t6=db.Column(db.DECIMAL(65,2),default=0.00) 
    edl_pav_villa_prix_t7=db.Column(db.DECIMAL(65,2),default=0.00) 
    edl_pav_villa_prix_t8=db.Column(db.DECIMAL(65,2),default=0.00) 
    chif_appt_prix_stu=db.Column(db.DECIMAL(65,2),default=0.00) 
    chif_appt_prix_f1 =db.Column(db.DECIMAL(65,2),default=0.00) 
    chif_appt_prix_f2 =db.Column(db.DECIMAL(65,2),default=0.00) 
    chif_appt_prix_f3 =db.Column(db.DECIMAL(65,2),default=0.00) 
    chif_appt_prix_f4 =db.Column(db.DECIMAL(65,2),default=0.00) 
    chif_appt_prix_f5 =db.Column(db.DECIMAL(65,2),default=0.00) #f6
    chif_appt_prix_f6 =db.Column(db.DECIMAL(65,2),default=0.00)
    chif_pav_villa_prix_t1=db.Column(db.DECIMAL(65,2),default=0.00) 
    chif_pav_villa_prix_t2=db.Column(db.DECIMAL(65,2),default=0.00) 
    chif_pav_villa_prix_t3=db.Column(db.DECIMAL(65,2),default=0.00) 
    chif_pav_villa_prix_t4=db.Column(db.DECIMAL(65,2),default=0.00) 
    chif_pav_villa_prix_t5=db.Column(db.DECIMAL(65,2),default=0.00) 
    chif_pav_villa_prix_t6=db.Column(db.DECIMAL(65,2),default=0.00) 
    chif_pav_villa_prix_t7=db.Column(db.DECIMAL(65,2),default=0.00) 
    chif_pav_villa_prix_t8=db.Column(db.DECIMAL(65,2),default=0.00) 
    code_tva=db.Column(db.String,default='')
    taux_meuble=db.Column(db.Integer)#Is thisFloat??
    referent_as_client=db.Column(db.Integer, ForeignKey('Expert.id', onupdate="CASCADE", ondelete="CASCADE")) 
    referent__data=db.relationship("Expert", 
        primaryjoin=(referent_as_client == Expert.id),
        backref=db.backref('referent__data',  uselist=False),  uselist=False)

    com_as_sur_ca_client = db.Column(db.DECIMAL(65,2),default=0.00)

    cell_dev_ref_responsable =db.Column(db.Integer, ForeignKey('Expert.id', onupdate="CASCADE", ondelete="CASCADE")) 
    cell_dev__data=db.relationship("Expert", 
        primaryjoin=(cell_dev_ref_responsable == Expert.id),
        backref=db.backref('cell_dev__data',  uselist=False),  uselist=False)

    com_cell_dev_ref_responsable = db.Column(db.DECIMAL(65,2),default=0.00)

    cell_dev_ref_agent =db.Column(db.Integer, ForeignKey('Expert.id', onupdate="CASCADE", ondelete="CASCADE")) 
    cell_dev_ref_data=db.relationship("Expert", 
        primaryjoin=(cell_dev_ref_agent == Expert.id),
        backref=db.backref('cell_dev_ref_data',  uselist=False),  uselist=False)

    com_cell_dev_ref_agent = db.Column(db.DECIMAL(65,2),default=0.00)
    
    cell_tech_ref_agent=db.Column(db.Integer, ForeignKey('Expert.id', onupdate="CASCADE", ondelete="CASCADE")) 
    cell_tech_ref_agent__data=db.relationship("Expert", 
        primaryjoin=(cell_tech_ref_agent == Expert.id),
        backref=db.backref('cell_tech_ref_agent__data',  uselist=False),  uselist=False)

    com_cell_tech_Ref_agent = db.Column(db.DECIMAL(65,2),default=0.00)

    cell_tech_ref_responsable =db.Column(db.Integer, ForeignKey('Expert.id', onupdate="CASCADE", ondelete="CASCADE")) 
    cell_tech_ref_responsable__data=db.relationship("Expert", 
        primaryjoin=(cell_tech_ref_responsable == Expert.id),
        backref=db.backref('cell_tech_ref_responsable__data',  uselist=False),  uselist=False)

    com_cell_tech_ref_responsable  = db.Column(db.DECIMAL(65,2),default=0.00)

    cell_tech_ref_suiveur=db.Column(db.Integer, ForeignKey('Expert.id', onupdate="CASCADE", ondelete="CASCADE")) 
    cell_tech_ref_suiveur__data=db.relationship("Expert", 
        primaryjoin=(cell_tech_ref_suiveur == Expert.id),
        backref=db.backref('cell_tech_ref_suiveur__data',  uselist=False),  uselist=False)
    com_cell_tech_ref_suiveur = db.Column(db.DECIMAL(65,2),default=0.00)

    cell_planif_ref_responsable =db.Column(db.Integer, ForeignKey('Expert.id', onupdate="CASCADE", ondelete="CASCADE")) 
    cell_planif_ref_responsable_data=db.relationship("Expert", 
        primaryjoin=(cell_planif_ref_responsable  == Expert.id),
        backref=db.backref('cell_planif_ref_responsable_data',  uselist=False),  uselist=False)

    com_cell_planif_ref_responsable = db.Column(db.DECIMAL(65,2),default=0.00)

    cell_planif_ref_suiveur =db.Column(db.Integer, ForeignKey('Expert.id', onupdate="CASCADE", ondelete="CASCADE")) 
    cell_planif_ref_suiveur__data=db.relationship("Expert", 
        primaryjoin=(cell_planif_ref_suiveur  == Expert.id),
        backref=db.backref('cell_planif_ref_suiveur__data',  uselist=False),  uselist=False)

    com_cell_planif_ref_suiveur = db.Column(db.DECIMAL(65,2),default=0.00)

    cell_planif_ref_agent_saisie =db.Column(db.Integer, ForeignKey('Expert.id', onupdate="CASCADE", ondelete="CASCADE")) 
    cell_planif_ref_agent_saisie__data=db.relationship("Expert", 
        primaryjoin=(cell_planif_ref_agent_saisie  == Expert.id),
        backref=db.backref('cell_planif_ref_agent_saisie__data',  uselist=False),  uselist=False)

    com_cell_planif_ref_agent_saisie = db.Column(db.DECIMAL(65,2),default=0.00)

    prix_autre= db.Column(db.String,default='')
    commentaire_libre= db.Column(db.String,default='')
    date=db.Column(db.DateTime(),default=datetime.utcnow)
    visibility =db.Column(db.Boolean,default=True)
    
    


    def __repr__(self):
        return '<Tarifs %r>' %self.id

class Mission(db.Model):
    __table_args__ = {'extend_existing': True}

    __tablename__ = 'Mission'

    id = db.Column(db.Integer,primary_key=True)
    Reference_BAILLEUR	= db.Column(db.Integer, ForeignKey('Client.id', onupdate="CASCADE", ondelete="CASCADE"))   
    old= db.Column(db.String,default='')
    Bailleur__data=db.relationship("Client", 
        primaryjoin=(Reference_BAILLEUR == Client.id),
        backref=db.backref('Bailleur__data',  uselist=False),  uselist=False)
    NRO_FACTURE	 = db.Column(db.String,default='')#try putting facture as foreign key,think
    ABONNEMENT	 = db.Column(db.String,default='')
    ID_AS	 = db.Column(db.Integer, ForeignKey('Expert.id', onupdate="CASCADE", ondelete="CASCADE")) 
    AS__data=db.relationship("Expert", 
        primaryjoin=(ID_AS == Expert.id),
        backref=db.backref('CONCESS__data',  uselist=False),  uselist=False)
    PRIX_HT_EDL	 = db.Column(db.DECIMAL(65,2),default=0.00)  
    DATE_REALISE_EDL =db.Column(db.DateTime(),default=datetime.utcnow) 	
    ID_INTERV = db.Column(db.Integer, ForeignKey('Expert.id', onupdate="CASCADE", ondelete="CASCADE")) 
    INTERV__data=db.relationship("Expert", 
        primaryjoin=(ID_INTERV == Expert.id),
        backref=db.backref('INTERV__data',  uselist=False),  uselist=False)	
    Reference_LOCATAIRE	 =  db.Column(db.String,default='') 
    Adresse1_Bien	 = db.Column(db.String,default='')  
    Adresse2_Bien	 = db.Column(db.String,default='') 
    CP_Bien	 = db.Column(db.Integer)  
    Ville_Bien	 = db.Column(db.String,default='')  
    TVA_EDL = db.Column(db.DECIMAL(65,2),default=0.00)
    PRIX_TTC_EDL = db.Column(db.DECIMAL(65,2),default=0.00)#float
    CA_HT_AS = db.Column(db.DECIMAL(65,2),default=0.00) #float	
    TVA_AS	 = db.Column(db.DECIMAL(65,2),default=0.00) #float
    CA_TTC_AS = db.Column(db.DECIMAL(65,2),default=0.00) #float	
    CA_HT_AC = db.Column(db.DECIMAL(65,2),default=0.00) #float	
    CA_TTC_AC	 = db.Column(db.DECIMAL(65,2),default=0.00) #float
    CA_HT_TRUST	 = db.Column(db.DECIMAL(65,2),default=0.00) #float
    TVA_TRUST	 = db.Column(db.DECIMAL(65,2),default=0.00) #float
    Date_chiffrage_regle = db.Column(db.DateTime(),default=None) 
    Prix_ht_chiffrage	 = db.Column(db.DECIMAL(65,2),default=0.00) 
    POURCENTAGE_suiveur_chiffrage	 = db.Column(db.DECIMAL(65,2),default=0.00) #float
    POURCENTAGE_AS_chiffrage = db.Column(db.DECIMAL(65,2),default=0.00) 	#float
    POURCENTAGE_manager_chiffrage  = db.Column(db.DECIMAL(65,2),default=0.00) #float	
    ID_manager_chiffrage  = db.Column(db.Integer, ForeignKey('Expert.id', onupdate="CASCADE", ondelete="CASCADE"), nullable=True) 
    manager_chiffrage__data=db.relationship("Expert", 
        primaryjoin=(ID_manager_chiffrage == Expert.id),
        backref=db.backref('manager_chiffrage__data',  uselist=False),  uselist=False)	
    POURCENTAGE_agent_chiffrage = db.Column(db.DECIMAL(65,2),default=0.00) 	#float
    ID_agent_chiffrage  = db.Column(db.Integer, ForeignKey('Expert.id', onupdate="CASCADE", ondelete="CASCADE"), nullable=True) 	
    agent_chiffrage__data=db.relationship("Expert", 
        primaryjoin=(ID_agent_chiffrage == Expert.id),
        backref=db.backref('agent_chiffrage__data',  uselist=False),  uselist=False)
    TYPE_EDL = db.Column(db.String,default='') 	
    DATE_FACTURE = db.Column(db.DateTime(),default=None) # db.Column(db.DateTime())
    TITREPROPRIO = db.Column(db.String,default='') 		
    NOMPROPRIO = db.Column(db.String,default='') 	
    DATE_FACT_REGLEE = db.Column(db.DateTime(),default=None) 	
    TYPE_LOGEMENT = db.Column(db.String,default='') 	
    CODE_AMEXPERT = db.Column(db.String,default='') 	
    COMMENTAIRE_FACTURE = db.Column(db.String,default='') 	 	
    LOGEMENT_MEUBLE = db.Column(db.String,default='') 	
    CODE_FACTURATION = db.Column(db.String,default='') 	
    TYPE_DE_BIEN = db.Column(db.String,default='') 	
    surface_logement1 = db.Column(db.DECIMAL(65,2),default=0.00) 	#float	
    Ref_commande = db.Column(db.String,default='') 	
    POURCENTAGE_COM_AS_DU_CLIENT = db.Column(db.DECIMAL(65,2),default=0.00) 	#float
    ID_Respon_Cell_Dev	 = db.Column(db.Integer, ForeignKey('Expert.id', onupdate="CASCADE", ondelete="CASCADE"), nullable=True) 
    Respon_Cell_Dev__data=db.relationship("Expert", 
        primaryjoin=(ID_Respon_Cell_Dev == Expert.id),
        backref=db.backref('Respon_Cell_Dev__data',  uselist=False),  uselist=False)
    POURCENTAGE_Respon_Cell_Dev = db.Column(db.DECIMAL(65,2),default=0.00) 	#float
    ID_agent_Cell_Dev = db.Column(db.Integer, ForeignKey('Expert.id', onupdate="CASCADE", ondelete="CASCADE"), nullable=True) 	
    agent_Cell_Dev__data=db.relationship("Expert", 
        primaryjoin=(ID_agent_Cell_Dev == Expert.id),
        backref=db.backref('agent_Cell_Dev__data',  uselist=False),  uselist=False)
    POURCENTAGE_Agent_Cell_Dev = db.Column(db.DECIMAL(65,2),default=0.00) 	#float
    ID_Agent_CellTech = db.Column(db.Integer, ForeignKey('Expert.id', onupdate="CASCADE", ondelete="CASCADE"), nullable=True)  	
    Agent_CellTech__data=db.relationship("Expert", 
        primaryjoin=(ID_Agent_CellTech == Expert.id),
        backref=db.backref('Agent_CellTech__data',  uselist=False),  uselist=False)
    POURCENTAGE_Agent_Cell_Tech = db.Column(db.DECIMAL(65,2),default=0.00) 	#float
    ID_Respon_Cell_Tech = db.Column(db.Integer, ForeignKey('Expert.id', onupdate="CASCADE", ondelete="CASCADE"), nullable=True) #######
    Respon_Cell_Tech__data=db.relationship("Expert", 
        primaryjoin=(ID_Respon_Cell_Tech == Expert.id),
        backref=db.backref('Respon_Cell_Tech__data',  uselist=False),  uselist=False)	
    POURCENTAGE_Respon_Cell_Tech = db.Column(db.DECIMAL(65,2),default=0.00) #float	
    ID_Suiveur_Cell_Tech  = db.Column(db.Integer, ForeignKey('Expert.id', onupdate="CASCADE", ondelete="CASCADE"), nullable=True) 
    Suiveur_Cell_Tech__data=db.relationship("Expert", 
        primaryjoin=(ID_Suiveur_Cell_Tech == Expert.id),
        backref=db.backref('Suiveur_Cell_Tech__data',  uselist=False),  uselist=False)
    POURCENTAGE_Suiveur_Cell_Tech	 = db.Column(db.DECIMAL(65,2),default=0.00) #float
    ID_Respon_Cell_Planif = db.Column(db.Integer, ForeignKey('Expert.id', onupdate="CASCADE", ondelete="CASCADE"), nullable=True) 
    Respon_Cell_Planif__data=db.relationship("Expert", 
        primaryjoin=(ID_Respon_Cell_Planif == Expert.id),
        backref=db.backref('Respon_Cell_Planif__data',  uselist=False),  uselist=False)
    POURCENTAGE_Respon_Cell_Planif  = db.Column(db.DECIMAL(65,2),default=0.00) 	#float
    ID_Suiveur_Cell_Planif  = db.Column(db.Integer, ForeignKey('Expert.id', onupdate="CASCADE", ondelete="CASCADE"), nullable=True) 
    Suiveur_Cell_Planif__data=db.relationship("Expert", 
        primaryjoin=(ID_Suiveur_Cell_Planif == Expert.id),
        backref=db.backref('Suiveur_Cell_Planif__data',  uselist=False),  uselist=False)
    POURCENTAGE_Suiveur_Cell_Planif	 = db.Column(db.DECIMAL(65,2),default=0.00) #float
    ID_Agent_saisie_Cell_Planif  = db.Column(db.Integer, ForeignKey('Expert.id', onupdate="CASCADE", ondelete="CASCADE"), nullable=True)
    Agent_saisie_Cell_Planif__data=db.relationship("Expert", 
        primaryjoin=(ID_Agent_saisie_Cell_Planif == Expert.id),
        backref=db.backref('Agent_saisie_Cell_Planif__data',  uselist=False),  uselist=False)  	
    POURCENTAGE_Agent_saisie_CEll_planif  = db.Column(db.DECIMAL(65,2),default=0.00) #float

    Anomalie  = db.Column(db.Boolean,default=False)
    appli =db.Column(db.Boolean,default=False)
    Facex  = db.Column(db.Boolean,default=False)
    coherent  = db.Column(db.Boolean,default=True)
    reason = db.Column(db.String,default='')
    Visibility =db.Column(db.Boolean,default=True)
    

    
    


    def __repr__(self):
        return '<Mission %r>' %self.id

class facturation_client(db.Model):
    __table_args__ = {'extend_existing': True}

    __tablename__ = 'facturation_client'

    id = db.Column(db.Integer,primary_key=True)
    n_facture = db.Column(db.String,default='')   
    Montant_HT = db.Column(db.DECIMAL(65,2),default=0.00)
    client	= db.Column(db.Integer, ForeignKey('Client.id', onupdate="CASCADE", ondelete="CASCADE"))   
    client__data_=db.relationship("Client", 
        primaryjoin=(client == Client.id),
        backref=db.backref('client__data_',  uselist=False),  uselist=False)
    Date_de_creation=db.Column(db.DateTime(),default=datetime.utcnow)
    Date_mission=db.Column(db.DateTime())
    Date_reglement_client=db.Column(db.String,default='')
    missions_s=db.Column(db.String,default='')
    missions_f=db.Column(db.String,default='')
    Statut=db.Column(db.String,default='') #(payé ou en attente) differentes types de satus
    Observations_suivi_paiement=db.Column(db.String,default='')
    Date_première_relance=db.Column(db.String,default='') # date cree plus 15 jr
    Date_seconde_relance=db.Column(db.String,default='') # date cree plus seconde relance plus 15 jr
    Date_mise_en_demeure=db.Column(db.String,default='') # date seconde plus 15jr
    valide=db.Column(db.Boolean,default=False)
    visibility =db.Column(db.Boolean,default=True)
#valider=db.Column(db.Boolean,default=False)

    def __repr__(self):
        return '<facturation_client %r>' %self.id

class facturation_mission(db.Model):
    __table_args__ = {'extend_existing': True}

    __tablename__ = 'facturation_mission'

    id = db.Column(db.Integer,primary_key=True)
    ref_mission = db.Column(db.Integer, ForeignKey('Mission.id', onupdate="CASCADE", ondelete="CASCADE")) 
    fact_mission = db.Column(db.Integer, ForeignKey('facturation_client.id', onupdate="CASCADE", ondelete="CASCADE"))
    mission__data_=db.relationship("Mission", 
        primaryjoin=(ref_mission == Mission.id),
        backref=db.backref('mission__data_',  uselist=False),  uselist=False)
    facturation_client__data_=db.relationship("facturation_client", 
        primaryjoin=(fact_mission == facturation_client.id),
        backref=db.backref('facturation_client__data_',  uselist=False),  uselist=False)
    
    visibility =db.Column(db.Boolean,default=True)

    def __repr__(self):
        return '<facturation_mission %r>' %self.id

class Facturation_history(db.Model):
    __table_args__ = {'extend_existing': True}

    __tablename__ = 'Facturation_history'

    id = db.Column(db.Integer,primary_key=True)
    date=db.Column(db.DateTime())
    mission = db.Column(db.Integer, ForeignKey('Mission.id', onupdate="CASCADE", ondelete="CASCADE"))
    facture = db.Column(db.Integer, ForeignKey('facturation_client.id', onupdate="CASCADE", ondelete="CASCADE"))
    mission__data=db.relationship("Mission", 
        primaryjoin=(mission == Mission.id),
        backref=db.backref('mission__data',  uselist=False),  uselist=False)
    facturation_client__data=db.relationship("facturation_client", 
        primaryjoin=(facture == facturation_client.id),
        backref=db.backref('facturation_client__data',  uselist=False),  uselist=False)
    done=db.Column(db.DateTime(),default=datetime.utcnow)
    visibility =db.Column(db.Boolean,default=True)


    def __repr__(self):
        return '<Facturation_history %r>' %self.id
    
class compte_mensuel(db.Model):
    __table_args__ = {'extend_existing': True}

    __tablename__ = 'compte_mensuel'
    id = db.Column(db.Integer,primary_key=True)
    mission = db.Column(db.Integer, ForeignKey('Mission.id', onupdate="CASCADE", ondelete="CASCADE"))
    facture = db.Column(db.String,default='')
    intervenant=db.Column(db.String,default='')
    date_cmpte_mensuel=db.Column(db.DateTime())
    date_generation= db.Column(db.DateTime())
    date_envoie_Facture=db.Column(db.DateTime())
    prix_mission=db.Column(db.DECIMAL(65,2),default=0.00)
    commission_ac =db.Column(db.DECIMAL(65,2),default=0.00)
    etat= db.Column(db.Boolean)#(En contrôle/Non acquitté)
    anomalie=db.Column(db.Boolean)
    total=db.Column(db.DECIMAL(65,2),default=0.00)
    releve=db.Column(db.DECIMAL(65,2),default=0.00)
    mission__data=db.relationship("Mission", 
        primaryjoin=(mission == Mission.id),
        backref=db.backref('mission__cmpte',  uselist=False),  uselist=False)
	
    def __repr__(self):
        return '<compte_mensuel %r>' %self.id
    
class Type_expert(db.Model):
    __table_args__ = {'extend_existing': True}

    __tablename__ = 'Type_expert'
    id = db.Column(db.Integer,primary_key=True)
    type_ex = db.Column(db.String,default='')
    type_releve=db.Column(db.Integer)
    pourcentage =db.Column(db.DECIMAL(65,2),default=0.00)
    
    def __repr__(self):
        return '<Type_expert %r>' %self.id

class expert_facturation(db.Model):
    __table_args__ = {'extend_existing': True}

    __tablename__ = 'expert_facturation'
    id = db.Column(db.Integer,primary_key=True)
    facture = db.Column(db.String,default='')
    mission = db.Column(db.Integer, ForeignKey('compte_mensuel.id', onupdate="CASCADE", ondelete="CASCADE"))
    expert_id= db.Column(db.Integer, ForeignKey('Expert.id', onupdate="CASCADE", ondelete="CASCADE"))
    type_expert = db.Column(db.Integer, ForeignKey('Type_expert.id', onupdate="CASCADE", ondelete="CASCADE"))
    commision=db.Column(db.DECIMAL(65,2),default=0.00)
    date_retrait_facture=db.Column(db.DateTime(),default=None)
    anomalie=db.Column(db.Boolean)
    envoye=db.Column(db.Boolean,default=False)  #(True/False)
    mission__data=db.relationship("compte_mensuel", 
            primaryjoin=(mission == compte_mensuel.id),
            backref=db.backref('mission__expert',  uselist=False),  uselist=False)
    releve_data=db.relationship("Type_expert", 
            primaryjoin=(type_expert == Type_expert.id),
            backref=db.backref('releve_data',  uselist=False),  uselist=False)
    expert_data=db.relationship("Expert", 
        primaryjoin=(expert_id == Expert.id),
        backref=db.backref('expert_data',  uselist=False),  uselist=False)
	
    def __repr__(self):
        return '<expert_facturation %r>' %self.id 

    




	

    
	
	
	
	


