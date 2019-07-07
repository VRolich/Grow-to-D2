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

        dictionary = super().receive_data(send_cmd)
        parsed_dict = dfi_parser.DFIParser(dictionary)
        json_dict = parsed_dict.parser_to_json()

        return json_dict
