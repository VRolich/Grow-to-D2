"""Parent Class for 'df-i' Command Parsing"""

import json

from parsers import cmd_parser


class DFIParser(cmd_parser.CMDParsed):
    def parse_to_json(byte_input):
        """Parser Byte Date to JSON for 'df-i' command.

        Args:
          byte_input: input date of byte type.

        Returns:
          json_dict: a data dict.
        """
        dfi_output = cmd_parser.CMDParsed.parse_to_json(byte_input)

        check_keys = ['Filesystem', 'Inodes', 'IUsed', 'IFree', 'IUse%', 'Mounted on']

        for key in dfi_output.keys():
          if key not in check_keys:
            del dfi_output[key]

        json_dict = json.dumps(dfi_output)

        return json_dict