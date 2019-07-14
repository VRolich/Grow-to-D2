"""Parent Class for 'df' Commands Parsing"""


class CMDParsed:
    def __init__(self, cmd_output, cmd_err, err):
        self._cmd_output = cmd_output
        self._cmd_err = cmd_err
        self._err = err
        self._cmd_execution_result = {}
        self._json_dict = None

    @staticmethod
    def parser_to_str(byte_input):
        """Parser Byte Date to sting lines.
        Args:
            byte_input: input date of byte type.

        Returns:
            parsed_dict: string lines.
        """
        byte_input = byte_input.decode("utf-8")
        lines = byte_input.splitlines()
        lines = list(line.split() for line in lines)
        return lines

    def parser_to_dict(self, byte_input):
        """Parser Byte Date to Dictionary.

        Args:
            byte_input: input date of byte type.

        Returns:
            parsed_dict: a data dict.
        """
        lines = self.parser_to_str(byte_input)
        columns = []
        for i in range(len(lines[1])):
            column = []
            for line in lines:
                column.append(line[i])
            columns.append(column)

        parsed_dict = {column[0]: column[1:] for column in columns}
        parsed_dict['Mounted on'] = parsed_dict['Mounted']
        del parsed_dict['Mounted']
        return parsed_dict

    @staticmethod
    def key_verifier(some_dict, key_list):
        """Verifier of right keys in dict.

        Args:
            some_dict: dict which keys to be checked.
            key_list: list of key that should contain dict.
        Returns:
            some_dict: verified dict.
        """
        for key in some_dict.keys():
            if key not in key_list:
                del some_dict[key]
        return some_dict

    def dict_former(self):
        """Form dictionary by parsing one of it's values
        Returns:
            dictionary: updated dict.
        """
        if self._err == 0:
            self._cmd_execution_result['status'] = 'success'
            self._cmd_execution_result['result'] = \
                self.parser_to_dict(self._cmd_output)
        else:
            self._cmd_execution_result['status'] = 'failure'
            self._cmd_execution_result['error'] = \
                self.parser_to_str(self._cmd_err)

        return self._cmd_execution_result
