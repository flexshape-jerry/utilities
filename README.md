# Utilities
A series of utilities to help with development

## Text Utils
Utilities that help with text manipulation

### Regex Replace
Searches a file or a directory recursively, matching a regex line by line, and applys a text transformation function on the matches, 
essentially doing a regex find and replace with a custom text transformation function.

Currently implemented function is to change all instances of `maybeMyVariable` to `myVariableOpt`


```
usage: regex_replace.py [-h] [-r] [--regex REGEX]
                        [--function {maybe_to_opt,default_grpc_to_public_grpc}]
                        path

Apply regex pattern to files.

positional arguments:
  path                  Path to directory or file

options:
  -h, --help            show this help message and exit
  -r                    Recursively apply to files in directories
  --regex REGEX         Regex pattern to apply
  --function {maybe_to_opt,default_grpc_to_public_grpc}
                        Function to apply (default: maybe_to_opt)
```

