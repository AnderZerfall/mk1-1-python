from file_manager import FileManager
import pytest
import os


@pytest.fixture(scope='class', autouse=True)
def init_manager(request):
    request.cls.manager = FileManager()
    yield


class TestFileManager():
    @pytest.mark.parametrize("source_file,expected_outcome", [('public/text.txt', ['Test line 1', 'Test line boo 2', 'Test line foo 3', 'Test line boo 4'])])
    def test_read_file(self, source_file, expected_outcome):
        lines = self.manager.read_file(source_file)
        assert lines == expected_outcome

    @pytest.mark.parametrize("source_lines,target, expected_outcome", [(['Test line 1', 'Test line boo 2', 'Test line foo 3', 'Test line boo 4'], 'boo', ['Test line boo 2', 'Test line boo 4',])])
    def test_filter_lines(self, source_lines, target, expected_outcome):
        lines = self.manager.filter_lines(source_lines, target)
        assert lines == expected_outcome

    @pytest.mark.parametrize("source_lines,target_file", [(['Test line boo 2', 'Test line boo 4',], 'public/filtered_test.txt')])
    def test_save_file(self, source_lines, target_file):
        self.manager.save_file(source_lines, target_file)
        assert os.path.exists(target_file)
        assert self.manager.read_file(target_file) == source_lines

        os.remove(target_file)
    
    # TO DO: add more parameters if I'll have time 
