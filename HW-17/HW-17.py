#5
def custom_print(*args, **kwargs):
    separator = ' '
    end_of_str = '\n'
    if "sep" in kwargs:
        separator = kwargs["sep"]
    if "end" in kwargs:
        end_of_str = kwargs["end"]
    L1 = []
    for arg in args:
        L1.append(str(arg))
    for key, value in kwargs.items():
        if key not in ['sep', 'end']:
            L1.append(f"{key}={value}")
    print(separator.join(L1), end=end_of_str)
