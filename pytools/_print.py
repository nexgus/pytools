from typing import Any


def printdir(obj: Any) -> None:
    prefix = None
    attrs = []
    for x in dir(obj):
        if x.startswith('__') and x.endswith('__'):
            continue
        x0 = x[1] if x[0] == '_' else x[0]
        if x0 != prefix:
            if len(attrs) > 0:
                print(', '.join(attrs))
                attrs = []
            prefix = x0

        if isinstance(getattr(obj, x), property):
            attrs.append(x)
        else:
            # This should be a method.
            attrs.append(f'[{x}]')


if __name__ == '__main__':
    printdir(dict())
