-- Insert a record into DailyNotes
INSERT INTO DailyNotes (date, highlights, day_note) 
VALUES ('2024-12-27', 'NASDAQ is Up, INR Falling, US 10 Yr TreasuryBond yeald UP', 'US to increase Import tax, Russia - Ukrain Tension increased');

INSERT INTO DailyImages (daily_note_id, image_type, image_path, image_note)
VALUES
(1, 'Day Chart', '/Users/Downloadssample/image1.png', 'Bullish Inverted Hammer Candlestick'),
(1, '1hr Chart', '/Users/Downloadssample/image2.png', 'Failed to break open'),
(1, '15min Chart', '/Users/Downloadssample/image3.png', 'Detailed 15min chart.'),
(1, '5min Chart', '/Users/Downloadssample/image4.png', 'Short-term trends.'),
(1, '1min Chart', '//Users/Downloadssample/image5.png', 'Minute-level insights.');

