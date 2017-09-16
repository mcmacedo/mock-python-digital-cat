"""Este módulo reune as classes que representam os modelos para os exemplos dos tutoriais:
    - Python Mocks: a gentle introduction - Part 1
    - Python Mocks: a gentle introduction - Part 2

.. _Python Mocks: a gentle introduction:
    http://blog.thedigitalcatonline.com/blog/2016/03/06/python-mocks-a-gentle-introduction-part-1/
    http://blog.thedigitalcatonline.com/blog/2016/09/27/python-mocks-a-gentle-introduction-part-2/
"""

import datetime
import os


class MyObj(object):
    """Classe que chama um método de um recurso/objeto externo."""
    def __init__(self, repository):
        """Constroi instancia da classe MyObj.

        :param repository (obj): objeto que pode acessar o recurso externo.
        """
        self._repo = repository
        repository.connect()

    def setup(self):
        """
        Configura o recurso/objeto externo.
        """
        self._repo.setup(cache=True, max_connections=256)


class FileInfo(object):
    """Classe que agrega as informações sobre um arquivo.

    Attributes:
        _original_path = path original do arquivo passado como argumento no construtor.
        _file_name = nome do arquivo
    """
    def __init__(self, path: str):
        """Constroi instancia da classe FileInfo.
        :param path (str): Caminho relativo para o arquivo.
        """
        self._original_path = path
        self._file_name = os.path.basename(path)

    @property
    def file_name(self):
        """Retorna o nome do arquivo.
        :return (str): nome do arquivo.
        """
        return self._file_name

    def get_info(self):
        """
        Método que retorna informações sobre o arquivo.

        Returns (tuple): tupla com o nome do arquivo, o path original e o path absoluto.
        """
        return (self.file_name,
                self._original_path,
                os.path.abspath(self.file_name),
                os.path.getsize(self.file_name))


class Logger(object):
    """Cria loggs para gerencimento do sistema.

    Attributes:
        _messages (list): mensagens que devem ser logadas.
    """
    def __init__(self):
        self._messages = []

    def log(self, message: str):
        """
        Gera a mensagem de log com data e hora e mensagem.
        Args:
            message (str): Mensagem que deve aparecer no log.
        """
        self._messages.append((datetime.datetime.now(), message))

    @property
    def messages(self):
        """
        Retorna a lista de mensagens.
        Returns (list): lista com as mensagens logadas até o momento

        """
        return self._messages
