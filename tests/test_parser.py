"""Module Tests for Parsers"""

import json
import unittest

from parameterized import parameterized
from parsers import cmd_parser, df_parser, dfh_parser, dfi_parser


class TestParser(unittest.TestCase):
    """Test parser functions"""
    @classmethod
    def setUpClass(cls):

        cls._byte_input = \
            b'Filesystem     1K-blocks     Used Available Use% Mounted on\n'\
            b'udev             4062048        0   4062048   0% /dev\n'\
            b'tmpfs             816832     1404    815428   1% /run\n'\
            b'/dev/sda1       51341792 26827224  21876848  56% /\n'\
            b'tmpfs            4084140    69784   4014356   2% /dev/shm\n'\
            b'tmpfs               5120        4      5116   1% /run/lock\n'\
            b'tmpfs            4084140        0   4084140   0% /sys/fs/cgroup\n'\
            b'/dev/loop0          3840     3840         0 100% /snap/gnome-system-monitor/100\n'\
            b'tmpfs             816828       36    816792   1% /run/user/1000\n'\
            b'/dev/loop22        55808    55808         0 100% /snap/core18/1066\n'\

        cls._cmd_parser_object = cmd_parser.CMDParsed(cls._byte_input, '', 0)
        cls._df_parser_object = df_parser.DFParser(cls._byte_input, '', 0)
        cls._dfh_parser_object = dfh_parser.DFHParser(cls._byte_input, '', 0)
        cls._dfi_parser_object = dfi_parser.DFIParser(cls._byte_input, '', 0)

        cls._parsed_dict = {
            'Filesystem': ['udev', 'tmpfs', '/dev/sda1', 'tmpfs', 'tmpfs', 'tmpfs', '/dev/loop0', 'tmpfs',
                           '/dev/loop22'],
            '1K-blocks': ['4062048', '816832', '51341792', '4084140', '5120', '4084140', '3840', '816828', '55808'],
            'Used': ['0', '1404', '26827224', '69784', '4', '0', '3840', '36', '55808'],
            'Available': ['4062048', '815428', '21876848', '4014356', '5116', '4084140', '0', '816792', '0'],
            'Use%': ['0%', '1%', '56%', '2%', '1%', '0%', '100%', '1%', '100%'],
            'Mounted_on': ['/dev', '/run', '/', '/dev/shm', '/run/lock', '/sys/fs/cgroup',
                           '/snap/gnome-system-monitor/100', '/run/user/1000', '/snap/core18/1066']}

        cls._result_dict = {
            "status": "success", "result": {
                "Filesystem": ["udev", "tmpfs", "/dev/sda1", "tmpfs", "tmpfs", "tmpfs", "/dev/loop0", "tmpfs",
                               "/dev/loop22"],
                "1K-blocks": ["4062048", "816832", "51341792", "4084140", "5120", "4084140", "3840", "816828",
                              "55808"],
                "Used": ["0", "1404", "26827224", "69784", "4", "0", "3840", "36", "55808"],
                "Available": ["4062048", "815428", "21876848", "4014356", "5116", "4084140", "0", "816792", "0"],
                "Use%": ["0%", "1%", "56%", "2%", "1%", "0%", "100%", "1%", "100%"],
                "Mounted_on": ["/dev", "/run", "/", "/dev/shm", "/run/lock", "/sys/fs/cgroup",
                               "/snap/gnome-system-monitor/100", "/run/user/1000", "/snap/core18/1066"]}}

    @parameterized.expand([([['first', 'line'], ['second', 'line'], ['third', 'line']],
                            b'first line\nsecond line\nthird line')])
    def test_parser_to_str(self, result, test_data):
        self.assertEqual(result, self._cmd_parser_object.parser_to_str(
            test_data))

    def test_parser_to_dict(self):
        self.assertDictEqual(self._parsed_dict, self._cmd_parser_object.parser_to_dict(
            self._cmd_parser_object._cmd_output))

    @parameterized.expand([({'a': 1, 'b': 2, 'c': 3}, ['a', 'c']),
                           ({'vip': 'sdfjkl', 'dip': 324, 'pip': '123', 'tip': 12345}, ['pip', 'tip', 'vip'])])
    def test_key_verifier(self, test_dict, result_keys):
        self.assertEqual(result_keys, sorted(self._cmd_parser_object.key_verifier(
            test_dict, result_keys).keys()))

    @parameterized.expand([
        (df_parser.DFParser,),
        (dfh_parser.DFHParser,),
        (dfi_parser.DFIParser,)
    ])
    def test_parser_to_json(self, parser_object):
        parser = parser_object(self._byte_input, '', 0)
        json_string = parser.parser_to_json()
        actual = json.loads(json_string)
        self.assertEqual(self._result_dict.keys(), actual.keys())
