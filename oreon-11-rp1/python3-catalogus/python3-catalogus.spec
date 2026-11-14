# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 0737aced12078b67e9ef5c0cd5fda0a8c14fd6007a83c1e4c1930a2245e2bd9a
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-catalogus
Version: 0.1.2
Release: 1%{?dist}
Summary: Classes to provide name-to-object registry-like support
License: GPL-2.0-or-later
URL: https://pypi.org/project/catalogus/
Source0: https://files.pythonhosted.org/packages/e9/70/d88303967b16fd7f937a281fe9899ea5c34602296d8a6a07bb188acaf218/catalogus-0.1.2.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
BuildRequires: python3-setuptools_scm
Requires: python3

%description
Classes to provide name-to-object registry-like support

%prep
%oreon_sha256
%autosetup -n catalogus-0.1.2

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import catalogus'

%files -f %{_builddir}/%{name}.files
