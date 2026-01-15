import ab12345_config as config

def print_header():
    print("-" * 30)
    print(f"{config.UNIVERSITY_NAME}")
    print(f"{config.FACULTY}")
    print("-" * 30)

def format_result(label, value):
    return f"{label}: {value}"