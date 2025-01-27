
class utils:
    def __init__(self):
        pass

    def read_file(file_name: str) -> str: 
        with open(file_name, 'r') as f:
            lines = f.readlines()
        return lines

    def write_file(file_name: str, text: str) -> None:
        with open(file_name, "w") as f:
            f.write(str)
        return 
