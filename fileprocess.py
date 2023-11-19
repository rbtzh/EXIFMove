import subprocess
import re
import os


class CreatedDate:
    def __init__(self, datelist):
        self.year = datelist[0]
        self.month = datelist[1]
        self.day = datelist[2]
        self.hour = datelist[3]
        self.minute = datelist[4]
        self.second = datelist[5]


def get_created_date(filepath: str) -> CreatedDate:
    # use exiftool to get EXIF:Created Date of filename
    processmassage = subprocess.run(
        ["exiftool", "-createdate", filepath],
        capture_output=True,
    )
    datelist = list(filter(
        lambda e: e != '' and e != 'Create' and e != 'Date',
        re.split(':| |\n', processmassage.stdout.decode())
    ))

    return CreatedDate(datelist)


def get_all_filename_in_a_directory(root_path: str, extension_name_tuple: tuple) -> list:
    # case convert
    all_case_list = []
    for string in extension_name_tuple:
        all_case_list.append("." + string)
        all_case_list.append("." + string.upper())
        all_case_list.append("." + string.lower())
    all_case_tuple = tuple(all_case_list)

    filename_list = []
    for file in os.listdir(root_path):
        if file.endswith(all_case_tuple):
            filename_list.append(os.path.join(root_path, file))

    return filename_list
