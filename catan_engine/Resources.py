from abc import ABC, abstractmethod
from typing import TypeVar

# Clay , Wheat , Rock , Wood , Wool , Knight
# Progress (ie, other cards from progress that aren't knight)
class Resource (ABC):
    pass
R = TypeVar('R', bound=Resource)

class Wool (Resource):
    pass

class Wood (Resource):
    pass

class Clay (Resource):
    pass

class Stone (Resource):
    pass

class Wheat (Resource):
    pass

class Knight (Resource):
    pass
