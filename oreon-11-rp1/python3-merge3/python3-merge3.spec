# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 4a8251068cdb2c1aba76d31ae6aff5e6a47c79a1ee1071d5a58f37bf09f2a790
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-merge3
Version: 1.0.0
Release: 1%{?dist}
Summary: Python implementation of 3-way merge
License: MIT
URL: https://pypi.org/project/merge3/
Source0: https://files.pythonhosted.org/packages/41/f7/5c8c25a763bf630cc26a466c86bb336ee2ed607e459c6d12dac20a6d3aad/merge3-1.0.0.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
Requires: python3

%description
Python implementation of 3-way merge

%prep
%oreon_sha256
%autosetup -n merge3-1.0.0

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import merge3'

%files -f %{_builddir}/%{name}.files
