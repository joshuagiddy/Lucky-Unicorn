def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


print(formatter("-", "Welcome to the lucky Unicorn Game"))
print(formatter("!", "Congratulations you get a Unicorn"))
print(formatter("*", "Goodbye"))
