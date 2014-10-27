
CREATE TABLE run (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE series (
    id SERIAL PRIMARY KEY,
    runId INTEGER REFERENCES run(id),
    name VARCHAR(50)
);

CREATE TABLE point (
    id SERIAL PRIMARY KEY,
    seriesId INTEGER REFERENCES series(id),
    sequence INTEGER,
    value REAL
);
