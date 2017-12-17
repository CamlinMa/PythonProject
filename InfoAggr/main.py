# -*- coding:utf-8 -*-

import manager
data_source=[
    'sohu',
    'tencent',
    'sina',
    'autohome'
]
start_date='2017-01-01'
end_date='2017-11-08'

flag='report'  # report   update

if __name__=='__main__':
    m=manager
    if flag=='update':
        m.UpdateData(data_source)
    else:
        m.ReportMaker(start_date,end_date)
