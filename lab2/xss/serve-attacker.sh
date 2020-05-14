#!/bin/bash
gunicorn -w 1 -b 0.0.0.0:4444 --access-logfile attacker.log attacker:app
