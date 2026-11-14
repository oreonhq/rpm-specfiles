# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash d40e8859d71b1d4918e1d918c667bce05928286f2cbd09cfb7a6cc1f3f308ad0
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-scripttest
Version: 3.0
Release: 1%{?dist}
Summary: Helper to test command-line scripts
License: MIT
URL: https://pypi.org/project/scripttest/
Source0: https://files.pythonhosted.org/packages/d9/15/4400839ca2813a77b4110351d1de9956966f74fa5ae702c2faf7fd86ae0d/scripttest-3.0.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-flit-core
Requires: python3

%description
Helper to test command-line scripts

%prep
%oreon_sha256
%autosetup -n scripttest-3.0

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import scripttest'

%files -f %{_builddir}/%{name}.files
