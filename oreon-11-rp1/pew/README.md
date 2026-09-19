# Pew

Python Env Wrapper is a set of commands to manage multiple virtual
environments. Pew can create, delete and copy your environments, using a
single command to switch to them wherever you are, while keeping them in a
single (configurable) location.

## Python version management functionality is removed in Fedora 30+

Fedora provides excellent native means for using multiple different Python
versions. One can install a non-default Python version, e.g. Python 3.6, by
using:

```
sudo dnf install python36
```

For more information, refer to:
https://developer.fedoraproject.org/tech/languages/python/multiple-pythons.html.

Hence, removing the Python versions management from Pew itself should really
be a non-issue.
In addition, there is strong support upstream to either remove Pew's Python
version management or replace it with pyenv:
https://github.com/berdario/pew/issues/195.
