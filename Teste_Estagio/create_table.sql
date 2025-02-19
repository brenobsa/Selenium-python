CREATE TABLE IF NOT EXISTS noticias_globo(
    id SERIAL PRIMARY KEY,
    titulo TEXT,
    link TEXT,
    data_extracao TIMESTAMP DEFAULT NOW()
);
CREATE TABLE IF NOT EXISTS noticias_tech(
    id SERIAL PRIMARY KEY,
    titulo TEXT,
    link TEXT,
    data_extracao TIMESTAMP DEFAULT NOW()
);