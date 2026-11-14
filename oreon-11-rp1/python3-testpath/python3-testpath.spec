# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 2f1b97e6442c02681ebe01bd84f531028a7caea1af3825000f52345c30285e0f
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-testpath
Version: 0.6.0
Release: 1%{?dist}
Summary: Test utilities for code working with files and commands
License: BSD License
URL: https://pypi.org/project/testpath/
Source0: https://files.pythonhosted.org/packages/08/ad/a3e7d580902f57e31d2181563fc4088894692bb6ef79b816344f27719cdc/testpath-0.6.0.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-flit-core
Requires: python3

%description
Test utilities for code working with files and commands

%prep
%oreon_sha256
%autosetup -n testpath-0.6.0

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import testpath'

%files -f %{_builddir}/%{name}.files
