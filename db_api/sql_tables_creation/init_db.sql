

-- CREATE DATABASE constractors_union;


USE constractors_union;

CREATE TABLE constractor(
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(64)

);

CREATE TABLE project(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(64),
    address VARCHAR(64),
    constructor_id INT NOT NULL,
    notes VARCHAR(256),
    FOREIGN KEY(constructor_id) REFERENCES constractor(id)
    ON DELETE CASCADE
    

);

CREATE TABLE employee(
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(64),
    phone_number VARCHAR(64),
    job VARCHAR(64),
    status ENUM ("true","false") NOT NULL DEFAULT "true",
    constructor_id INT NOT NULL,
    project_id INT,
    FOREIGN KEY(project_id) REFERENCES project(id),
    FOREIGN KEY(constructor_id) REFERENCES constractor(id)
    ON DELETE CASCADE

);

CREATE TABLE time_line(
    project_id INT NOT NULL PRIMARY KEY,
    name VARCHAR(64),
    start_date VARCHAR(64) NOT NULL,
    end_date VARCHAR(64) NOT NULL,
    FOREIGN KEY(project_id) REFERENCES project(id)
    ON DELETE CASCADE

);