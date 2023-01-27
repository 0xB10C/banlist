# gen-banlist.py

Generates a banlist from a supplied `entities.toml` file. Requires Python >=3.11.

```
usage: gen-banlist [-h] [--bantime BANTIME] [input_file] output_directory

Generates scripts to ban the IPs listed on the banlist

positional arguments:
  input_file         the input TOML file to read from
  output_directory   The output path for the generated banlist scripts.

options:
  -h, --help         show this help message and exit
  --bantime BANTIME  Ban time in seconds (used where supporte
```
