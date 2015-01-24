#!/bin/bash

psql market -c DateStyle='dmy' -f copyDemand.sql
