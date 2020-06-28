CREATE TABLE movie
(
    movie_name TEXT PRIMARY KEY, -- 电影名称
    year       TEXT    NOT NULL, -- 上映日期
    length     INTEGER NOT NULL, -- 片长
    score      REAL    NOT NULL, -- 评分
    img_url    TEXT    NOT NULL, -- 图片路径
    rank       INTEGER NOT NULL,
    country    TEXT    NOT NULL
);
CREATE TABLE director
(
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    director_name TEXT NOT NULL,
    movie_name    TEXT NOT NULL,
    FOREIGN KEY (movie_name) REFERENCES movie (movie_name)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
CREATE TABLE actor
(
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    actor_name TEXT NOT NULL,
    movie_name TEXT NOT NULL,
    FOREIGN KEY (movie_name) REFERENCES movie (movie_name)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
CREATE TABLE comment
(
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    comm       TEXT NOT NULL,
    movie_name TEXT NOT NULL,
    FOREIGN KEY (movie_name) REFERENCES movie (movie_name)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
CREATE TABLE genre
(
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    type       TEXT NOT NULL,
    movie_name TEXT NOT NULL,
    FOREIGN KEY (movie_name) REFERENCES movie (movie_name)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);