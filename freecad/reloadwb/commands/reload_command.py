# Developer tool to reload the workbench.

from importlib import import_module, reload
import sys

import FreeCAD as App
import FreeCADGui as Gui

from freecad.reloadwb.commands.base import BaseCommand

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

        # def _reload_module(module_name: str) -> None:
        #     try:
        #         module = import_module(module_name)
        #     except ImportError:
        #         return
        #     reload(module)

        try:
            Gui.activateWorkbench('PartWorkbench')
        except:
            App.Console.PrintWarning("Failed to switch to PartWorkbench")

        try:
            Gui.activateWorkbench('PartWorkbench')
        except:
            print('failed to switch to Part WB')

        try:
            Gui.removeWorkbench('ReloadWB')
        except:
            print('failed to remove ReloadWB')

        for mod in [mod for mod in sys.modules if 'reloadwb' in mod]:
            print(f'Reloading {mod}')
            reload(sys.modules[mod])

        Gui.activateWorkbench('ReloadWorkbench')

Gui.addCommand('ReloadCommand', ReloadCommand())
