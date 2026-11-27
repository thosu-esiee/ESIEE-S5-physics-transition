-- Automatically imported ONLY when the MySQL data directory is first initialized.
USE energy_lab;
CREATE TABLE IF NOT EXISTS readings (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    measurement_date DATE NOT NULL,
    building VARCHAR(80) NOT NULL,
    energy_kwh DECIMAL(10,2) NOT NULL,
    emission_factor DECIMAL(7,4) NOT NULL
);
INSERT INTO readings (measurement_date, building, energy_kwh, emission_factor) VALUES
('2026-10-11','Library',120.50,0.0600),
('2026-10-11','Laboratory',210.20,0.0600),
('2026-10-12','Library',114.00,0.0600),
('2026-10-12','Laboratory',208.60,0.0600),
('2026-10-13','Library',118.30,0.0600),
('2026-10-13','Laboratory',199.80,0.0600),
('2026-10-14','Library',126.00,0.0600),
('2026-10-14','Laboratory',220.10,0.0600);
