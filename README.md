# py-todo-csv

The simplest python ToDo app.

View your current unfinished activities in your favorite terminal. Designed in way to not procrastinate.

- Add your tasks
- View them in a nice (not pretty) table
- Rename them if you made a mistake
- Mark them when you're finished

 You are NOT able to delete your tasks, unless you have marked them all.

## Installation

To install the program, just open your favorite terminal and use pip

```
pip install py-todo-csv
```

After the installation is complete, you can use the program by typing `todo` followed by the commands.

## Usage


### view

By typing `todo view`, it will show your current ToDos.

### add

Use `todo add "your todo here"` to add your todo to the bottom of the list. If the name of the todo is one word only, you don't need to use the quotes

### mark

To finish your tasks, enter `todo mark` followed by the index of the task. ToDos have a index starting from 0, so if you want to mark your top task, use `todo mark 0`

### rename

If you made a typo or just want to rename the entire task, use `todo rename` followed by the task index and by the new name

Example:
```
    Task         Finished
--  -----------  ----------
 0  a cool task  ❌
```

```
todo rename 0 "a REALLY cool task"
```

```
    Task                Finished
--  ------------------  ----------
 0  a REALLY cool task  ❌
```

And that's it! You are ready to improve your productivity without the need to install heavy GUI programs!

> NOTE: You cannot delete your tasks. The list will be empty after using the view command and all of the tasks are finished.
