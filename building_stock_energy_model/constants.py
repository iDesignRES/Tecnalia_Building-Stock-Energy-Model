# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright (c) 2025 Tecnalia Research & Innovation


VERSION = 'v0.9.5'
SCIENTIFIC_NOTATION = False
WINTER_TEMPERATURE = 12
SUMMER_TEMPERATURE = 22.5
SAVE_RESULT_ALLOWED = False

DATABASE = ['database/01-ACH.csv',
            'database/02-BaseTemperatures.csv',
            'database/03-BES_Capacity.csv',
            'database/04-BES_CAPEX.csv',
            'database/05-BES_OPEX.csv',
            'database/06-DemandNinja_Radiation_DB.csv',
            'database/07-DemandNinja_Temperature_DB.csv',
            'database/08-DHW&InternalGains.csv',
            'database/09-DwellingSizeAndShare.csv',
            'database/13-R_T_hh_eff.xlsx',
            'database/14-RES.csv',
            'database/15-RES_hh_tes.xlsx',
            'database/16-RetrofittingCost.csv',
            'database/17-RetrofittingUValues.csv',
            'database/18-Schedule.csv',
            'database/19-SER_hh_tes.xlsx',
            'database/20-SolarGainsNONOffice(Wm2).csv',
            'database/21-SolarGainsOffice(Wm2).csv',
            'database/22-UValues.csv',
            'database/23-YearPeriods.csv',
            'database/24-Sectors.csv',
            'database/25-CategorizationShare.csv',
            'database/26-Season.csv',
            'database/27-Calendar.csv']

BUILDING_USES = ['Apartment Block',
                 'Single family- Terraced houses',
                 'Hotels and Restaurants',
                 'Health',
                 'Education',
                 'Offices',
                 'Trade',
                 'Other non-residential buildings',
                 'Sport']

REGIONS = 'AL01,AL02,AL03,AT11,AT12,AT13,AT21,AT22,AT31,AT32,AT33,AT34,' \
          'BE10,BE21,BE22,BE23,BE24,BE25,BE31,BE32,BE33,BE34,BE35,BG31,' \
          'BG32,BG33,BG34,BG41,BG42,CH01,CH02,CH03,CH04,CH05,CH06,CH07,' \
          'CY00,CZ01,CZ02,CZ03,CZ04,CZ05,CZ06,CZ07,CZ08,DE11,DE12,DE13,' \
          'DE14,DE21,DE22,DE23,DE24,DE25,DE26,DE27,DE30,DE40,DE50,DE60,' \
          'DE71,DE72,DE73,DE80,DE91,DE92,DE93,DE94,DEA1,DEA2,DEA3,DEA4,' \
          'DEA5,DEB1,DEB2,DEB3,DEC0,DED2,DED4,DED5,DEE0,DEF0,DEG0,DK01,' \
          'DK02,DK03,DK04,DK05,EE00,EL30,EL41,EL42,EL43,EL51,EL52,EL53,' \
          'EL54,EL61,EL62,EL63,EL64,EL65,ES11,ES12,ES13,ES21,ES22,ES23,' \
          'ES24,ES30,ES41,ES42,ES43,ES51,ES52,ES53,ES61,ES62,ES63,ES64,' \
          'FI19,FI1B,FI1C,FI1D,FI20,FR10,FRB0,FRC1,FRC2,FRD1,FRD2,FRE1,' \
          'FRE2,FRF1,FRF2,FRF3,FRG0,FRH0,FRI1,FRI2,FRI3,FRJ1,FRJ2,FRK1,' \
          'FRK2,FRL0,FRM0,HR02,HR03,HR05,HR06,HU11,HU12,HU21,HU22,HU23,' \
          'HU31,HU32,HU33,IE04,IE05,IE06,IS00,ITC1,ITC2,ITC3,ITC4,ITF1,' \
          'ITF2,ITF3,ITF4,ITF5,ITF6,ITG1,ITG2,ITH1,ITH2,ITH3,ITH4,ITH5,' \
          'ITI1,ITI2,ITI3,ITI4,LI00,LT01,LT02,LU00,LV00,ME00,MK00,MT00,' \
          'NL11,NL12,NL13,NL21,NL22,NL23,NL32,NL34,NL35,NL36,NL41,NL42,' \
          'NO02,NO06,NO07,NO08,NO09,NO0A,NO0B,PL21,PL22,PL41,PL42,PL43,' \
          'PL51,PL52,PL61,PL62,PL63,PL71,PL72,PL81,PL82,PL84,PL91,PL92,' \
          'PT11,PT15,PT19,PT1A,PT1B,PT1C,PT1D,PT20,PT30,RO11,RO12,RO21,' \
          'RO22,RO31,RO32,RO41,RO42,RS11,RS12,RS21,RS22,SE11,SE12,SE21,' \
          'SE22,SE23,SE31,SE32,SE33,SI03,SI04,SK01,SK02,SK03,SK04,TR10,' \
          'TR21,TR22,TR31,TR32,TR33,TR41,TR42,TR51,TR52,TR61,TR62,TR63,' \
          'TR71,TR72,TR81,TR82,TR83,TR90,TRA1,TRA2,TRB1,TRB2,TRC1,TRC2,' \
          'TRC3,UA11,UA12,UA13,UA14,UA21,UA22,UA31,UA32,UA33,UA41,UA42,' \
          'UA43,UA44,UA45,UA51,UA52,UA53,UA61,UA62,UA63,UA71,UA72,UA73,' \
          'UA74,UA81,UA82,UA83,XK00'
REGION_LIST = [region.strip() for region in REGIONS.split(',')]

LEVELS = ['High', 'Medium', 'Low']
