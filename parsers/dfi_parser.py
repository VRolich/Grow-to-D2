"""Parent Class for 'df-i' Command Parsing"""

import json

from parsers import cmd_parser


class DFIParser(cmd_parser.CMDParsed):
    def __init__(self, dictionary):
        super().__init__(dictionary=dictionary)
        self.json_dict = None

    def parser_to_json(self):
        """Parser Byte Date to JSON for 'df-i' command.

        Args:
            byte_input: input date of byte type.

        Returns:
            json_dict: a data dict.
        """
        self.dictionary = self.form_dict()

        key_list = ['Filesystem', 'Inodes', 'IUsed',
                    'IFree', 'IUse%', 'Mounted on']

        self.dictionary['result'] = super().key_verifier(
            self.dictionary['result'], key_list)
        self.json_dict = json.dumps(self.dictionary)

        return self.json_dict
