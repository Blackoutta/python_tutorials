from random import randint
from sys import exit


# 所有场景的基类(base class)
class Scene:

    def enter(self):
        print("This scene is not yet configured. Subclass it and implement enter()")


# Engine
class Engine:

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print("\n---------")
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


# Scenes
class Death(Scene):
    quips = [
        "You died.",
        "You suck",
        "You lose"
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips) - 1)])


class CentralCorridor(Scene):

    def enter(self):
        pass


class LaserWeaponArmory(Scene):

    def enter(self):
        pass


class TheBridge(Scene):

    def enter(self):
        pass


class EscapePod(Scene):

    def enter(self):
        pass


# Map
class Map:

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)

a_game.play()