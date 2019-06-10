"""Parent Class for 'df' Commands Parsing"""

class CMDParsed:

    def parse_to_json(byte_input):
        """Parser Byte Date to Dictionary.

        Args:
          byte_input: input date of byte type.

        Returns:
          json_dict: a data dict.
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
