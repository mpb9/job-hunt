from sqlite3 import Date


def format_date():
    date = Date.today()

    year = date.strftime("%Y")
    month = date.strftime("%B")
    day = date.strftime("%d")
    if day[0] == "0":
        day = day[1:]

    return f"{month} {day}, {year}"


def skip_line(docx):
    docx.add_paragraph("")


def parse_arg(arg):
    temp_arg = arg.split("_")
    return " ".join(temp_arg)


def parse_arg_list(arg):
    temp_arg = parse_arg(arg)
    return temp_arg.split(",")


def combine_arg_lists(required, known, max_len=5):
    both = [arg for arg in required if arg in known]
    unknown = [arg for arg in required if arg not in known]
    unrequired = [arg for arg in known if arg not in required]
    return both + unknown + unrequired[: max(0, max_len - len(both) - len(unknown))]


def convert_list_to_str(arg_list, known=None, max_len=5):
    if known:
        arg_list = combine_arg_lists(arg_list, known, max_len)

    if len(arg_list) == 1:
        return arg_list[0]

    if len(arg_list) == 2:
        return " and ".join(arg_list)

    if len(arg_list) >= 3:
        last_arg = arg_list.pop()
        arg_list.append(f"and {last_arg}")
        return ", ".join(arg_list)

    return None
