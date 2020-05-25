#!/usr/bin/env python3
# coding=utf-8

import argparse
from typing import Any


__version__ = "0.1.0"

project_name = "{{cookiecutter.project_slug}}"

description = """\
{{cookiecutter.project_short_description}}
"""

epilog = """\
See ``{project_name} --readme`` for more details.
""".format(
    project_name=project_name
)
""

VERBOSITY_ERROR = 0
VERBOSITY_INFO = 1
VERBOSITY_VERBOSE = 2
VERBOSITY_VVERBOSE = 3
_max_verbosity = VERBOSITY_INFO


def get_max_verbosity() -> int:
    return _max_verbosity


def set_max_verbosity(max_verbosity: int) -> None:
    global _max_verbosity
    _max_verbosity = max_verbosity


def _print_verbosity(verbosity: int, *args: Any, **kwargs: Any) -> None:
    if verbosity <= _max_verbosity:
        print(*args, flush=True, **kwargs)


def vvprint(*args: Any, **kwargs: Any) -> None:
    _print_verbosity(VERBOSITY_VVERBOSE, *args, **kwargs)


def vprint(*args: Any, **kwargs: Any) -> None:
    _print_verbosity(VERBOSITY_VERBOSE, *args, **kwargs)


def iprint(*args: Any, **kwargs: Any) -> None:
    _print_verbosity(VERBOSITY_INFO, *args, **kwargs)


def eprint(*args: Any, **kwargs: Any) -> None:
    _print_verbosity(VERBOSITY_ERROR, *args, **kwargs)


def readme_from_pkg_resources() -> str:
    # This method works when the package is properly installed via "pip".
    import pkg_resources
    import email
    import textwrap

    try:
        dist = pkg_resources.get_distribution(project_name)
        meta = dist.get_metadata(dist.PKG_INFO)
    except (pkg_resources.DistributionNotFound, FileNotFoundError):
        return ""
    msg = email.message_from_string(meta)
    desc = msg.get("Description", "").strip()
    if not desc and not msg.is_multipart():
        desc = msg.get_payload().strip()
    if "\n" in desc:
        first, rest = desc.split("\n", 1)
        desc = "\n".join([first, textwrap.dedent(rest)])
    return desc


def readme_from_file() -> str:
    # This method works with PyInstaller.
    import pkgutil

    text = ""
    try:
        readme = pkgutil.get_data(project_name, "README.rst")
        if readme is not None:
            text = readme.decode("utf-8")
    except FileNotFoundError:
        text = ""
    return text


def readme() -> None:
    desc = readme_from_pkg_resources()
    if not desc:
        desc = readme_from_file()
    if not desc:
        desc = "README.rst is not available."
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
        "-v", "--verbose", action="count", default=0, help="verbose output",
    )

    parser.add_argument(
        "-q", "--quiet", action="count", default=0, help="quiet output",
    )

    parser.add_argument(
        "--readme", action="store_true", help="display README.rst"
    )
    return parser


class Main:
    def __init__(self, args: argparse.Namespace) -> None:
        self.args = args

    def run(self) -> None:
        set_max_verbosity(VERBOSITY_INFO + self.args.verbose - self.args.quiet)

        if self.args.readme:
            readme()
            return

        # TODO: Application logic here.
        vvprint("vvprint demo")
        vprint("vprint demo")
        iprint("iprint demo")
        eprint("eprint demo")


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
