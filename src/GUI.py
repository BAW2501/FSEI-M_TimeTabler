# -*- coding: utf-8 -*-
import datetime
import os
import sys

import resources
from Gui_files.inputDiags import *
from Gui_files.ui_window import *
from src.Solver import *


def session_type_from_int(task):
    if task == 1:
        return "Lecture"
    elif task == 2:
        return "TD"
    else:
        return "TP"


def room_type_from_int(task):
    if task == 1:
        return "Amphi"
    elif task == 2:
        return "TD"
    else:
        return "TP"


class MainWindow(QMainWindow):
    def __init__(self):

        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.promos = [{'Effective per Group': 25,
                        'Name': 'TC-MI',
                        'Number of Groups': 14,
                        'Number of Sections': 2},
                       {'Effective per Group': 23,
                        'Name': 'L2-INFO',
                        'Number of Groups': 9,
                        'Number of Sections': 1},
                       {'Effective per Group': 22,
                        'Name': 'L3-INFO',
                        'Number of Groups': 7,
                        'Number of Sections': 1},
                       {'Effective per Group': 22,
                        'Name': 'L2-MATH',
                        'Number of Groups': 2,
                        'Number of Sections': 1},
                       {'Effective per Group': 22,
                        'Name': 'L3-MATH',
                        'Number of Groups': 2,
                        'Number of Sections': 1},
                       {'Effective per Group': 22,
                        'Name': 'M1-ISI',
                        'Number of Groups': 4,
                        'Number of Sections': 1},
                       {'Effective per Group': 22,
                        'Name': 'M1-RéSys',
                        'Number of Groups': 1,
                        'Number of Sections': 1},
                       {'Effective per Group': 22,
                        'Name': 'M1-AF',
                        'Number of Groups': 1,
                        'Number of Sections': 1},
                       {'Effective per Group': 23,
                        'Name': 'M1-MCO',
                        'Number of Groups': 1,
                        'Number of Sections': 1},
                       {'Effective per Group': 22,
                        'Name': 'TC-SM',
                        'Number of Groups': 4,
                        'Number of Sections': 1},
                       {'Effective per Group': 21,
                        'Name': 'L2-PHYS',
                        'Number of Groups': 1,
                        'Number of Sections': 1},
                       {'Effective per Group': 22,
                        'Name': 'L3-PHYS',
                        'Number of Groups': 1,
                        'Number of Sections': 1},
                       {'Effective per Group': 22,
                        'Name': 'L2-CHIM',
                        'Number of Groups': 2,
                        'Number of Sections': 1},
                       {'Effective per Group': 22,
                        'Name': 'L3-CHIM',
                        'Number of Groups': 2,
                        'Number of Sections': 1},
                       {'Effective per Group': 21,
                        'Name': 'M1-PM',
                        'Number of Groups': 1,
                        'Number of Sections': 1}]

        self.profs = ['Abbassa',
                      'Abbes',
                      'ABID M.',
                      'Adda',
                      'BAHNES N.',
                      'Beghdad',
                      'Belayachi',
                      'Belhachemi',
                      'Belhakem',
                      'belhalfaoui',
                      'Belhouari',
                      'Belouatek',
                      'BENAMEUR',
                      'Bencherif',
                      'Benguettat',
                      'BENHAMED',
                      'BENIDRIS F.Z',
                      'Benmalti',
                      'Benotsmane',
                      'BENSALLOUA',
                      'BENTAOUZA C',
                      'BESNASSI',
                      'BESSAOUD K.',
                      'BETOUATI',
                      'Bouattou',
                      'Boukra',
                      'Boulenouar',
                      'Bourada',
                      'Bourahla',
                      'BOUZEBIBA',
                      'DELALI A.',
                      'DJAHAFI',
                      'DJEBBARA R.',
                      'FILALI F.',
                      'HABIB ZAHMANI M',
                      'HAMAMI',
                      'Hamiani',
                      'harrats',
                      'HASSAINE',
                      'HENNI F',
                      'HENNI K',
                      'HENNI K.',
                      'Hentit H',
                      'Hentit N',
                      'HOCINE N.',
                      'Kadi',
                      'KAID SLIMANE',
                      'KENNICHE A.',
                      'KHELIFA N.',
                      'KHIAT',
                      'Labdelli',
                      'LAREDJ A. M',
                      'Latreuch',
                      'M. AMIR A.',
                      'M. Andasmas M',
                      'M. B. BENDOUKHA',
                      'M. BELAIDI Benharrat',
                      'M. BELARBI Lakehal',
                      'M. Belhamiti Omar',
                      'M. Benchehida',
                      'M. Benyatou Kamel',
                      'M. Benzidane',
                      'M. BOUZIT Hamid',
                      'M. Dahmani Z.',
                      'M. Fettouch Houari',
                      'M. Ghezzar Med',
                      'M. Kaid',
                      'M. Kaid Med',
                      'M. Medeghri Ahmed',
                      'M. Menad Abdallah',
                      'M. Mohammedi Mustapha',
                      'M. Ould Ali M',
                      'M. Zoubir DAHMANI',
                      'M.Ould ali',
                      'MAGHNI SANDID Z.',
                      'MECHAOUI M. D.G',
                      'Meghoufel',
                      'Mekemmeche',
                      'Melati',
                      'MENAD',
                      'MEROUFEL B.',
                      'Messaoudi',
                      'MIDOUN M.',
                      'MIROUD',
                      'Mlle Ali Merina.H',
                      'Mlle Amina FERRAOUN',
                      'Mlle Benaouad',
                      'Mlle Bouzid',
                      'Mlle Bouzid Leila',
                      'Mlle Dj. BENSIKADDOUR',
                      'Mlle Dj.BENSIKADDOUR',
                      'Mlle FERRAOUN A.',
                      'Mlle Hamou Maamar.M',
                      'Mlle Lakeb Ouda',
                      'Mlle Medeghri Ahmed',
                      'Mlle Zelmat Souhila',
                      'Mme Ablaoui',
                      'Mme Belmouhoub-Ould ali',
                      'Mme Bendahmane Hafida',
                      'Mme Bendehmane H',
                      'Mme Bouabdelli',
                      'Mme Diala.H',
                      'Mme Kaisserli',
                      'Mme Limam',
                      'Mme SAIDANI',
                      'Mme TABHARIT',
                      'Mme.Bechaoui',
                      'MOUMEN M.',
                      'MOUSSA M.',
                      'Mr Ablaoui H.',
                      'Mr Bouzit H',
                      'Mr S. M. Bahri',
                      'Mr. BOUAGADA',
                      'Mr.Senouci',
                      'SEHABA K.',
                      'Terki']
        self.rooms = [{'Capacity': 45, 'Name': 'S1', 'RoomType': 2},
                      {'Capacity': 25, 'Name': 'S8', 'RoomType': 2},
                      {'Capacity': 25, 'Name': 'S9', 'RoomType': 2},
                      {'Capacity': 25, 'Name': 'S10', 'RoomType': 2},
                      {'Capacity': 25, 'Name': 'S11', 'RoomType': 2},
                      {'Capacity': 25, 'Name': 'S7', 'RoomType': 2},
                      {'Capacity': 25, 'Name': 'S6', 'RoomType': 2},
                      {'Capacity': 25, 'Name': 'S5', 'RoomType': 2},
                      {'Capacity': 25, 'Name': 'S4', 'RoomType': 2},
                      {'Capacity': 45, 'Name': 'S3', 'RoomType': 2},
                      {'Capacity': 45, 'Name': 'S2', 'RoomType': 2},
                      {'Capacity': 45, 'Name': 'S16', 'RoomType': 2},
                      {'Capacity': 25, 'Name': 'S15', 'RoomType': 2},
                      {'Capacity': 25, 'Name': 'S14', 'RoomType': 2},
                      {'Capacity': 25, 'Name': 'S13', 'RoomType': 2},
                      {'Capacity': 25, 'Name': 'S12', 'RoomType': 2},
                      {'Capacity': 25, 'Name': 'M3', 'RoomType': 3},
                      {'Capacity': 25, 'Name': 'M2', 'RoomType': 3},
                      {'Capacity': 25, 'Name': 'M1', 'RoomType': 3},
                      {'Capacity': 25, 'Name': 'C4', 'RoomType': 2},
                      {'Capacity': 25, 'Name': 'C3', 'RoomType': 2},
                      {'Capacity': 25, 'Name': 'C2', 'RoomType': 2},
                      {'Capacity': 25, 'Name': 'C1', 'RoomType': 2},
                      {'Capacity': 25, 'Name': 'B4', 'RoomType': 2},
                      {'Capacity': 25, 'Name': 'B3', 'RoomType': 2},
                      {'Capacity': 25, 'Name': 'B2', 'RoomType': 2},
                      {'Capacity': 25, 'Name': 'B1', 'RoomType': 2},
                      {'Capacity': 360, 'Name': 'Amphi4', 'RoomType': 1},
                      {'Capacity': 230, 'Name': 'Amphi3', 'RoomType': 1},
                      {'Capacity': 230, 'Name': 'Amphi2', 'RoomType': 1},
                      {'Capacity': 230, 'Name': 'Amphi1', 'RoomType': 1},
                      {'Capacity': 25, 'Name': 'A4', 'RoomType': 3},
                      {'Capacity': 25, 'Name': 'A3', 'RoomType': 3},
                      {'Capacity': 25, 'Name': 'A2', 'RoomType': 3},
                      {'Capacity': 25, 'Name': 'A1', 'RoomType': 3}]
        self.modules = [[{'Name': ' Analyse 2', 'abriv': 'ANA2', 'nb_cour': 2, 'nb_td': 1, 'nb_tp': 0},
                         {'Name': ' Algèbre 2', 'abriv': 'ALG2', 'nb_cour': 1, 'nb_td': 1, 'nb_tp': 0},
                         {'Name': ' Algorithmique et structure de données 2',
                          'abriv': 'ASD2',
                          'nb_cour': 1,
                          'nb_td': 1,
                          'nb_tp': 1},
                         {'Name': ' Structure machine 2',
                          'abriv': 'SM2',
                          'nb_cour': 1,
                          'nb_td': 1,
                          'nb_tp': 0},
                         {'Name': ' Introduction aux probabilités et statistique descriptive',
                          'abriv': 'IPSD',
                          'nb_cour': 1,
                          'nb_td': 1,
                          'nb_tp': 0},
                         {'Name': " Technologie de l'Information et de la Communication",
                          'abriv': 'TIC',
                          'nb_cour': 1,
                          'nb_td': 0,
                          'nb_tp': 0},
                         {'Name': ' Outils de programmation pour les mathématiques',
                          'abriv': 'OPM',
                          'nb_cour': 1,
                          'nb_td': 0,
                          'nb_tp': 1},
                         {'Name': ' Physique 2(électricité générale)',
                          'abriv': 'PHY2',
                          'nb_cour': 1,
                          'nb_td': 1,
                          'nb_tp': 0}],
                        [{'Name': ' Théorie des langages',
                          'abriv': 'TL',
                          'nb_cour': 1,
                          'nb_td': 1,
                          'nb_tp': 1},
                         {'Name': " Système d'exploitation 1",
                          'abriv': 'SE1',
                          'nb_cour': 1,
                          'nb_td': 1,
                          'nb_tp': 1},
                         {'Name': ' Bases de données',
                          'abriv': 'BDD',
                          'nb_cour': 1,
                          'nb_td': 1,
                          'nb_tp': 1},
                         {'Name': ' Réseaux', 'abriv': 'RÉS', 'nb_cour': 1, 'nb_td': 1, 'nb_tp': 1},
                         {'Name': ' Programmation orienté objet',
                          'abriv': 'POO',
                          'nb_cour': 1,
                          'nb_td': 0,
                          'nb_tp': 1},
                         {'Name': ' Développement d Applications Web',
                          'abriv': 'DAW',
                          'nb_cour': 1,
                          'nb_td': 0,
                          'nb_tp': 1}],
                        [{'Name': ' Applications Mobiles',
                          'abriv': 'AP',
                          'nb_cour': 1,
                          'nb_td': 0,
                          'nb_tp': 1},
                         {'Name': ' Sécurité Informatique',
                          'abriv': 'SI',
                          'nb_cour': 1,
                          'nb_td': 1,
                          'nb_tp': 0},
                         {'Name': ' Intelligence Artificielle',
                          'abriv': 'IA',
                          'nb_cour': 1,
                          'nb_td': 0,
                          'nb_tp': 1},
                         {'Name': ' Données semi-structurées',
                          'abriv': 'DSS',
                          'nb_cour': 1,
                          'nb_td': 0,
                          'nb_tp': 1},
                         {'Name': ' Rédaction Scientifique',
                          'abriv': 'RS',
                          'nb_cour': 0,
                          'nb_td': 1,
                          'nb_tp': 0},
                         {'Name': ' Créer et développer une startup',
                          'abriv': 'CDS',
                          'nb_cour': 1,
                          'nb_td': 0,
                          'nb_tp': 0}],
                        [{'Name': 'Analyse 4', 'abriv': 'ANA4', 'nb_cour': 2, 'nb_td': 2, 'nb_tp': 0},
                         {'Name': 'Algèbre 4', 'abriv': 'ALG4', 'nb_cour': 1, 'nb_td': 1, 'nb_tp': 0},
                         {'Name': 'Analyse complexe',
                          'abriv': 'AC',
                          'nb_cour': 2,
                          'nb_td': 1,
                          'nb_tp': 0},
                         {'Name': 'Analyse Numérique 2',
                          'abriv': 'ANUM2',
                          'nb_cour': 1,
                          'nb_td': 1,
                          'nb_tp': 1},
                         {'Name': 'Probabilités',
                          'abriv': 'PROBA',
                          'nb_cour': 1,
                          'nb_td': 1,
                          'nb_tp': 0},
                         {'Name': 'Géométrie', 'abriv': 'GÉOMÉ', 'nb_cour': 1, 'nb_td': 1, 'nb_tp': 0},
                         {'Name': 'Application des mathématiques aux autres sciences',
                          'abriv': 'APsciences',
                          'nb_cour': 1,
                          'nb_td': 1,
                          'nb_tp': 0}],
                        [{'Name': 'Introduction à la théorie des opérateurs linéaire',
                          'abriv': 'TOL',
                          'nb_cour': 2,
                          'nb_td': 2,
                          'nb_tp': 0},
                         {'Name': 'EDP', 'abriv': 'EDP', 'nb_cour': 2, 'nb_td': 2, 'nb_tp': 0},
                         {'Name': ' Transformations intégrales dans les espaces L',
                          'abriv': 'TRAL',
                          'nb_cour': 2,
                          'nb_td': 1,
                          'nb_tp': 0},
                         {'Name': 'Géométrie différentielle',
                          'abriv': 'Géo. Diff',
                          'nb_cour': 2,
                          'nb_td': 1,
                          'nb_tp': 0},
                         {'Name': "Ethique et déontologie de l'enseignement et de la recherche",
                          'abriv': 'ETHrecherche',
                          'nb_cour': 1,
                          'nb_td': 0,
                          'nb_tp': 0}],
                        [{'Name': 'Administration et organisation des SI ',
                          'abriv': 'AOSI',
                          'nb_cour': 1,
                          'nb_td': 1,
                          'nb_tp': 1},
                         {'Name': 'Architecture logicielle orientée service',
                          'abriv': 'ALOS',
                          'nb_cour': 1,
                          'nb_td': 0,
                          'nb_tp': 1},
                         {'Name': 'Sécurité des SI',
                          'abriv': 'SSI',
                          'nb_cour': 1,
                          'nb_td': 0,
                          'nb_tp': 1},
                         {'Name': 'Ontologie et Web Sémantique',
                          'abriv': 'OWS',
                          'nb_cour': 1,
                          'nb_td': 1,
                          'nb_tp': 0},
                         {'Name': 'Fouille de données',
                          'abriv': 'FDD',
                          'nb_cour': 1,
                          'nb_td': 0,
                          'nb_tp': 1},
                         {'Name': 'Recherche opérationnelle',
                          'abriv': 'RO',
                          'nb_cour': 1,
                          'nb_td': 0,
                          'nb_tp': 1},
                         {'Name': 'Gestion de projets',
                          'abriv': 'GP',
                          'nb_cour': 1,
                          'nb_td': 0,
                          'nb_tp': 0},
                         {'Name': 'Systèmes multi-agents',
                          'abriv': 'SMA',
                          'nb_cour': 1,
                          'nb_td': 0,
                          'nb_tp': 1}],
                        [{'Name': 'Gestion des services réseaux',
                          'abriv': 'GSR',
                          'nb_cour': 1,
                          'nb_td': 1,
                          'nb_tp': 1},
                         {'Name': 'Virtualisation des systèmes',
                          'abriv': 'VS',
                          'nb_cour': 1,
                          'nb_td': 0,
                          'nb_tp': 1},
                         {'Name': 'Sécurité des réseaux et internet',
                          'abriv': 'SRI',
                          'nb_cour': 1,
                          'nb_td': 0,
                          'nb_tp': 1},
                         {'Name': 'Administration des serveurs de BD et applications',
                          'abriv': 'ASBDA',
                          'nb_cour': 1,
                          'nb_td': 0,
                          'nb_tp': 0},
                         {'Name': 'Programmation réseaux',
                          'abriv': 'PR',
                          'nb_cour': 1,
                          'nb_td': 0,
                          'nb_tp': 1},
                         {'Name': 'Administration et Organisation des SI',
                          'abriv': 'AOSI',
                          'nb_cour': 1,
                          'nb_td': 1,
                          'nb_tp': 1},
                         {'Name': 'Recherche Opérationnelle ',
                          'abriv': 'RO',
                          'nb_cour': 1,
                          'nb_td': 1,
                          'nb_tp': 0},
                         {'Name': 'Gestion de projet ',
                          'abriv': 'GP',
                          'nb_cour': 1,
                          'nb_td': 0,
                          'nb_tp': 0}],
                        [{'Name': 'Analyse Complexe II',
                          'abriv': 'AC2',
                          'nb_cour': 1,
                          'nb_td': 2,
                          'nb_tp': 0},
                         {'Name': 'Th. Des Opérateurs II',
                          'abriv': 'TO2',
                          'nb_cour': 1,
                          'nb_td': 1,
                          'nb_tp': 0},
                         {'Name': 'Géo. Diff II',
                          'abriv': 'GéoDiff2',
                          'nb_cour': 1,
                          'nb_td': 2,
                          'nb_tp': 0},
                         {'Name': 'Distributions II',
                          'abriv': 'Dis2',
                          'nb_cour': 1,
                          'nb_td': 1,
                          'nb_tp': 0},
                         {'Name': 'EDP II', 'abriv': 'EDP2', 'nb_cour': 1, 'nb_td': 2, 'nb_tp': 0},
                         {'Name': 'Statistiques II',
                          'abriv': 'STAT2',
                          'nb_cour': 1,
                          'nb_td': 1,
                          'nb_tp': 0},
                         {'Name': 'Semi-Groupes',
                          'abriv': 'SEMIGROUP',
                          'nb_cour': 1,
                          'nb_td': 1,
                          'nb_tp': 0},
                         {'Name': 'Anglais II',
                          'abriv': 'Anglais2',
                          'nb_cour': 1,
                          'nb_td': 0,
                          'nb_tp': 0}],
                        [{'Name': 'Modélisation 2',
                          'abriv': 'Mod2',
                          'nb_cour': 1,
                          'nb_td': 1,
                          'nb_tp': 0},
                         {'Name': 'OAF 2', 'abriv': 'OAF 2', 'nb_cour': 2, 'nb_td': 1, 'nb_tp': 0},
                         {'Name': 'Th. Contrôle',
                          'abriv': 'TCONTROL',
                          'nb_cour': 1,
                          'nb_td': 1,
                          'nb_tp': 0},
                         {'Name': 'Cal. Fract 1',
                          'abriv': 'CFRAC',
                          'nb_cour': 1,
                          'nb_td': 1,
                          'nb_tp': 0},
                         {'Name': 'Th. Des Graphes',
                          'abriv': 'TG',
                          'nb_cour': 1,
                          'nb_td': 1,
                          'nb_tp': 1},
                         {'Name': 'Prog. Quadratique',
                          'abriv': 'PROGQUAD',
                          'nb_cour': 1,
                          'nb_td': 1,
                          'nb_tp': 1},
                         {'Name': 'Latex', 'abriv': 'Latex', 'nb_cour': 1, 'nb_td': 0, 'nb_tp': 0},
                         {'Name': 'Anglais',
                          'abriv': 'Anglais',
                          'nb_cour': 1,
                          'nb_td': 0,
                          'nb_tp': 0}],
                        [{'Name': 'Mathématiques 2',
                          'abriv': 'Maths2',
                          'nb_cour': 2,
                          'nb_td': 2,
                          'nb_tp': 0},
                         {'Name': 'Physique 2',
                          'abriv': 'Chim2',
                          'nb_cour': 2,
                          'nb_td': 2,
                          'nb_tp': 0},
                         {'Name': 'Chimie 2', 'abriv': 'Phys2', 'nb_cour': 2, 'nb_td': 2, 'nb_tp': 0},
                         {'Name': 'Informatique 2',
                          'abriv': 'Info2',
                          'nb_cour': 1,
                          'nb_td': 0,
                          'nb_tp': 1},
                         {'Name': 'Histoire des Sciences',
                          'abriv': 'HisSci',
                          'nb_cour': 1,
                          'nb_td': 0,
                          'nb_tp': 0}],
                        [{'Name': 'Thermodynamique',
                          'abriv': 'Thdyna',
                          'nb_cour': 2,
                          'nb_td': 2,
                          'nb_tp': 0},
                         {'Name': 'Fonction de la Variable Complexe',
                          'abriv': 'FVC',
                          'nb_cour': 2,
                          'nb_td': 2,
                          'nb_tp': 0},
                         {'Name': 'Mécanique Quantique',
                          'abriv': 'MQ',
                          'nb_cour': 2,
                          'nb_td': 2,
                          'nb_tp': 0},
                         {'Name': 'Electromagnétisme',
                          'abriv': 'elecmag',
                          'nb_cour': 2,
                          'nb_td': 2,
                          'nb_tp': 0},
                         {'Name': 'Electronique Générale',
                          'abriv': 'elecgen',
                          'nb_cour': 2,
                          'nb_td': 0,
                          'nb_tp': 0}],
                        [{'Name': 'Physique du Solide',
                          'abriv': 'PhysSol',
                          'nb_cour': 2,
                          'nb_td': 2,
                          'nb_tp': 0},
                         {'Name': 'Physique Nucléaire',
                          'abriv': 'PhysNuc',
                          'nb_cour': 2,
                          'nb_td': 2,
                          'nb_tp': 0},
                         {'Name': 'Transfert de Chaleur',
                          'abriv': 'TransCha',
                          'nb_cour': 2,
                          'nb_td': 2,
                          'nb_tp': 0},
                         {'Name': 'Physique Atomique',
                          'abriv': 'PhysAto',
                          'nb_cour': 2,
                          'nb_td': 2,
                          'nb_tp': 0}],
                        [{'Name': 'Chimie Organique 2',
                          'abriv': 'ChiOrg2',
                          'nb_cour': 2,
                          'nb_td': 1,
                          'nb_tp': 0},
                         {'Name': 'Thermodynamique & Cinétique Chimique',
                          'abriv': 'ThermoCin',
                          'nb_cour': 2,
                          'nb_td': 1,
                          'nb_tp': 0},
                         {'Name': 'Chimie Analytique',
                          'abriv': 'ChimAna',
                          'nb_cour': 1,
                          'nb_td': 1,
                          'nb_tp': 0},
                         {'Name': 'Chimie Quantique',
                          'abriv': 'ChiQuan',
                          'nb_cour': 1,
                          'nb_td': 1,
                          'nb_tp': 0},
                         {'Name': 'Chimie Inorganique',
                          'abriv': 'ChimInorg',
                          'nb_cour': 1,
                          'nb_td': 1,
                          'nb_tp': 0},
                         {'Name': 'Anglais 4',
                          'abriv': 'Anglais 4',
                          'nb_cour': 1,
                          'nb_td': 0,
                          'nb_tp': 0},
                         {'Name': 'Techniques d’Analyse Physico- chimique II',
                          'abriv': 'TAPC2',
                          'nb_cour': 1,
                          'nb_td': 0,
                          'nb_tp': 0}],
                        [{'Name': 'Thermodynamique des Solutions ',
                          'abriv': 'TS',
                          'nb_cour': 2,
                          'nb_td': 1,
                          'nb_tp': 0},
                         {'Name': 'Electrochimie',
                          'abriv': 'ElecChemi',
                          'nb_cour': 2,
                          'nb_td': 1,
                          'nb_tp': 0},
                         {'Name': 'Spectroscopie Moléculaire',
                          'abriv': 'SpecMol',
                          'nb_cour': 2,
                          'nb_td': 1,
                          'nb_tp': 0},
                         {'Name': 'Chimie des Surfaces et catalyse',
                          'abriv': 'CSC',
                          'nb_cour': 2,
                          'nb_td': 1,
                          'nb_tp': 0},
                         {'Name': 'Ethique et Déontologie',
                          'abriv': 'Ethique',
                          'nb_cour': 1,
                          'nb_td': 0,
                          'nb_tp': 0},
                         {'Name': 'Anglais Scientifique ',
                          'abriv': 'Anglais',
                          'nb_cour': 1,
                          'nb_td': 0,
                          'nb_tp': 0}],
                        [{'Name': 'Physique des semiconducteurs',
                          'abriv': 'PhysSemiC',
                          'nb_cour': 2,
                          'nb_td': 1,
                          'nb_tp': 0},
                         {'Name': 'Physique statistique II  ',
                          'abriv': 'PhysicStat2',
                          'nb_cour': 2,
                          'nb_td': 1,
                          'nb_tp': 0},
                         {'Name': 'Méthodes numériques de simulation',
                          'abriv': 'MNS',
                          'nb_cour': 1,
                          'nb_td': 1,
                          'nb_tp': 0},
                         {'Name': 'Spectroscopie atomique et moléculaire',
                          'abriv': 'SAM',
                          'nb_cour': 2,
                          'nb_td': 1,
                          'nb_tp': 0},
                         {'Name': 'Anglais',
                          'abriv': 'Anglais',
                          'nb_cour': 1,
                          'nb_td': 0,
                          'nb_tp': 0}]]
        self.module_assignments = [[[{'number': 1, 'prof_name': 96, 'type': 1},
                                     {'number': 1, 'prof_name': 110, 'type': 1},
                                     {'number': 2, 'prof_name': 71, 'type': 2},
                                     {'number': 2, 'prof_name': 96, 'type': 2},
                                     {'number': 2, 'prof_name': 99, 'type': 2},
                                     {'number': 4, 'prof_name': 66, 'type': 2},
                                     {'number': 2, 'prof_name': 91, 'type': 2},
                                     {'number': 2, 'prof_name': 100, 'type': 2}],
                                    [{'number': 2, 'prof_name': 68, 'type': 1},
                                     {'number': 5, 'prof_name': 105, 'type': 2},
                                     {'number': 4, 'prof_name': 104, 'type': 2},
                                     {'number': 5, 'prof_name': 101, 'type': 2}],
                                    [{'number': 2, 'prof_name': 39, 'type': 1},
                                     {'number': 1, 'prof_name': 39, 'type': 2},
                                     {'number': 3, 'prof_name': 46, 'type': 2},
                                     {'number': 4, 'prof_name': 19, 'type': 2},
                                     {'number': 3, 'prof_name': 12, 'type': 2},
                                     {'number': 1, 'prof_name': 107, 'type': 2},
                                     {'number': 2, 'prof_name': 34, 'type': 2},
                                     {'number': 1, 'prof_name': 39, 'type': 3},
                                     {'number': 3, 'prof_name': 46, 'type': 3},
                                     {'number': 4, 'prof_name': 19, 'type': 3},
                                     {'number': 3, 'prof_name': 12, 'type': 3},
                                     {'number': 1, 'prof_name': 107, 'type': 3},
                                     {'number': 2, 'prof_name': 34, 'type': 3}],
                                    [{'number': 2, 'prof_name': 38, 'type': 1},
                                     {'number': 3, 'prof_name': 38, 'type': 2},
                                     {'number': 8, 'prof_name': 35, 'type': 2},
                                     {'number': 3, 'prof_name': 31, 'type': 2}],
                                    [{'number': 2, 'prof_name': 89, 'type': 1},
                                     {'number': 1, 'prof_name': 89, 'type': 2},
                                     {'number': 2, 'prof_name': 60, 'type': 2},
                                     {'number': 5, 'prof_name': 102, 'type': 2},
                                     {'number': 2, 'prof_name': 61, 'type': 2},
                                     {'number': 2, 'prof_name': 86, 'type': 2},
                                     {'number': 2, 'prof_name': 95, 'type': 2}],
                                    [{'number': 2, 'prof_name': 41, 'type': 1}],
                                    [{'number': 2, 'prof_name': 84, 'type': 1},
                                     {'number': 4, 'prof_name': 84, 'type': 3},
                                     {'number': 5, 'prof_name': 92, 'type': 3},
                                     {'number': 3, 'prof_name': 87, 'type': 3},
                                     {'number': 2, 'prof_name': 93, 'type': 3}],
                                    [{'number': 2, 'prof_name': 59, 'type': 1},
                                     {'number': 4, 'prof_name': 59, 'type': 2},
                                     {'number': 5, 'prof_name': 50, 'type': 2},
                                     {'number': 5, 'prof_name': 77, 'type': 2}]],
                                   [[{'number': 1, 'prof_name': 22, 'type': 1},
                                     {'number': 3, 'prof_name': 22, 'type': 2},
                                     {'number': 3, 'prof_name': 21, 'type': 2},
                                     {'number': 3, 'prof_name': 82, 'type': 2},
                                     {'number': 3, 'prof_name': 22, 'type': 3},
                                     {'number': 3, 'prof_name': 21, 'type': 3},
                                     {'number': 3, 'prof_name': 82, 'type': 3}],
                                    [{'number': 1, 'prof_name': 47, 'type': 1},
                                     {'number': 3, 'prof_name': 47, 'type': 2},
                                     {'number': 2, 'prof_name': 49, 'type': 2},
                                     {'number': 2, 'prof_name': 31, 'type': 2},
                                     {'number': 2, 'prof_name': 29, 'type': 2},
                                     {'number': 3, 'prof_name': 47, 'type': 3},
                                     {'number': 3, 'prof_name': 31, 'type': 3},
                                     {'number': 3, 'prof_name': 40, 'type': 3}],
                                    [{'number': 1, 'prof_name': 74, 'type': 1},
                                     {'number': 5, 'prof_name': 74, 'type': 2},
                                     {'number': 3, 'prof_name': 79, 'type': 2},
                                     {'number': 1, 'prof_name': 83, 'type': 2},
                                     {'number': 3, 'prof_name': 83, 'type': 3},
                                     {'number': 4, 'prof_name': 23, 'type': 3},
                                     {'number': 2, 'prof_name': 80, 'type': 3}],
                                    [{'number': 1, 'prof_name': 51, 'type': 1},
                                     {'number': 3, 'prof_name': 51, 'type': 2},
                                     {'number': 6, 'prof_name': 29, 'type': 2},
                                     {'number': 7, 'prof_name': 15, 'type': 3},
                                     {'number': 2, 'prof_name': 108, 'type': 3}],
                                    [{'number': 1, 'prof_name': 2, 'type': 1},
                                     {'number': 6, 'prof_name': 2, 'type': 3},
                                     {'number': 3, 'prof_name': 23, 'type': 3}],
                                    [{'number': 1, 'prof_name': 114, 'type': 1},
                                     {'number': 5, 'prof_name': 114, 'type': 3},
                                     {'number': 4, 'prof_name': 40, 'type': 3}]],
                                   [[{'number': 1, 'prof_name': 75, 'type': 1},
                                     {'number': 7, 'prof_name': 75, 'type': 3}],
                                    [{'number': 1, 'prof_name': 16, 'type': 1},
                                     {'number': 7, 'prof_name': 16, 'type': 2}],
                                    [{'number': 1, 'prof_name': 30, 'type': 1},
                                     {'number': 7, 'prof_name': 30, 'type': 3}],
                                    [{'number': 1, 'prof_name': 44, 'type': 1},
                                     {'number': 7, 'prof_name': 44, 'type': 3}],
                                    [{'number': 1, 'prof_name': 44, 'type': 1}],
                                    [{'number': 7, 'prof_name': 44, 'type': 2}],
                                    [{'number': 1, 'prof_name': 82, 'type': 1}]],
                                   [[{'number': 1, 'prof_name': 103, 'type': 1},
                                     {'number': 2, 'prof_name': 103, 'type': 2}],
                                    [{'number': 1, 'prof_name': 73, 'type': 1},
                                     {'number': 2, 'prof_name': 73, 'type': 2}],
                                    [{'number': 1, 'prof_name': 85, 'type': 1},
                                     {'number': 2, 'prof_name': 85, 'type': 2}],
                                    [{'number': 1, 'prof_name': 58, 'type': 1},
                                     {'number': 2, 'prof_name': 58, 'type': 2}],
                                    [{'number': 1, 'prof_name': 70, 'type': 1},
                                     {'number': 2, 'prof_name': 70, 'type': 2}],
                                    [{'number': 1, 'prof_name': 98, 'type': 1},
                                     {'number': 2, 'prof_name': 98, 'type': 2}],
                                    [{'number': 1, 'prof_name': 65, 'type': 1}]],
                                   [[{'number': 1, 'prof_name': 69, 'type': 1},
                                     {'number': 2, 'prof_name': 69, 'type': 2}],
                                    [{'number': 1, 'prof_name': 97, 'type': 1},
                                     {'number': 2, 'prof_name': 97, 'type': 2}],
                                    [{'number': 1, 'prof_name': 103, 'type': 1},
                                     {'number': 2, 'prof_name': 54, 'type': 2}],
                                    [{'number': 1, 'prof_name': 57, 'type': 1},
                                     {'number': 2, 'prof_name': 64, 'type': 2}],
                                    [{'number': 1, 'prof_name': 67, 'type': 1}]],
                                   [[{'number': 1, 'prof_name': 48, 'type': 1},
                                     {'number': 2, 'prof_name': 48, 'type': 2},
                                     {'number': 2, 'prof_name': 49, 'type': 2},
                                     {'number': 2, 'prof_name': 48, 'type': 3},
                                     {'number': 2, 'prof_name': 49, 'type': 3}],
                                    [{'number': 1, 'prof_name': 108, 'type': 1},
                                     {'number': 4, 'prof_name': 108, 'type': 3}],
                                    [{'number': 1, 'prof_name': 20, 'type': 1},
                                     {'number': 4, 'prof_name': 20, 'type': 3}],
                                    [{'number': 1, 'prof_name': 32, 'type': 1},
                                     {'number': 4, 'prof_name': 32, 'type': 3}],
                                    [{'number': 1, 'prof_name': 107, 'type': 1},
                                     {'number': 4, 'prof_name': 34, 'type': 3}],
                                    [{'number': 1, 'prof_name': 4, 'type': 1},
                                     {'number': 2, 'prof_name': 4, 'type': 2},
                                     {'number': 2, 'prof_name': 83, 'type': 2},
                                     {'number': 2, 'prof_name': 4, 'type': 3},
                                     {'number': 2, 'prof_name': 83, 'type': 3}],
                                    [{'number': 1, 'prof_name': 30, 'type': 1}],
                                    [{'number': 1, 'prof_name': 80, 'type': 1},
                                     {'number': 4, 'prof_name': 80, 'type': 3}]],
                                   [[{'number': 1, 'prof_name': 51, 'type': 1},
                                     {'number': 1, 'prof_name': 51, 'type': 2},
                                     {'number': 1, 'prof_name': 51, 'type': 3}],
                                    [{'number': 1, 'prof_name': 33, 'type': 1},
                                     {'number': 1, 'prof_name': 33, 'type': 3}],
                                    [{'number': 1, 'prof_name': 20, 'type': 1},
                                     {'number': 1, 'prof_name': 20, 'type': 3}],
                                    [{'number': 1, 'prof_name': 34, 'type': 1},
                                     {'number': 1, 'prof_name': 34, 'type': 3}],
                                    [{'number': 1, 'prof_name': 44, 'type': 1},
                                     {'number': 1, 'prof_name': 44, 'type': 3}],
                                    [{'number': 1, 'prof_name': 48, 'type': 1},
                                     {'number': 1, 'prof_name': 49, 'type': 2},
                                     {'number': 1, 'prof_name': 49, 'type': 3}],
                                    [{'number': 1, 'prof_name': 4, 'type': 1},
                                     {'number': 1, 'prof_name': 4, 'type': 2}],
                                    [{'number': 1, 'prof_name': 30, 'type': 1}]],
                                   [[{'number': 1, 'prof_name': 56, 'type': 1},
                                     {'number': 1, 'prof_name': 56, 'type': 2}],
                                    [{'number': 1, 'prof_name': 55, 'type': 1},
                                     {'number': 1, 'prof_name': 55, 'type': 2}],
                                    [{'number': 1, 'prof_name': 57, 'type': 1},
                                     {'number': 1, 'prof_name': 57, 'type': 2}],
                                    [{'number': 1, 'prof_name': 62, 'type': 1},
                                     {'number': 1, 'prof_name': 62, 'type': 2}],
                                    [{'number': 1, 'prof_name': 54, 'type': 1},
                                     {'number': 1, 'prof_name': 54, 'type': 2}],
                                    [{'number': 1, 'prof_name': 90, 'type': 1},
                                     {'number': 1, 'prof_name': 90, 'type': 2}],
                                    [{'number': 1, 'prof_name': 94, 'type': 1},
                                     {'number': 1, 'prof_name': 94, 'type': 2}],
                                    [{'number': 1, 'prof_name': 63, 'type': 1}]],
                                   [[{'number': 1, 'prof_name': 88, 'type': 1},
                                     {'number': 1, 'prof_name': 88, 'type': 2}],
                                    [{'number': 1, 'prof_name': 111, 'type': 1},
                                     {'number': 1, 'prof_name': 111, 'type': 2}],
                                    [{'number': 1, 'prof_name': 112, 'type': 1},
                                     {'number': 1, 'prof_name': 112, 'type': 2}],
                                    [{'number': 1, 'prof_name': 72, 'type': 1},
                                     {'number': 1, 'prof_name': 72, 'type': 2}],
                                    [{'number': 1, 'prof_name': 109, 'type': 1},
                                     {'number': 1, 'prof_name': 109, 'type': 2},
                                     {'number': 1, 'prof_name': 109, 'type': 3}],
                                    [{'number': 1, 'prof_name': 53, 'type': 1},
                                     {'number': 1, 'prof_name': 53, 'type': 2},
                                     {'number': 1, 'prof_name': 53, 'type': 3}],
                                    [{'number': 1, 'prof_name': 100, 'type': 1}],
                                    [{'number': 1, 'prof_name': 63, 'type': 1}]],
                                   [[{'number': 1, 'prof_name': 106, 'type': 1},
                                     {'number': 4, 'prof_name': 106, 'type': 2}],
                                    [{'number': 1, 'prof_name': 7, 'type': 1},
                                     {'number': 3, 'prof_name': 7, 'type': 2},
                                     {'number': 1, 'prof_name': 36, 'type': 2}],
                                    [{'number': 1, 'prof_name': 113, 'type': 1},
                                     {'number': 4, 'prof_name': 14, 'type': 2}],
                                    [{'number': 1, 'prof_name': 3, 'type': 1},
                                     {'number': 4, 'prof_name': 3, 'type': 3}],
                                    [{'number': 1, 'prof_name': 14, 'type': 1}]],
                                   [[{'number': 1, 'prof_name': 42, 'type': 1},
                                     {'number': 1, 'prof_name': 42, 'type': 2}],
                                    [{'number': 1, 'prof_name': 52, 'type': 1},
                                     {'number': 1, 'prof_name': 52, 'type': 2}],
                                    [{'number': 1, 'prof_name': 76, 'type': 1},
                                     {'number': 1, 'prof_name': 76, 'type': 2}],
                                    [{'number': 1, 'prof_name': 1, 'type': 1},
                                     {'number': 1, 'prof_name': 1, 'type': 2}],
                                    [{'number': 1, 'prof_name': 78, 'type': 1},
                                     {'number': 1, 'prof_name': 78, 'type': 3}]],
                                   [[{'number': 1, 'prof_name': 24, 'type': 1},
                                     {'number': 1, 'prof_name': 24, 'type': 2},
                                     {'number': 1, 'prof_name': 24, 'type': 3}],
                                    [{'number': 1, 'prof_name': 0, 'type': 1},
                                     {'number': 1, 'prof_name': 0, 'type': 2}],
                                    [{'number': 1, 'prof_name': 25, 'type': 1},
                                     {'number': 1, 'prof_name': 25, 'type': 2}],
                                    [{'number': 1, 'prof_name': 5, 'type': 1},
                                     {'number': 1, 'prof_name': 5, 'type': 2},
                                     {'number': 1, 'prof_name': 5, 'type': 3}]],
                                   [[{'number': 1, 'prof_name': 45, 'type': 1},
                                     {'number': 2, 'prof_name': 45, 'type': 2}],
                                    [{'number': 1, 'prof_name': 6, 'type': 1},
                                     {'number': 2, 'prof_name': 6, 'type': 2},
                                     {'number': 2, 'prof_name': 6, 'type': 3}],
                                    [{'number': 1, 'prof_name': 27, 'type': 1},
                                     {'number': 2, 'prof_name': 27, 'type': 2},
                                     {'number': 2, 'prof_name': 27, 'type': 3}],
                                    [{'number': 1, 'prof_name': 17, 'type': 1},
                                     {'number': 2, 'prof_name': 26, 'type': 2}],
                                    [{'number': 1, 'prof_name': 81, 'type': 1},
                                     {'number': 2, 'prof_name': 81, 'type': 2}],
                                    [{'number': 1, 'prof_name': 37, 'type': 1}],
                                    [{'number': 1, 'prof_name': 9, 'type': 1}]],
                                   [[{'number': 1, 'prof_name': 8, 'type': 1},
                                     {'number': 2, 'prof_name': 8, 'type': 2},
                                     {'number': 2, 'prof_name': 36, 'type': 3}],
                                    [{'number': 1, 'prof_name': 6, 'type': 1},
                                     {'number': 2, 'prof_name': 6, 'type': 2},
                                     {'number': 2, 'prof_name': 6, 'type': 3}],
                                    [{'number': 1, 'prof_name': 11, 'type': 1},
                                     {'number': 2, 'prof_name': 11, 'type': 2}],
                                    [{'number': 1, 'prof_name': 28, 'type': 1},
                                     {'number': 2, 'prof_name': 28, 'type': 2},
                                     {'number': 2, 'prof_name': 28, 'type': 3}],
                                    [{'number': 1, 'prof_name': 36, 'type': 1}],
                                    [{'number': 1, 'prof_name': 37, 'type': 1}]],
                                   [[{'number': 1, 'prof_name': 13, 'type': 1},
                                     {'number': 1, 'prof_name': 13, 'type': 2}],
                                    [{'number': 1, 'prof_name': 18, 'type': 1},
                                     {'number': 1, 'prof_name': 18, 'type': 2}],
                                    [{'number': 1, 'prof_name': 10, 'type': 1},
                                     {'number': 1, 'prof_name': 10, 'type': 2}],
                                    [{'number': 1, 'prof_name': 115, 'type': 1},
                                     {'number': 1, 'prof_name': 115, 'type': 2}],
                                    [{'number': 1, 'prof_name': 43, 'type': 1}]]]
        self.datashows = [{"id": "ds1", "allocated": [0, 1, 2, 3, 4, 5, 6, 7, 8]},
                          {"id": "ds2", "allocated": [0, 1, 2, 3, 4, 5, 6, 7, 8]},
                          {"id": "ds3", "allocated": [0, 1, 2, 3, 4, 5, 6, 7, 8]},
                          {"id": "ds4", "allocated": [0, 1, 2, 3, 4, 5, 6, 7, 8]},
                          {"id": "ds5", "allocated": [12, 13]},
                          {"id": "ds6", "allocated": [12, 13]},
                          {"id": "ds7", "allocated": [9, 10, 11, 14]},
                          {"id": "ds8", "allocated": [9, 10, 11, 14]},
                          ]
        self.number_of_days_per_week_input = 5
        self.number_of_slots_per_day_input = 7
        self.slot_duration_input = 60
        self.starting_day_input = 1
        self.professor_availability_constraint_checked = True
        self.student_availability_constraint_checked = True

        self.room_availability_constraint_checked = True
        self.three_consecutive_sessions_constraint_checked = False
        self.two_cour_per_day_max_constraint_checked = False
        self.unique_session_daily_constraint_checked = False
        self.faculty = Faculty("FSEI-MOSTA")
        self.problem_emploi_du_temp = None

    def bind(self):

        self.ui.promo_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.professor_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.room_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.modules_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.modules_assign_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.datashows_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.timetable_tableview.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.timetable_tableview.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.pick_promo__modules_comboBox.setCurrentIndex(0)

        self.ui.promo_add_pushbutton.clicked.connect(self.promo_input)
        self.ui.promo_edit__pushbutton.clicked.connect(self.edit_promo)
        self.ui.promo_remove_pushbutton.clicked.connect(self.delete_promo)
        self.ui.prof_add_pushbutton.clicked.connect(self.prof_input)
        self.ui.prof_edit_pushbutton.clicked.connect(self.edit_prof)
        self.ui.prof_remove_pushbutton.clicked.connect(self.delete_prof)
        self.ui.room_add_pushbutton.clicked.connect(self.room_input)
        self.ui.room_edit_pushbutton.clicked.connect(self.edit_room)
        self.ui.room_remove_pushbutton.clicked.connect(self.delete_room)
        self.ui.module_add_pushbutton.clicked.connect(self.module_input)
        self.ui.module_edit_pushbutton.clicked.connect(self.edit_module)
        self.ui.module_remove_pushbutton.clicked.connect(self.delete_module)
        self.ui.assignment_add_pushbutton.clicked.connect(self.assign_input)
        self.ui.assignment_edit_pushbutton.clicked.connect(self.edit_assign_data)
        self.ui.assignment_remove_pushbutton.clicked.connect(self.delete_assign_data)
        self.ui.datashow_add_pushbutton.clicked.connect(self.datashow_input)
        self.ui.datashow_edit_pushbutton.clicked.connect(self.edit_datashow)
        self.ui.datashow_remove_pushbutton.clicked.connect(self.delete_datashow)

        self.ui.pick_promo__modules_comboBox.currentIndexChanged.connect(self.load_module_data)
        self.ui.assign_pick_promo_assign_comboBox.currentIndexChanged.connect(self.refresh_modules_combo)

        self.ui.assign_pick_promo_assign_comboBox.currentIndexChanged.connect(self.load_assign_data)
        self.ui.module_picker_comboBox.currentIndexChanged.connect(self.load_assign_data)

        self.ui.pick_promo_comboBox_TT.currentIndexChanged.connect(self.refresh_section_combo)
        self.ui.timetable_tableview.doubleClicked.connect(self.timetable_input)
        self.ui.pick_section_comboBox.currentIndexChanged.connect(self.load_timetable_data)
        self.ui.pick_promo_comboBox_TT.currentIndexChanged.connect(self.load_timetable_data)

        self.ui.days_per_week_spinBox.valueChanged.connect(self.update_options)
        self.ui.slots_perday_spinBox.valueChanged.connect(self.update_options)
        self.ui.slot_duration_spinBox.valueChanged.connect(self.update_options)
        self.ui.starting_day_comboBox.currentIndexChanged.connect(self.update_options)
        self.ui.professoravailability_checkBox.stateChanged.connect(self.update_options)
        self.ui.studentavailability_checkBox.stateChanged.connect(self.update_options)
        self.ui.roomavailability_checkBox.stateChanged.connect(self.update_options)
        self.ui.threeconsecutivemaxsessions_checkBox.stateChanged.connect(self.update_options)
        self.ui.twocourderdaymax_checkBox.stateChanged.connect(self.update_options)
        self.ui.uniquesessiondaily_checkBox.stateChanged.connect(self.update_options)

        self.load_promo_data()
        self.load_prof_data()
        self.load_room_data()
        self.load_module_data()
        self.load_assign_data()
        self.load_datashow_data()
        self.ui.spec_ribbon.currentChanged.connect(self.on_spec_tab_change)
        self.ui.ribbon.currentChanged.connect(self.on_ribbon_tab_change)

        # self.ui.verticalLayout_15.removeWidget(self.ui.timetable_tableview)
        # self.ui.verticalLayout_15.addWidget(self.ui.timetable_tableview)
        self.ui.generate_pushButton.setEnabled(True)
        self.ui.generate_pushButton.clicked.connect(self.generate_timetable)
        self.update_options()

    def promo_input(self):
        diag = PromoInputDialog()
        diag.setModal(True)
        if diag.exec():
            row = diag.get_inputs()
            insert_row_index = self.ui.promo_table.rowCount()
            self.modules.append([])
            self.module_assignments.append([])

            self.ui.promo_table.insertRow(insert_row_index)
            for j, v in enumerate(row):
                self.ui.promo_table.setItem(
                    insert_row_index, j, QTableWidgetItem(str(v)))
            self.promos.append({'Name': row[0], 'Number of Sections': row[1], 'Number of Groups': row[2],
                                'Effective per Group': row[3]})

    def load_promo_data(self):
        self.ui.promo_table.setRowCount(len(self.promos))

        for i, promo in enumerate(self.promos):
            self.ui.promo_table.setItem(i, 0, QTableWidgetItem(promo["Name"]))
            self.ui.promo_table.setItem(i, 1, QTableWidgetItem(str(promo["Number of Sections"])))
            self.ui.promo_table.setItem(i, 2, QTableWidgetItem(str(promo['Number of Groups'])))
            self.ui.promo_table.setItem(i, 3, QTableWidgetItem(str(promo['Effective per Group'])))

    def edit_promo(self):
        index = self.ui.promo_table.selectedIndexes()
        if index:
            index = index[0].row()  # cause single selection
            diag = PromoInputDialog()

            diag.name.setText(self.ui.promo_table.item(index, 0).text())
            diag.numberOfSectionsSpinBox.setValue(
                int(self.ui.promo_table.item(index, 1).text()))
            diag.numberOfGroupsSpinBox.setValue(
                int(self.ui.promo_table.item(index, 2).text()))
            diag.effectivePerGroupSpinBox.setValue(
                int(self.ui.promo_table.item(index, 3).text()))

            diag.setModal(True)
            if diag.exec():
                for j, v in enumerate(diag.get_inputs()):
                    self.ui.promo_table.setItem(
                        index, j, QTableWidgetItem(str(v)))

            data = diag.get_inputs()
            # pprint(self.promos)
            self.promos[index] = {'Name': data[0], 'Number of Sections': data[1], 'Number of Groups': data[2],
                                  'Effective per Group': data[3]}
        else:
            QMessageBox.about(self, "Error", "Please select a row")

    def delete_promo(self):
        index = self.ui.promo_table.selectedIndexes()
        if index:
            index = index[0].row()  # cause single selection
            self.ui.promo_table.removeRow(index)
            self.promos.pop(index)
            self.modules.pop(index)
            self.module_assignments.pop(index)
            for ds in self.datashows:
                # updating indexes upon removal
                ds["allocated"] = [x if x < index else x - 1 for x in ds["allocated"] if x != index]

            self.load_datashow_data()

        else:
            QMessageBox.about(self, "Error", "Please select a row")

    def prof_input(self):
        diag = ProfInputDialog()
        diag.setModal(True)
        if diag.exec():
            name = diag.get_inputs()
            insert_row_index = self.ui.professor_table.rowCount()
            self.ui.professor_table.insertRow(insert_row_index)
            self.ui.professor_table.setItem(
                insert_row_index, 0, QTableWidgetItem(name))
            self.profs.append(name)
            # print(self.profs)

    def load_prof_data(self):
        self.ui.professor_table.setRowCount(len(self.profs))
        for i, prof in enumerate(self.profs):
            self.ui.professor_table.setItem(i, 0, QTableWidgetItem(prof))
            # print(prof)
            # self.ui.promo_table.setItem(i, j, QTableWidgetItem(str(v)))

    def edit_prof(self):
        index = self.ui.professor_table.selectedIndexes()
        if index:
            index = index[0].row()  # cause single selection
            diag = ProfInputDialog()

            diag.name.setText(self.ui.professor_table.item(index, 0).text())
            diag.setModal(True)
            if diag.exec():
                self.ui.professor_table.setItem(
                    index, 0, QTableWidgetItem(diag.get_inputs()))

            # pprint(self.promos)

            self.profs[index] = diag.get_inputs()
            # print(self.profs)
        else:
            QMessageBox.about(self, "Error", "Please select a row")

    def delete_prof(self):
        index = self.ui.professor_table.selectedIndexes()
        if index:
            index = index[0].row()  # cause single selection
            self.ui.professor_table.removeRow(index)
            self.profs.pop(index)
            for i, promo_canvas in enumerate(self.module_assignments):
                for j, module in enumerate(promo_canvas):
                    promo_canvas[j] = [assignment for assignment in promo_canvas[j] if assignment["prof_name"] != index]
                    for assignment in promo_canvas[j]:
                        if assignment["prof_name"] > index:
                            assignment["prof_name"] -= 1

            print(self.module_assignments)
        else:
            QMessageBox.about(self, "Error", "Please select a row")

    def load_room_data(self):
        self.ui.room_table.setRowCount(len(self.rooms))
        for i, room in enumerate(self.rooms):
            self.ui.room_table.setItem(i, 0, QTableWidgetItem(room["Name"]))
            self.ui.room_table.setItem(i, 1, QTableWidgetItem(str(room["Capacity"])))
            self.ui.room_table.setItem(i, 2, QTableWidgetItem(room_type_from_int(room["RoomType"])))

    def room_input(self):
        diag = RoomInputDialog()
        diag.setModal(True)
        if diag.exec():
            row = diag.get_inputs()
            insert_row_index = self.ui.room_table.rowCount()
            self.ui.room_table.insertRow(insert_row_index)
            for j, v in enumerate(row):
                self.ui.room_table.setItem(
                    insert_row_index, j, QTableWidgetItem(str(v)))
            self.rooms.append(
                {'Name': row[0], 'Capacity': row[1], 'RoomType': row[2]})

    def edit_room(self):
        index = self.ui.room_table.selectedIndexes()
        if index:
            index = index[0].row()  # cause single selection
            diag = RoomInputDialog()

            diag.name.setText(self.rooms[index]["Name"])
            diag.capacitySpinBox.setValue(self.rooms[index]["Capacity"])
            diag.typecomboBox.setCurrentIndex(self.rooms[index]["RoomType"] - 1)

            diag.setModal(True)
            if diag.exec():
                name, cap, room_int = diag.get_inputs()
                self.ui.room_table.setItem(index, 0, QTableWidgetItem(name))
                self.ui.room_table.setItem(index, 1, QTableWidgetItem(str(cap)))
                self.ui.room_table.setItem(index, 2, QTableWidgetItem(room_type_from_int(room_int)))

            data = diag.get_inputs()
            # pprint(self.promos)
            self.rooms[index] = {'Name': data[0], 'Capacity': data[1], 'RoomType': data[2]}
        else:
            QMessageBox.about(self, "Error", "Please select a row")

    def delete_room(self):
        index = self.ui.room_table.selectedIndexes()
        if index:
            index = index[0].row()  # cause single selection
            self.ui.room_table.removeRow(index)
            self.rooms.pop(index)
        else:
            QMessageBox.about(self, "Error", "Please select a row to delete")

    def module_input(self):
        diag = ModuleInputDialog()
        diag.setModal(True)
        if diag.exec():
            row = diag.get_inputs()
            insert_row_index = self.ui.modules_table.rowCount()
            self.ui.modules_table.insertRow(insert_row_index)
            for j, v in enumerate(row):
                self.ui.modules_table.setItem(
                    insert_row_index, j, QTableWidgetItem(str(v)))
            promo_index = self.ui.pick_promo__modules_comboBox.currentIndex()
            self.modules[promo_index].append(
                {"Name": row[0], "abriv": row[1], "nb_cour": row[2], "nb_td": row[3], "nb_tp": row[4]})
            self.module_assignments[promo_index].append([])

    def edit_module(self):
        index = self.ui.modules_table.selectedIndexes()
        if index:
            index = index[0].row()  # cause single selection
            diag = ModuleInputDialog()

            diag.name.setText(self.ui.modules_table.item(index, 0).text())
            diag.abriv.setText(self.ui.modules_table.item(index, 1).text())
            diag.numberOfLecturesSpinBox.setValue(
                int(self.ui.modules_table.item(index, 2).text()))
            diag.numberOfTDsSpinBox.setValue(
                int(self.ui.modules_table.item(index, 3).text()))
            diag.numberOfTPsSpinBox.setValue(
                int(self.ui.modules_table.item(index, 4).text()))

            diag.setModal(True)
            if diag.exec():
                for j, v in enumerate(diag.get_inputs()):
                    self.ui.modules_table.setItem(
                        index, j, QTableWidgetItem(str(v)))

            data = diag.get_inputs()
            promo_index = self.ui.pick_promo__modules_comboBox.currentIndex()

            self.modules[promo_index][index] = {"Name": data[0], "abriv": data[1], "nb_cour": data[2], "nb_td": data[3],
                                                "nb_tp": data[4]}
        else:
            QMessageBox.about(self, "Error", "Please select a row")

    def delete_module(self):
        index = self.ui.modules_table.selectedIndexes()
        if index:
            index = index[0].row()  # cause single selection
            self.ui.modules_table.removeRow(index)
            promo_index = self.ui.pick_promo__modules_comboBox.currentIndex()
            self.modules[promo_index].pop(index)
            self.module_assignments[promo_index].pop(index)
        else:
            QMessageBox.about(self, "Error", "Please select a row")

    def load_module_data(self):
        promo_index = self.ui.pick_promo__modules_comboBox.currentIndex()
        # print(promo_index)
        self.ui.modules_table.setRowCount(len(self.modules[promo_index]))
        for i, module in enumerate(self.modules[promo_index]):
            for j, v in enumerate(module.values()):
                self.ui.modules_table.setItem(i, j, QTableWidgetItem(str(v)))
                # print(i,j,str(v))

    def on_spec_tab_change(self, i):
        # for modules we need promos
        if i == 3:
            if len(self.promos) == 0:
                self.ui.modules_tab.setEnabled(False)
                self.ui.modules_table.setRowCount(0)
                self.ui.pick_promo__modules_comboBox.clear()
                QMessageBox.information(
                    self, "", "in order to assign modules to promos u must first have promos")
            else:
                self.ui.pick_promo__modules_comboBox.clear()
                for promo in self.promos:
                    self.ui.pick_promo__modules_comboBox.addItem(promo["Name"])
                self.ui.modules_tab.setEnabled(True)
        elif i == 4:
            if len(self.promos) == 0 or any(len(modules) == 0 for modules in self.modules) or len(self.profs) == 0:
                self.ui.assignements_tab.setEnabled(False)
                self.ui.modules_assign_table.setRowCount(0)
                self.ui.assign_pick_promo_assign_comboBox.clear()

                QMessageBox.information(self, "", "in order to assign modules to promos and modules u must first have"
                                                  " promos and each promo must have at least one module")
            else:
                self.ui.assign_pick_promo_assign_comboBox.clear()
                self.ui.module_picker_comboBox.clear()
                for promo in self.promos:
                    self.ui.assign_pick_promo_assign_comboBox.addItem(promo["Name"])
                self.refresh_modules_combo()
                self.ui.assignements_tab.setEnabled(True)
        elif i == 5:
            if len(self.promos) == 0:
                self.ui.datashows_tab.setEnabled(False)
                self.ui.datashows_table.setRowCount(0)
                QMessageBox.information(self, "", "in order to add data shows to promos  u must first have at least one"
                                                  " promo")
            else:
                self.ui.datashows_tab.setEnabled(True)

    def on_ribbon_tab_change(self, i):
        if i == self.ui.ribbon.indexOf(self.ui.timetable_tab):
            there_is_promos = len(self.promos) != 0
            there_is_profs = len(self.profs) != 0
            there_is_rooms = len(self.rooms) != 0
            there_is_modules_for_each_promo = [len(modules_of_a_promo) != 0 for modules_of_a_promo in self.modules]
            there_is_assignments_for_each_module_for_each_promo = [len(assignment) != 0
                                                                   for promo_assignments in self.module_assignments
                                                                   for assignment in promo_assignments]
            conditions_to_generate = [
                there_is_promos,
                there_is_profs,
                there_is_rooms,
                *there_is_modules_for_each_promo,
                *there_is_assignments_for_each_module_for_each_promo
            ]
            if all(conditions_to_generate):
                self.ui.timetable_tab.setEnabled(True)
                self.ui.pick_promo_comboBox_TT.clear()
                self.ui.pick_promo_comboBox_TT.addItems([promo["Name"] for promo in self.promos])
                self.refresh_section_combo()
                self.update_faculty_data()

            else:
                # print(conditions_to_generate)
                self.ui.timetable_tab.setEnabled(False)
                msg_str = ""
                if not there_is_promos:
                    msg_str += "there are no promos\n"
                if not there_is_profs:
                    msg_str += "there are no profs\n"
                if not there_is_rooms:
                    msg_str += "there are no rooms\n"
                if not all(there_is_modules_for_each_promo):
                    msg_str += "some or all of the promos are missing modules\n"
                if not all(there_is_assignments_for_each_module_for_each_promo):
                    for i in range(len(self.module_assignments)):
                        for j in range(len(self.module_assignments[i])):
                            if len(self.module_assignments[i][j]) == 0:
                                msg_str += "the module called " +self.modules[i][j]["Name"] + " is missinng assigned profs\n"
                                print(self.profs.index('HOCINE N.'))

                QMessageBox.information(self, "", msg_str)
        elif i == 4:
            print("debug message")

    def update_faculty_data(self):
        resources.timeslots_per_day = self.number_of_slots_per_day_input
        resources.days_per_week = self.number_of_days_per_week_input

        promo, room, ds = self.build_data_model()
        self.faculty.list_promo = promo
        self.faculty.list_rooms = room
        self.faculty.list_datashows = ds
        Professor.cache_clear()
        # TODO MAKE EDIT FLAG HERE
        self.problem_emploi_du_temp = PET(self.faculty)
        # print(sum(len(session_list) for session_list in problem_emploi_du_temp.sessions_list))
        if self.professor_availability_constraint_checked:
            self.problem_emploi_du_temp.add_hard_constraint(ProfessorAvailability())
        if self.student_availability_constraint_checked:
            self.problem_emploi_du_temp.add_hard_constraint(StudentAvailability())
        if self.room_availability_constraint_checked:
            self.problem_emploi_du_temp.add_hard_constraint(RoomAvailability())
        if self.three_consecutive_sessions_constraint_checked:
            self.problem_emploi_du_temp.add_hard_constraint(ThreeConsecutiveMaxSessions())
        if self.two_cour_per_day_max_constraint_checked:
            self.problem_emploi_du_temp.add_hard_constraint(TwoCourPerDayMax())
        if self.unique_session_daily_constraint_checked:
            self.problem_emploi_du_temp.add_hard_constraint(UniqueSessionDaily())

    def generate_timetable(self):
        try:
            if self.problem_emploi_du_temp.solve():
                self.load_timetable_data()
            else:
                print("messed up somewhere")
        except Exception as e:
            QMessageBox.about(self, "Error", str(e))

    def refresh_section_combo(self):
        promo_index = self.ui.pick_promo_comboBox_TT.currentIndex()
        sections_range = range(1, self.promos[promo_index]["Number of Sections"] + 1)
        self.ui.pick_section_comboBox.clear()
        self.ui.pick_section_comboBox.addItems([str(section_index) for section_index in sections_range])
        self.ui.pick_section_comboBox.setCurrentIndex(0)

    def assign_input(self):

        diag = AssignModuleInputDialog(self.profs)
        diag.setModal(True)
        if diag.exec():
            row = diag.get_inputs()
            insert_row_index = self.ui.modules_assign_table.rowCount()
            self.ui.modules_assign_table.insertRow(insert_row_index)

            self.ui.modules_assign_table.setItem(insert_row_index, 0, QTableWidgetItem(self.profs[row[0]]))
            self.ui.modules_assign_table.setItem(insert_row_index, 1, QTableWidgetItem(str(row[1])))
            self.ui.modules_assign_table.setItem(insert_row_index, 2, QTableWidgetItem(session_type_from_int(row[2])))
            promo_index = self.ui.assign_pick_promo_assign_comboBox.currentIndex()
            module_index = self.ui.module_picker_comboBox.currentIndex()
            self.module_assignments[promo_index][module_index].append(
                {"prof_name": row[0], "number": row[1], "type": row[2]})

    def refresh_modules_combo(self):
        promo_index = self.ui.assign_pick_promo_assign_comboBox.currentIndex()
        self.ui.module_picker_comboBox.clear()
        for module in self.modules[promo_index]:
            self.ui.module_picker_comboBox.addItem(module["Name"])

    def load_assign_data(self):
        promo_index = self.ui.assign_pick_promo_assign_comboBox.currentIndex()
        module_index = self.ui.module_picker_comboBox.currentIndex()
        # print(promo_index)
        self.ui.modules_assign_table.setRowCount(len(self.module_assignments[promo_index][module_index]))
        for i, task in enumerate(self.module_assignments[promo_index][module_index]):
            self.ui.modules_assign_table.setItem(i, 0, QTableWidgetItem(self.profs[task['prof_name']]))
            self.ui.modules_assign_table.setItem(i, 1, QTableWidgetItem(str(task['number'])))
            session_type = session_type_from_int(task["type"])
            self.ui.modules_assign_table.setItem(i, 2, QTableWidgetItem(session_type))

    def edit_assign_data(self):
        index = self.ui.modules_assign_table.selectedIndexes()
        promo_index = self.ui.assign_pick_promo_assign_comboBox.currentIndex()
        module_index = self.ui.module_picker_comboBox.currentIndex()
        if index:
            self._extracted_from_edit_assign_data_6(promo_index, module_index, index)
        else:
            QMessageBox.about(self, "Error", "Please select a row")

    def _extracted_from_edit_assign_data_6(self, promo_index, module_index, index):
        index = index[0].row()  # cause single selection
        diag = AssignModuleInputDialog(self.profs)
        name, val, session_type = self.module_assignments[promo_index][module_index][index].values()
        session_type -= 1

        diag.SelectProfComboBox.setCurrentIndex(name)
        diag.CardinalitySpinBox.setValue(val)
        diag.type_sessionComboBox.setCurrentIndex(session_type)
        diag.setModal(True)
        if diag.exec():
            row = diag.get_inputs()
            self.ui.modules_assign_table.setItem(index, 0, QTableWidgetItem(self.profs[row[0]]))
            self.ui.modules_assign_table.setItem(index, 1, QTableWidgetItem(str(row[1])))
            self.ui.modules_assign_table.setItem(index, 2, QTableWidgetItem(session_type_from_int(row[2])))
            self.module_assignments[promo_index][module_index][index] = {"prof_name": row[0], "number": row[1],
                                                                         "type": row[2]}

    def delete_assign_data(self):
        index = self.ui.modules_assign_table.selectedIndexes()
        if index:
            index = index[0].row()  # cause single selection
            promo_index = self.ui.assign_pick_promo_assign_comboBox.currentIndex()
            module_index = self.ui.module_picker_comboBox.currentIndex()
            self.ui.modules_assign_table.removeRow(index)
            self.module_assignments[promo_index][module_index].pop(index)
        else:
            QMessageBox.about(self, "Error", "Please select a row")

    def datashow_input(self):
        diag = DataShowInputDialog(self.promos)
        diag.setModal(True)
        if diag.exec():
            name, allocations = diag.get_inputs()
            # print(name,allocations)
            str_allocations = [self.promos[i]["Name"] for i in allocations]
            insert_row_index = self.ui.datashows_table.rowCount()
            self.ui.datashows_table.insertRow(insert_row_index)
            self.ui.datashows_table.setItem(insert_row_index, 0, QTableWidgetItem(name))
            self.ui.datashows_table.setItem(insert_row_index, 1, QTableWidgetItem(",".join(str_allocations)))
            self.datashows.append({"id": name, "allocated": allocations})

    def load_datashow_data(self):
        self.ui.datashows_table.setRowCount(len(self.datashows))
        for i, ds in enumerate(self.datashows):
            name, allocations = ds.values()
            allocations = [self.promos[i]["Name"] for i in allocations]
            self.ui.datashows_table.setItem(i, 0, QTableWidgetItem(name))
            self.ui.datashows_table.setItem(i, 1, QTableWidgetItem(",".join(allocations)))

    def edit_datashow(self):
        index = self.ui.datashows_table.selectedIndexes()
        if index:
            index = index[0].row()  # cause single selection
            diag = DataShowInputDialog(self.promos)

            diag.id.setText(self.datashows[index]["id"])
            for i in self.datashows[index]["allocated"]:
                diag.promoCheckboxes[i].setEnabled(True)
            diag.setModal(True)
            if diag.exec():
                name, allocations = diag.get_inputs()
                str_allocations = [self.promos[i]["Name"] for i in allocations]
                self.ui.datashows_table.setItem(index, 0, QTableWidgetItem(name))
                self.ui.datashows_table.setItem(index, 1, QTableWidgetItem(",".join(str_allocations)))
                self.datashows[index] = {"id": name, "allocated": allocations}
                # print(self.datashows,index)
        else:
            QMessageBox.about(self, "Error", "Please select a row")

    def generate_days_slots(self):
        days_str = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        start = datetime.datetime(100, 1, 1, 8, 30, 0)
        starting_index = self.ui.starting_day_comboBox.currentIndex()
        slot_duration = self.ui.slot_duration_spinBox.value()
        slots_len = self.ui.slots_perday_spinBox.value()

        result_days = [days_str[(i + starting_index) % len(days_str)] for i in range(len(days_str))]
        result_slots = []
        for _ in range(1, slots_len + 1):
            end = start + datetime.timedelta(minutes=slot_duration)
            result_slots.append(start.strftime('%H:%M') + " - " + end.strftime('%H:%M'))
            start = end
        return result_days, result_slots

    def update_options(self):
        # this should be done asynchronously for each option but i'm lazy
        self.number_of_days_per_week_input = self.ui.days_per_week_spinBox.value()
        self.number_of_slots_per_day_input = self.ui.slots_perday_spinBox.value()
        self.ui.timetable_tableview.setRowCount(self.number_of_days_per_week_input)
        self.ui.timetable_tableview.setColumnCount(self.number_of_slots_per_day_input)
        self.ui.timetable_tableview.setHorizontalHeaderLabels([])
        self.slot_duration_input = self.ui.slot_duration_spinBox.value()
        self.starting_day_input = self.ui.starting_day_comboBox.currentIndex()
        self.professor_availability_constraint_checked = self.ui.professoravailability_checkBox.isChecked()
        self.student_availability_constraint_checked = self.ui.studentavailability_checkBox.isChecked()

        self.room_availability_constraint_checked = self.ui.roomavailability_checkBox.isChecked()
        self.three_consecutive_sessions_constraint_checked = self.ui.threeconsecutivemaxsessions_checkBox.isChecked()
        self.two_cour_per_day_max_constraint_checked = self.ui.twocourderdaymax_checkBox.isChecked()
        self.unique_session_daily_constraint_checked = self.ui.uniquesessiondaily_checkBox.isChecked()

    def delete_datashow(self):
        index = self.ui.datashows_table.selectedIndexes()
        if index:
            index = index[0].row()  # cause single selection
            self.ui.datashows_table.removeRow(index)
            self.datashows.pop(index)

    def timetable_input(self, mi):
        row = mi.row()
        column = mi.column()
        # print(row, column)
        promo_index = self.ui.pick_promo_comboBox_TT.currentIndex()
        section_index = self.ui.pick_section_comboBox.currentIndex()
        diag = SessionSetterInputDialog(self.problem_emploi_du_temp, self.faculty, promo_index, section_index, row,
                                        column)
        diag.setModal(True)
        if diag.exec():
            self.load_timetable_data()
            # # print(name,allocations)
            # str_allocations = [self.promos[i]["Name"] for i in allocations]
            # insert_row_index = self.ui.datashows_table.rowCount()
            # self.ui.datashows_table.insertRow(insert_row_index)
            # self.ui.datashows_table.setItem(insert_row_index, 0, QTableWidgetItem(name))
            # self.ui.datashows_table.setItem(insert_row_index, 1, QTableWidgetItem(",".join(str_allocations)))
            # self.datashows.append({"id": name, "allocated": allocations})

    def build_data_model(self):
        # making all the promo objects
        promo_list = [Promotion(p["Name"]) for p in self.promos]
        # adding sections to each of the promos
        for i, promo in enumerate(promo_list):
            promo.list_section = [Section(i + 1) for i in range(self.promos[i]["Number of Sections"])]
        # giving each section an close to even split of groups
        for promo_index, promo in enumerate(promo_list):
            number_of_sections = self.promos[promo_index]["Number of Sections"]
            Number_of_Groups = self.promos[promo_index]["Number of Groups"]
            group_effective = self.promos[promo_index]["Effective per Group"]

            groups_in_promo = [Group(i + 1, group_effective) for i in range(Number_of_Groups)]
            # fancy ceiling function nothing to see here
            groups_per_section = Number_of_Groups // number_of_sections + bool(Number_of_Groups % number_of_sections)
            for i in range(0, Number_of_Groups, groups_per_section):
                valid_index = i // groups_per_section
                promo.list_section[valid_index].list_group = groups_in_promo[i:i + groups_per_section]

        # making a list of modules and making a list of assignments
        list_canvases = []
        for promo_index, promo_canvas in enumerate(self.modules):
            canvas = [Module(*module.values()) for module in promo_canvas]
            list_canvases.append(canvas)
            promo_list[promo_index].canvas = canvas
            for module_index, module in enumerate(canvas):
                self.generate_cour_sessions(canvas, module_index, promo_index, promo_list)
                self.generate_td_sessions(canvas, module_index, promo_index, promo_list)
                self.generate_tp_sessions(canvas, module_index, promo_index, promo_list)
        # making a list of all the rooms
        rooms_list = [Room(room["Name"], room["RoomType"], room["Capacity"]) for room in self.rooms]
        # making a list of all the data-shows
        data_shows_list = [DataShow([promo_list[i] for ds in self.datashows for i in ds["allocated"]])]
        # finally return it all
        return promo_list, rooms_list, data_shows_list

    def generate_tp_sessions(self, canvas, module_index, promo_index, promo_list):
        assignments = self.module_assignments[promo_index][module_index]
        tp_assign = [assignment for assignment in assignments if assignment["type"] == SessionType.Tp.value]
        profs = []
        sessions_per_week = 0
        for assignment in tp_assign:
            name = self.profs[assignment["prof_name"]]
            sections_taught = assignment["number"]
            sessions_per_week = canvas[module_index].nb_tp
            profs.extend([Professor(name) for _ in range(sections_taught * sessions_per_week)])
        for sect in promo_list[promo_index].list_section:
            for group in sect.list_group:
                sect.add_required_sessions(
                    [(profs.pop(0), group, canvas[module_index], SessionType.Tp) for _ in
                     range(sessions_per_week)])
        assert len(profs) == 0

    def generate_td_sessions(self, canvas, module_index, promo_index, promo_list):
        assignments = self.module_assignments[promo_index][module_index]
        td_assign = [assignment for assignment in assignments if assignment["type"] == SessionType.Td.value]
        profs = []
        sessions_per_week = 0
        for assignment in td_assign:
            name = self.profs[assignment["prof_name"]]
            sections_taught = assignment["number"]
            sessions_per_week = canvas[module_index].nb_td
            profs.extend([Professor(name) for _ in range(sections_taught * sessions_per_week)])
        for sect in promo_list[promo_index].list_section:
            for group in sect.list_group:
                sect.add_required_sessions(
                    [(profs.pop(0), group, canvas[module_index], SessionType.Td) for _ in
                     range(sessions_per_week)])
        assert len(profs) == 0

    def generate_cour_sessions(self, canvas, module_index, promo_index, promo_list):
        assignments = self.module_assignments[promo_index][module_index]
        cour_assign = [assignment for assignment in assignments if assignment["type"] == SessionType.Cour.value]

        profs = []
        sessions_per_week = 0
        for assignment in cour_assign:
            name = self.profs[assignment["prof_name"]]
            sections_taught = assignment["number"]
            sessions_per_week = canvas[module_index].nb_cour
            profs.extend([Professor(name) for _ in range(sections_taught * sessions_per_week)])
        for sect in promo_list[promo_index].list_section:
            sect.add_required_sessions([(profs.pop(0), sect, canvas[module_index], SessionType.Cour) for _ in
                                        range(sessions_per_week)])
        assert len(profs) == 0

    def load_timetable_data(self):
        # self.ui.timetable_tableview.clear()
        promo_index = self.ui.pick_promo_comboBox_TT.currentIndex()
        section_index = self.ui.pick_section_comboBox.currentIndex()
        section_index = 0 if section_index < 0 else section_index
        # print(promo_index, section_index)
        font = QFont()
        font.setPointSize(8)
        self.ui.timetable_tableview.setRowCount(self.number_of_days_per_week_input)
        self.ui.timetable_tableview.setColumnCount(self.number_of_slots_per_day_input)
        vertical_headers, horizontal_headers = self.generate_days_slots()
        self.ui.timetable_tableview.setVerticalHeaderLabels(vertical_headers)
        self.ui.timetable_tableview.setHorizontalHeaderLabels(horizontal_headers)
        self.ui.timetable_tableview.horizontalHeader().setFont(font)
        self.ui.timetable_tableview.verticalHeader().setFont(font)
        font.setPointSize(7)
        if self.faculty.list_promo and self.problem_emploi_du_temp:
            timetable_index = sum(promo.nb_section for promo in self.faculty.list_promo[0:promo_index]) + section_index
            timetable_needed = self.problem_emploi_du_temp.section_list[timetable_index].EDT
            for i, day in enumerate(timetable_needed):
                for j, slot in enumerate(day):
                    cell_str = "\n".join(str(session) for session in slot.sessions)
                    item = QTableWidgetItem(cell_str)
                    item.setFont(font)
                    self.ui.timetable_tableview.setItem(i, j, item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    os.chdir("Gui_files")

    window = MainWindow()
    window.bind()
    window.show()

    sys.exit(app.exec())

    # TODO make session added diag for manual session setting
    # TODO parse excel data to normal gui data for testing
    # TODO make all data serializable and savable into a file
    # TODO define project file xml for saving (maybe json instead of xml)
    # TODO make open,edit,save project methods and connect them to the home tab

    # TODO OPTIONAL FEATURE custom sessions adding after TT generation
    # TODO OPTIONAL FEATURE generate professor TT in excel export
    # TODO OPTIONAL FEATURE add Professor soft unavailable times for preference
