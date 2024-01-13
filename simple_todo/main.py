import os
import platform
from datetime import datetime, timedelta
import typer
import pandas as pd
from tabulate import tabulate

app = typer.Typer(help="The simplest python ToDo cli app")

pasta = os.path.dirname(os.path.abspath(__file__))
caminho_csv = os.path.join(pasta, ".list.csv")

sys = platform.system()


def is_bissexto(x: int):
    if str(x)[-2:] == "00":
        if x % 400:
            return True
    else:
        if x % 4 == 0:
            return True
        else:
            return False


def time_transform(x):
    time_task = datetime.strptime(x, "%Y-%M-%d %H:%M:%S")
    diff = datetime.now() - time_task
    diff = diff.total_seconds
    types_time = {0: 0, 60 * 60 * 24 * 7: 0, 60 * 60 * 24: 0, 60 * 60: 0, 60: 0, 1: 0}
    types_time_string = [
        " years,",
        " weeks,",
        " days,",
        " hours,",
        " minutes,",
        " seconds",
    ]
    if is_bissexto(datetime.today().year()):
        types_time[0] = 60 * 60 * 24 * 366
    else:
        types_time[0] = 60 * 60 * 24 * 365
    temp = diff
    for key in types_time.keys():
        count = 0
        while temp >= key:
            temp -= key
            count += 1
        types_time.update({key: count})
    final_string = []
    i = 0
    for value in types_time.values():
        if value:
            if value == 1:
                if i != 5:
                    types_time_string[i].replace("s", "")
                else:
                    types_time_string[5] = " second"
            final_string.append(f"{value}{types_time_string[i]}")
        i += 1


@app.command()
def view():
    """
    Views the current ToDos, whether marked or unmarked.
    If the user didn't add any ToDos, it creates an empty ToDo list.
    If the user finishes all tasks, it clears the file.
    """
    try:
        file = pd.read_csv(caminho_csv, sep=",")
        # all_done condition to clear the file
        all_done = False
        empty = file["Finished"].isnull().all()
        if file["Finished"].all() and not empty:
            all_done = True
        # change true/false to cool emojis
        emoji_map = {True: "✅", False: "❌"}
        file["Finished"] = file["Finished"].map(emoji_map)
        # make time look cool
        file["Time"] = file["Time"].apply()
        if not empty:
            if sys == "Windows":
                os.system("cls")
            else:
                os.system("clear")
            print(
                f'{tabulate(file, headers=file.head(), tablefmt="simple",showindex="always")}\n'
            )
            if all_done:
                print("You've finished all of your tasks!")
                os.remove(caminho_csv)
                with open(caminho_csv, "w") as file:
                    file.write("Task,Finished,Time")

    except FileNotFoundError:
        with open(caminho_csv, "w") as file:
            print("You didn't add any ToDos!")
            file.write("Task,Finished,Time")


@app.command()
def add(item: str):
    """
    Adds a new todo at the bottom at the list

    Usage: add "your todo here"
    """
    today = datetime.now().strftime("%Y-%M-%d %H:%M:%S")
    with open(caminho_csv, "a+") as file:
        file.write(f"\n{item},False,{today}")


@app.command()
def mark(row: int):
    """
    Marks one of your tasks

    Example: mark 2 3
    Then the rows 2 and 3 will be checked
    """
    try:
        file = pd.read_csv(caminho_csv)
        if 0 <= row < len(file):
            if not file.at[row, "Finished"]:
                file.at[row, "Finished"] = True
                file.to_csv(caminho_csv, index=False)
            else:
                print(f"Task {row} was already finished!")
        else:
            print("Please inform valid rows")
    except FileNotFoundError:
        with open(caminho_csv, "w") as file:
            file.write("Task,Finished,Time")


@app.command()
def rename(row: int, task: str):
    """
    Renames one of your current tasks
    Example: rename 2 "your todo"
    Then the task with index 2 will be renamed to "your todo" (without quotes)
    """
    try:
        file = pd.read_csv(caminho_csv)
        if 0 <= row < len(file):
            file.at[row, "Task"] = task
            file.to_csv(caminho_csv, index=False)
            print("The task was renamed")
        else:
            print("Please inform a valid row")
    except FileNotFoundError:
        with open(caminho_csv, "w") as file:
            file.write("Task,Finished,Time")
