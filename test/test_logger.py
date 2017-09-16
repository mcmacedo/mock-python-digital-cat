"""Este módulo reune métodos de testes para os exemplos dos tutoriais:
    - Python Mocks: a gentle introduction - Part 1
    - Python Mocks: a gentle introduction - Part 2

.. _Python Mocks: a gentle introduction:
    http://blog.thedigitalcatonline.com/blog/2016/03/06/python-mocks-a-gentle-introduction-part-1/
    http://blog.thedigitalcatonline.com/blog/2016/09/27/python-mocks-a-gentle-introduction-part-2/
"""

from unittest.mock import patch

from models import Logger


def test_init():
    """Testa se a classe Logger é instanciado corretamente."""
    log = Logger()
    assert log.messages == []


@patch('models.datetime.datetime')
def test_log(mock_now):
    """Testa se uma nova mensagem foi adicionada à lista de mensagens do objeto da classe Logger"""
    test_now = 123
    test_message = 'A test message'

    mock_now.now.return_value = test_now
    log = Logger()
    log.log(test_message)

    assert log.messages == [(test_now, test_message)]

