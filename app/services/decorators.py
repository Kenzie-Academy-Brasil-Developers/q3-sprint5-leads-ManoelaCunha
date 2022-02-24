from flask import request
from functools import wraps

def verify_keys(trusted_keys: list[str]):

    def inner_function(func):
        @wraps(func)

        def key_is_correct():
            data = request.get_json()

            try:
                for key in trusted_keys:
                    data[key]

                return func()

            except KeyError:
                errors = []
                for key in data.keys():
                    errors.append(key)

                return {
                    "error": "chave(s) incorreta(s)",
                    "expected": trusted_keys,
                    "received": errors
                    }, 400

        return key_is_correct
    return inner_function
