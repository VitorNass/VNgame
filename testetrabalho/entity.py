#!/usr/bin/python
# -*- coding: utf-8 -*-

class Entity:
    def __init__(self):
        self.name = None  # Nome da entidade
        self.surf = None  # Superfície gráfica (exemplo, em jogos)
        self.rect = None  # Área retangular para colisões ou posição

    def move(self) -> None:
        """
        Move a entidade para uma nova posição.
        Implementação será definida mais tarde.
        """
        pass
