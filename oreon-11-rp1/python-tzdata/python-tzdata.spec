%global source0_hash 8cc73c0a0bfca7dbfa59235d60b2eff82231dee33f53d206db1acd9173cfc0a7
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: python-tzdata
Version: 2026.5
Release: 1%{?dist}
Summary: IANA time zone data for Python
License: Apache-2.0
URL: https://github.com/python/tzdata
Source0: https://files.pythonhosted.org/packages/d9/68/f1b440335057bfce71b6e50a9d09445aa2ecbd08359a337976627b8409e7/tzdata-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: oreon-rpm-macros-python
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
BuildRequires: python3-wheel
%endif

Provides: python3-tzdata = %{version}-%{release}
Requires: python3

%description
tzdata ships the IANA time zone database for Python.

%prep
%oreon_sha256
%autosetup -n tzdata-%{version} -p1

%build
%oreon_py_build

%install
%oreon_py_install
%oreon_py_save_files tzdata
python3 - %{oreon_py_files} << 'PY'
import os
import sys
from pathlib import Path
p = Path(sys.argv[1])
lines = p.read_text().splitlines()
seen = set(lines)
extra = []
for line in lines:
    path = line.strip().strip('"')
    if not path.endswith(".py"):
        continue
    if "/lib/python3." not in path and "/lib64/python3." not in path:
        continue
    glob = os.path.dirname(path) + "/__pycache__/*"
    if glob not in seen:
        seen.add(glob)
        extra.append(glob)
text = "\n".join(lines + extra)
p.write_text(text + ("\n" if text else ""))
PY

%files -f %{oreon_py_files}
%license LICENSE licenses/LICENSE_APACHE
