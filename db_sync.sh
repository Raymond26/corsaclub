#!/bin/bash
heroku pg:backups:capture
heroku pg:backups:download
pg_restore --verbose --clean --no-acl --no-owner -h localhost -U raymondlau -d cardb latest.dump
rm latest.dump
