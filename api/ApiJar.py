from typing import List, Type

from api.models import ClassFile
from api.models.ClassFile import ClassFile
import zipfile


class ApiJar:
    def __init__(self, file_path):
        if not zipfile.is_zipfile(file_path):
            raise ValueError("File don\'t exist")
        self.zip_file = zipfile.ZipFile(file_path)

    def get_info_list(self):
        return self.zip_file.infolist()

    def get_files_from_jar(self) -> list[ClassFile]:
        class_files = []
        for info in self.get_info_list():
            name = info.filename
            if name.endswith('.class'):
                data = self.zip_file.read(name)
                class_files.append(ClassFile(filename=name, bytecode=data))
        return class_files

    def get_manifest(self):
        pass