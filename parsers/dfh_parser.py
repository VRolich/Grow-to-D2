"""Parent Class for 'df-h' Command Parsing"""

from parsers import cmd_parser


class DFHParser(cmd_parser.CMDParsed):

    def __init__(self, cmd_output, cmd_err, err):
        super().__init__(cmd_output, cmd_err, err)
        self._key_list = ['Filesystem', 'Size', 'Used',
                          'Avail', 'Use%', 'Mounted on']

