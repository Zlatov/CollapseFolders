import sublime, sublime_plugin
import pprint, subprocess, re
from pprint import pprint

class CollapseFoldersFocusCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.view.window().run_command("reveal_in_side_bar")
    self.view.window().run_command("focus_side_bar")
