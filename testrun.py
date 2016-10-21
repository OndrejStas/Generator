# -*- coding: utf-8 -*-
"""
Created on Fri Sep 02 21:11:26 2016

@author: os
"""

#import tablegen
#import sqlCmd


inp = """ 
            
            public string zadatel_tit_pred { get; set; }
            public int zadatel_prav_osoba { get; set; }
            public string zadatel_tit_za { get; set; }
            public string zadatel_jmeno { get; set; }
            public string zadatel_prijmeni { get; set; }
            public string zadatel_obchJmeno { get; set; }
            public string zadatel_ulice { get; set; }
            public string zadatel_cp { get; set; }
            public string zadatel_mesto { get; set; }
            public string zadatel_psc { get; set; }
            public string zadatel_email { get; set; }
            public string zadatel_telefon { get; set; }
            public string zadatel_fax { get; set; }
            public string zadatel_dic { get; set; }
            public string zadatel_dat_schranka { get; set; }
            public string zadatel_cel_ic { get; set; }
            public int zadatel_podnikatel { get; set; }
            public string zadatel_kontakt_osoba { get; set; }
            public string op_tit_pred { get; set; }
            public string op_tit_za { get; set; }
            public string op_kontaktni_osoba { get; set; }
            public string op_dat_schranka { get; set; }
            public string op_dic { get; set; }
            public int op_prav_osoba { get; set; }
            public bool op_podnikatel { get; set; }
            public string op_osoba_jmeno { get; set; }
            public string op_obchJmeno { get; set; }
            public string op_osoba_prijmeni { get; set; }
            public string op_ulice { get; set; }
            public string op_cp { get; set; }
            public string op_mesto { get; set; }
            public string op_psc { get; set; }
            public string op_osoba_email { get; set; }
            public string op_osoba_telefon { get; set; }
            public string op_osoba_fax { get; set; }
            public string op_osoba_cel_ic { get; set; }
            public string zmocnenec_tit_pred { get; set; }
            public string zmocnenec_tit_za { get; set; }
            public string zmocnenec_jmeno { get; set; }
            public string zmocnenec_prijmeni { get; set; }
            public string zmocnenec_obchJmeno { get; set; }
            public string zmocnenec_ulice { get; set; }
            public string zmocnenec_cp { get; set; }
            public string zmocnenec_mesto { get; set; }
            public string zmocnenec_psc { get; set; }
            public string zmocnenec_email { get; set; }
            public string zmocnenec_telefon { get; set; }
            public string zmocnenec_fax { get; set; }
            public string zmocnenec_cel_ic { get; set; }
            public int zmocnenec_prav_osoba { get; set; }
            public string zmocnenec_dic { get; set; }
            public bool zmocnenec_podnikatel { get; set; }
            public string zmocnenec_dat_schranka { get; set; }
            public string zmocnenec_kon_osoba { get; set; }
            public string zisz_reissue_num { get; set; }
            public DateTime zisz_reissue_valid_from { get; set; }
            public string zisz_nomen_code { get; set; }
            public bool hs { get; set; }
            public bool cn { get; set; }
            public bool tc_taric { get; set; }
            public bool ep { get; set; }
            public bool ot { get; set; }
            public string ot_text { get; set; }
            public bool druh_pouziti { get; set; }
            public string navrh_zarazeni { get; set; }
            public string popis_zbozi { get; set; }
            public string obchodni_nazev { get; set; }
            public bool vzorky_popis { get; set; }
            public bool vzorky_dokumentace { get; set; }
            public bool vzorky_fotografie { get; set; }
            public bool vzorky_vzorky { get; set; }
            public bool vzorky_ostatni { get; set; }
            public bool vzorky_vraceny { get; set; }
            public bool vydana_zadost { get; set; }
            public bool vydane_zisz_jinym { get; set; }
            public DateTime datum_podpis { get; set; }
            public int typ_zadosti { get; set; }
            public string vase_znacka { get; set; }
            public string jmeno_podpis { get; set; }
            public string prijmeni_podpis { get; set; }
            public int stav_zadosti { get; set; }
            public string IdentName { get; set; }
            public string Cj { get; set; }
            public int TisZadistId { get; set; }
            public string UredniZaznam { get; set; }
            public bool Obr_kesnimani { get; set; }
            public int Obr_Pocet { get; set; }
            public string JazykZISZPodana { get; set; }
            public string MistoPrijeti { get; set; }
            public DateTime DatumPrijeti { get; set; }
            public string DuverneInformace { get; set; }
            public string DodatecneInformace { get; set; }
            public string MistoUcetnictvi { get; set; }
            public bool VedomostRizeni { get; set; }
            public int genid { get; set; }

"""

#inp = """
#
#
#CREATE TABLE [dbo].[KRTy]([KRT_ID] [int] NOT NULL,[KRT_ID_FARnosti] [int] NOT NULL,[KRT_Kniha] [int] NOT NULL
#
# """
#str = inp.split("\n")
#print len(str) 

#print tablegen.createClass(inp,"JmenpTridy")
#print tablegen.generateHtmlTable(tablegen.getDefinitions(inp))

#sqlCmd.GenInsert(inp)