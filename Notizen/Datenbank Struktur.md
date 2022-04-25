# Datenbank Struktur

## Tabellen

### User

| Feld       | Typ     |
| ---------- | ------- |
| id         | integer |
| name       | varchar |
| password   | varchar |
| registered | date    |

### Score

| Feld       | Typ     |
| ---------- | ------- |
| userid     | integer |
| gameid     | integer |
| difficulty | integer |
| win        | integer |
| loss       | integer |

### Game

| Feld | Typ     |
| ---- | ------- |
| id   | integer |
| name | varchar |
