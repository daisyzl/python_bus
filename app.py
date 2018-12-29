#!/usr/bin/env python
#-*-coding:utf-8-*-   
#说明:与celery有关

from celery_app import task1, task2

task1.add.delay(2, 4)

task2.multiply.delay(4, 5)

print ('end.......')