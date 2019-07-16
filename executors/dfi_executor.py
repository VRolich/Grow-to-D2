"""Execute 'df-i'-command"""

from executors import executor
from parsers import dfi_parser


class DFIExecutor(executor.Executor):
    def __init__(self, cmd='df -i', parser=dfi_parser.DFIParser):
        super().__init__(cmd, parser)
