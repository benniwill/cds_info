# -*- coding: utf-8 -*-
from GERICS_ERA5_DownloadMask import *
import sys
import os
import cdsapi
import datetime as dt
# - - - - - - - - - - - -
class Downi(Ui_DownloadTool):
    def __init__(self,window):
        self.setupUi()
        self.starter.clicked.connect(self.downmask)
        
    def downmask(self):
        x = "Logfile_" + dt.datetime.now().strftime("%d_%b_%Y_%Hh%M") + ".txt"
        f = open(x,'w+')
        f.writelines('*-#-*-#-*-#-*-#-*-#-*-#-*-#-*-#-*-#-*-#-*')
        f.writelines('\nStarting Logfile at : ' + str(dt.datetime.now()))
        f.writelines('\n*-#-*-#-*-#-*-#-*-#-*-#-*-#-*-#-*-#-*-#-*')
                
        # read year
        f.writelines('\n*-#-*-#-*-#-*-#-*-#-*-#-*-#-*-#-*-#-*-#-*')
        f.writelines('\n'+str(dt.datetime.now())+'| Reading year checkboxes')
        jahr = []
        if self.y1969.isChecked() == True:
            jahr.append('1969')
        if self.y1970.isChecked() == True:
            jahr.append('1970')
        if self.y1971.isChecked() == True:
            jahr.append('1971')
        if self.y1972.isChecked() == True:
            jahr.append('1972')
        if self.y1973.isChecked() == True:
            jahr.append('1973')
        if self.y1974.isChecked() == True:
            jahr.append('1974')
        if self.y1975.isChecked() == True:
            jahr.append('1975')
        if self.y1976.isChecked() == True:
            jahr.append('1976')
        if self.y1977.isChecked() == True:
            jahr.append('1977')
        if self.y1978.isChecked() == True:
            jahr.append('1978')
        if self.y1979.isChecked() == True:
            jahr.append('1979')
        if self.y1980.isChecked() == True:
            jahr.append('1980')
        if self.y1981.isChecked() == True:
            jahr.append('1981')
        if self.y1982.isChecked() == True:
            jahr.append('1982')
        if self.y1983.isChecked() == True:
            jahr.append('1983')
        if self.y1984.isChecked() == True:
            jahr.append('1984')
        if self.y1985.isChecked() == True:
            jahr.append('1985')
        if self.y1986.isChecked() == True:
            jahr.append('1986')
        if self.y1987.isChecked() == True:
            jahr.append('1987')
        if self.y1988.isChecked() == True:
            jahr.append('1988')
        if self.y1989.isChecked() == True:
            jahr.append('1989')
        if self.y1990.isChecked() == True:
            jahr.append('1990')
        if self.y1991.isChecked() == True:
            jahr.append('1991')
        if self.y1992.isChecked() == True:
            jahr.append('1992')
        if self.y1993.isChecked() == True:
            jahr.append('1993')
        if self.y1994.isChecked() == True:
            jahr.append('1994')
        if self.y1995.isChecked() == True:
            jahr.append('1995')
        if self.y1996.isChecked() == True:
            jahr.append('1996')
        if self.y1997.isChecked() == True:
            jahr.append('1997')
        if self.y1998.isChecked() == True:
            jahr.append('1998')
        if self.y1999.isChecked() == True:
            jahr.append('1999')
        if self.y2000.isChecked() == True:
            jahr.append('2000')
        if self.y2001.isChecked() == True:
            jahr.append('2001')
        if self.y2002.isChecked() == True:
            jahr.append('2002')
        if self.y2003.isChecked() == True:
            jahr.append('2003')
        if self.y2004.isChecked() == True:
            jahr.append('2004')
        if self.y2005.isChecked() == True:
            jahr.append('2005')
        if self.y2006.isChecked() == True:
            jahr.append('2006')
        if self.y2007.isChecked() == True:
            jahr.append('2007')
        if self.y2008.isChecked() == True:
            jahr.append('2008')
        if self.y2009.isChecked() == True:
            jahr.append('2009')
        if self.y2010.isChecked() == True:
            jahr.append('2010')
        if self.y2011.isChecked() == True:
            jahr.append('2011')
        if self.y2012.isChecked() == True:
            jahr.append('2012')
        if self.y2013.isChecked() == True:
            jahr.append('2013')
        if self.y2014.isChecked() == True:
            jahr.append('2014')
        if self.y2015.isChecked() == True:
            jahr.append('2015')
        if self.y2016.isChecked() == True:
            jahr.append('2016')
        if self.y2017.isChecked() == True:
            jahr.append('2017')
        if self.y2018.isChecked() == True:
            jahr.append('2018')
        if self.y2019.isChecked() == True:
            jahr.append('2019')
        if self.y2020.isChecked() == True:
            jahr.append('2020')
        #if self.y2021.isChecked() == True:
        #    jahr.append('2021')
        #if self.y2022.isChecked() == True:
        #    jahr.append('2022')
        f.writelines('\nYear loop finished at :' + str(dt.datetime.now()))
        f.writelines('\n*-#-*-#-*-#-*-#-*-#-*-#-*-#-*-#-*-#-*-#-*')
        
        # read month
        f.writelines('\n'+str(dt.datetime.now())+'| Reading month checkboxes')
        monat = []
        if self.allmonths.isChecked() == True:
            monat = ['01','02','03','04','05','06','07','08','09','10','11','12']
        if self.m_jan.isChecked() == True:
            monat.append('01')
        if self.m_feb.isChecked() == True:
            monat.append('02')
        if self.m_mar.isChecked() == True:
            monat.append('03')
        if self.m_apr.isChecked() == True:
            monat.append('04')
        if self.m_may.isChecked() == True:
            monat.append('05')
        if self.m_jun.isChecked() == True:
            monat.append('06')
        if self.m_jul.isChecked() == True:
            monat.append('07')
        if self.m_aug.isChecked() == True:
            monat.append('08')
        if self.m_sep.isChecked() == True:
            monat.append('09')
        if self.m_oct.isChecked() == True:
            monat.append('10')
        if self.m_nov.isChecked() == True:
            monat.append('11')
        if self.m_dec.isChecked() == True:
            monat.append('12')
        f.writelines('\nMonth loop finished at ' + str(dt.datetime.now()))
        f.writelines('\n*-#-*-#-*-#-*-#-*-#-*-#-*-#-*-#-*-#-*-#-*')
        
        # read day
        f.writelines('\n'+str(dt.datetime.now())+'| Reading day checkboxes')
        tag = []
        if self.alldays.isChecked() == True:
            tag = ['01','02','03','04','05','06','07','08','09','10','11','12',
                   '13','14','15','16','17','18','19','20','21','22','23','24',
                   '25','26','27','28','29','30','31']
        if self.d_01.isChecked() == True:
            tag.append('01')
        if self.d_02.isChecked() == True:
            tag.append('02')
        if self.d_03.isChecked() == True:
            tag.append('03')
        if self.d_04.isChecked() == True:
            tag.append('04')
        if self.d_05.isChecked() == True:
            tag.append('05')
        if self.d_06.isChecked() == True:
            tag.append('06')
        if self.d_07.isChecked() == True:
            tag.append('07')
        if self.d_08.isChecked() == True:
            tag.append('08')
        if self.d_09.isChecked() == True:
            tag.append('09')
        if self.d_10.isChecked() == True:
            tag.append('10')
        if self.d_11.isChecked() == True:
            tag.append('11')
        if self.d_12.isChecked() == True:
            tag.append('12')
        if self.d_13.isChecked() == True:
            tag.append('13')
        if self.d_14.isChecked() == True:
            tag.append('14')
        if self.d_15.isChecked() == True:
            tag.append('15')
        if self.d_16.isChecked() == True:
            tag.append('16')
        if self.d_17.isChecked() == True:
            tag.append('17')
        if self.d_18.isChecked() == True:
            tag.append('18')
        if self.d_19.isChecked() == True:
            tag.append('19')
        if self.d_20.isChecked() == True:
            tag.append('20')
        if self.d_21.isChecked() == True:
            tag.append('21')
        if self.d_22.isChecked() == True:
            tag.append('22')
        if self.d_23.isChecked() == True:
            tag.append('23')
        if self.d_24.isChecked() == True:
            tag.append('24')
        if self.d_25.isChecked() == True:
            tag.append('25')
        if self.d_26.isChecked() == True:
            tag.append('26')
        if self.d_27.isChecked() == True:
            tag.append('27')
        if self.d_28.isChecked() == True:
            tag.append('28')
        if self.d_29.isChecked() == True:
            tag.append('29')
        if self.d_30.isChecked() == True:
            tag.append('30')
        if self.d_31.isChecked() == True:
            tag.append('31')
        f.writelines('\nDay loop finished at ' + str(dt.datetime.now()))
        f.writelines('\n*-#-*-#-*-#-*-#-*-#-*-#-*-#-*-#-*-#-*-#-*')
        
        # read time
        f.writelines('\n'+str(dt.datetime.now())+'| Reading time checkboxes')
        zeit = []
        if self.t_0.isChecked() == True:
            zeit.append('00:00')
        if self.t_1.isChecked() == True:
            zeit.append('01:00')
        if self.t_2.isChecked() == True:
            zeit.append('02:00')
        if self.t_3.isChecked() == True:
            zeit.append('03:00')
        if self.t_4.isChecked() == True:
            zeit.append('04:00')
        if self.t_5.isChecked() == True:
            zeit.append('05:00')
        if self.t_6.isChecked() == True:
            zeit.append('06:00')
        if self.t_7.isChecked() == True:
            zeit.append('07:00')
        if self.t_8.isChecked() == True:
            zeit.append('08:00')
        if self.t_9.isChecked() == True:
            zeit.append('09:00')
        if self.t_10.isChecked() == True:
            zeit.append('10:00')
        if self.t_11.isChecked() == True:
            zeit.append('11:00')
        if self.t_12.isChecked() == True:
            zeit.append('12:00')
        if self.t_13.isChecked() == True:
            zeit.append('13:00')
        if self.t_14.isChecked() == True:
            zeit.append('14:00')
        if self.t_15.isChecked() == True:
            zeit.append('15:00')
        if self.t_16.isChecked() == True:
            zeit.append('16:00')
        if self.t_17.isChecked() == True:
            zeit.append('17:00')
        if self.t_18.isChecked() == True:
            zeit.append('18:00')
        if self.t_19.isChecked() == True:
            zeit.append('19:00')
        if self.t_20.isChecked() == True:
            zeit.append('20:00')
        if self.t_21.isChecked() == True:
            zeit.append('21:00')
        if self.t_22.isChecked() == True:
            zeit.append('22:00')
        if self.t_23.isChecked() == True:
            zeit.append('23:00')
        f.writelines('\nTime loop finished at ' + str(dt.datetime.now()))
        f.writelines('\n*-#-*-#-*-#-*-#-*-#-*-#-*-#-*-#-*-#-*-#-*')
        
        # check 
        if self.modell.currentText() == "ERA5 Hourly Data 1979 - 2020" or self.modell.currentText() == "ERA5 Monthly Data 1979 - 2020":
            typ = 'reanalysis-era5-single-levels'
            if self.allyears.isChecked == True:
                jahr = ['1979','1980','1981','1982','1983','1984','1985','1986',
                        '1987','1988','1989','1990','1991','1992','1993','1994',
                        '1995','1996','1997','1998','1999','2000','2001','2002',
                        '2003','2004','2005','2006','2007','2008','2009','2010',
                        '2011','2012','2013','2014','2015','2016','2017','2018',
                        '2019','2020']
            f.writelines('\n'+str(dt.datetime.now())+'| Input:')
            f.writelines('\n'+jahr)