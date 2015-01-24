-- Date,Hour,Total Ontario,Northwest,Northeast,Ottawa,East,Toronto,Essa,Bruce,Southwest,Niagara,West,Tot Zones,diff

DROP TABLE IF EXISTS rawdemand;
DROP TABLE IF EXISTS demand;

CREATE TABLE rawdemand (
    the_day DATE,
    the_hour INTEGER,
    total INTEGER,
    northwest INTEGER,
    northeast INTEGER,
    ottawa INTEGER,
    east INTEGER,
    toronto INTEGER,
    essa INTEGER,
    bruce INTEGER,
    southwest INTEGER,
    niagara INTEGER,
    west INTEGER,
    zonetotal INTEGER,
    diff INTEGER
);

CREATE TABLE demand (
    the_day DATE,
    the_hour INTEGER,
    the_zone INTEGER,
    demand INTEGER,
    temperature FLOAT DEFAULT NULL
);

CREATE INDEX ON demand (the_day);
CREATE INDEX ON demand (the_zone);
CREATE INDEX ON demand (the_day, the_hour, the_zone);

COPY rawdemand FROM '/home/jrootham/dev/marketModel/data/demand/fixed2003.csv' WITH (FORMAT csv, HEADER);
COPY rawdemand FROM '/home/jrootham/dev/marketModel/data/demand/fixed2004.csv' WITH (FORMAT csv, HEADER);
COPY rawdemand FROM '/home/jrootham/dev/marketModel/data/demand/fixed2005.csv' WITH (FORMAT csv, HEADER);
COPY rawdemand FROM '/home/jrootham/dev/marketModel/data/demand/fixed2006.csv' WITH (FORMAT csv, HEADER);
COPY rawdemand FROM '/home/jrootham/dev/marketModel/data/demand/fixed2007.csv' WITH (FORMAT csv, HEADER);
COPY rawdemand FROM '/home/jrootham/dev/marketModel/data/demand/fixed2008.csv' WITH (FORMAT csv, HEADER);
COPY rawdemand FROM '/home/jrootham/dev/marketModel/data/demand/fixed2009.csv' WITH (FORMAT csv, HEADER);
COPY rawdemand FROM '/home/jrootham/dev/marketModel/data/demand/fixed2010.csv' WITH (FORMAT csv, HEADER);
COPY rawdemand FROM '/home/jrootham/dev/marketModel/data/demand/fixed2011.csv' WITH (FORMAT csv, HEADER);
COPY rawdemand FROM '/home/jrootham/dev/marketModel/data/demand/fixed2012.csv' WITH (FORMAT csv, HEADER);
COPY rawdemand FROM '/home/jrootham/dev/marketModel/data/demand/fixed2013.csv' WITH (FORMAT csv, HEADER);
