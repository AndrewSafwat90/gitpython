from abc import ABCMeta, abstractmethod


class programming(metaclass=ABCMeta):
    @abstractmethod
    def has_oop(self):
        pass


class python(programming):
    def has_oop(self):
        return True


class java(programming):
    def has_oop(self):
        return True


lang = programming()
print(lang.has_oop())  # This will raise NotImplementedError
