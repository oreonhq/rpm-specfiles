# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 7fc905272cefa4f364c1a3429cbbe9c0f98b793988efb5bf90aac80f08db09b1
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-parameterized
Version: 0.9.0
Release: 1%{?dist}
Summary: Parameterized testing for Python
License: BSD-2-Clause
URL: https://github.com/wolever/parameterized
Source0: https://files.pythonhosted.org/packages/ea/49/00c0c0cc24ff4266025a53e41336b79adaa5a4ebfad214f433d623f9865e/parameterized-0.9.0.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
Requires: python3

%description
Parameterized testing with any Python test framework.

%prep
%oreon_sha256
%autosetup -n parameterized-%{version}

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import parameterized'

%files -f %{_builddir}/%{name}.files

%changelog
%autochangelog
