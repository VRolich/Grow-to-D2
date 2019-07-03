"""Execute 'df-h'-command"""

from executors import executor
from parsers import dfh_parser


class DFHExecutor(executor.Executor):
    def receive_data(self, send_cmd='df -h'):
        """Execute Linux 'df -h' Command.

        Args:
            send_cmd: Linux 'df' command.

        Returns:
            parsed_output: a data dict.
            parsed_err: an error dict.
        """
        json_dict = dfh_parser.DFHParser.parser_to_dict(
            executor.Executor.receive_data(send_cmd))

        return json_dict

