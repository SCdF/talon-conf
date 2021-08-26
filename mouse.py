import os
import pathlib
import subprocess

from talon import Module, Context, actions

from talon import (
    Module,
    actions,
    app,
    clip,
    cron,
    ctrl,
    imgui,
    noise,
    ui,
    canvas,
)

mod = Module()

@mod.action_class
class Actions:
    def mouse_center():
        """move the mouse cursor to the center of the currently active window"""
        rect = ui.main_screen().rect
        ctrl.mouse_move(rect.left + (rect.width / 2), rect.top + (rect.height / 2))
        # center fuction is not really needed, just for the print output in the log
        center = (rect.x + rect.width / 2, rect.y + rect.height / 2)
        print(rect, center)
    def mouse_center_window():
        """move the mouse cursor to the center of the currently active window"""
        rect = ui.active_window().rect
        ctrl.mouse_move(rect.left + (rect.width / 2), rect.top + (rect.height / 2))
        # center fuction is not really needed, just for the print output in the log
        center = (rect.x + rect.width / 2, rect.y + rect.height / 2)
        print(rect, center)
