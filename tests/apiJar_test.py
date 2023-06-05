from api.ApiJar import ApiJar
import unittest


class TestApiJar(unittest.TestCase):
    def setUp(self) -> None:
        self.file = 'C:\\diplom\\common-7.4.4.jar'

    def test_get_info_list(self):
        api_jar = ApiJar(self.file)
        info = api_jar.get_info_list()
        self.assertNotEqual(len(info), 0)

    def test_get_files_from_jar(self):
        api_jar = ApiJar(self.file)
        files = api_jar.get_files_from_jar()
        self.assertNotEqual(len(files), 0)

    def test_getS4At(self):
        api_jar = ApiJar(self.file)
        files = api_jar.get_files_from_jar()
        file = files[0]
        magic = file.getS4At(file.OFFSET_OF_MAGIC)
        minor = file.getU2At(file.OFFSET_OF_MINOR)
        major = file.getU2At(file.OFFSET_OF_MAJOR)
        constant_pool_count = file.getU2At(file.OFFSET_OF_CONSTANT_POOL_COUNT)

        self.assertEqual(magic, 0xCAFEBABE)
