"""Parent Class for 'df-h' Command Parsing"""

import json

from parsers import cmd_parser


class DFHParser(cmd_parser.CMDParsed):
    def parser_to_json(self, byte_input):
        """Parser Byte Date to JSON for 'df-f' command.

        Args:
            byte_input: input date of byte type.

        Returns:
            json_dict: a data dict.
        """
        dfh_output = super().parser_to_dict(byte_input)

        key_list = ['Filesystem', 'Size', 'Used', 'Avail', 'Use%', 'Mounted on']

        dfh_output = cmd_parser.CMDParsed.key_verifier(dfh_output, key_list)
        json_dict = json.dumps(dfh_output)

        return json_dict
