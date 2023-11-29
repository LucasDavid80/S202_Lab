from abc import ABC  # , abstractmethod

from classes.adm import Administrador


class Permissao(ABC):
    # @abstractmethod
    # def tem_permissao_administrador(self, pessoa):
    #     pass

    def verificar_permissao(self, pessoa):
        return isinstance(pessoa, Administrador)
