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
            b'/dev/loop1         55680    55680         0 100% /snap/core18/1055\n'\
            b'/dev/loop2         15104    15104         0 100% /snap/gnome-characters/296\n'\
            b'/dev/loop3          2432     2432         0 100% /snap/gnome-calculator/180\n'\
            b'/dev/loop4         99840    99840         0 100% /snap/docker/384\n'\
            b'/dev/loop16       144128   144128         0 100% /snap/gnome-3-26-1604/88\n'\
            b'/dev/loop6         14848    14848         0 100% /snap/gnome-logs/37\n'\
            b'/dev/loop8         43904    43904         0 100% /snap/gtk-common-themes/1313\n'\
            b'/dev/loop9         90624    90624         0 100% /snap/core/6964\n'\
            b'/dev/loop12       144128   144128         0 100% /snap/gnome-3-26-1604/90\n'\
            b'/dev/loop14         2304     2304         0 100% /snap/gnome-calculator/260\n'\
            b'/dev/loop13         4224     4224         0 100% /snap/gnome-calculator/406\n'\
            b'/dev/loop15        14976    14976         0 100% /snap/gnome-logs/45\n'\
            b'/dev/loop11        99840    99840         0 100% /snap/docker/321\n'\
            b'/dev/loop17        36224    36224         0 100% /snap/gtk-common-themes/1198\n'\
            b'/dev/loop18         3840     3840         0 100% /snap/gnome-system-monitor/95\n'\
            b'/dev/loop19         1024     1024         0 100% /snap/gnome-logs/61\n'\
            b'/dev/loop20       153600   153600         0 100% /snap/gnome-3-28-1804/63\n'\
            b'/dev/loop21        15104    15104         0 100% /snap/gnome-characters/292\n'\
            b'/dev/loop5        153600   153600         0 100% /snap/gnome-3-28-1804/67\n'\
            b'/dev/loop10        90624    90624         0 100% /snap/core/7270\n'\
            b'tmpfs             816828       36    816792   1% /run/user/1000\n'\
            b'/dev/loop22        55808    55808         0 100% /snap/core18/1066\n'\

        cls._cmd_parser_object = cmd_parser.CMDParsed(cls._byte_input, '', 0)
        cls._df_parser_object = df_parser.DFParser(cls._byte_input, '', 0)
        cls._dfh_parser_object = dfh_parser.DFHParser(cls._byte_input, '', 0)
        cls._dfi_parser_object = dfi_parser.DFIParser(cls._byte_input, '', 0)

        cls._parsed_dict = {
            'Filesystem': ['udev', 'tmpfs', '/dev/sda1', 'tmpfs', 'tmpfs', 'tmpfs', '/dev/loop0', '/dev/loop1',
                           '/dev/loop2', '/dev/loop3', '/dev/loop4', '/dev/loop16', '/dev/loop6', '/dev/loop8',
                           '/dev/loop9', '/dev/loop12', '/dev/loop14', '/dev/loop13', '/dev/loop15', '/dev/loop11',
                           '/dev/loop17', '/dev/loop18', '/dev/loop19', '/dev/loop20', '/dev/loop21', '/dev/loop5',
                           '/dev/loop10', 'tmpfs', '/dev/loop22'],
            '1K-blocks': ['4062048', '816832', '51341792', '4084140', '5120', '4084140', '3840', '55680', '15104',
                          '2432', '99840', '144128', '14848', '43904', '90624', '144128', '2304', '4224', '14976',
                          '99840', '36224', '3840', '1024', '153600', '15104', '153600', '90624', '816828', '55808'],
            'Used': ['0', '1404', '26827224', '69784', '4', '0', '3840', '55680', '15104', '2432', '99840', '144128',
                     '14848', '43904', '90624', '144128', '2304', '4224', '14976', '99840', '36224', '3840', '1024',
                     '153600', '15104', '153600', '90624', '36', '55808'],
            'Available': ['4062048', '815428', '21876848', '4014356', '5116', '4084140', '0', '0', '0', '0', '0', '0',
                          '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '816792', '0'],
            'Use%': ['0%', '1%', '56%', '2%', '1%', '0%', '100%', '100%', '100%', '100%', '100%', '100%', '100%',
                     '100%', '100%', '100%', '100%', '100%', '100%', '100%', '100%', '100%', '100%', '100%', '100%',
                     '100%', '100%', '1%', '100%'],
            'Mounted on': ['/dev', '/run', '/', '/dev/shm', '/run/lock', '/sys/fs/cgroup',
                           '/snap/gnome-system-monitor/100', '/snap/core18/1055', '/snap/gnome-characters/296',
                           '/snap/gnome-calculator/180', '/snap/docker/384', '/snap/gnome-3-26-1604/88',
                           '/snap/gnome-logs/37', '/snap/gtk-common-themes/1313', '/snap/core/6964',
                           '/snap/gnome-3-26-1604/90', '/snap/gnome-calculator/260', '/snap/gnome-calculator/406',
                           '/snap/gnome-logs/45', '/snap/docker/321', '/snap/gtk-common-themes/1198',
                           '/snap/gnome-system-monitor/95', '/snap/gnome-logs/61', '/snap/gnome-3-28-1804/63',
                           '/snap/gnome-characters/292', '/snap/gnome-3-28-1804/67', '/snap/core/7270',
                           '/run/user/1000', '/snap/core18/1066']}

        cls._result_dict = {
            "status": "success", "result": {
                "Filesystem": ["udev", "tmpfs", "/dev/sda1", "tmpfs", "tmpfs", "tmpfs", "/dev/loop0", "/dev/loop1",
                               "/dev/loop2", "/dev/loop3", "/dev/loop4", "/dev/loop16", "/dev/loop6", "/dev/loop8",
                               "/dev/loop9", "/dev/loop12", "/dev/loop14", "/dev/loop13", "/dev/loop15", "/dev/loop11",
                               "/dev/loop17", "/dev/loop18", "/dev/loop19", "/dev/loop20", "/dev/loop21", "/dev/loop5",
                               "/dev/loop10", "tmpfs", "/dev/loop22"],
                "1K-blocks": ["4062048", "816832", "51341792", "4084140", "5120", "4084140", "3840", "55680", "15104",
                              "2432", "99840", "144128", "14848", "43904", "90624", "144128", "2304", "4224", "14976",
                              "99840", "36224", "3840", "1024", "153600", "15104", "153600", "90624", "816828",
                              "55808"],
                "Used": ["0", "1404", "26827224", "69784", "4", "0", "3840", "55680", "15104", "2432", "99840",
                         "144128", "14848", "43904", "90624", "144128", "2304", "4224", "14976", "99840", "36224",
                         "3840", "1024", "153600", "15104", "153600", "90624", "36", "55808"],
                "Available": ["4062048", "815428", "21876848", "4014356", "5116", "4084140", "0", "0", "0", "0", "0",
                              "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "816792",
                              "0"],
                "Use%": ["0%", "1%", "56%", "2%", "1%", "0%", "100%", "100%", "100%", "100%", "100%", "100%", "100%",
                         "100%", "100%", "100%", "100%", "100%", "100%", "100%", "100%", "100%", "100%", "100%", "100%",
                         "100%", "100%", "1%", "100%"],
                "Mounted on": ["/dev", "/run", "/", "/dev/shm", "/run/lock", "/sys/fs/cgroup",
                               "/snap/gnome-system-monitor/100", "/snap/core18/1055", "/snap/gnome-characters/296",
                               "/snap/gnome-calculator/180", "/snap/docker/384", "/snap/gnome-3-26-1604/88",
                               "/snap/gnome-logs/37", "/snap/gtk-common-themes/1313", "/snap/core/6964",
                               "/snap/gnome-3-26-1604/90", "/snap/gnome-calculator/260", "/snap/gnome-calculator/406",
                               "/snap/gnome-logs/45", "/snap/docker/321", "/snap/gtk-common-themes/1198",
                               "/snap/gnome-system-monitor/95", "/snap/gnome-logs/61", "/snap/gnome-3-28-1804/63",
                               "/snap/gnome-characters/292", "/snap/gnome-3-28-1804/67", "/snap/core/7270",
                               "/run/user/1000", "/snap/core18/1066"]}}

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
