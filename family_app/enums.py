from enum import IntEnum


class RelationTypes(IntEnum):
    PARENT =1
    CHILD = 2
    SIBLING = 3
    SPOUSE = 4
    
    @classmethod
    def choices(cls):
        return [(key.value,key.name)  for key in cls ]
