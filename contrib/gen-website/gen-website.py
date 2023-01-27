#!/usr/bin/env python3

import tomllib
import argparse

import markdown

REPO_OWNER = "0xB10C"
REPO_NAME = "banlist"
REPO_URL = "https://github.com/" + REPO_OWNER + "/" + REPO_NAME + "/"

DEFAULT_INPUT_FILE = "entities.toml"
OUTPUT_INDEX = "index.html"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="x-ua-compatible" content="ie=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="description" content="An optional, centralized, and likely incomplete banlist containing the IP addresses of possibly malicious entities on the Bitcoin network."/>
    <title>Bitcoin banlist</title>
    <link rel="stylesheet" href="https://cdn.simplecss.org/simple.min.css">
    <style>
        :root {{
            --accent: orange;
        }}
    </style>
  </head>
  <body>
    <header>
      <h1>Bitcoin banlist</h1>
      <p>
        An optional, centralized, and likely incomplete banlist containing the IP addresses of possibly malicious entities on the Bitcoin network.
      </p>
    </header>
    <main>
        <p>
            The banlist is available in these formats:
            <ul>
                <li>
                    Bitcoin Core bitcoin-cli: <a href="{}/blob/main/banlist_cli.txt">banlist_cli.txt</a>
                </li>
                <li>
                    Bitcoin Core GUI: <a href="{}/blob/main/banlist_gui.txt">banlist_gui.txt</a>
                </li>
                <li>
                    Plain IP list: <a href="{}/blob/main/banlist_plain.txt">banlist_plain.txt</a>
                </li>
            </ul>
            These files are not scripts. Always check the contents first before using the banlist.
        </p>
        <h2>Entities</h2>
        <hr>
        {}
    </main>
    <footer>
        <a href="https://github.com/0xb10c/banlist">GitHub ⧉</a>
    </footer>
  </body>
</html>
"""

def main():
    parser = argparse.ArgumentParser(
        prog="gen-website",
        description='Generates a HTML file that lists the entities on the banlist'
    )

    parser.add_argument('input_file', nargs='?', type=argparse.FileType('rb'), default=open(DEFAULT_INPUT_FILE, "rb"), help="the input TOML file to read from")
    parser.add_argument('output_directory', type=str, help='The output path for the generated html files.')

    args = parser.parse_args()
    data = tomllib.load(args.input_file)
    print("loaded {} entities with {} IP addresses".format(len(data["entities"]), sum(len(e["ips"]) for e in data["entities"])))

    html_content = ""

    for entity in sorted(data["entities"], key=lambda x: x["added"]):
        entity_content = ""
        entity_content += "<h3 style='margin-bottom: 1rem;'>{}</h3>\n".format(entity["name"])
        tags = ""
        for tag in entity["tags"]:
            tags += "<mark>{}</mark> ".format(tag)
        if tags != "":
            entity_content += "<span>tags: {}\n</span>".format(tags)
            entity_content += "<br>\n"
        entity_content += "<span>added: {}</span>\n".format(entity["added"])
        entity_content += markdown.markdown(entity["description"])
        for ip in entity["ips"]:
            pass
        html_content += "<div>{}</div>".format(entity_content)

    with open(args.output_directory + "/" + OUTPUT_INDEX, 'w') as findex:
        html = HTML_TEMPLATE.format(REPO_URL, REPO_URL, REPO_URL, html_content)
        findex.write(html)

if __name__ == '__main__':
    main()
