import sublime, sublime_plugin
import pprint, subprocess, re
from pprint import pprint

class CollapseFoldersCommand(sublime_plugin.TextCommand):
  def run(self, edit):
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
          xdotool mousemove 16 80 &&
          sleep .05 &&
          xdotool keydown Alt+Ctrl click 1 &&
          xdotool keyup Alt+Ctrl &&
          sleep 1 &&
          xdotool click 1
        """
      ]
    )
