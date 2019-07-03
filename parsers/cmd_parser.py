"""Parent Class for 'df' Commands Parsing"""

class CMDParsed:

    def parser_to_dict(self, byte_input):
        """Parser Byte Date to Dictionary.

        Args:
            byte_input: input date of byte type.

        Returns:
            parsed_dict: a data dict.
        """
        byte_input = byte_input.decode("utf-8")
        lines = byte_input.splitlines()
        lines = list(line.split() for line in lines)
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
        """
        for key in some_dict.keys():
            if key not in key_list:
                del some_dict[key]
        return some_dict
