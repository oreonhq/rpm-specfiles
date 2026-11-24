# Taken from https://sourceforge.net/p/ruamel-yaml/tickets/534/

from io import StringIO
from ruamel.yaml import YAML

original = '0: foo\n'
py_original = {0: 'foo'}
prefix = '%YAML 1.1\n---\n'

yaml = YAML()
yaml.version = (1, 1)

loaded = yaml.load(original)
assert loaded == py_original

print('Fresh')
stream = StringIO()
yaml.dump(py_original, stream)
fresh = stream.getvalue()
print(fresh)
assert fresh.startswith(prefix)
trimmed = fresh[len(prefix):]
assert trimmed == original, f"{trimmed!r} != {original!r}"

print('Round trip')
stream = StringIO()
yaml.dump(loaded, stream)
round_tripped = stream.getvalue()
print(round_tripped)
assert round_tripped.startswith(prefix)
trimmed = round_tripped[len(prefix):]
assert trimmed == original, f"{trimmed!r} != {original!r}"
