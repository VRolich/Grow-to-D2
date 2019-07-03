"""Parent Class for 'df' Command Parsing"""

import json

from parsers import cmd_parser


class DFParser(cmd_parser.CMDParsed):
    def parser_to_json(self, byte_input):
        """Parser Byte Date to JSON for 'df' command.

        Args:
            byte_input: input date of byte type.

        Returns:
            json_dict: a data dict.
        """
        df_output = super().parser_to_dict(byte_input)

        key_list = ['Filesystem', '1K-blocks', 'Used', 'Available', 'Use%', 'Mounted on']

        df_output = super().key_verifier(df_output, key_list)
        json_dict = json.dumps(df_output)

        return json_dict
