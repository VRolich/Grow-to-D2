"""Parent Class for 'df' Command Parsing"""

import json

from parsers import cmd_parser


class DFParser(cmd_parser.CMDParsed):
    def __init__(self, dictionary):
        super().__init__(dictionary=dictionary)
        self.json_dict = None

    def parser_to_json(self):
        """Parser Byte Date to JSON for 'df' command.
        Returns:
            json_dict: a data dict.
        """
        self.dictionary = self.form_dict()

        key_list = ['Filesystem', '1K-blocks', 'Used',
                    'Available', 'Use%', 'Mounted on']

        self.dictionary['result'] = super().key_verifier(
            self.dictionary['result'], key_list)
        self.json_dict = json.dumps(self.dictionary)

        return self.json_dict
