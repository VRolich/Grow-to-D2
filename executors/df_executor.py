"""Execute 'df'-command"""

from executors import executor
from parsers import df_parser


class DFExecutor(executor.Executor):
    def receive_data(self, send_cmd='df'):
        """Execute Linux 'df' Command.

        Args:
            send_cmd: Linux 'df' command.

        Returns:
            json_dict: data dict in JSON-format.
        """
        dictionary = super().receive_data(send_cmd)
        parsed_dict = df_parser.DFParser(dictionary)
        json_dict = parsed_dict.parser_to_json()

        return json_dict
