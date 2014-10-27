#!/bin/sh
createdb market

psql market -f createDatabase.sql
