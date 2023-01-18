import sys
import os
import datetime
import openpyxl
import xlrd,xlwt
from flask import Flask,render_template,url_for,flash,redirect,request,Blueprint,send_from_directory
from Database_project.project.data_base_.Models import db,Mission,Client,Expert,prospect,Client_History,prospect_History




class data():
    def cl(self,id,T):
        client=Client.query.filter_by(id=id).first()
        history=Client_History.query.filter_by(id=id).first()
        if T == "n":
            return client.nom
        if T == "t":
            return client.titre
        if T == "r":
            return client.reference
        if T == "a":
            return history.adresse1
        if T == "a2":
            return history.adresse2
        if T == "cp":
            return history.cp
        if T == "v":
            return history.ville
    
    def pl(self,id,T):
        client=prospect.query.filter_by(id=id).first()
        history=prospect_History.query.filter_by(id=id).first()
        if T == "n":
            return client.nom
        if T == "t":
            return client.titre
        if T == "a":
            return history.adresse1
        if T == "a2":
            return history.adresse2
        if T == "cp":
            return history.cp
        if T == "v":
            return history.ville
        
    def exn(self,id,T):
        client=Expert.query.filter_by(id=id).first()
        if T == "n":
            return client.nom
        if T == "t":
            return client.genre

        
class Export(data):
    dat=data()

    def export(self,av,filename):
        ba=[]
        v=0
        for oo in av:
            tr=len(oo)
        for i in range(0,tr):
            ba.append(i)
        wb = xlwt.Workbook()
        style1 = xlwt.easyxf(num_format_str='D-MMM-YY')
        ws = wb.add_sheet('Export')
        for oo in av:
                for q,i in zip(ba,oo) :
                    if isinstance(i,datetime.datetime) == True:
                        ws.write(v, q, i,style1)
                    elif isinstance(i,datetime.date) == True:
                        ws.write(v, q, i,style1) 
                    else:
                        ws.write(v, q, i)
                v=v+1
        #filename='expert_export.xls'
        file_path = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static','export'),filename)
        loc=str(file_path)
        # set the file path
        #uploaded_file.save(file_path)
        wb.save(loc)
        return send_from_directory(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static','export'), filename,as_attachment=True)
     
    def mission_data(self,miss,mi,dat=dat):
        for i in miss:
            mi.append([dat.cl(i.Reference_BAILLEUR,"r"),dat.cl(i.Reference_BAILLEUR,"t"),dat.cl(i.Reference_BAILLEUR,"n"),dat.cl(i.Reference_BAILLEUR,"a"),
    dat.cl(i.Reference_BAILLEUR,"a2"),dat.cl(i.Reference_BAILLEUR,"cp"),dat.cl(i.Reference_BAILLEUR,"v"),i.NRO_FACTURE,	 
    i.ABONNEMENT,dat.exn(i.ID_AS,'t'),dat.exn(i.ID_AS,'n'),i.DATE_REALISE_EDL,i.PRIX_HT_EDL,i.TVA_EDL,i.PRIX_TTC_EDL,dat.exn(i.ID_INTERV,'t'),
    dat.exn(i.ID_INTERV,'n'),i.Reference_LOCATAIRE,'','',i.Adresse1_Bien,i.Adresse2_Bien,i.CP_Bien,i.Ville_Bien,i.CA_HT_AS,i.TVA_AS,
    i.CA_TTC_AS,i.CA_HT_AC,i.CA_TTC_AC,i.CA_HT_TRUST,i.TVA_TRUST,i.Date_chiffrage_regle,i.Prix_ht_chiffrage,i.POURCENTAGE_suiveur_chiffrage,
    i.POURCENTAGE_AS_chiffrage,i.POURCENTAGE_manager_chiffrage,dat.exn(i.ID_manager_chiffrage,'n'),i.POURCENTAGE_agent_chiffrage,
    dat.exn(i.ID_agent_chiffrage,'n'), i.TYPE_EDL,i.DATE_FACTURE,i.TITREPROPRIO,
    i.NOMPROPRIO,i.DATE_FACT_REGLEE,"","","","",i.TYPE_LOGEMENT,"","","",i.CODE_AMEXPERT,i.COMMENTAIRE_FACTURE,"","","",i.LOGEMENT_MEUBLE,i.CODE_FACTURATION,
    i.TYPE_DE_BIEN,i.surface_logement1,"","","",i.POURCENTAGE_COM_AS_DU_CLIENT,dat.exn(i.ID_Respon_Cell_Dev,'n'),i.POURCENTAGE_Respon_Cell_Dev,
    dat.exn(i.ID_agent_Cell_Dev,'n'),i.POURCENTAGE_Agent_Cell_Dev,dat.exn(i.ID_Agent_CellTech,'n'),i.POURCENTAGE_Agent_Cell_Tech,
    dat.exn(i.ID_Respon_Cell_Tech,'n'),i.POURCENTAGE_Respon_Cell_Tech,dat.exn(i.ID_Suiveur_Cell_Tech,'n'),i.POURCENTAGE_Suiveur_Cell_Tech,
    dat.exn(i.ID_Respon_Cell_Planif,'n'),i.POURCENTAGE_Respon_Cell_Planif,dat.exn(i.ID_Suiveur_Cell_Planif,'n'),i.POURCENTAGE_Suiveur_Cell_Planif,
    dat.exn(i.ID_Agent_saisie_Cell_Planif,'n'),i.POURCENTAGE_Agent_saisie_CEll_planif])
        return mi

    def expert_data(self,exp,ex,dat=dat):
        for i,v in exp:
            ex.append([i.id,i.nom,i.trigramme,i.date_entree,v.actif_parti,i.TYPE,
    v.secteur,"",i.siret,v.adresse1,v.adresse2,v.cp,v.ville,i.code_tva,i.taux_tva,i.numero,i.email,i.email_perso,v.login_backof,v.pwd_backof,
    v.login_google,v.pwd_extranet,v.login_extranet,v.pwd_extranet,v.pwd_gsuite,v.pwd_google,v.observations_de_suivi]) #,v.date_certification_initiale,v.date_renouv_certification,v.type_certification
        return ex

    def client_data(self,exp,ex,dat=dat):
        for i,h in exp:
            ex.append([i.id,i.reference,i.TYPE,'CLIENT',i.societe,i.enseigne,i.titre,i.nom,i.email,i.numero,i.siret,i.date_creation,
    h.adresse1,h.adresse2,h.etat_client,h.cp,h.ville,h.pays,h.login_extranet,h.mpd_extranet,h.abonnement])
        return ex
    def prospect_data(self,exp,ex,dat=dat):
        for i,h in exp:
            ex.append([i.id,i.reference,i.TYPE,'PROSPECT',i.societe,i.enseigne,i.titre,i.nom,i.email,i.numero,i.siret,i.date_creation,
    h.adresse1,h.adresse2,h.etat_client,h.cp,h.ville,h.pays,h.login_extranet,h.mpd_extranet,h.abonnement])
        return ex
    def nego_data(self,exp,ex,dat=dat):
        for i,h in exp:
            ex.append([dat.cl(i.client_id,"n"),i.sexe,i.nom,i.email,i.numero,i.date_creation,h.adresse,h.etat_client,h.cp,h.ville,h.pays,h.abonnement])
        return ex
        
    
    def suivi_data(self,exp,ex,dat=dat):
        for i in exp:
            ex.append([dat.cl(i.client,"n"),i.responsable,i.commentaire,i.date_creation,i.date_modif])
        return ex
    def suivip_data(self,exp,ex,dat=dat):
        for i in exp:
            ex.append([dat.pl(i.prospect_id,"n"),i.responsable,i.commentaire,i.date_creation,i.date_modif])
        return ex
    
    def taaf(self,exp,ex,dat=dat):
        for i in exp:
            ex.append([dat.cl(i.reference_client,"n"),i.edl_prix_std,i.edl_appt_prix_f1,i.edl_appt_prix_f2,i.edl_appt_prix_f3,i.edl_appt_prix_f4,i.edl_appt_prix_f5,i.edl_appt_prix_f6, 
    i.edl_pav_villa_prix_t1,i.edl_pav_villa_prix_t2,i.edl_pav_villa_prix_t3,i.edl_pav_villa_prix_t4,i.edl_pav_villa_prix_t5,i.edl_pav_villa_prix_t6, 
    i.edl_pav_villa_prix_t7,i.edl_pav_villa_prix_t8,i.chif_appt_prix_stu,i.chif_appt_prix_f1,i.chif_appt_prix_f2,i.chif_appt_prix_f3,i.chif_appt_prix_f4,  
    i.chif_appt_prix_f5,i.chif_appt_prix_f6,i.chif_pav_villa_prix_t1,i.chif_pav_villa_prix_t2,i.chif_pav_villa_prix_t3,i.chif_pav_villa_prix_t4,i.chif_pav_villa_prix_t5, 
    i.chif_pav_villa_prix_t6,i.chif_pav_villa_prix_t7,i.chif_pav_villa_prix_t8,i.code_tva,i.taux_meuble,i.referent_as_client,i.com_as_sur_ca_client,i.cell_dev_ref_responsable,  
    i.com_cell_dev_ref_responsable,i.cell_dev_ref_agent,i.com_cell_dev_ref_agent,i.cell_tech_ref_agent,i.com_cell_tech_Ref_agent,i.cell_tech_ref_responsable,i.com_cell_tech_ref_responsable  
    ,i.cell_tech_ref_suiveur,i.com_cell_tech_ref_suiveur,i.cell_planif_ref_responsable,i.com_cell_planif_ref_responsable,i.cell_planif_ref_suiveur,i.com_cell_planif_ref_suiveur, 
    i.cell_planif_ref_agent_saisie,i.com_cell_planif_ref_agent_saisie,i.prix_autre,i.commentaire_libre])
        return ex
        
