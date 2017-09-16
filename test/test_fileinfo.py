"""Este módulo reune métodos de testes para os exemplos dos tutoriais:
    - Python Mocks: a gentle introduction - Part 1
    - Python Mocks: a gentle introduction - Part 2

.. _Python Mocks: a gentle introduction:
    http://blog.thedigitalcatonline.com/blog/2016/03/06/python-mocks-a-gentle-introduction-part-1/
    http://blog.thedigitalcatonline.com/blog/2016/09/27/python-mocks-a-gentle-introduction-part-2/
"""

from unittest.mock import patch
from models import FileInfo


def test_init():
    """Testa se a instancia de FileInfo foi construida corretamente a partir do nome do arquivo."""
    file_name = 'somefile.txt'
    relative_path = f'../{file_name}'
    file_info = FileInfo(relative_path)
    assert file_info.file_name == file_name


@patch('os.path.getsize')
@patch('os.path.abspath')
def test_get_info(abspath_mock, getsize_mock):
    """Testa se a instancia de FileInfo retorna uma tupla com os dados do arquivo a partir da chamada
    do método get_info() do objeto."""
    file_name = 'somefile.txt'
    original_path = f'../{file_name}'

    test_abspath = 'algum/abs/path'
    abspath_mock.return_value = test_abspath

    test_size = 1234
    getsize_mock.return_value = test_size

    file_info = FileInfo(original_path)
    assert file_info.get_info() == (file_name, original_path, test_abspath, test_size)
