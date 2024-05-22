CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    created_at INTEGER,
    updated_at INTEGER
);
INSERT INTO user (name, password)
   SELECT name, password
       FROM (
             SELECT 'demo_user' AS name, '5c90b96a75d4f9d5a1cfaa6f532afdc8' AS password
            ) AS o
      WHERE NOT EXISTS (
                        SELECT *
                          FROM user
                         WHERE name == o.name AND password == o.password
                       );
--VALUES ('demo_user', '5c90b96a75d4f9d5a1cfaa6f532afdc8');
