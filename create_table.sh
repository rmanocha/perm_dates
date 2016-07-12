#!/bin/bash
echo "create table perm_dates (rid integer primary key, timestamp datetime, data text);" | sqlite3 perm_dates.db
