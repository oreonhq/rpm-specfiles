# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash a7db850025b95ded1eae8a46181a1a6c56c92c96f0e2b005d9ff8dc0210cab44
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-idna
Version: 3.20
Release: 1%{?dist}
Summary: Internationalized Domain Names in Applications (IDNA)
License: MIT
URL: https://pypi.org/project/idna/
Source0: https://files.pythonhosted.org/packages/f5/08/8eea9d4b8302028f3abb2c0813953f7aec26d33b7a8960ed760e65ff29fa/idna-3.20.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-flit-core
Requires: python3

%description
Internationalized Domain Names in Applications (IDNA)

%prep
%oreon_sha256
%autosetup -n idna-3.20

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import idna'

%files -f %{_builddir}/%{name}.files
