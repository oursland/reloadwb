import os

import FreeCAD as App
import FreeCADGui as Gui

from freecad.reloadwb.commands.base import BaseCommand

__all__ = ["TestCommand"]


class TestCommand(BaseCommand):

    def GetResources(self):
        return {
            "Pixmap": 'Std_Tool12',
            "MenuText": "TestCommand",
            "ToolTip": "Test!!",
        }

    def Activated(self) -> None:
        App.Console.PrintWarning("TEST")

    def IsActive(self) -> bool:
        return True

Gui.addCommand('TestCommand', TestCommand())
