"""Parent Class for 'df' Command Parsing"""

import json

from parsers import cmd_parser


class DFParser(cmd_parser.CMDParsed):
    def parse_to_json(byte_input):
        """Parser Byte Date to JSON for 'df' command.

        Args:
          byte_input: input date of byte type.

        Returns:
          json_dict: a data dict.
        """
        df_output = cmd_parser.CMDParsed.parse_to_json(byte_input)

        check_keys = ['Filesystem', '1K-blocks', 'Used', 'Available', 'Use%', 'Mounted on']

        for key in df_output.keys():
            if key not in check_keys:
                del df_output[key]

        json_dict = json.dumps(df_output)

        return json_dict