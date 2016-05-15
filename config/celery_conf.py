#!/usr/bin/env python
# encoding: utf-8

from __future__ import absolute_import
from kombu import Exchange, Queue

CELERY_TASK_RESULT_EXPIRES = 3600
CELERY_TASK_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_SERIALIZER = 'json'

CELERY_DEFAULT_EXCHANGE = 'tasks'
CELERY_DEFAULT_EXCHANGE_TYPE = 'direct'

CELERY_QUEUES = (
  Queue('machine1',exchange='tasks',routing_key='machine1'),
  Queue('machine2',exchange='tasks',routing_key='machine2'),
)