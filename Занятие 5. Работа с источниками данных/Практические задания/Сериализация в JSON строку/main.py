# TODO Импортируйте модуль json
import json

def serialize_to_json_str(python_obj: dict) -> str:
    return json.dumps(python_obj, indent = 4 )
    ...  # TODO Сериализуйте python объект в json строку с отступами


if __name__ == '__main__':
    decimal_to_hex = {decimal: hex(decimal) for decimal in range(16)}
    # print(decimal_to_hex)
    json_str = serialize_to_json_str(decimal_to_hex)
    print(json_str)
