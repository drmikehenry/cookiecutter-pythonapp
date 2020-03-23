#!/usr/bin/env python3
# coding=utf-8

import argparse
from typing import Any
import sys


__version__ = "0.1.0"

project_name = "{{cookiecutter.project_slug}}"

description = """\
{{cookiecutter.project_short_description}}
"""

epilog = """\
TODO: Epilog.
"""


_verbose = False  # type: bool


def set_verbose(verbose: bool) -> None:
    global _verbose
    _verbose = verbose


def vprint(*args: Any, **kwargs: Any) -> None:
    if _verbose:
        print(*args, flush=True, **kwargs)


def eprint(*args: Any, **kwargs: Any) -> None:
    print(*args, flush=True, **kwargs)


def iprint(*args: Any, **kwargs: Any) -> None:
    print(*args, flush=True, **kwargs)


def readme() -> None:
    import pkg_resources
    import email
    import textwrap

    try:
        dist = pkg_resources.get_distribution(project_name)
        meta = dist.get_metadata(dist.PKG_INFO)
    except (pkg_resources.DistributionNotFound, FileNotFoundError):
        eprint("Cannot access README (try installing via pip or setup.py)")
        sys.exit(1)
    msg = email.message_from_string(meta)
    desc = msg.get("Description", "").strip()
    if not desc and not msg.is_multipart():
        desc = msg.get_payload().strip()
    if not desc:
        desc = "No README found"
    if "\n" in desc:
        first, rest = desc.split("\n", 1)
        desc = "\n".join([first, textwrap.dedent(rest)])
    iprint(desc)


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=description,
        epilog=epilog,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--version", action="version", version="%(prog)s " + __version__
    )
    parser.add_argument(
        "--verbose", action="store_true", default=False, help="verbose output",
    )
    parser.add_argument(
        "--readme", action="store_true", help="display README.rst"
    )
    return parser


class Main:
    def __init__(self, args: argparse.Namespace) -> None:
        self.args = args

    def run(self) -> None:
        set_verbose(self.args.verbose)

        if self.args.readme:
            readme()
            return

        # TODO: Application logic here.


def main() -> None:
    parser = make_parser()
    args = parser.parse_args()
    try:
        m = Main(args)
        m.run()

    except KeyboardInterrupt:
        eprint("Keyboard interrupt")


if __name__ == "__main__":
    main()
