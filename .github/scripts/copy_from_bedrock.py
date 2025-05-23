#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import argparse
import os
import shutil
from pathlib import Path


def main():
    # Read command line input parameters
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--firefox",
        required=True,
        dest="firefox_path",
        help="Path to the www-firefox-l10n local clone",
    )
    parser.add_argument(
        "--www",
        required=True,
        dest="www_path",
        help="Path to the www-l10n local clone",
    )
    args = parser.parse_args()

    # Get list of files in en folder of www-firefox-l10n
    en_path = Path(args.firefox_path) / "en"
    en_files = []
    for ftl_path in en_path.rglob("*.ftl"):
        en_files.append(str(ftl_path.relative_to("en")))

    # Get a list of locales in www-firefox-l10n
    firefox_path = Path(args.firefox_path)
    locales = [
        str(folder)
        for folder in firefox_path.iterdir()
        if folder.is_dir()
        and folder.name not in ("en", "en-US")
        and not folder.name.startswith(".")
    ]
    locales.sort()

    # Some files were moved compared to Bedrock
    # springfield_path -> bedrock_path
    file_mapping = {
        "firefox/browsers/mobile/get-app.ftl": "firefox/mobile.ftl",
        "firefox/download/desktop.ftl": "firefox/new/desktop.ftl",
        "firefox/download/download.ftl": "firefox/new/download.ftl",
        "firefox/download/platform.ftl": "firefox/new/platform.ftl",
        "firefox/more/best-browser.ftl": "firefox/browsers/best-browser.ftl",
        "firefox/more/browser-history.ftl": "firefox/browsers/history/browser-history.ftl",
        "firefox/more/faq.ftl": "firefox/faq.ftl",
        "firefox/more/more.ftl": "firefox/more.ftl",
        "firefox/more/what-is-a-browser.ftl": "firefox/browsers/history/what-is-a-browser.ftl",
        "firefox/more/windows-64-bit.ftl": "firefox/browsers/windows-64-bit.ftl",
        "newsletter/nwesletters.ftl": "mozorg/newsletters.ftl",
    }
    www_path = Path(args.www_path)

    for file in en_files:
        # Copy the file to each locale folder in www-l10n
        for locale in locales:
            src = www_path / locale / file_mapping.get(file, file)
            dest = firefox_path / locale / file
            if src.exists():
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dest)


if __name__ == "__main__":
    main()
