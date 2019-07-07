"""Parent Class for 'df' Commands Executing"""

import subprocess


class Executor:
    def receive_data(self, send_cmd):
        """Process Linux 'df' Commands.

        Args:
            send_cmd: Linux 'df'-type command.

        Returns:
            parsed_output: a data dict.
            parsed_err: an error dict.
        """
        p = subprocess.Popen(args=send_cmd.split(),
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        cmd_output, cmd_err = p.communicate()
        err = p.returncode

        dictionary = {
            'status': 'None',
            'error': 'None',
            'result': 'None'}
        if err == 0:
            dictionary['status'] = 'success'
            dictionary['result'] = cmd_output
        else:
            dictionary['status'] = 'failure'
            dictionary['error'] = cmd_err
        return dictionary

