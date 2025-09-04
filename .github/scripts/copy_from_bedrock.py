#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import argparse
import shutil
import sys
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
    parser.add_argument(
        "--locales",
        nargs="*",
        dest="locales",
        help="List of locales to copy files to",
    )
    args = parser.parse_args()

    # Get list of files in en folder of www-firefox-l10n
    en_path = Path(args.firefox_path) / "en"
    en_files = []
    for ftl_path in en_path.rglob("*.ftl"):
        en_files.append(str(ftl_path.relative_to("en")))

    # Get a list of locales in www-firefox-l10n
    firefox_path = Path(args.firefox_path)

    if args.locales:
        # Check that locales exist
        locales = [loc for loc in args.locales if (firefox_path / loc).is_dir()]
        invalid_locales = set(args.locales) - set(locales)
        if invalid_locales:
            print(f"Ignored locales: {', '.join(invalid_locales)}")
        if not locales:
            sys.exit("No valid locales found in the list provided.")
    else:
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
        "firefox/whatsnew/developer/evergreen.ftl": "firefox/developer.ftl",
        "firefox/whatsnew/evergreen.ftl": "firefox/whatsnew/whatsnew.ftl",
        "firefox/whatsnew/nightly/evergreen.ftl": "firefox/nightly/whatsnew.ftl",
    }
    www_path = Path(args.www_path)

    for file in en_files:
        # Only copy files explicitly listed in the mapping
        if file not in file_mapping:
            continue
        # Copy the file to each locale folder in www-l10n
        for locale in locales:
            src = www_path / locale / file_mapping.get(file, file)
            dest = firefox_path / locale / file
            if src.exists():
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dest)


if __name__ == "__main__":
    main()
