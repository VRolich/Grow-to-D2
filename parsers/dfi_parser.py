"""Parent Class for 'df-i' Command Parsing"""

from parsers import cmd_parser


class DFIParser(cmd_parser.CMDParsed):

    def __init__(self, cmd_output, cmd_err, err):
        super().__init__(cmd_output, cmd_err, err)
        self._key_list = ['Filesystem', 'Inodes', 'IUsed',
                          'IFree', 'IUse%', 'Mounted on']

