#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""helloworld level snippets."""
import requests

def main():
    msg = "Hello World"
    print(msg)
    msg = msg.capitalize()

    print(requests.__version__)

    resp = requests.get("https://sixty-north.com/c/t.txt")

    print(resp.text)

    print("done")


if __name__ == "__main__":
    # running as script, this is the main() for this package
    main()