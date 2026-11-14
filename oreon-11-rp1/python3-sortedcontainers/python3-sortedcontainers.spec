# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 25caa5a06cc30b6b83d11423433f65d1f9d76c4c6a0c90e3379eaa43b9bfdb88

Name: python3-sortedcontainers
Version: 2.4.0
Release: 1%{?dist}
Summary: Sorted container types for Python
License: Apache-2.0
URL: https://github.com/grantjenks/python-sortedcontainers
Source0: https://files.pythonhosted.org/packages/e8/c4/ba2f8066cceb6f23394729afe52f3bf7adec04bf9ed2c820b39e19299111/sortedcontainers-%{version}.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
BuildRequires: python3-wheel

Requires: python3
Provides: python3dist(sortedcontainers) = %{version}

%description
Pure-Python sorted list, dictionary, and set implementations.

%prep
%oreon_sha256
%autosetup -n sortedcontainers-%{version}

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} python3 - <<'PY'
from sortedcontainers import SortedDict, SortedList, SortedSet
assert SortedList([3, 1, 2]) == [1, 2, 3]
assert list(SortedDict({"b": 2, "a": 1})) == ["a", "b"]
assert list(SortedSet([3, 1, 1])) == [1, 3]
PY

%files -f %{_builddir}/%{name}.files
%license LICENSE

%changelog
%autochangelog
