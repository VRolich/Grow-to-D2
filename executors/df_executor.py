"""Execute 'df'-command"""

from executors import executor
from parsers import df_parser


class DFExecutor(executor.Executor):
    def receive_data(send_cmd='df'):
        """Execute Linux 'df' Command.

        Args:
            send_cmd: Linux 'df' command.

        Returns:
            parsed_output: a data dict.
            parsed_err: an error dict.
        """
        json_dict = df_parser.DFParser.parse_to_json(
            executor.Executor.receive_data(send_cmd))

        return json_dict