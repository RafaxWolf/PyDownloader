from abc import ABC, abstractmethod

class BaseProvider(ABC):
    @abstractmethod
    def supports(slef, url: str) -> bool:
        pass

    @abstractmethod
    def download(self, url: str, path: str, audio_format: str = "mp3"):
        pass

    @abstractmethod
    def search(self, url: str):
        pass