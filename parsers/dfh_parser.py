"""Parent Class for 'df-h' Command Parsing"""

import json

from parsers import cmd_parser


class DFHParser(cmd_parser.CMDParsed):
    def __init__(self, dictionary):
        super().__init__(dictionary=dictionary)
        self.json_dict = None

    def parser_to_json(self):
        """Parser Byte Date to JSON for 'df-f' command.

        Returns:
            json_dict: a data dict.
        """
        self.dictionary = self.dict_former()

        key_list = ['Filesystem', 'Size', 'Used',
                    'Avail', 'Use%', 'Mounted on']

        self.dictionary['result'] = super().key_verifier(
            self.dictionary['result'], key_list)
        self.json_dict = json.dumps(self.dictionary)

        return self.json_dict
