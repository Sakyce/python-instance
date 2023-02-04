from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

uid = int(0)

class Instance(ABC):
    "Roblox-like Composite class"
    
    def __init__(self) -> None:
        global uid

        self._children: List[Instance] = []
        self.Name = self.__class__.__name__
        self._parent = None 
        self.uid = uid
        uid += 1

    def ClassName(self) -> str:
        return self.__class__.__name__

    @property
    def Parent(self) -> Instance|None:
        return self._parent

    @Parent.setter
    def Parent(self, parent: Instance|None):
        if self._parent:
            oldparent = self._parent
            oldparent._children.remove(self)
        self._parent = parent
        if parent:
            parent._children.append(self)

    def Destroy(self) -> None:
        "Set the Parent of Instance and it's Children to None"
        for Children in self.GetChildren():
            Children.Destroy()
        self.Parent = None

    def GetChildren(self) -> List[Instance]:
        "Get every children"
        return self._children

    def __repr__(self) -> str:
        return self.Name

    def __hash__(self) -> int:
        return hash(self.uid)