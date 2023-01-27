# gen-website.py

Generates a static HTML website with the data from the supplied TOML file.
Requires Python >=3.11 and the `markdown` package.

```
usage: gen-website [-h] [input_file] output_directory

Generates a HTML file that lists the entities on the banlist

positional arguments:
  input_file        the input TOML file to read from
  output_directory  The output path for the generated html files.

options:
  -h, --help        show this help message and exit
```
