"""Initialization of the Reload Workbench"""

from importlib import resources

import FreeCAD as App
import FreeCADGui as Gui

from freecad.reloadwb.commands import get_all_commands
from freecad import reloadwb

ROOT_DIR = resources.files(reloadwb)
RESOURCES_DIR = ROOT_DIR / "resources"
ICONS_DIR = RESOURCES_DIR / "icons"
WORKBENCH_ICON_FILE = ICONS_DIR / "reloadwb-icon.svg"


class ReloadWorkbench(Gui.Workbench):
    MenuText = "ReloadWB"
    Tooltip = "Test Reload Workbench"
    Icon = str(WORKBENCH_ICON_FILE)

    def Initialize(self):
        App.Console.PrintWarning("Initializing workbench")
        command_names = []
        for command_name, _ in get_all_commands().items():
            command_names.append(command_name)
        App.Console.PrintWarning(f"Adding {len(command_names)} commands")
        self.appendToolbar("ReloadWB", command_names)
        self.appendMenu("ReloadWB", command_names)
        App.Console.PrintWarning(f"Using icons in {ICONS_DIR}")
        Gui.addIconPath(str(ICONS_DIR))

try:
    Gui.removeWorkbench("ReloadWorkbench")
    App.Console.PrintWarning(f"Removing ReloadWorkbench")
    Gui.removeWorkbench("ReloadWorkbench")
except:
    pass

Gui.addWorkbench(ReloadWorkbench())
