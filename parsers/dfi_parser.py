"""Parent Class for 'df-i' Command Parsing"""

import json

from parsers import cmd_parser


class DFIParser(cmd_parser.CMDParsed):
    def parser_to_json(self, byte_input):
        """Parser Byte Date to JSON for 'df-i' command.

        Args:
            byte_input: input date of byte type.

        Returns:
            json_dict: a data dict.
        """
        dfi_output = cmd_parser.CMDParsed.parser_to_dict(byte_input)

        key_list = ['Filesystem', 'Inodes', 'IUsed', 'IFree', 'IUse%', 'Mounted on']

        dfi_output = cmd_parser.CMDParsed.key_verifier(dfi_output, key_list)
        json_dict = json.dumps(dfi_output)

        return json_dict
