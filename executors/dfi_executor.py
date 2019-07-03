"""Execute 'df-i'-command"""

from executors import executor
from parsers import dfi_parser


class DFIExecutor(executor.Executor):
    def receive_data(self, send_cmd='df -i'):
        """Execute Linux 'df-i' Command.

        Args:
            send_cmd: Linux 'df -i' command.

        Returns:
            json_dict: data dict in JSON-format.
        """

        byte_input = super().receive_data(send_cmd)
        parsed_dict = dfi_parser.DFIParser()
        json_dict = parsed_dict.parser_to_json(byte_input)

        return json_dict
