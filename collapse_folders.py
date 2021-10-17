import sublime, sublime_plugin
import pprint, subprocess, re
from pprint import pprint

# Сворачивает все папки проекта и ставит фокус в сайдбар, использует управление
# мышью через xdotool.
class CollapseFoldersCommand(sublime_plugin.TextCommand):
  def get_settings(self, key = None):
    settings = sublime.load_settings('CollapseFolders.sublime-settings')
    if key is None:
      return settings
    return settings.get(key)

  def run(self, edit):
    coordinates = self.get_settings('arrow_coordinates')
    if len(coordinates) < 2 :
      return None
    x, y = coordinates
    subprocess.Popen(
      [
        '/bin/bash',
        '-c',
        """
          sleep .1 &&
          xdotool key Ctrl+0 &&
          sleep .1 &&
          xdotool key Home &&
          sleep .5 &&
          xdotool mousemove {} {} &&
          sleep .05 &&
          xdotool keydown Alt+Ctrl click 1 &&
          xdotool keyup Alt+Ctrl &&
          sleep 1 &&
          xdotool click 1
        """.format(x, y)
      ]
    )
