%global source0_hash 7ebcb3c29a92f3ceafe79a7a48a5c45677e9e004bbeec5742ac0bbb00560b7a2
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: python-dateutil
Version: 3.0.0
Release: 1%{?dist}
Summary: Date utilities for Python
License: Apache-2.0 OR BSD-3-Clause
URL: https://github.com/dateutil/dateutil
Source0: https://files.pythonhosted.org/packages/0e/df/f15f80383f152452d8985b36d95cb8751f901a3e0ff4cd27f7e118f168e2/python_dateutil-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: oreon-rpm-macros-python
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
BuildRequires: python3-setuptools_scm
BuildRequires: python3-wheel
%endif

Provides: python3-dateutil = %{version}-%{release}
Requires: python3

%description
python-dateutil is a date utility library.

%prep
%oreon_sha256
%autosetup -n python_dateutil-%{version} -p1
sed -i 's/setuptools_scm<8.0/setuptools_scm>=8/' pyproject.toml

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%oreon_py_build

%install
%oreon_py_install
%oreon_py_save_files dateutil
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
%license LICENSE
