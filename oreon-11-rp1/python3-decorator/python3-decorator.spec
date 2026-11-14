# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 4cbcdd55a6efadb9dbea26b858f4fb3264567b52d69ca0d25b721b553f60ea82

Name: python3-decorator
Version: 5.3.1
Release: 1%{?dist}
Summary: Decorators for Python
License: BSD-2-Clause
URL: https://github.com/micheles/decorator
Source0: https://files.pythonhosted.org/packages/60/8b/32f9823da46cde7df2087faa08cd98d01b908f8dcab982cdba9c84e85355/decorator-%{version}.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools

Requires: python3
Provides: python3dist(decorator) = %{version}

%description
Utilities for defining signature-preserving Python decorators.

%prep
%oreon_sha256
%autosetup -n decorator-%{version}

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} python3 - <<'PY'
from decorator import decorator
@decorator
def passthrough(func, *args, **kwargs):
    return func(*args, **kwargs)
@passthrough
def add(left, right):
    return left + right
assert add(2, 3) == 5
PY

%files -f %{_builddir}/%{name}.files
%license LICENSE.txt

%changelog
%autochangelog
