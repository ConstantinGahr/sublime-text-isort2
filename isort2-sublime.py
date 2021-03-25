"""
Sublime Text package to format Python imports using `isort`. Supersedes `isort`.
https://github.com/ConstantinGahr/isort2
"""
import subprocess

import sublime
from sublime_plugin import EventListener, TextCommand

SETTINGS_FILE_NAME = "isort2.sublime-settings"
SORT_CMD = "isort_sort"


class IsortSort(TextCommand):
    def run(self, edit):
        if not is_python(self.view):
            sublime.message_dialog(
                "This file is not a Python file and its imports cannot be sorted."
            )
            return

        path = sublime.load_settings(SETTINGS_FILE_NAME).get("path")
        args = sublime.load_settings(SETTINGS_FILE_NAME).get("args")
        file_name = self.view.file_name()

        if not file_name:
            sublime.message_dialog("Please save your file before trying to sort.")
            return

        cmd = [path, " ".join(args), file_name]
        try:
            _ = subprocess.Popen(cmd)
        except FileNotFoundError:
            sublime.error_message(
                "Command '{}' doesn't exist.".format(path)
                + " Is the path to 'isort' correctly set? Please check your settings!"
            )


class IsortEventListener(EventListener):
    def on_pre_save(self, view):
        if is_python(view) and sublime.load_settings(SETTINGS_FILE_NAME).get(
            "isort_on_save"
        ):
            view.run_command(SORT_CMD)


def is_python(view):
    return view.match_selector(0, "source.python")
