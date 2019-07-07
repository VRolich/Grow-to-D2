"""Execute 'df-h'-command"""

from executors import executor
from parsers import dfh_parser


class DFHExecutor(executor.Executor):
    def receive_data(self, send_cmd='df -h'):
        """Execute Linux 'df -h' Command.
        Args:
            send_cmd: Linux 'df -h' command.
        Returns:
            json_dict: data dict in JSON-format.
        """
        dictionary = super().receive_data(send_cmd)
        parsed_dict = dfh_parser.DFHParser(dictionary)
        json_dict = parsed_dict.parser_to_json()

        return json_dict
