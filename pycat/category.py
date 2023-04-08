import typing

T = typing.TypeVar("T")


class Object(typing.Generic[T]):

    def __init__(self, value: T) -> None:
        self.value = value


class Morphism(typing.Generic[T]):

    def __init__(self, domain: Object[T], codomain: Object[T]) -> None:
        self.domain = domain
        self.codomain = codomain

    def compose(self, morphism):
        return CompositeMorphism(morphism, self)


class IdentityMorphism(Morphism):

    def __init__(self, codomain: Object[T]) -> None:
        self.codomain = codomain


class NamedMorphism(Morphism):

    def __init__(self, domain: Object[T], codomain: Object[T], name: str) -> None:
        self.domain = domain
        self.codomain = codomain
        self.name = name


class CompositeMorphism(Morphism):

    def __init__(self, morphism1: Morphism[T], morphism2: Morphism[T]) -> None:
        self.morphism1 = morphism1
        self.morphism2 = morphism2

    @staticmethod 
    def components(self)  -> tuple:
        if isinstance(self.morphism2, CompositeMorphism[T]):
            return (self.morphism1, *self.morphism2.components)
        elif isinstance(self.morphism2, IdentityMorphism[T]):
            return self.morphism1
        else:
            return (self.morphism1, self.morphism2)

    @property 
    def domain(self) -> Morphism[T]:
        return self.morphism1.domain
    
    @property 
    def codomain(self) -> Morphism[T]:
        return self.morphism2.codomain


class Category(typing.Generic[T]):

    def __init__(self, objects: set[Object[T]], morphisms: set[Morphism[T]], name: str) -> None:
        self.objects = objects
        self.morphisms = morphisms
        self.name = name