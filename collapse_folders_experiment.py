import sublime, sublime_plugin
import pprint, subprocess, re
from pprint import pprint

class CollapseFoldersExperimentCommand(sublime_plugin.TextCommand):
  def get_settings(self, key = None):
    settings = sublime.load_settings('CollapseFolders.sublime-settings')
    # settings.set("some_key", "some_value")
    if key is None:
      return settings
    return settings.get(key)

  def run(self, edit):
    coordinates = self.get_settings('arrow_coordinates')
    print("coordinates [", type(coordinates), "]: ", coordinates, sep='')
