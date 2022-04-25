CREATE DATABASE IF NOT EXISTS JahresAbschlussProjektGruppe1;
USE JahresAbschlussProjektGruppe1;

CREATE TABLE user (
    id INT(255) PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL,
    password VARCHAR(30) NOT NULL,
    registered TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE game (
    id INT(255) PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL
);

CREATE TABLE score (
    userid INT(255),
    gameid INT(255),
    difficulty INT(255),
    win INT(255),
    loss INT(255),
    PRIMARY KEY(userid, gameid, difficulty)
);