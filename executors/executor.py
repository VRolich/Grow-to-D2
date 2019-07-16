"""Parent Class for 'df' Commands Executing"""

import subprocess


class Executor:

    def __init__(self, cmd, parser):
        self.cmd = cmd
        self.parser = parser

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

        json_dict = self.parser(cmd_output, cmd_err, err).parser_to_json()
        return json_dict


