
import FreeCAD as App # type: ignore
import FreeCADGui as Gui # type: ignore

from freecad.reloadwb.commands.base import BaseCommand
from .utils import HotSwapCommand

__all__ = ["TestCommand"]


class TestCommand(BaseCommand):

    def Activated(self) -> None:
        App.Console.PrintWarning("TEST7")

    def IsActive(self) -> bool:
        return True

Gui.addCommand(
    'TestCommand',
    HotSwapCommand(
        resources={
            "Pixmap": 'Std_Tool12',
            "MenuText": "TestCommand",
            "ToolTip": "Test!!",
        },
        impl=TestCommand,
    ),
)
