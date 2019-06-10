"""Parent Class for 'df-h' Command Parsing"""

import json

from parsers import cmd_parser


class DFHParser(cmd_parser.CMDParsed):
    def parse_to_json(byte_input):
        """Parser Byte Date to JSON for 'df-f' command.

        Args:
          byte_input: input date of byte type.

        Returns:
          json_dict: a data dict.
        """
        dfh_output = cmd_parser.CMDParsed.parse_to_json(byte_input)

        check_keys = ['Filesystem', 'Size', 'Used', 'Avail', 'Use%', 'Mounted on']

        for key in dfh_output.keys():
            if key not in check_keys:
                del dfh_output[key]

        json_dict = json.dumps(dfh_output)

        return json_dict