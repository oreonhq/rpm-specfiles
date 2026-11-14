# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 181d3c6996452cb1189c4046c61599b84a5a86e099562ffde77d26984ff26d0f

Name: python3-dns
Version: 2.8.0
Release: 1%{?dist}
Summary: DNS toolkit for Python
License: ISC
URL: https://www.dnspython.org/
Source0: https://files.pythonhosted.org/packages/8c/8b/57666417c0f90f08bcafa776861060426765fdb422eb10212086fb811d26/dnspython-%{version}.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-hatchling
BuildRequires: python3-pytest

Requires: python3
Provides: python3-dnspython = %{version}-%{release}
Provides: python3dist(dnspython) = %{version}

%description
dnspython is a DNS toolkit for Python.

%prep
%oreon_sha256
%autosetup -n dnspython-%{version}

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} python3 -m pytest -v

%files -f %{_builddir}/%{name}.files
%license LICENSE

%changelog
%autochangelog
