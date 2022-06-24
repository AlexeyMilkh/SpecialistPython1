# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"

text = input("Put your text here:")

if text.count(",") > text.count("."):
    print("More: ,")
elif text.count(".") > text.count(","):
    print("More: .")
else:
    print("=")
