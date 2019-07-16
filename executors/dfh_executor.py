"""Execute 'df-h'-command"""

from executors import executor
from parsers import dfh_parser


class DFHExecutor(executor.Executor):
    def __init__(self, cmd='df -h', parser=dfh_parser.DFHParser):
        super().__init__(cmd, parser)
