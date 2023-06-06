from api.ApiJar import ApiJar
from api.models.ClassFile import ClassFile
import unittest


class TestApiJar(unittest.TestCase):
    def setUp(self) -> None:
        self.file = 'C:\\diplom\\common-7.4.4\\com\\cloudera\\cmf\\AuthorityAware.class'
        self.jar  =  'C:\\diplom\\common-7.4.4.jar'

    def test_get_info_list(self):
        api_jar = ApiJar(self.file)
        info = api_jar.get_info_list()
        self.assertNotEqual(len(info), 0)

    def test_get_files_from_jar(self):
        api_jar = ApiJar(self.jar)
        files = api_jar.get_files_from_jar()
        file = files[0]
        a = file.getS4At(file.OFFSET_OF_MAGIC)
        self.assertEqual(a, 0xCAFEBABE)
        self.assertNotEqual(len(files), 0)

    def test_getS4At(self):
        f = open(self.file, 'rb')
        name = f.name
        bytecode = f.read()
        bytecode = [byte for byte in bytecode]
        #api_jar = ApiJar(self.file)
        #files = api_jar.get_files_from_jar()
        file = ClassFile(filename=name, bytecode=bytecode)
        magic = file.getS4At(file.OFFSET_OF_MAGIC)
        self.assertEqual(magic, 0xCAFEBABE)
        minor = file.getU2At(file.OFFSET_OF_MINOR)
        major = file.getU2At(file.OFFSET_OF_MAJOR)
        constant_pool = file.getU2At(file.OFFSET_OF_CONSTANT_POOL)
        constant_pool_count = file.getU2At(file.OFFSET_OF_CONSTANT_POOL_COUNT)
        file.constant_pool_count = constant_pool_count

        self.assertEqual(magic, 0xCAFEBABE)
