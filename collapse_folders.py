import sublime, sublime_plugin
import pprint, subprocess, re
from pprint import pprint

class CollapseFolders(sublime_plugin.TextCommand):
  def run(self, edit):
    subprocess.Popen(
      [
        '/bin/bash',
        '-c',
        """
          sleep .1 &&
          xdotool key Ctrl+0 &&
          xdotool key Page_Up Page_Up Page_Up Page_Up Page_Up &&
          xdotool mousemove 12 75 &&
          xdotool keydown Alt+Ctrl click 1 &&
          xdotool keyup Alt+Ctrl &&
          xdotool click 1
        """
      ]
    )
