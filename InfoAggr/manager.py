# -*- coding:utf-8 -*-

from download.autohome import autohome_data
from download.tencent_auto import tencent_data
from download.sina_auto import sina_auto
from download.souhu_auto import sohu

from analyse.parser import Parser

from config import *
from datetime import date,timedelta,datetime
from analyse.report import Report

class UpdateData:
    def __init__(self,source):

        flag=self.check_update()
        if flag==1:
            print('已是最新')
            return
        print('开始更新....')
        self.yestoday = str(date.today() + timedelta(days=-1))

        if 'sohu' in source:
            sohu(self.yestoday)
        print('sohu ok')
        if 'sina' in source:
            sina_auto(self.yestoday)
        print('sina ok')
        if 'tencent' in source:
            tencent_data(self.yestoday)
        print('tencent ok')
        if 'autohome' in source:
            autohome_data(self.yestoday)
        print('autohome ok')
        print('更新完成......')
        print('正在解析......')
        Parser(self.yestoday)
        print('完成......')

        return


    def check_update(self):
        yestoday=str(date.today()+timedelta(days=-1))
        path=[
            get_content_path()+yestoday+'_'+'tencent.txt',
            get_content_path() + yestoday + '_' + 'autohome.txt',
            get_content_path() + yestoday + '_' + 'sohu.txt',
            get_content_path() + yestoday + '_' + 'sina.txt',
        ]
        for p in path:
            if os.path.exists(p):
                return 1
        return 0


class ReportMaker:
    def __init__(self,start_date,end_date):
        self.date_range=self.dateRange(start_date,end_date)
        print('正在加载文件......')
        Report(self.date_range)
        print('完成......')

    def dateRange(self,beginDate, endDate):
        dates = []
        dt = datetime.strptime(beginDate, "%Y-%m-%d")
        date = beginDate[:]
        while date <= endDate:
            dates.append(date)
            dt = dt + timedelta(1)
            date = dt.strftime("%Y-%m-%d")
        return dates
