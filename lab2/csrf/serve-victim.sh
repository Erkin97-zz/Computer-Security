#!/bin/bash
gunicorn -w 1 -b 0.0.0.0:8888 --access-logfile victim.log victim:app
