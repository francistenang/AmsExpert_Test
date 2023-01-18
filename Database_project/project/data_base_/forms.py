from flask_wtf import FlaskForm,RecaptchaField, Recaptcha
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SelectField, IntegerField,DecimalField,TextAreaField,HiddenField
from wtforms.validators import DataRequired,length,Email,EqualTo,ValidationError,Optional,NumberRange
from Database_project.project.data_base_.Models import Expert ,Client,Tarif_base,Client_negotiateur,prospect
from wtforms.fields.html5 import DateField
from sqlalchemy import or_, and_, desc,asc
from flask import Flask,render_template,url_for,flash,redirect,request,Blueprint
from datetime import date,timedelta,datetime,timezone 
import wtforms.validators as validators




 #bitvicessh
def validatep(self,email):
        try :
            int(email.data)
        except:
            raise ValidationError("Le numero n'a pas ete bien saisie")

def validates(self,email):
        try :
            int(email.data)
            
        except:
            raise ValidationError("Le numero n'a pas ete bien saisie")

def validatei(self,email):
        a=str(email.data)
        if len(a) < 5 or len(a)>5:
            
            raise ValidationError("5 chiffres")

class RegistrationForm1(FlaskForm):
    def validate2(self,email,expert):
        email = Expert.query.filter(and_(Expert.email==email,Expert.id!=expert)).first()
      
        if email:
            return True

    nom =StringField("Nom * ", validators=[validators.InputRequired(),length(min=4 ,max=20)])

    prenom =StringField("Prénom *", validators=[validators.InputRequired(),length(min=4 ,max=20)])

    
    login =StringField("Identifiant *" , validators=[validators.InputRequired(),Email() ])

    email =StringField('E-mail *',render_kw={'readonly':True} ,validators=[validators.InputRequired(),Email() ])

    submit = SubmitField('Enregistrer')

class rectify_Form(FlaskForm):
    
    TYPE_LOGEMENT =  StringField("TYPE_LOGEMENT",
                        validators=[validators.InputRequired()])	

    CODE_FACTURATION =StringField("CODE_FACTURATION",
                        validators=[validators.InputRequired()])  	

    submit = SubmitField('Modifier')

class mission_export(FlaskForm):
    
    Temps =  SelectField('Saison Export',
                             choices=[('Semaine', 'Semaine'), ('Mois', 'Mois'),('Jour','Jour')])

    Date =DateField('Date Export',
                    format='%Y-%m-%d',
                    validators=[validators.InputRequired()]
                   )  	

    submit = SubmitField('Exporter')

    #def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
    '''def val(self,val):
        if not self.Date.data:
            now_utc = datetime.now(timezone.utc)
            start=datetime.combine(now_utc,datetime.min.time())
            self.Date.data = val'''

class RegistrationForm(FlaskForm):
    def validate_email(self,email):
        email = Expert.query.filter_by(email=email.data).first()

        if email:
            raise ValidationError('Cet e-mail est déjà utilisé par un autre utilisateur')

    def validate_username(self,username): 
        user = Expert.query.filter_by(nom=username.data).first()

        if user:
            raise ValidationError("Ce nom d'utilisateur est pris. Veuillez choisir un autre nom")

    username =StringField("Identifiant *",
                                validators=[validators.InputRequired(),length(min=4 ,max=20)])
    
    Numero =StringField('Téléphone portable *',
                                validators=[validators.InputRequired(),validatep,length(min=10 ,max=10)])

    email =StringField('E-mail *',
                           validators=[validators.InputRequired(),Email(),validate_email])

    password =PasswordField('Mot de passe',
                                  validators=[length(min=8 ,max=20)])

    confirm_password =PasswordField('Confirmer le mot de passe',
                                  validators=[EqualTo('password')])
    
    email_perso =StringField('E-mail perso *' ,validators=[validators.InputRequired()])

    Type_Expert=SelectField('Type d\'expert',
                             choices=[('Interv', 'Interv'), ('CONCESS', 'CONCESS'), ('agent Cell Dev', 'agent Cell Dev'),('Interv', 'Interv'),('Suiveur Cell Tech', 'Suiveur Cell Tech'),('Suiveur Cell Planif', 'Suiveur Cell Planif'),('Admin', 'Admin'),('Audit', 'Audit')])

    Sexe=SelectField('Titre',
                             choices=[('MME', 'MME'), ('M.', 'M.')])
    
    secteur =StringField('Secteur')


    siret =IntegerField('siret *', validators=[validators.InputRequired()])

    trigramme =StringField('trigramme')

    code_tva =StringField('Code TVA')
                        
    taux_tva =DecimalField('Taux TVA', validators=[validators.InputRequired()])

    actif_parti =SelectField('actif_parti',
                             choices=[('ACTIF', 'ACTIF'), ('PARTI', 'PARTI')])

    ville =StringField('Ville')
    
    #type_certification=StringField('Type certification',
    #                       validators=[validators.InputRequired()])
   # date_certification=DateField('Date de certification',
    #                       validators=[validators.InputRequired()])
    #date_certification_renouv=DateField('Date de recertification')
    adresse=StringField('Adresse 1')

    adresse2=StringField('Adresse 2')

    cp=IntegerField('CP')
    login_google=StringField('Login google')
    pwd_google=StringField('Pwd google')
    login_backof=StringField('Login Backof')
    pwd_backof=StringField('Pwd Backof') #endeavour to hash all passwords
    login_extranet=StringField('Login Extranet')
    pwd_extranet=StringField('Pwd Etranet')
    pwd_gsuite=StringField('Pwd Gsuite')
    Expert_id=HiddenField()
    observations_de_suivi=StringField('Observations de suivi')

    submit = SubmitField('Enregistrer')

    modifier = SubmitField('Modifier')
    


class Expert_editForm(FlaskForm):
    def validate2(self,email,expert):
        email = Expert.query.filter(and_(Expert.email==email,Expert.id!=expert)).first()

        if email:
            return True

    username =StringField("Identifiant")
                                #validators=[validators.InputRequired(),length(min=4 ,max=20)])
    
    Numero =IntegerField('Téléphone portable',
                                validators=[validators.InputRequired()])#,validatep,length(min=9 ,max=9)])

    email =StringField('E-mail')

    email_perso =StringField('E-mail perso')


    Sexe=SelectField('Titre',
                             choices=[('MME', 'MME'), ('M.', 'M.')])


    #Type =SelectField('Type',
     #                        choices=[('Interv', 'Interv'), ('CONCESS', 'CONCESS'), ('agent Cell Dev', 'agent Cell Dev'),('Interv', 'Interv'),('Suiveur Cell Tech', 'Suiveur Cell Tech'),('Suiveur Cell Planif', 'Suiveur Cell Planif'),('Admin', 'Admin'),('Audit', 'Audit')])


    secteur =StringField('Secteur')


    siret =IntegerField('siret', validators=[validators.InputRequired()])

    trigramme =StringField('Trigramme')

    code_tva =StringField('Code TVA')
                        
    taux_tva =DecimalField('Taux TVA', validators=[validators.InputRequired()])

    actif_parti =SelectField('Actif parti',
                             choices=[('ACTIF', 'ACTIF'), ('PARTI', 'PARTI')])

    ville =StringField('Ville')
    
   # type_certification=StringField('Type certification',
    #                       validators=[validators.InputRequired()])
    #date_certification=DateField('Date de certification',
    #                       validators=[validators.InputRequired()])
    #date_certification_renouv=DateField('Date de recertification')
    
    date_entree=StringField('Date de entree',render_kw={'readonly':True})


    #mdp=DateField('Date de sortie')

    adresse=StringField('Adresse 1')

    adresse2=StringField('Adresse 2')

    cp=IntegerField('Code Postal', validators=[validators.InputRequired()])
    login_google=StringField('Login google')
    pwd_google=StringField('Pwd Google')
    login_backof=StringField('Login Backof')
    pwd_backof=StringField('Pwd Backof') #endeavour to hash all passwords
    login_extranet=StringField('Login Extranet')
    pwd_extranet=StringField('Pwd Extranet')
    pwd_gsuite=StringField('Pwd Gsuite')
    Expert_id=HiddenField()
    observations_de_suivi=StringField('Observations de suivi')

    modifier = SubmitField('Modifier')

class RequestResetForm(FlaskForm):
    email =StringField('Email',
                           validators=[validators.InputRequired(),Email()])
    submit = SubmitField('Request Password Reset')

    #recaptcha = RecaptchaField(validators=[Recaptcha(message="Le reCAPTCHA n'a pas été saisi correctement. Revenez en arrière et essayez à nouveau.")])

    def validate_username(self,username):
        user = Expert.query.filter_by(EMAIL=email.data).first()## add visibility

        if user is None:
            raise ValidationError('There is no account with this email.You must register first.')

class ResetPasswordForm(FlaskForm):
    password =PasswordField('Mot de Passe',
                                  validators=[validators.InputRequired(),length(min=8 ,max=20)])
    confirm_password =PasswordField('Confirmez votre Mot de Passe',
                                  validators=[validators.InputRequired(),EqualTo('password')])
    submit = SubmitField('Réinitialiser le mot de passe')
class LoginForm(FlaskForm):
    username =StringField("Identifiant",
                                     validators=[validators.InputRequired(),length(min=4 ,max=20, message='Le champ est obligatoire')])

    password =PasswordField('Mot de passe',
                                  validators=[validators.InputRequired(),length(min=4 ,max=20, message="Le champ doit comporter entre 4 et 20 caractères.")])
    
    recaptcha = RecaptchaField(validators=[Recaptcha(message="Le reCAPTCHA n'a pas été saisi correctement. Revenez en arrière et essayez à nouveau.")])
    remember = BooleanField('Se rappeler de moi')                              
    submit = SubmitField('Se connecter')
    
class tableform(FlaskForm):
        table =StringField('table',validators=[validators.InputRequired()])

        submit = SubmitField('Recherchez')



class Tarif_Form(FlaskForm):
    def validate_email(self,email):
        email = Expert.query.filter_by(id=email.data).first()

        if email is None :
            raise ValidationError("Cette utilisateur n'existe pas, utilisé  un autre utilisateur")

    def validate_price_STD(self,edl_prix_std): 
            base = Tarif_base.query.filter(and_(Tarif_base.pav_appartement=='APPT',Tarif_base.Type=='STD')).first()
            if edl_prix_std.data== 0 or edl_prix_std.data == None:
                raise ValidationError("Veuillez mettre une bonne valeur") 

            if base.Prix_EDL>edl_prix_std.data:
               
                raise ValidationError("le tarif de base  STD es moin que le tarif normal "+str(base.Prix_EDL)+"€")
    def validate_price_F1(self,edl_appt_prix_f1): 
            base = Tarif_base.query.filter(and_(Tarif_base.pav_appartement=='APPT',Tarif_base.Type=='F1')).first()
            

            
            if edl_appt_prix_f1.data == 0 or edl_appt_prix_f1.data == None:

                raise ValidationError("Veuillez mettre une bonne valeur")

            if base.Prix_EDL>edl_appt_prix_f1.data:
                raise ValidationError("le tarif de base F1 es moin que le tarif normal "+str(base.Prix_EDL)+"€")

    def validate_price_F2(self,edl_appt_prix_f2): 
            base = Tarif_base.query.filter(and_(Tarif_base.pav_appartement=='APPT',Tarif_base.Type=='F2')).first()
            
            if edl_appt_prix_f2.data == 0 or edl_appt_prix_f2.data == None:
                 raise ValidationError("Veuillez mettre une bonne valeur")

            if base.Prix_EDL>edl_appt_prix_f2.data:
                raise ValidationError("le tarif de base F2 es moin que le tarif normal "+str(base.Prix_EDL)+"€")

    def validate_price_F3(self,edl_appt_prix_f3): 
            base = Tarif_base.query.filter(and_(Tarif_base.pav_appartement=='APPT',Tarif_base.Type=='F3')).first()
            
            if edl_appt_prix_f3.data == 0 or edl_appt_prix_f3.data == None:
                 raise ValidationError("Veuillez mettre une bonne valeur")

            if base.Prix_EDL>edl_appt_prix_f3.data:
                raise ValidationError("le tarif de base F3 es moin que le tarif normal "+str(base.Prix_EDL)+"€")

    def validate_price_F4(self,edl_appt_prix_f4): 
            base = Tarif_base.query.filter(and_(Tarif_base.pav_appartement=='APPT',Tarif_base.Type=='F4')).first()
            
            if edl_appt_prix_f4.data == 0 or edl_appt_prix_f4.data == None:
                 raise ValidationError("Veuillez mettre une bonne valeur")

            if base.Prix_EDL>edl_appt_prix_f4.data:
                raise ValidationError("le tarif de base F4 es moin que le tarif normal "+str(base.Prix_EDL)+"€")

    def validate_price_F5(self,edl_appt_prix_f5): 
            base = Tarif_base.query.filter(and_(Tarif_base.pav_appartement=='APPT',Tarif_base.Type=='F5')).first()
            
            if edl_appt_prix_f5.data == 0 or edl_appt_prix_f5.data ==None:
                 raise ValidationError("Veuillez mettre une bonne valeur")

            if base.Prix_EDL>edl_appt_prix_f5.data:
                raise ValidationError("le tarif de base F5 es moin que le tarif normal "+str(base.Prix_EDL)+"€")
    
    def validate_price_F6(self,edl_appt_prix_f6): 
            base = Tarif_base.query.filter(and_(Tarif_base.pav_appartement=='APPT',Tarif_base.Type=='F6')).first()
            
            if edl_appt_prix_f6.data == 0 or edl_appt_prix_f6.data ==None:
                 raise ValidationError("Veuillez mettre une bonne valeur")

            if base.Prix_EDL>edl_appt_prix_f6.data:
                raise ValidationError("le tarif de base F6 es moin que le tarif normal "+str(base.Prix_EDL)+"€")

#PRIX CHIFFRAGE APPARTEMENT
    def validate_chif_STD(self,chif_appt_prix_stu): 
            base = Tarif_base.query.filter(and_(Tarif_base.pav_appartement=='APPT',Tarif_base.Type=='STD')).first()
            
            if chif_appt_prix_stu.data == 0 or chif_appt_prix_stu.data ==None:
                 raise ValidationError("Veuillez mettre une bonne valeur")

            if base.Prix_EDL>chif_appt_prix_stu.data:
                raise ValidationError("le tarif de base  STD es moin aue le tarif normal "+str(base.Prix_EDL)+"€")
    
    def validate_chif_F1(self,chif_appt_prix_f1): 
            base = Tarif_base.query.filter(and_(Tarif_base.pav_appartement=='APPT',Tarif_base.Type=='F1')).first()
            
            if chif_appt_prix_f1.data == 0 or chif_appt_prix_f1.data ==None:
                 raise ValidationError("Veuillez mettre une bonne valeur")

            if base.Prix_EDL>chif_appt_prix_f1.data:
                raise ValidationError("le tarif de base F1 es moin que le tarif normal "+str(base.Prix_EDL)+"€")

    def validate_chif_F2(self,chif_appt_prix_f2): 
            base = Tarif_base.query.filter(and_(Tarif_base.pav_appartement=='APPT',Tarif_base.Type=='F2')).first()
            
            if chif_appt_prix_f2.data == 0 or chif_appt_prix_f2.data ==None:
                 raise ValidationError("Veuillez mettre une bonne valeur")

            if base.Prix_EDL>chif_appt_prix_f2.data:
                raise ValidationError("le tarif de base F2 es moin que le tarif normal "+str(base.Prix_EDL)+"€")

    def validate_chif_F3(self,chif_appt_prix_f3): 
            base = Tarif_base.query.filter(and_(Tarif_base.pav_appartement=='APPT',Tarif_base.Type=='F3')).first()
            
            if chif_appt_prix_f3.data == 0 or chif_appt_prix_f3.data ==None:
                 raise ValidationError("Veuillez mettre une bonne valeur")

            if base.Prix_EDL>chif_appt_prix_f3.data:
                raise ValidationError("le tarif de base F3 es moin que le tarif normal "+str(base.Prix_EDL)+"€")

    def validate_chif_F4(self,chif_appt_prix_f4): 
            base = Tarif_base.query.filter(and_(Tarif_base.pav_appartement=='APPT',Tarif_base.Type=='F4')).first()
            
            if chif_appt_prix_f4.data == 0 or chif_appt_prix_f4.data ==None:
                 raise ValidationError("Veuillez mettre une bonne valeur")

            if base.Prix_EDL>chif_appt_prix_f4.data:
                raise ValidationError("le tarif de base F4 es moin que le tarif normal "+str(base.Prix_EDL)+"€")

    def validate_chif_F5(self,chif_appt_prix_f5): 
            base = Tarif_base.query.filter(and_(Tarif_base.pav_appartement=='APPT',Tarif_base.Type=='F5')).first()
            
            if chif_appt_prix_f5.data == 0 or chif_appt_prix_f5.data ==None:
                 raise ValidationError("Veuillez mettre une bonne valeur")

            if base.Prix_EDL>chif_appt_prix_f5.data:
                raise ValidationError("le tarif de base F5 es moin que le tarif normal "+str(base.Prix_EDL)+"€")
    
    def validate_chif_F6(self,chif_appt_prix_f6): 
            base = Tarif_base.query.filter(and_(Tarif_base.pav_appartement=='APPT',Tarif_base.Type=='F6')).first()
            
            if chif_appt_prix_f6.data == 0 or chif_appt_prix_f6.data ==None:
                 raise ValidationError("Veuillez mettre une bonne valeur")

            if base.Prix_EDL>chif_appt_prix_f6.data:
                raise ValidationError("le tarif de base F6 es moin que le tarif normal "+str(base.Prix_EDL)+"€")

    
#PRICE VILLA
    def validate_price_T1(self,edl_pav_villa_prix_t1): 
            base = Tarif_base.query.filter(and_(Tarif_base.pav_appartement=='PAV',Tarif_base.Type=='T1')).first()
            
            if edl_pav_villa_prix_t1.data == 0 or edl_pav_villa_prix_t1.data == None:
                 raise ValidationError("Veuillez mettre une bonne valeur")

            if base.Prix_EDL>edl_pav_villa_prix_t1.data:
                raise ValidationError("le tarif de base T1 es moin que le tarif normal "+str(base.Prix_EDL)+"€")

    def validate_price_T2(self,edl_pav_villa_prix_t2): 
            base = Tarif_base.query.filter(and_(Tarif_base.pav_appartement=='PAV',Tarif_base.Type=='T2')).first()
            
            if edl_pav_villa_prix_t2.data == 0 or edl_pav_villa_prix_t2.data == None:
                 raise ValidationError("Veuillez mettre une bonne valeur")

            if base.Prix_EDL>edl_pav_villa_prix_t2.data:
                raise ValidationError("le tarif de base T2 es moin que le tarif normal "+str(base.Prix_EDL)+"€")

    def validate_price_T3(self,edl_pav_villa_prix_t3): 
            base = Tarif_base.query.filter(and_(Tarif_base.pav_appartement=='PAV',Tarif_base.Type=='T3')).first()
            
            if edl_pav_villa_prix_t3.data == 0 or edl_pav_villa_prix_t3.data == None:
                 raise ValidationError("Veuillez mettre une bonne valeur")

            if base.Prix_EDL>edl_pav_villa_prix_t3.data:
                raise ValidationError("le tarif de base T3 es moin que le tarif normal "+str(base.Prix_EDL)+"€")

    def validate_price_T4(self,edl_pav_villa_prix_t4): 
            base = Tarif_base.query.filter(and_(Tarif_base.pav_appartement=='PAV',Tarif_base.Type=='T4')).first()
            
            if edl_pav_villa_prix_t4.data == 0 or edl_pav_villa_prix_t4.data == None:
                 raise ValidationError("Veuillez mettre une bonne valeur")

            if base.Prix_EDL>edl_pav_villa_prix_t4.data:
                raise ValidationError("le tarif de base T4 es moin que le tarif normal "+str(base.Prix_EDL)+"€")

    def validate_price_T5(self,edl_pav_villa_prix_t5): 
            base = Tarif_base.query.filter(and_(Tarif_base.pav_appartement=='PAV',Tarif_base.Type=='T5')).first()
            
            if edl_pav_villa_prix_t5.data == 0 or edl_pav_villa_prix_t5.data == None:
                 raise ValidationError("Veuillez mettre une bonne valeur")

            if base.Prix_EDL>edl_pav_villa_prix_t5.data:
                raise ValidationError("le tarif de base T5 es moin que le tarif normal "+str(base.Prix_EDL)+"€")

    def validate_price_T6(self,edl_pav_villa_prix_t6): 
            base = Tarif_base.query.filter(and_(Tarif_base.pav_appartement=='PAV',Tarif_base.Type=='T6')).first()
            
            if edl_pav_villa_prix_t6.data == 0 or edl_pav_villa_prix_t6.data == None:
                 raise ValidationError("Veuillez mettre une bonne valeur")

            if base.Prix_EDL>edl_pav_villa_prix_t6.data:
                raise ValidationError("le tarif de base T6 es moin que le tarif normal "+str(base.Prix_EDL)+"€")

    
    def validate_price_T7(self,edl_pav_villa_prix_t7): 
            base = Tarif_base.query.filter(and_(Tarif_base.pav_appartement=='PAV',Tarif_base.Type=='T7')).first()
            
            if edl_pav_villa_prix_t7.data == 0 or edl_pav_villa_prix_t7.data == None:
                 raise ValidationError("Veuillez mettre une bonne valeur")

            if base.Prix_EDL>edl_pav_villa_prix_t7.data:
                raise ValidationError("le tarif de base T7 es moin que le tarif normal "+str(base.Prix_EDL)+"€")

    def validate_price_T8(self,edl_pav_villa_prix_t8): 
            base = Tarif_base.query.filter(and_(Tarif_base.pav_appartement=='PAV',Tarif_base.Type=='T8')).first()
            
            if edl_pav_villa_prix_t8.data == 0 or edl_pav_villa_prix_t8.data == None:
                 raise ValidationError("Veuillez mettre une bonne valeur")

            if base.Prix_EDL>edl_pav_villa_prix_t8.data:
                raise ValidationError("le tarif de base T8 es moin que le tarif normal "+str(base.Prix_EDL)+"€")

#Prix CHiffrage Pav
    def validate_chif_T1(self,chif_pav_villa_prix_t1): 
            base = Tarif_base.query.filter(and_(Tarif_base.pav_appartement=='PAV',Tarif_base.Type=='T1')).first()
            
            if chif_pav_villa_prix_t1.data == 0 or chif_pav_villa_prix_t1.data == None:
                 raise ValidationError("Veuillez mettre une bonne valeur")

            if base.Prix_EDL>chif_pav_villa_prix_t1.data:
                raise ValidationError("le tarif de base T1 es moin que le tarif normal "+str(base.Prix_EDL)+"€")

    def validate_chif_T2(self,chif_pav_villa_prix_t2): 
            base = Tarif_base.query.filter(and_(Tarif_base.pav_appartement=='PAV',Tarif_base.Type=='T2')).first()
            
            if chif_pav_villa_prix_t2.data == 0 or chif_pav_villa_prix_t2.data == None:
                 raise ValidationError("Veuillez mettre une bonne valeur")

            if base.Prix_EDL>chif_pav_villa_prix_t2.data:
                raise ValidationError("le tarif de base T2 es moin que le tarif normal "+str(base.Prix_EDL)+"€")

    def validate_chif_T3(self,chif_pav_villa_prix_t3): 
            base = Tarif_base.query.filter(and_(Tarif_base.pav_appartement=='PAV',Tarif_base.Type=='T3')).first()
            
            if chif_pav_villa_prix_t3.data == 0 or chif_pav_villa_prix_t3.data == None:
                 raise ValidationError("Veuillez mettre une bonne valeur")

            if base.Prix_EDL>chif_pav_villa_prix_t3.data:
                raise ValidationError("le tarif de base T3 es moin que le tarif normal "+str(base.Prix_EDL)+"€")

    def validate_chif_T4(self,chif_pav_villa_prix_t4): 
            base = Tarif_base.query.filter(and_(Tarif_base.pav_appartement=='PAV',Tarif_base.Type=='T4')).first()
            
            if chif_pav_villa_prix_t4.data == 0 or chif_pav_villa_prix_t4.data == None:
                 raise ValidationError("Veuillez mettre une bonne valeur")

            if base.Prix_EDL>chif_pav_villa_prix_t4.data:
                raise ValidationError("le tarif de base T4 es moin que le tarif normal "+str(base.Prix_EDL)+"€")

    def validate_chif_T5(self,chif_pav_villa_prix_t5): 
            base = Tarif_base.query.filter(and_(Tarif_base.pav_appartement=='PAV',Tarif_base.Type=='T5')).first()
            
            if chif_pav_villa_prix_t5.data == 0 or chif_pav_villa_prix_t5.data == None:
                 raise ValidationError("Veuillez mettre une bonne valeur")

            if base.Prix_EDL>chif_pav_villa_prix_t5.data:
                raise ValidationError("le tarif de base T5 es moin que le tarif normal "+str(base.Prix_EDL)+"€")

    def validate_chif_T6(self,chif_pav_villa_prix_t6): 
            base = Tarif_base.query.filter(and_(Tarif_base.pav_appartement=='PAV',Tarif_base.Type=='T6')).first()
            
            if chif_pav_villa_prix_t6.data == 0 or chif_pav_villa_prix_t6.data == None:
                 raise ValidationError("Veuillez mettre une bonne valeur")

            if base.Prix_EDL>chif_pav_villa_prix_t6.data:
                raise ValidationError("le tarif de base T6 es moin que le tarif normal "+str(base.Prix_EDL)+"€")

    
    def validate_chif_T7(self,chif_pav_villa_prix_t7): 
            base = Tarif_base.query.filter(and_(Tarif_base.pav_appartement=='PAV',Tarif_base.Type=='T7')).first()
            
            if chif_pav_villa_prix_t7.data == 0 or chif_pav_villa_prix_t7.data == None:
                 raise ValidationError("Veuillez mettre une bonne valeur")

            if base.Prix_EDL>chif_pav_villa_prix_t7.data:
                raise ValidationError("le tarif de base T7 es moin que le tarif normal "+str(base.Prix_EDL)+"€")

    def validate_chif_T8(self,chif_pav_villa_prix_t8): 
            base = Tarif_base.query.filter(and_(Tarif_base.pav_appartement=='PAV',Tarif_base.Type=='T8')).first()
            
            if chif_pav_villa_prix_t8.data == 0 or chif_pav_villa_prix_t8.data == None:
                raise ValidationError("Veuillez mettre une bonne valeur")

            if base.Prix_EDL>chif_pav_villa_prix_t8.data:
                raise ValidationError("le tarif de base T8 es moin que le tarif normal "+str(base.Prix_EDL)+"€")

    edl_prix_std=DecimalField('EDL prix std', validators=[validators.InputRequired(),validate_price_STD])     
    edl_appt_prix_f1=DecimalField('EDL appt prix f1', validators=[validators.InputRequired(),validate_price_F1])
    edl_appt_prix_f2=DecimalField('EDL appt prix f2', validators=[validators.InputRequired(),validate_price_F2]) 
    edl_appt_prix_f3=DecimalField('EDL appt prix f3', validators=[validators.InputRequired(),validate_price_F3])
    edl_appt_prix_f4=DecimalField('EDL appt prix f4', validators=[validators.InputRequired(),validate_price_F4]) 
    edl_appt_prix_f5=DecimalField('EDL appt prix f5', validators=[validators.InputRequired(),validate_price_F5])
    edl_appt_prix_f6=DecimalField('EDL appt prix f6', validators=[validators.InputRequired(),validate_price_F6])
    edl_pav_villa_prix_t1=DecimalField('EDL pav villa prix t1', validators=[validators.InputRequired(),validate_price_T1])
    edl_pav_villa_prix_t2=DecimalField('EDL pav villa prix t2', validators=[validators.InputRequired(),validate_price_T2])
    edl_pav_villa_prix_t3=DecimalField('EDL pav villa prix t3', validators=[validators.InputRequired(),validate_price_T3])
    edl_pav_villa_prix_t4=DecimalField('EDL pav villa prix t4', validators=[validators.InputRequired(),validate_price_T4]) 
    edl_pav_villa_prix_t5=DecimalField('EDL pav villa prix t5', validators=[validators.InputRequired(),validate_price_T5])
    edl_pav_villa_prix_t6=DecimalField('EDL pav villa prix t6', validators=[validators.InputRequired(),validate_price_T6])
    edl_pav_villa_prix_t7=DecimalField('EDL pav villa prix t7', validators=[validators.InputRequired(),validate_price_T7]) 
    edl_pav_villa_prix_t8=DecimalField('EDL pav villa prix t8', validators=[validators.InputRequired(),validate_price_T8])
    chif_appt_prix_stu=DecimalField('CHIF appt prix stu', validators=[validators.InputRequired(),validate_chif_STD])
    chif_appt_prix_f1 =DecimalField('CHIF appt prix f1', validators=[validators.InputRequired(),validate_chif_F1]) 
    chif_appt_prix_f2 =DecimalField('CHIF appt prix f2', validators=[validators.InputRequired(),validate_chif_F2]) 
    chif_appt_prix_f3 =DecimalField('CHIF appt prix f3', validators=[validators.InputRequired(),validate_chif_F3]) 
    chif_appt_prix_f4 =DecimalField('CHIF appt prix f4', validators=[validators.InputRequired(),validate_chif_F4]) 
    chif_appt_prix_f5 =DecimalField('CHIF appt prix f5', validators=[validators.InputRequired(),validate_chif_F5]) 
    chif_appt_prix_f6 =DecimalField('CHIF appt prix f6', validators=[validators.InputRequired(),validate_chif_F6]) 
    chif_pav_villa_prix_t1=DecimalField('CHIF pav villa prix t1', validators=[validators.InputRequired(),validate_chif_T1])
    chif_pav_villa_prix_t2=DecimalField('CHIF pav villa prix t2', validators=[validators.InputRequired(),validate_chif_T2]) 
    chif_pav_villa_prix_t3=DecimalField('CHIF pav villa prix t3', validators=[validators.InputRequired(),validate_chif_T3])
    chif_pav_villa_prix_t4=DecimalField('CHIF pav villa prix t4', validators=[validators.InputRequired(),validate_chif_T4])
    chif_pav_villa_prix_t5=DecimalField('CHIF pav villa prix t5', validators=[validators.InputRequired(),validate_chif_T5])
    chif_pav_villa_prix_t6=DecimalField('CHIF pav villa prix t6', validators=[validators.InputRequired(),validate_chif_T6])
    chif_pav_villa_prix_t7=DecimalField('CHIF pav villa prix t7', validators=[validators.InputRequired(),validate_chif_T7]) 
    chif_pav_villa_prix_t8=DecimalField('CHIF pav villa prix t8', validators=[validators.InputRequired(),validate_chif_T8])
    prix_autre=StringField('Prix € autre', validators=[Optional()])

    code_tva= StringField('code TVA', validators=[Optional()])

    taux_meuble= IntegerField('Taux meuble', validators=[Optional()])

    referent_as_client= IntegerField('Referent as client', validators=[validators.InputRequired(),validate_email])

    com_as_sur_ca_client=DecimalField('Com as sur ca client', validators=[validators.InputRequired()])

    cell_dev_ref_responsable = IntegerField('Cell dev ref responsable', validators=[validators.InputRequired(),validate_email])

    com_cell_dev_ref_responsable = DecimalField('Com cell dev ref responsable', validators=[validators.InputRequired()])

    cell_dev_ref_agent = IntegerField('Cell dev ref agent', validators=[validators.InputRequired(),validate_email])

    com_cell_dev_ref_agent = DecimalField('Com cell dev ref agent', validators=[validators.InputRequired()])

    cell_tech_ref_agent = IntegerField('Cell tech ref agent', validators=[validators.InputRequired(),validate_email])

    com_cell_tech_Ref_agent = DecimalField('Com cell tech Ref agent', validators=[validators.InputRequired()])

    cell_tech_ref_responsable  = IntegerField('Cell tech ref responsable', validators=[validators.InputRequired(),validate_email])

    com_cell_tech_ref_responsable = DecimalField('Com cell tech ref responsable', validators=[validators.InputRequired()])

    cell_tech_ref_suiveur = IntegerField('Cell tech ref suiveur', validators=[validators.InputRequired(),validate_email])

    com_cell_tech_ref_suiveur  = DecimalField('Com cell tech ref suiveur', validators=[validators.InputRequired()])

    cell_planif_ref_responsable = IntegerField('Cell planif ref responsable', validators=[validators.InputRequired(),validate_email])

    com_cell_planif_ref_responsable = DecimalField('Com cell planif ref responsable', validators=[validators.InputRequired()])

    cell_planif_ref_suiveur = IntegerField('Cell planif ref suiveur', validators=[validators.InputRequired(),validate_email])

    com_cell_planif_ref_suiveur  =  DecimalField('Com cell planif ref suiveur', validators=[validators.InputRequired()])

    cell_planif_ref_agent_saisie  =  IntegerField('Cell planif ref agent saisie', validators=[validators.InputRequired(),validate_email])

    com_cell_planif_ref_agent_saisie  =  DecimalField('Com cell planif ref gent saisie', validators=[validators.InputRequired()])

    commentaire_libre = TextAreaField('Commentaire libre', validators=[Optional()])

    tafid =HiddenField()
    
    submit = SubmitField('Enregistrer')

    modifier = SubmitField('Modifier')

    
    
   


class Facturation_Form(FlaskForm):
    Reference_client=IntegerField('Reference client',
                           render_kw={'readonly':True})

    Demarrer=StringField('Demarrer',
                           render_kw={'readonly':True})

    Fin=StringField('Fin',
                           render_kw={'readonly':True})
    
    Montant_HT =StringField('Montant €HT',
                             render_kw={'readonly':True})


    Data=HiddenField()

    Missions=HiddenField()

    Mission =StringField('Mission ID',
                             render_kw={'readonly':True})

    
    Statut=SelectField('Statut',
                             choices=[('paye', 'paye'), ('attente', 'attente')])
    
    #Observations_suivi_paiement=SelectField('Type_',
                            # choices=[('Entrant', 'Entrant'), ('Sortant', 'Sortant')])


    submit = SubmitField('Enregistrer')

class Facturationex_Form(FlaskForm):
    
    Demarrer=StringField('Demarrer',
                           render_kw={'readonly':True})

    Fin=StringField('Fin',
                           render_kw={'readonly':True})
    
    Montant_HT =StringField('Montant €HT',
                             render_kw={'readonly':True})
    
    Total_HT =StringField('Total €HT',
                             render_kw={'readonly':True})


    Date_EDL=StringField('Date EDL',
                           render_kw={'readonly':True})
    Data=HiddenField()

    Missions=HiddenField()

    Mission =StringField('Mission ID',
                             render_kw={'readonly':True})

    
    Statut=SelectField('Statut',
                             choices=[('paye', 'paye'), ('attente', 'attente')])
    

    submit = SubmitField('Générer')


class Facturationind_Form(FlaskForm):

    Mission =StringField('Mission ID',
                             render_kw={'readonly':True})

    Montant_HT =DecimalField('Montant €HT')

    Date_EDL=StringField('Date EDL',
                           render_kw={'readonly':True})

    Statut=SelectField('Statut',
                             choices=[('paye', 'paye'), ('attente', 'attente')])

    submit = SubmitField('Facture')


class Client_Form(FlaskForm):
       
    Type=SelectField('Type',
                             choices=[ ('Particulier', 'Particulier'),('Professionnel', 'Professionnel')])

    Societe =StringField('Société',
                           validators=[validators.InputRequired()])

    Sexe=SelectField('Titre',
                             choices=[('Monsieur', 'Monsieur',), ('Madame', 'Madame'),('Maître', 'Maître'), ('Mr et Mme', 'Mr et Mme'),('Société', 'Société'), ('Mademoiselle', 'Mademoiselle')])



    nom = StringField('Nom *',  validators=[validators.InputRequired()])
    
    prenom = StringField('Prénom *',  validators=[validators.InputRequired()])
    email =StringField('E-mail',
                           validators=[validators.InputRequired(),Email()])

    Numero =StringField('Téléphone portable',
                           validators=[validatep,length(min=10 ,max=10)])

    Adresse1=StringField('Adresse1')
    
    Adresse2=StringField('Adresse2')

    CP=IntegerField('Code Postal',
                           validators=[validators.InputRequired(),validatei])
    
    Ville=StringField('Ville',
                           validators=[validators.InputRequired()])
    
    Siret=StringField('Siret',
                           validators=[validatep,length(min=14 ,max=14)])  

    Pays=SelectField("Pays ", choices=[('France', 'France'), ('Belgique', 'Belgique')],
                        validators=[validators.InputRequired()])

    Reference=IntegerField("Reference")
    
    Date_Creation=StringField("Date Creation",
                           render_kw={'readonly':True})

    EtatClient=SelectField("Etat Client", choices=[('Actif', 'Actif'), ('Parti', 'Parti')],
                        validators=[validators.InputRequired()])

    LoginExtranet = StringField("Login Extranet")

    MdpExtranet = StringField("MdpExtranet")


    Enseigne=StringField("Enseigne")

    submit = SubmitField('Enregistrer')

    modifier = SubmitField('Modifier')



    def validate_username(self,username):
        user = Client.query.filter_by(nom=username.data).first()

        if user:
            raise ValidationError("Ce nom d'utilisateur est pris. Veuillez choisir un autre nom")

    def validate_email(self,email):
        email = Client.query.filter_by(email=email.data).first()

        if email:
            raise ValidationError('Cet e-mail est déjà utilisé par un autre utilisateur')

class Client_edit(FlaskForm):

    def validate2(self,email,client):
        if email !='':
            email = Client.query.filter(and_(Client.email==email,Client.id!=client)).first()

            if email:
                return True
        
    def validate3(self,email,client):
        if email !='':
            email = prospect.query.filter(and_(prospect.email==email,prospect.id!=client)).first()

            if email:
                return True
    
    

    Type=SelectField('Type *',
                             choices=[('Professionnel', 'Professionnel'), ('Particulier', 'Particulier')],
                             validators=[validators.InputRequired()])

    Societe =StringField('Société *',validators=[validators.InputRequired(),length(min=4 ,max=20)])
                           #validators=[validators.InputRequired()])

    Sexe=SelectField('Titre *'
                            ,validators=[validators.InputRequired()]
                            ,choices=[('Monsieur', 'Monsieur',), ('Madame', 'Madame'),('Maître', 'Maître'), ('Mr et Mme', 'Mr et Mme'),('Société', 'Société'), ('Mademoiselle', 'Mademoiselle')])

    # NOM =StringField('Nom et prénom *',validators=[validators.InputRequired(),length(min=4 ,max=20)]) 
                           #validators=[validators.InputRequired()])
    nom = StringField('Nom *',validators=[validators.InputRequired(),length(min=4 ,max=20)])

    prenom = StringField('Prénom *',validators=[validators.InputRequired(),length(min=4 ,max=20)])

    email =StringField('E-mail *',validators=[validators.InputRequired(),length(min=4 ,max=20)])

    Numero =IntegerField('Téléphone portable *',validators=[validators.InputRequired()])
                           #validators=[validatep,length(min=9 ,max=9)])

    Adresse1=StringField('Adresse1 *',validators=[validators.InputRequired(),length(min=4 ,max=20)])
    
    Adresse2=StringField('Adresse2 *',validators=[validators.InputRequired(),length(min=4 ,max=20)])

    CP=IntegerField('Code Postal *',validators=[validators.InputRequired()])
                           #validators=[validatep,length(min=5 ,max=5)])
    
    Ville=StringField('Ville *',validators=[validators.InputRequired(),length(min=4 ,max=20)])
                           #validators=[validators.InputRequired()])
    
    Siret=IntegerField('Siret *')#,validatep,,validators=[validators.InputRequired()]])

    Pays=SelectField("Pays *", choices=[('France', 'France'), ('Belgique', 'Belgique')],
                        validators=[validators.InputRequired()])

    Reference=IntegerField('Reference *',validators=[validators.InputRequired()])
    
    Date_Creation=StringField("Date Creation",
                           render_kw={'readonly':True})

    EtatClient=SelectField("Etat du client *",validators=[validators.InputRequired(),length(min=4 ,max=20)],choices=[('Actif', 'Actif',), ('Inactif', 'Inactif')]) 
    
    LoginExtranet = StringField("Login Extranet *", validators=[validators.InputRequired(),length(min=4 ,max=20)], render_kw={'readonly':True})

    MdpExtranet = StringField("MdpExtranet *",validators=[validators.InputRequired(),length(min=4 ,max=20)], render_kw={'readonly':True})

    client_id = HiddenField()

    Enseigne=StringField("Enseigne *", validators=[validators.InputRequired(),length(min=4 ,max=20)])

    submit = SubmitField('Enregistrer')

    modifier = SubmitField('Modifier')



    def validate_username(self,username):
        user = Client.query.filter_by(nom=username.data).first()

        if user:
            raise ValidationError("Ce nom d'utilisateur est pris. Veuillez choisir un autre nom")


class Negotiateur_Form(FlaskForm):

    def nego(self,email,cont):
        if email !='':
            email = Client_negotiateur.query.filter(and_(Client_negotiateur.email==email,Client_negotiateur.id!=cont)).first()

            if email:
                return True
       

    Sexe=SelectField('Titre',
                             choices=[('Monsieur', 'Monsieur',), ('Madame', 'Madame'),('Maître', 'Maître'), ('Mr et Mme', 'Mr et Mme'), ('Mademoiselle', 'Mademoiselle')])

    NOM =StringField('Nom et prénom')
                           #validators=[validators.InputRequired()])
    
    email =StringField('E-mail')

    Numero =IntegerField('Téléphone portable',
                           validators=[validators.InputRequired()])

    Adresse=StringField('Adresse')

    CP=IntegerField('Code Postal',
                           validators=[validators.InputRequired()])
    
    Ville=StringField('Ville')
    
    client_id = HiddenField()

    Date_Creation=StringField("Date Creation",
                           render_kw={'readonly':True})

    Pays=SelectField("Pays ", choices=[('France', 'France'), ('Belgique', 'Belgique')])

    submit = SubmitField('Enregistrer')

    modifier = SubmitField('Modifier')



    def validate_username(self,username):
        user = Client_negotiateur.query.filter_by(nom=username.data).first()

        if user:
            raise ValidationError("Ce nom d'utilisateur est pris. Veuillez choisir un autre nom")

    
    

class Negotiateur_Form1(FlaskForm):  

    def validate_username(self,nom):
        user = Client_negotiateur.query.filter_by(nom=nom.data).first()

        if user:
            raise ValidationError("Ce nom d'utilisateur est pris. Veuillez choisir un autre nom")

    def validate_email(self,email):
        email = Client_negotiateur.query.filter_by(email=email.data).first()

        if email:
            raise ValidationError('Cet e-mail est déjà utilisé par un autre utilisateur')

  

    nom =StringField('Nom *',
                           validators=[validators.InputRequired(),validate_username])
    
    prenom =StringField('Prénom',
                           validators=[validators.InputRequired()])
    
    Sexe=SelectField('Sexe',  choices=[('Monsieur', 'Monsieur',), ('Madame', 'Madame'),('Maître', 'Maître'), ('Mr et Mme', 'Mr et Mme'), ('Mademoiselle', 'Mademoiselle')])

    email =StringField('E-mail',
                           validators=[validators.InputRequired(),Email(),validate_email])

    Numero =StringField('Téléphone portable',
                           validators=[validatep,length(min=10 ,max=10)])

    Adresse=StringField('Adresse')

    CP=IntegerField('Code Postal',
                           validators=[validators.InputRequired(),validatei])
    
    Ville=StringField('Ville')
    

    Pays=SelectField("Pays ", choices=[('France', 'France'), ('Belgique', 'Belgique')])

    submit = SubmitField('Enregistrer')

    modifier = SubmitField('Modifier')



    

class Suivi_Client(FlaskForm):
    def validate_email(self,email):
        email = Expert.query.filter(and_(Expert.trigramme==email.data,Expert.trigramme!='')).first() #.lower()

        if email is None:
            raise ValidationError("Cet expert n'existe pas veuillez ressaisir le trigramme")

    expert=StringField("Trigramme Expert",
                        validators=[validators.InputRequired(),validate_email])

    commentaire=StringField("Commentaire",
                        validators=[validators.InputRequired()])

    submit = SubmitField('Enregistrer')



class Mission_add(FlaskForm):
    def validate_email(self,email):
        email = Expert.query.filter_by(id=email.data).first()

        if email is None :
            raise ValidationError("Cette utilisateur n'existe pas, utilisé  un autre utilisateur")

    def validate_client(self,email):
        email = Client.query.filter_by(reference=email.data).first()

        if email is None :
            raise ValidationError("Cette utilisateur n'existe pas, utilisé  un autre utilisateur")


    Reference_client=IntegerField("Reference Client",
                        validators=[validators.InputRequired(),validate_client])

    ID_Concessionaire=IntegerField("ID Concessionaire",
                        validators=[validators.InputRequired(),validate_email])

    ABONNEMENT=StringField("ABONNEMENT")
    
    PRIX_HT_EDL=DecimalField("Prix €HT EDL",
                        validators=[validators.InputRequired()])
    
    DATE_REALISE_EDL=DateField("DATE REALISE EDL",
                        validators=[validators.InputRequired()])
    
    DATE_FACTURE=DateField("DATE FACTURE",render_kw={'readonly':True})

    NRO_FACTURE=StringField("NRO FACTURE",render_kw={'readonly':True})

    COMMENTAIRE_FACTURE=StringField("COMMENTAIRE FACTURE",render_kw={'readonly':True})
                        
    DATE_FACT_REGLEE =DateField("DATE FACT REGLEE",render_kw={'readonly':True})

    ID_INTERV=IntegerField("ID INTERV",
                        validators=[validators.InputRequired(),validate_email])
    
    Reference_LOCATAIRE=StringField("Reference Locataire")
    
    Adresse1_Bien=StringField("Adresse1 Bien")
    
    Adresse2_Bien=StringField("Adresse2 Bien")
      
    CP_Bien=IntegerField("Code Postal Bien",
                        validators=[validators.InputRequired(),validatei])
    
    Ville_Bien=StringField("Ville Bien")
    
    TVA_EDL=DecimalField("TVA EDL",
                        validators=[validators.InputRequired()])
    
    PRIX_TTC_EDL=DecimalField("Prix €TTC EDL",
                        validators=[validators.InputRequired()])
    
    CA_HT_AS=DecimalField("CA €HT AS",
                        validators=[validators.InputRequired()])

    TVA_AS=DecimalField("TVA AS",
                        validators=[validators.InputRequired()])
    
    CA_TTC_AS=DecimalField("CA €TTC AS",
                        validators=[validators.InputRequired()])
    
    CA_HT_AC=DecimalField("CA €HT AC",
                        validators=[validators.InputRequired()])
    
    CA_TTC_AC=DecimalField("CA €TC AC",
                        validators=[validators.InputRequired()])
    
    CA_HT_TRUST=DecimalField("CA €HT TRUST",
                        validators=[validators.InputRequired()])
    
    TVA_TRUST=DecimalField("TVA €TRUST",
                        validators=[validators.InputRequired()])
    
    Date_chiffrage_regle=DateField("Date chiffrage regle",
                        validators=[validators.InputRequired()])
    
    Prix_ht_chiffrage=DecimalField("Prix €HT chiffrage",
                        validators=[validators.InputRequired()])
    
    POURCENTAGE_suiveur_chiffrage=DecimalField("Pourcentage suiveur chiffrage",
                        validators=[validators.InputRequired()])

    POURCENTAGE_AS_chiffrage=DecimalField("Pourcentage AS chiffrage",
                        validators=[validators.InputRequired()])
    
    POURCENTAGE_manager_chiffrage=DecimalField("Pourcentage manager chiffrage",
                        validators=[validators.InputRequired()])
    
    ID_manager_chiffrage=IntegerField("ID manager chiffrage",
                        validators=[validators.InputRequired(),validate_email])

    POURCENTAGE_agent_chiffrage =DecimalField("Pourcentage agent chiffrage",
                        validators=[validators.InputRequired()])
    
    ID_agent_chiffrage =IntegerField("ID Agent Chiffrage",
                        validators=[validators.InputRequired(),validate_email])

    TYPE_EDL=SelectField("Type EDL",
                             choices=[('Entrant', 'Entrant'), ('Sortant', 'Sortant')])
         
    TITREPROPRIO=SelectField('Titre Proprio',
                             choices=[('Monsieur', 'Monsieur'), ('Madame', 'Madame'), ('Mademoiselle', 'Mademoiselle')])# select field

    NOMPROPRIO=StringField("Nom Proprio")


    CODE_AMEXPERT=StringField("CODE AMEXPERT")

    

    surface_logement1=DecimalField("Surface Logement 1",
                        validators=[validators.InputRequired()])

    Ref_commande=StringField("Ref Commande")
    
    POURCENTAGE_COM_AS_DU_CLIENT=DecimalField("Pourcentage COM AS DU CLIENT",
                        validators=[validators.InputRequired()])
    
    ID_Respon_Cell_Dev=IntegerField("ID Respon Cell Dev",
                        validators=[validators.InputRequired(),validate_email])

    POURCENTAGE_Respon_Cell_Dev=DecimalField("Pourcentage Respon Cell Dev",
                        validators=[validators.InputRequired()])

    ID_agent_Cell_Dev=IntegerField("ID agent Cell Dev",
                        validators=[validators.InputRequired(),validate_email])
    
    TYPE_LOGEMENT =  StringField("TYPE LOGEMENT")	

    LOGEMENT_MEUBLE = SelectField("LOGEMENT MEUBLE",
                             choices=[('OUI', 'OUI'), ('NON', 'NON')]) 	
    CODE_FACTURATION =StringField("CODE FACTURATION",
                        validators=[validators.InputRequired()])  	
    TYPE_DE_BIEN = SelectField("TYPE DE BIEN",
                             choices=[('APPARTEMENT', 'APPARTEMENT'), ('PAVILLON', 'PAVILLON')]) 
      
    POURCENTAGE_Agent_Cell_Dev =  DecimalField("Pourcentage Agent Cell Dev",
                        validators=[validators.InputRequired()])	

    ID_Agent_CellTech = IntegerField("ID Agent Cell Tech",
                        validators=[validators.InputRequired(),validate_email]) 	
    
    POURCENTAGE_Agent_Cell_Tech =DecimalField("Pourcentage Agent Cell Tech",
                        validators=[validators.InputRequired()])  	

    ID_Respon_Cell_Tech = IntegerField("ID Respon Cell Tech",
                        validators=[validators.InputRequired(),validate_email]) 
    
    POURCENTAGE_Respon_Cell_Tech = DecimalField("Pourcentage Respon Cell Tech",
                        validators=[validators.InputRequired()])
    
    ID_Suiveur_Cell_Tech =  IntegerField("ID Suiveur Cell Tech",
                        validators=[validators.InputRequired(),validate_email])	

    POURCENTAGE_Suiveur_Cell_Tech = DecimalField("Pourcentage Suiveur Cell Tech",
                        validators=[validators.InputRequired()]) 	

    ID_Respon_Cell_Planif =IntegerField("ID Respon Cell Planif",
                        validators=[validators.InputRequired(),validate_email])  

    POURCENTAGE_Respon_Cell_Planif = DecimalField("Pourcentage Respon Cell Planif",
                        validators=[validators.InputRequired()]) 
    
    ID_Suiveur_Cell_Planif =  IntegerField("ID Suiveur Cell Planif",
                        validators=[validators.InputRequired(),validate_email])	

    POURCENTAGE_Suiveur_Cell_Planif	 = DecimalField("Pourcentage Suiveur Cell Planif",
                        validators=[validators.InputRequired()]) 	

    ID_Agent_saisie_Cell_Planif =IntegerField("ID Agent Saisie Cell Planif",
                        validators=[validators.InputRequired(),validate_email])  	

    POURCENTAGE_Agent_saisie_CEll_planif = DecimalField("Pourcentage Agent Saisie Cell Planif",
                        validators=[validators.InputRequired()]) 

    misid =HiddenField()
    
   
    submit = SubmitField('Enregistrer')

    modifier = SubmitField('Modifier')


class Mission_editForm(FlaskForm):

  
    def validate_email(self,email):
        email = Expert.query.filter_by(id=email.data).first()

        if email is None :
            raise ValidationError("Cette utilisateur n'existe pas, utilisé  un autre utilisateur")

    def validate_client(self,email):
        email = Client.query.filter_by(reference=email.data).first()

        if email is None :
            raise ValidationError("Cette utilisateur n'existe pas, utilisé  un autre utilisateur")


    Reference_client=IntegerField("Reference Client",
                        validators=[validators.InputRequired(),validate_client])

    
    Nom= StringField("Nom Bailleur *",render_kw={'readonly':True})
    
    

    ID_Concessionaire=IntegerField("ID Concessionairess ", render_kw={'readonly':True}, 
                        validators=[validators.InputRequired("You got to enter some rating!"),validate_email])

    ABONNEMENT=StringField("Abonnement")
    
    PRIX_HT_EDL=DecimalField("Prix €HT EDL",
                        validators=[validators.InputRequired()])
    
    DATE_REALISE_EDL=StringField("Date realiser EDL",render_kw={'readonly':True})
    
    DATE_FACTURE=StringField("Date Facture",render_kw={'readonly':True})

    NRO_FACTURE=StringField("NRO Facture",render_kw={'readonly':True})

    COMMENTAIRE_FACTURE=StringField("Commentaire Facture",render_kw={'readonly':True})
                        
    DATE_FACT_REGLEE =StringField("Date Facture Réglée",render_kw={'readonly':True})

    ID_INTERV=IntegerField("ID INTERV",
                        validators=[validators.InputRequired(),validate_email])
    
    Reference_LOCATAIRE=StringField("Reference Locataire")
    
    Adresse1_Bien=StringField("Adresse1 Bien")
    
    Adresse2_Bien=StringField("Adresse2 Bien")
      
    CP_Bien=IntegerField("CP Bien")
    
    Ville_Bien=StringField("Ville Bien")
    
    TVA_EDL=DecimalField("TVA EDL",
                        validators=[validators.InputRequired("You got to enter some rating!")])
    
    PRIX_TTC_EDL=DecimalField("Prix €TTC EDL",
                        validators=[validators.InputRequired()])
    
    CA_HT_AS=DecimalField("CA €HT AS",
                        validators=[validators.InputRequired()])

    TVA_AS=DecimalField("TVA AS",
                        validators=[validators.InputRequired()])
    
    CA_TTC_AS=DecimalField("CA €TTC AS",
                        validators=[validators.InputRequired()])
    
    CA_HT_AC=DecimalField("CA €HT AC",
                        validators=[validators.InputRequired()])
    
    CA_TTC_AC=DecimalField("CA €TTC AC",
                        validators=[validators.InputRequired()])
    
    CA_HT_TRUST=DecimalField("CA €HT TRUST",
                        validators=[validators.InputRequired()])
    
    TVA_TRUST=DecimalField("TVA TRUST",
                        validators=[validators.InputRequired()])
    
    #Date_chiffrage_regle=DateField("Date Chiffrage_regle")
    
    Prix_ht_chiffrage=DecimalField("Prix €HT Chiffrage",
                        validators=[validators.InputRequired()])
    
    POURCENTAGE_suiveur_chiffrage=DecimalField("Pourcentage suiveur chiffrage",
                        validators=[validators.InputRequired()])

    POURCENTAGE_AS_chiffrage=DecimalField("Pourcentage AS chiffrage",
                        validators=[validators.InputRequired()])
    
    POURCENTAGE_manager_chiffrage=DecimalField("Pourcentage manager chiffrage",
                        validators=[validators.InputRequired()])
    
    ID_manager_chiffrage=IntegerField("ID manager chiffrage",
                        validators=[validators.InputRequired(),validate_email])

    POURCENTAGE_agent_chiffrage =DecimalField("Pourcentage agent chiffrage",
                        validators=[validators.InputRequired()])
    
    ID_agent_chiffrage =IntegerField("ID agent chiffrage",
                        validators=[validators.InputRequired(),validate_email])

    TYPE_EDL=SelectField("Type EDL",
                             choices=[('Entrant', 'Entrant'), ('Sortant', 'Sortant')])
    
    TITREPROPRIO=SelectField('Titre Proprio',
                             choices=[('Monsieur', 'Monsieur',), ('Madame', 'Madame'), ('Mademoiselle', 'Mademoiselle')])# select field

    NOMPROPRIO=StringField("Nom du  Proprio")


    CODE_AMEXPERT=StringField("Code AMEXPERT")

    

    surface_logement1=DecimalField("surface Logement m²",
                        validators=[validators.InputRequired()])

    Ref_commande=StringField("Ref Commande")
    
    POURCENTAGE_COM_AS_DU_CLIENT=DecimalField("Pourcentage COM AS du Client",
                        validators=[validators.InputRequired()])
    
    ID_Respon_Cell_Dev=IntegerField("ID Respon Cell Dev",
                        validators=[validators.InputRequired(),validate_email])

    POURCENTAGE_Respon_Cell_Dev=DecimalField("Pourcentage Respon Cell Dev",
                        validators=[validators.InputRequired()])

    ID_agent_Cell_Dev=IntegerField("ID agent Cell Dev",
                        validators=[validators.InputRequired(),validate_email])
    
    TYPE_LOGEMENT =  StringField("Type Logement")	

    LOGEMENT_MEUBLE = SelectField("LOGEMENT MEUBLE",
                             choices=[('OUI', 'OUI'), ('NON', 'NON')]) 	
    CODE_FACTURATION =StringField("Code Facturation")  	
    TYPE_DE_BIEN = SelectField("TYPE DE BIEN",
                             choices=[('APPARTEMENT', 'APPARTEMENT'), ('PAVILLON', 'PAVILLON')])
    
    POURCENTAGE_Agent_Cell_Dev =  DecimalField("Pourcentage Agent Cell Dev",
                        validators=[validators.InputRequired()])	

    ID_Agent_CellTech = IntegerField("ID_Agent_CellTech",
                        validators=[validators.InputRequired(),validate_email]) 	

    POURCENTAGE_Agent_Cell_Tech =DecimalField("Pourcentage Agent Cell Tech",
                        validators=[validators.InputRequired()])  	

    ID_Respon_Cell_Tech = IntegerField("ID Respon Cell Tech",
                        validators=[validators.InputRequired(),validate_email]) 
    POURCENTAGE_Respon_Cell_Tech = DecimalField("Pourcentage Respon Cell Tech") 
    
    ID_Suiveur_Cell_Tech =  IntegerField("ID Suiveur Cell Tech",
                        validators=[validators.InputRequired(),validate_email])	

    POURCENTAGE_Suiveur_Cell_Tech = DecimalField("Pourcentage Suiveur Cell Tech",
                        validators=[validators.InputRequired()]) 	

    ID_Respon_Cell_Planif =IntegerField("ID Respon Cell Planif",
                        validators=[validators.InputRequired(),validate_email])  

    POURCENTAGE_Respon_Cell_Planif = DecimalField("Pourcentage Respon Cell Planif",
                        validators=[validators.InputRequired()]) 
    
    ID_Suiveur_Cell_Planif =  IntegerField("ID Suiveur Cell Planif",
                        validators=[validators.InputRequired(),validate_email])	

    POURCENTAGE_Suiveur_Cell_Planif	 = DecimalField("Pourcentage Suiveur Cell Planif",
                        validators=[validators.InputRequired()]) 	

    ID_Agent_saisie_Cell_Planif =IntegerField("ID Agent saisie Cell Planif",
                        validators=[validators.InputRequired(),validate_email])  	

    POURCENTAGE_Agent_saisie_CEll_planif = DecimalField("Pourcentage Agent saisie CEll Planif",
                        validators=[validators.InputRequired()]) 

    misid =HiddenField()
    

    modifier = SubmitField('Modifier')


class Agenda_form(FlaskForm):

    Titre_du_Rdv=StringField("Titre du Rdv",
                        validators=[validators.InputRequired()])

    Adresse1_Rdv=StringField("Address1 du Rdv",
                        validators=[validators.InputRequired()])

    Adresse2_Rdv=StringField("Address2 du Rdv",
                        validators=[validators.InputRequired()])

    Code_postal_Rdv=StringField("Code postal Rdv",
                        validators=[validators.InputRequired()])
    
    Ville_du_Rdv=StringField("Ville du Rdv",
                    validators=[validators.InputRequired()])
    
    Date_Rdv=StringField("Date Rdv",
                    validators=[validators.InputRequired()])

    Heure_début_Rdv=StringField("Heure début Rdv",
                    validators=[validators.InputRequired()])
    
    Heure_fin_Rdv=StringField("Heure fin Rdv",
                    validators=[validators.InputRequired()])

    Date_Rdv_annulé=StringField("Date Rdv annulé",
                    validators=[validators.InputRequired()])

    Informations_réservées_service_planification=StringField("Informations réservées service planification",
                                                 validators=[validators.InputRequired()])

    Informations_générales=StringField("Informations générales",
                             validators=[validators.InputRequired()])

    Informations_de_suivi_de_Rdv=StringField("Informations de suivi de Rdv",
                                    validators=[validators.InputRequired()])

    Chemin_de_fichier_joint = StringField("Chemin de fichier joint",
                                    validators=[validators.InputRequired()])
    
    submit = SubmitField('Enregistrer')


class Invitation_Agenda(FlaskForm):

    Expert_invite=StringField("Expert invite",
                        validators=[validators.InputRequired()])

    submit = SubmitField('Enregistrer')

class Tarif_edit(FlaskForm):

    Type=StringField("Type ",
                        render_kw={'readonly':True})

    prix=DecimalField("prix *")
    
    tafid=HiddenField()

    surface=IntegerField("surface *")

    submit = SubmitField('Enregistrer')
class time(FlaskForm):

    Demarrer=DateField("Demarrer")


    submit = SubmitField('Enregistrer')

class mission_id(FlaskForm):
    ID=IntegerField("mission_id")

    submit = SubmitField('Enregistrer')

class Tarif_Base(FlaskForm):

    maison_appartement=StringField("maison appartement",
                        validators=[validators.InputRequired()])
    Nombre_de_piece=StringField("Nombre de piece",
                    validators=[validators.InputRequired()])   
    Prix_EDL=DecimalField("Prix € EDL",
                validators=[validators.InputRequired()])
    Prix_Chiffrage=DecimalField("Prix € Chiffrage",
                validators=[validators.InputRequired()])      
    submit = SubmitField('Enregistrer')


class UpdateAccountForm(FlaskForm):
    username =StringField('UserName',
                                validators=[validators.InputRequired(),length(min=4 ,max=20)])
    email =StringField('Email',
                           validators=[validators.InputRequired(),Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')
    
    def validate_username(self,username):
        if username.data != current_user.username:
            user = Expert.query.filter_by(Nom=username.data).first()

            if user:
                raise ValidationError('This username is taken.Please choose a different name')

    def validate_email(self,email):
        if email.data != current_user.email:
            user = Expert.query.filter_by(email=email.data).first()

            if user:
                raise ValidationError('This email is already used by  another user')
