# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 6b11616a6bcf3a40e635f082bb232fa57b5e0dd7f517bd7ddd69ec3794508a47

Name: python3-pyasn1
Version: 0.6.5
Release: 1%{?dist}
Summary: ASN.1 toolkit for Python
License: BSD-2-Clause
URL: https://github.com/pyasn1/pyasn1
Source0: https://files.pythonhosted.org/packages/88/7e/3c0da41061a2021cac7cd524fd57092adbe5b515e8bf9005702e366802e2/pyasn1-%{version}.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
BuildRequires: python3-pytest

Requires: python3
Provides: python3dist(pyasn1) = %{version}

%description
Pure-Python implementation of ASN.1 types and codecs.

%prep
%oreon_sha256
%autosetup -n pyasn1-%{version}

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} python3 -m pytest -v

%files -f %{_builddir}/%{name}.files
%license LICENSE.rst

%changelog
%autochangelog
