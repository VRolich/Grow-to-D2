"""Parent Class for 'df-i' Command Parsing"""

import json

from parsers import cmd_parser


class DFIParser(cmd_parser.CMDParsed):

    def parser_to_json(self):
        """Parser Byte Date to JSON for 'df-i' command.

        Args:
            byte_input: input date of byte type.

        Returns:
            json_dict: a data dict.
        """
        self._cmd_execution_result = self.dict_former()

        key_list = ['Filesystem', 'Inodes', 'IUsed',
                    'IFree', 'IUse%', 'Mounted on']

        self._cmd_execution_result['result'] = super().key_verifier(
            self._cmd_execution_result['result'], key_list)
        self._json_dict = json.dumps(self._cmd_execution_result)

        return self._json_dict
