"""Module Tests for Executors"""

import unittest

from parameterized import parameterized
from executors import executor
from parsers import df_parser, dfh_parser, dfi_parser


class TestExecutor(unittest.TestCase):
    """Test executor functions"""

    @parameterized.expand(('df', df_parser.DFParser),
                          ('df -h', dfh_parser.DFHParser),
                          ('df -i', dfi_parser.DFIParser))
    def test_receive_data(self, command, parser):
        test_executor = executor.Executor(command, parser)
        self.assertIsNotNone(test_executor.receive_data())
