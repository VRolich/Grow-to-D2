"""Base Class for Running Program"""
# Task 1
# Implement a command line utility which support several optional mutually exclusive parameters and
# should provide next functionality:
# - --human - Execute and parse linux system command “df -h”;
# - --inode - Execute and parse linux system command “df -i”;
# - In case of no options execute “df”.

import argparse

from executors import df_executor
from executors import dfh_executor
from executors import dfi_executor


def create_cmd_line_interface():
    parser = argparse.ArgumentParser(description='Please choose one '
                                                 'of the following Linux command: '
                                                 '"df -h" or "df -i"')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--human',
                       help='Execute and parse linux system command “df -h”',
                       action='store_true')
    group.add_argument('--inode',
                       help='Execute and parse linux system command “df -i”',
                       action='store_true')
    args = parser.parse_args()
    return args


def main():
    args = create_cmd_line_interface()
    if args.human:
        output = dfh_executor.DFHExecutor()
        json_output = output.receive_data()
    elif args.inode:
        output = dfi_executor.DFIExecutor()
        json_output = output.receive_data()
    else:
        output = df_executor.DFExecutor()
        json_output = output.receive_data()

    print(json_output)


if __name__ == '__main__':
    main()
