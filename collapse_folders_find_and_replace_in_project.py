import sublime, sublime_plugin
import pprint, subprocess, re
from pprint import pprint

import os
import json


class CollapseFoldersFindAndReplaceInProject(sublime_plugin.TextCommand):

  print('reloading FindAndReplaceInProject')

  def run(self, edit, from_current_file_path=None):
    # Текущее окно сублайма
    window = sublime.active_window()

    # В окне - проект, берём его настройки
    data = window.project_data()

    # Безопасное извлечение интересуемой настройки из многоуровнего словаря
    # через get
    exclusion_setting = data.get('settings', {}).get("collapse_folders_find_and_replace_in_project")

    # 
    project_path = window.project_file_name()
    is_project = project_path != None
    if project_path != None:
      project_file = open(project_path)
      json_project = project_file.read()
      dict_project = json.loads(json_project)
      if dict_project is not None and 'folders' in dict_project and dict_project['folders'][0] is not None:
        project_path = os.path.join(os.path.dirname(project_path), dict_project['folders'][0]['path'])
    # if project_path == None:
    #   project_path = window.folders()[0]

    # Путь к директории текущего открытого файла (если есть)
    file_path = self.view.file_name()
    if file_path is not None:
      dir_path = os.path.dirname(file_path)
      print('dir_path:', dir_path)

    # Бизнес логика

    # Определение пути поиска по исходным данным
    search_path = ""
    if from_current_file_path == True and dir_path is not None:
      search_path = dir_path
    elif is_project and project_path is not None:
      search_path = project_path
    elif is_project:
      search_path = "<project>"

    # Дополнение пути поиска исключенем
    path_string = search_path
    if exclusion_setting is not None:
      path_string = search_path + ", " + exclusion_setting

    # Аргументы для открытия панели
    panel_args = {
      "panel": "find_in_files",
      "regex": False
    }

    if path_string is not None:
      # # Копируем в буфер обмена
      # sublime.set_clipboard(path_string)
      # Передаём сразу в панель через аргументы
      panel_args.update({"where": path_string})

    # Показываем панель с настройками в panel_args
    self.view.window().run_command(
      "show_panel",
      panel_args
    )
