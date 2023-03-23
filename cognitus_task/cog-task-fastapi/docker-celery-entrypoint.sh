#!/bin/bash
celery -A tasks.celery worker -P threads -l info