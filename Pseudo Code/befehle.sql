# Benutzer registrieren

INSERT INTO user (name, password)
VALUES ({SQL-INJECTION-PROOF-NAME}, {HASHED-PW});

# Benutzer einloggen

SELECT id, name
FROM user
WHERE name={SQL-INJECTION-PROOF-NAME} AND password={HASHED-PW};
