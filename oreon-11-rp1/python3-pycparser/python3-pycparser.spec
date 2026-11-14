# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash f03387877eab82ce01bbdfd0ba7252ee55a90b1c708d5129e2ce915475cf1db6
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-pycparser
Version: 3.12
Release: 1%{?dist}
Summary: C parser in Python
License: BSD-3-Clause
URL: https://pypi.org/project/pycparser/
Source0: https://files.pythonhosted.org/packages/cb/27/eeb9f307bf07060f3d9f9aa0fb8c15b01bdfded0a941e4b2719c7f94cacd/pycparser-3.12.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
Requires: python3

%description
C parser in Python

%prep
%oreon_sha256
%autosetup -n pycparser-3.12

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import pycparser'

%files -f %{_builddir}/%{name}.files
