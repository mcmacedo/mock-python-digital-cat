"""Este módulo reune métodos de testes para os exemplos dos tutoriais:
    - Python Mocks: a gentle introduction - Part 1
    - Python Mocks: a gentle introduction - Part 2

.. _Python Mocks: a gentle introduction:
    http://blog.thedigitalcatonline.com/blog/2016/03/06/python-mocks-a-gentle-introduction-part-1/
    http://blog.thedigitalcatonline.com/blog/2016/09/27/python-mocks-a-gentle-introduction-part-2/
"""

from unittest import mock
from models import MyObj


def test_instantiation():
    """Testa se a classe MyObj é instanciada chamando o método 'connect()'
    do objeto passado como argumento.
    """
    external_object = mock.Mock()
    MyObj(external_object)
    external_object.connect.assert_called_with()


def test_setup():
    """Testa se uma instancia da classe MyObj chama o método setup do objeto
    externo passado no construtor com seus respectivos parâmetros.
    """
    external_object = mock.Mock()
    obj = MyObj(external_object)
    obj.setup()
    external_object.setup.assert_called_with(
        cache=True, max_connections=256
    )
