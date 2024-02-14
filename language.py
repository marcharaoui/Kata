# =========================================== #
# Kata project: number2word
# language script: abstract class to help define common 
# interface to control language classes
# Marc Haraoui - created on 14/02/2024
# =========================================== #

from abc import ABC, abstractmethod

# =========================================== #

class Lang(ABC):
    @abstractmethod
    def translate(self):
        pass