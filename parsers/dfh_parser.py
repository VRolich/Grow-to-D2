"""Parent Class for 'df-h' Command Parsing"""

import json

from parsers import cmd_parser


class DFHParser(cmd_parser.CMDParsed):

    def parser_to_json(self):
        """Parser Byte Date to JSON for 'df-f' command.

        Returns:
            json_dict: a data dict.
        """
        self._cmd_execution_result = self.dict_former()

        key_list = ['Filesystem', 'Size', 'Used',
                    'Avail', 'Use%', 'Mounted on']

        self._cmd_execution_result['result'] = self.key_verifier(
            self._cmd_execution_result['result'], key_list)
        self._json_dict = json.dumps(self._cmd_execution_result)

        return self._json_dict
