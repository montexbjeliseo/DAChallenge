import json
import pandas as pd

def export_to_json(data: list, filename: str):
    """Exportar datos a un archivo JSON."""
    with open(filename, "w") as file:
        json.dump(data, file)


def save_to_file(data, filename):
    with open(filename, "w") as file:
        file.write(data)
        file.close()
