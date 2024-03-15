import argparse
import os
import re
from typing import Callable


def default_grpc_to_public_grpc(default_in: str) -> str:
    raise NotImplementedError


def maybe_to_opt(maybe_in: str) -> str:
    return maybe_in if not maybe_in.startswith('maybe') else (
        maybe_in.split('maybe').pop()[0].lower() +
        maybe_in.split('maybe').pop()[1:] +
        'Opt')


def apply_function_to_matches_in_file(file_path: str, regex_pattern: str, func: Callable[[str], str]) -> None:
    try:
        with open(file_path, 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                matches = re.findall(regex_pattern, line)
                for match in matches:
                    modified_match = func(match)
                    line = line.replace(match, modified_match)
                file.write(line)
            file.truncate()
    except FileNotFoundError:
        print("File not found!")


def apply_function_to_files_in_directory(directory: str, regex_pattern: str, func: Callable[[str], str]) -> None:
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.scala') or file.endswith('.proto'):
                file_path = os.path.join(root, file)
                apply_function_to_matches_in_file(file_path, regex_pattern, func)


def main() -> None:
    parser = argparse.ArgumentParser(description='Apply regex pattern to files.')
    parser.add_argument('path', help='Path to directory or file')
    parser.add_argument('-r', action='store_true', help='Recursively apply to files in directories')
    parser.add_argument('--regex', default=r'maybe\w+', help='Regex pattern to apply')
    parser.add_argument('--function', choices=['maybe_to_opt', 'default_grpc_to_public_grpc'],
                        default='maybe_to_opt', help='Function to apply (default: maybe_to_opt)')

    args = parser.parse_args()
    path: str = args.path
    recursive_flag: bool = args.r
    regex_pattern: str = args.regex

    if args.function == 'default_grpc_to_public_grpc':
        function_to_apply: Callable[[str], str] = default_grpc_to_public_grpc
    else:
        function_to_apply = maybe_to_opt

    if os.path.isdir(path) and recursive_flag:
        apply_function_to_files_in_directory(path, regex_pattern, function_to_apply)
    elif os.path.isfile(path):
        apply_function_to_matches_in_file(path, regex_pattern, function_to_apply)
    else:
        print("Invalid path:", path)


if __name__ == '__main__':
    main()
