import sys

from util.supporting.settings import all_

from util.ui.ui import Ui
from util.obfuscation.obfuscate import Obfuscator

from rich import print
from rich.panel import Panel
from rich.align import Align
from rich.syntax import Syntax

from argparse import ArgumentParser


__version__ = "1.0.0"


class Main:
    def main(self):
        super_obf = all_.super_obf
        if any([args.file]):
            with open(args.file, encoding="utf8", errors="ignore") as f:
                file_content = f.read()
            print(Align.center(Panel.fit(file_content, title="Batch Content")))
            Obfuscator(args.file)
            return 0

        # initialize UI
        self.ui = Ui()

        # show main ui
        self.ui.main_ui()

        # get file location
        self.file_location = self.ui.get_user_file()

        # show inside of file (aesthetic trust)
        with open(self.file_location, encoding="utf8", errors="ignore") as f:
            syntax = Syntax(f.read(), "bat", line_numbers=True)
        print(Align.center(Panel.fit(syntax, title="Batch Content")))
        if super_obf:
            print("This is only available in the paid version of Somalifuscator.")
            input("Press any key to exit...")
        else:
            Obfuscator(self.file_location)

        return 0


if __name__ == "__main__":
    parse = ArgumentParser()
    parse.add_argument("-f", "--file", help="File to obfuscate", type=str)
    args = parse.parse_args()
    Main().main()
    sys.exit(0)
