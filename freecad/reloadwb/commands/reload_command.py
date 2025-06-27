# Developer tool to reload the workbench.

import FreeCAD as App
import FreeCADGui as Gui

from freecad.reloadwb.commands.base import BaseCommand
from .utils import HotSwapCommand

__all__ = ["ReloadCommand"]


class ReloadCommand(BaseCommand):
    """
    Command to reload the workbench.
    """

    def GetResources(self):
        return {
            'Pixmap': 'bulb',
            'MenuText': 'Reload the workbench',
            'Accel': 'W, R',
            'ToolTip': 'Reload the workbench',
        }

    def IsActive(self):
        """
        Define when the command should be active
        """
        return True

    def Activated(self) -> None:
        App.Console.PrintWarning("RELOAD!")
        HotSwapCommand.reload_all()

Gui.addCommand('ReloadCommand', ReloadCommand())
