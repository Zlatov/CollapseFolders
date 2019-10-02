import sublime, sublime_plugin
import pprint, subprocess, re
from pprint import pprint
import os
from subprocess import check_output

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

class CollapseFoldersOpenGitModifiedNewCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view # вьюха открытого файла?
    window = view.window() # экземпляр окна сублайма?

    project_path = window.project_file_name()
    if project_path == None:
      project_path = window.folders()[0]
    else:
      project_path = os.path.dirname(project_path)

    pprint(project_path)

    changed_files = check_output(
      [
        '/bin/bash',
        '-c',
        """
          cd {} &&
          git diff --name-only HEAD
        """.format(project_path)
      ]
    ).decode("utf-8")
    # print(changed_files)

    new_files = check_output(
      [
        '/bin/bash',
        '-c',
        """
          cd {} &&
          git ls-files --other --exclude-standard
        """.format(project_path)
      ]
    ).decode("utf-8")
    # print(new_files)

    open_files = ' '.join((changed_files + new_files).rstrip('\n').split("\n"))
    print("open_files:", open_files)

    subprocess.Popen(
      [
        '/bin/bash',
        '-c',
        """
          cd {} &&
          subl {}
        """.format(project_path, open_files)
      ]
    )
