-- USERS TABLE
CREATE TABLE Users (
    user_id  SERIAL PRIMARY KEY,
    email    VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- PROJECTS TABLE
CREATE TABLE Projects (
    project_id  SERIAL PRIMARY KEY,
    user_id     INT NOT NULL,
    name        VARCHAR(100) NOT NULL,
    description TEXT,

    CONSTRAINT fk_project_user
    FOREIGN KEY (user_id)
    REFERENCES Users(user_id)
    ON DELETE CASCADE
);

-- REVIEWS TABLE
CREATE TABLE Reviews (
    review_id      SERIAL PRIMARY KEY,
    project_id     INT NOT NULL,
    user_id        INT NOT NULL,
    filename       VARCHAR(255) NOT NULL,
    score          INT,
    readability    INT,
    accuracy       INT,
    best_practices INT,
    bugs           JSONB,
    security       VARCHAR(20),
    suggestions    JSONB,
    optimized_code TEXT,
    created_at     TIMESTAMP DEFAULT NOW(),

    CONSTRAINT fk_review_project
    FOREIGN KEY (project_id)
    REFERENCES Projects(project_id)
    ON DELETE CASCADE,

    CONSTRAINT fk_review_user
    FOREIGN KEY (user_id)
    REFERENCES Users(user_id)
    ON DELETE CASCADE
);
