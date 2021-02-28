#  MIT License
#
#  Copyright (c) 2021 MrMatOrg
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#

import sys
import argparse
import cli_ui

import connexion

from mrmat_python_flask_api import __version__


def get_greeting(name: str = 'World') -> dict:
    return {'greeting': f'Hello {name}'}


def main() -> int:
    """
    Main entry point for the CLI

    :return: Exit code
    """
    parser = argparse.ArgumentParser(description=f'mrmat-python-flask-api - {__version__}')
    parser.add_argument('-q', '--quiet', action='store_true', dest='quiet', help='Silent operation')
    parser.add_argument('-d', '--debug', action='store_true', dest='debug', help='Debug')

    args = parser.parse_args()
    cli_ui.setup(verbose=args.debug, quiet=args.quiet, timestamp=True)

    app = connexion.App(__name__, specification_dir='swagger/')
    app.add_api('hello-api.yaml')
    app.run(port=8080)

    return 0


if __name__ == '__main__':
    sys.exit(main())
