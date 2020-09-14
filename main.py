import tempfile
import os
import argparse
import json


def function_main():
    """Working with Python Console."""

    objects_all = argparse.ArgumentParser()
    objects_all.add_argument('--key', type=str, help='Return key\'s dictionary')
    objects_all.add_argument('--value', type=str, help='Return values\'s dictionary')

    arguments = objects_all.parse_args()

    if arguments.key is None:
        print('Error, key can not be None!')

    __key = arguments.key
    __value = arguments.value

    function_0(__key, __value)


def function_0(key, value, name_of_file='storage.data'):
    """The function for recording information in time-file."""

    storage_path = os.path.join(tempfile.gettempdir(), name_of_file)

    if os.path.isfile(name_of_file) is True:
        if key is not None:
            if value is not None:
                with open(storage_path, 'w+') as name_of_file:
                    mean = {'keys :': list(), 'value :': dict()}
                    json.dump(mean, name_of_file)
            else:
                with open(storage_path, 'r') as name_of_file:
                    json.load(name_of_file)
    else:
        print('File is not founded.')


function_main()
