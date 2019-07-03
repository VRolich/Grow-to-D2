"""Parent Class for 'df' Commands Executing"""

import subprocess


class Executor:
    def receive_data(self, send_cmd):
        """Process Linux 'df' Commands.

        Args:
            send_cmd: Linux 'df' command.

        Returns:
            parsed_output: a data dict.
            parsed_err: an error dict.
        """
        p = subprocess.Popen(args=send_cmd.split(),
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        cmd_output, cmd_err = p.communicate()
        if len(cmd_err) == 0:
            return cmd_output
        else:
            raise Exception(cmd_err)
