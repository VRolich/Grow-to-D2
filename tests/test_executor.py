"""Module Tests for Executors"""

import unittest
from unittest import mock

from parameterized import parameterized
from executors import executor
from parsers import df_parser, dfh_parser, dfi_parser


class TestExecutor(unittest.TestCase):
    """Test executor functions"""

    @parameterized.expand(((df_parser.DFParser,
                            (b'Filesystem     1K-blocks     Used Available Use% Mounted on\n'
                             b'udev             4062048        0   4062048   0% /dev'),
                            b'',
                            ('{"status": "success", "result": {"Filesystem": ["udev"], "1K-blocks": ["4062048"], '
                             '"Used": ["0"], "Available": ["4062048"], "Use%": ["0%"], "Mounted_on": ["/dev"]}}')),
                           (dfh_parser.DFHParser,
                            (b'Filesystem      Size  Used Avail Use% Mounted on\n'
                             b'udev            3,9G     0  3,9G   0% /dev'),
                            b'',
                            ('{"status": "success", "result": {"Filesystem": ["udev"], "Size": ["3,9G"], '
                             '"Used": ["0"], "Avail": ["3,9G"], "Use%": ["0%"], "Mounted_on": ["/dev"]}}')),
                           (dfi_parser.DFIParser,
                            (b'Filesystem      Inodes  IUsed   IFree IUse% Mounted on\n'
                             b'udev           1015512    470 1015042    1% /dev'),
                            b'',
                            ('{"status": "success", "result": {"Filesystem": ["udev"], "Inodes": ["1015512"], '
                             '"IUsed": ["470"], "IFree": ["1015042"], "IUse%": ["1%"], "Mounted_on": ["/dev"]}}'))))
    @mock.patch('subprocess.Popen')
    def test_receive_data(self, parser, stdout, stderr, expected, popen_mock):
        p_mock = popen_mock.return_value
        p_mock.communicate.return_value = stdout, stderr
        p_mock.returncode = 0

        actual = executor.Executor('test_cmd', parser).receive_data()
        self.assertEqual(expected, actual, actual)
        popen_mock.assert_called_once()
        p_mock.assert_not_called()
