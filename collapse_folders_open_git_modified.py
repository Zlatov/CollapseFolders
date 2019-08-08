import sublime, sublime_plugin
import pprint, subprocess, re
from pprint import pprint
import os

class CollapseFoldersOpenGitModifiedCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view # вьюха открытого файла?
    window = view.window() # экземпляр окна сублайма?

    project_path = window.project_file_name()
    if project_path == None:
      project_path = window.folders()[0]
    else:
      project_path = os.path.dirname(project_path)

    pprint(project_path)

    subprocess.Popen(
      [
        '/bin/bash',
        '-c',
        """
          cd {} &&
          subl `git diff --name-only HEAD`
        """.format(project_path)
      ]
    )
