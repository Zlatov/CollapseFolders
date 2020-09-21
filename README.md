# CollapseFolders

## Install

__ST2:__

```
cd  ~/.config/sublime-text-2/Packages
git clone git@github.com:Zlatov/CollapseFolders.git
```

__ST3:__

```
cd  ~/.config/sublime-text-3/Packages
git clone git@github.com:Zlatov/CollapseFolders.git
```

## Настройки

__Исключения для поска по файлам проекта__

Сублайм предоставляет настройки для исключения файлов и папок из процесса
индексации (F12) и настройки для исключения из боковой панели (из проекта).

Однако нет настрек для исключения файлов из "поиска по файлам проекта". В
проекте могут быть логи и другие файлы данных, которые должны присутствовать в
проекте, но по ним не должен происходить поиск.

Чтобы добавить такое исключение в проект необходимо:

1. Внестинастройку в проект файла `<project_name>.sublime-project`:

```json
{
  …
  "settings":
  {
    "collapse_folders_find_and_replace_in_project": "<project>; -some/path/; -*.file_ext"
  }
}
```

2. Назначить сочетание клавишь на команду в файле
`~/.config/sublime-text-3/Packages/User/Default (Linux).sublime-keymap`:

```json
[
  …
  { "keys": ["ctrl+shift+f"], "command": "collapse_folders_find_and_replace_in_project" }
]
```
