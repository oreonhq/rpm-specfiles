# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 2f284428dda6c3c48c580de0e18470ff9c7f5ef628a647ee8002f38c3f9097ca

Name: python3-hypothesis
Version: 6.151.9
Release: 1%{?dist}
Summary: Property-based testing library for Python
License: MPL-2.0
URL: https://hypothesis.works/
Source0: https://files.pythonhosted.org/packages/19/e1/ef365ff480903b929d28e057f57b76cae51a30375943e33374ec9a165d9c/hypothesis-%{version}.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
BuildRequires: python3-wheel
BuildRequires: python3-sortedcontainers

Requires: python3
Requires: python3-sortedcontainers >= 2.1.0
Provides: python3dist(hypothesis) = %{version}

%description
Hypothesis is a property-based testing library for Python.

%prep
%oreon_sha256
%autosetup -n hypothesis-%{version}

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} python3 - <<'PY'
from hypothesis import given, settings
from hypothesis import strategies as st
@settings(max_examples=50, derandomize=True)
@given(st.integers())
def check_roundtrip(value):
    assert int(str(value)) == value
check_roundtrip()
PY

%files -f %{_builddir}/%{name}.files
%license LICENSE.txt

%changelog
%autochangelog
