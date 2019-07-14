"""Parent Class for 'df' Commands Executing"""

import subprocess

from parsers import df_parser
from parsers import dfh_parser
from parsers import dfi_parser


class Executor:

    def __init__(self, cmd):
        self.cmd = cmd

    def receive_data(self):
        """Process Linux 'df' Commands.

        Args:
            send_cmd: Linux 'df'-type command.

        Returns:
            parsed_output: a data dict.
            parsed_err: an error dict.
        """
        p = subprocess.Popen(args=self.cmd.split(),
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        cmd_output, cmd_err = p.communicate()
        err = p.returncode

        if self.cmd == 'df':
            parsed_dict = df_parser.DFParser(cmd_output, cmd_err, err)
        elif self.cmd == 'df -h':
            parsed_dict = dfh_parser.DFHParser(cmd_output, cmd_err, err)
        elif self.cmd == 'df -i':
            parsed_dict = dfi_parser.DFIParser(cmd_output, cmd_err, err)
        json_dict = parsed_dict.parser_to_json()
        return json_dict


