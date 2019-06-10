"""Execute 'df-i'-command"""

from executors import executor
from parsers import dfi_parser


class DFIExecutor(executor.Executor):
    def receive_data(send_cmd='df -i'):
        """Execute Linux 'df-i' Command.

        Args:
            send_cmd: Linux 'df' command.

        Returns:
            parsed_output: a data dict.
            parsed_err: an error dict.
        """

        json_dict = dfi_parser.DFIParser.parse_to_json(
            executor.Executor.receive_data(send_cmd))

        return json_dict