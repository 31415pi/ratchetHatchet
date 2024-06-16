# ratchetHatchet
Development drop zone for whatever I discover (and the tools used in) hacking the Ratchet Eurorack Module by Schottkey Modular.

## Initial scripts to explore the save binary

### csv2bin/c2b.py
Converts a CSV into a save file binary.
CSV format is 64 width x 3 rows:
- Row 1: Step 0=off 1=on
- Row 2: Gate 0-6; If step is 1, gate must be 1
- Row 3: Ratchet 0-f, default 0

### bin2csv/b2c.py
Converts a save file binary into a CSV.
