#!/usr/bin/env python
#-*-coding:utf-8-*-   
#说明:

BROKER_URL = 'redis://localhost:6379/1'

CELERY_RESULT_BACKEND='redis://localhost:6379/2'

CELERY_TIMEZONE = 'Asia/Shanghai'

#导入指定的模块
CELERY_IMPORTS =(
    'celery_app.task1',
    'celery_app.task2',

)

