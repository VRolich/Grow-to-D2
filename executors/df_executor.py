"""Execute 'df'-command"""

from executors import executor
from parsers import df_parser


class DFExecutor(executor.Executor):
    def __init__(self, cmd='df', parser=df_parser.DFParser):
        super().__init__(cmd, parser)
