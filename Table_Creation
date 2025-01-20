CREATE TABLE DailyNotes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    highlights TEXT,
    day_note TEXT
);



CREATE TABLE DailyImages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    daily_note_id INT NOT NULL,
    image_type VARCHAR(20) NOT NULL,
    image_path TEXT NOT NULL,
    image_note TEXT,
    FOREIGN KEY (daily_note_id) REFERENCES DailyNotes(id) ON DELETE CASCADE
);