"""Execute 'df-h'-command"""

from executors import executor


class DFHExecutor(executor.Executor):
    def __init__(self, cmd='df -h'):
        super().__init__(cmd)
