"""Execute 'df-i'-command"""

from executors import executor


class DFIExecutor(executor.Executor):
    def __init__(self, cmd='df -i'):
        super().__init__(cmd)
