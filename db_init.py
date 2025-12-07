import sqlite3
import os


DB_PATH = '/data/rangement.db' if os.path.isdir('/data') else 'rangement.db'


SCHEMA = '''
CREATE TABLE IF NOT EXISTS blocs (
id TEXT PRIMARY KEY,
rows INTEGER,
cols INTEGER,
type TEXT
);


CREATE TABLE IF NOT EXISTS positions (
id TEXT PRIMARY KEY,
row INTEGER,
col INTEGER,
FOREIGN KEY(id) REFERENCES blocs(id)
);


CREATE TABLE IF NOT EXISTS tiroirs (
id TEXT PRIMARY KEY,
bloc_id TEXT,
position INTEGER,
FOREIGN KEY(bloc_id) REFERENCES blocs(id)
);


CREATE TABLE IF NOT EXISTS objets (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nom TEXT,
description TEXT,
tiroir_id TEXT,
FOREIGN KEY(tiroir_id) REFERENCES tiroirs(id)
);
'''


DEFAULT_BLOCKS = [
("A1", 0, 0, "carton_bazar"),
("B1", 2, 2, "2x2"),
("A2", 3, 3, "3x3"),
("B2", 3, 4, "3x4"),
("A3", 2, 1, "2x1"),
("B3", 2, 1, "2x1"),
("A4", 2, 2, "2x2"),
("B4", 2, 1, "2x1"),
("A5", 3, 3, "3x3"),
("B5", 3, 3, "3x3")
]


# Default positions following your original layout (col 1=left, col 2=right)
print('DB initialized at', DB_PATH)
