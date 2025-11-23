import typer
from src.sorting.constants import ALGOS, INT_ARRAY_TYPES, FLOAT_ARRAY_TYPES
from src.benchmark import benchmark_sorts

app = typer.Typer()


def print_help_commands() -> None:
    typer.echo("Доступные команды:")
    typer.echo("help                  - показать это сообщение")
    typer.echo("show config           - текущие настройки")
    typer.echo("set algo NAME         - выбрать алгоритм сортировки")
    typer.echo("set size N            - размер массива (целое число)")
    typer.echo("set type NAME         - тип массива: rand_int|rand_float|nearly|duplicates|reverse")
    typer.echo("run sort              - один запуск сортировки с текущими настройками")
    typer.echo("run bench             - прогнать все алгоритмы по всем типам массивов")
    typer.echo("quit                  - выход")


@app.command()
def interactive_session():
    """Starts an interactive session."""
    typer.echo("Напишите 'help' для списка команд.")
    current_algo = "quick"
    current_size = 1000
    current_type = "rand_int"

    while True:
        user_input = typer.prompt("sorting>")

        cmd = user_input.strip()
        if not cmd:
            continue

        if cmd == "quit":
            typer.echo("Пока.")
            break

        if cmd == "help":
            print_help_commands()
            continue

        if cmd == "show config":
            typer.echo(
                f"Алгоритм: {current_algo}, "
                f"размер: {current_size}, "
                f"тип массива: {current_type}"
            )
            continue

        parts = cmd.split()
        if parts[0] == "set" and len(parts) >= 3:
            what, value = parts[1], " ".join(parts[2:])

            if what == "algo":
                if value not in ALGOS:
                    typer.echo(f"Неизвестный алгоритм '{value}'. Доступны: {', '.join(ALGOS)}")
                else:
                    current_algo = value
                    typer.echo(f"Алгоритм установлен: {current_algo}")
                    if current_algo == "bucket":
                        current_type = "rand_float"
                        typer.echo(f"Для bucket установлен тип массива: {current_type}")
                    else:
                        current_type = "rand_int"
                        typer.echo(
                            f"Установлен тип массива: {current_type}\n"
                            f"Можно выбрать любой другой из списка: {list(INT_ARRAY_TYPES.keys())}"
                        )

            elif what == "size":
                try:
                    size = int(value)
                    if size <= 0:
                        raise ValueError
                    current_size = size
                    typer.echo(f"Размер массива установлен: {current_size}")
                except ValueError:
                    typer.echo("size должен быть положительным целым числом")

            elif what == "type":
                if value in FLOAT_ARRAY_TYPES and current_algo != "bucket":
                    typer.echo(
                        f"{current_type} не применим к {current_algo}!\n"
                        f"Сначала установи алгоритм bucket: set algo bucket"
                    )
                elif value in INT_ARRAY_TYPES and current_algo == "bucket":
                    typer.echo(
                        f"{current_type} не применим к {current_algo}!\n"
                        f"Сначала установи любой алгоритм кроме bucket: set algo NAME"
                    )
                else:
                    current_type = value
                    typer.echo(f"Тип массива установлен: {current_type}")
            else:
                typer.echo(f"Неизвестный параметр 'set {what}'")

            continue

        if cmd == "run sort":
            algo_func = ALGOS[current_algo]
            gen = INT_ARRAY_TYPES[current_type] if current_type in INT_ARRAY_TYPES else FLOAT_ARRAY_TYPES[current_type]
            arr = gen(current_size)
            typer.echo(
                f"Запуск {current_algo} на {current_type} массиве длины {current_size}..."
            )
            sorted_arr = algo_func(list(arr))
            typer.echo(f"Первые 25 исходных: {arr[:25]}")
            typer.echo(f"Первые 25 отсортированных: {sorted_arr[:25]}")
            continue

        if cmd == "run bench":
            typer.echo("Запуск бенчмарка для всех алгоритмов и всех типов массивов...")

            results = {}
            for algo_name, algo_func in ALGOS.items():
                if algo_name == "bucket":
                    arrays = {
                        name: gen(current_size)
                        for name, gen in FLOAT_ARRAY_TYPES.items()
                    }
                else:
                    arrays = {
                        name: gen(current_size)
                        for name, gen in INT_ARRAY_TYPES.items()
                    }
                results[algo_name] = {}
                for arr_name, arr in arrays.items():
                    avg_time = benchmark_sorts(
                        {arr_name: arr},
                        {algo_name: algo_func},
                    )[algo_name][arr_name]
                    results[algo_name][arr_name] = avg_time

            for algo_name, by_array in results.items():
                typer.echo(f"\nАлгоритм: {algo_name}")
                for arr_name, t in by_array.items():
                    typer.echo(f"  {arr_name}: {t:.6f} сек")
            continue

        typer.echo(f"Неизвестная команда: '{cmd}'. Напиши 'help'.")
