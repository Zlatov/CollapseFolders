import sublime, sublime_plugin
import os
import os.path

class SystemAutocompleteListener(sublime_plugin.EventListener):

  # TODO определить все скоупы в которых должно срабатывать это дополнение -
  # тогда можно фильтровать вывод автозаполения с помощью
  # sublime.INHIBIT_WORD_COMPLETIONS (см. return)...
  def on_query_completions(self, view, prefix, locations):
    # asd = view.match_selector(locations[0], "source.python")
    # asd = view.match_selector(locations[0], 'string.quoted.double')

    # Определить текущую директорию view_file_dir.
    view_file_path = view.file_name()
    view_file_dir = os.path.dirname(view_file_path)
    print('view_file_dir:', view_file_dir)
    # Определить указанный пользователем путь user_path.
    rowcol = view.rowcol(locations[0])
    line = view.line(locations[0])
    line_text = view.substr(line)
    left_text = line_text[0:rowcol[1]]
    doubl_quote_index = left_text.rfind("\"")
    singl_quote_index = left_text.rfind("'")
    quote_index = max(singl_quote_index, doubl_quote_index)
    user_path = left_text[quote_index+1:]
    if len(user_path) == 0: user_path = './'
    print('user_path:', user_path)
    # Определить предполагамемый пользователем абсолютный путь expected_path.
    expected_path = os.path.realpath(os.path.join(view_file_dir, user_path))
    if user_path[-1] != '/':
      expected_path = os.path.dirname(expected_path)
    print('expected_path:', expected_path)
    # Взять список файлов и папок в предполагаемом пути.
    folders = []
    files = []
    for item in os.listdir(expected_path):
      if os.path.isfile(os.path.join(expected_path, item)):
        files.append(item)
      if os.path.isdir(os.path.join(expected_path, item)):
        folders.append(item)
    folders.sort()
    files.sort()
    # Вывести с префиксом, который служит фильтром от остальных автозавершений.
    matches = []
    for folder in folders:
      matches.append(('%s\tDir' % ('SA: ' + folder), (folder + '/')))
    for file in files:
      matches.append(('%s\tFile' % ('SA: ' + file), file))

    return matches
    # sublime.DYNAMIC_COMPLETIONS |
    # return (
    #   matches,
    #   sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS | sublime.INHIBIT_REORDER
    # )
