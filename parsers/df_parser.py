"""Parent Class for 'df' Command Parsing"""

from parsers import cmd_parser


class DFParser(cmd_parser.CMDParsed):

    def __init__(self, cmd_output, cmd_err, err):
        super().__init__(cmd_output, cmd_err, err)
        self._key_list = ('Filesystem', '1K-blocks', 'Used',
                          'Available', 'Use%', 'Mounted_on')
