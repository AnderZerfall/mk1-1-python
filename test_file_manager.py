from file_manager import FileManager
import pytest
import os

SOURCE_FILE = 'public/text.txt'
SOURCE_LINES = [
    'Test line 1',
    'Test line boo 2',
    'Test line foo 3',
    'Test line boo 4']
FILTERED = ['Test line boo 2', 'Test line boo 4']
TARGET_FILE = 'public/filtered_test.txt'

FILTER_LINES_TEST_PARAMS = [pytest.param(SOURCE_LINES, 'boo', FILTERED,
                            id='positive'),
                            pytest.param(
    SOURCE_LINES, 'bruh', None, id='not found'),
]


@pytest.fixture(scope='class', autouse=True)
def init_manager(request):
    request.cls.manager = FileManager()
    yield


class TestFileManager():
    @pytest.mark.parametrize("source_file,expected_outcome",
                             [(SOURCE_FILE, SOURCE_LINES)])
    def test_read_file(self, source_file, expected_outcome):
        lines = self.manager.read_file(source_file)
        assert lines == expected_outcome

    @pytest.mark.parametrize("source_lines,target, expected_outcome",
                             FILTER_LINES_TEST_PARAMS)
    def test_filter_lines(self, source_lines, target, expected_outcome):
        lines = self.manager.filter_lines(source_lines, target)
        assert lines == expected_outcome

    @pytest.mark.parametrize("source_lines,target_file",
                             [(FILTERED, TARGET_FILE)])
    def test_save_file(self, source_lines, target_file):
        self.manager.save_file(source_lines, target_file)
        assert os.path.exists(target_file)
        assert self.manager.read_file(target_file) == source_lines

        os.remove(target_file)
