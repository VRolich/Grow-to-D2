"""Execute 'df'-command"""

from executors import executor


class DFExecutor(executor.Executor):
    def __init__(self, cmd='df'):
        super().__init__(cmd)
