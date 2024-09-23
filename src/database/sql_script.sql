-- Crear la tabla User
CREATE TABLE User (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    first_surname TEXT NOT NULL,
    second_surname TEXT
);

-- Crear la tabla ExerciseLog
CREATE TABLE ExerciseLog (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL, -- Usamos TEXT para almacenar la fecha en formato ISO8601, como 'YYYY-MM-DD'
    muscle TEXT NOT NULL,
    exercise_name TEXT NOT NULL,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES User(id)
);

-- Crear la tabla Repetitions
CREATE TABLE ExerciseSet (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    exercise_log_id INTEGER,
    set_number INTEGER NOT NULL,
    repetitions INTEGER NOT NULL,
    weight REAL NOT NULL, -- REAL se usa para números de punto fl,
    rest_duration INTEGER NOT NULL, -- Tiempo en segundos,
    FOREIGN KEY (exercise_log_id) REFERENCES ExerciseLog(id)
);
