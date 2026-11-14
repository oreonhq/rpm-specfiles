# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 4c422bd4d554fcff5de5b73e9596f85e41e9f97f7e553d8f7595ecb31a627bef
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-hatchling
Version: 1.33.0
Release: 1%{?dist}
Summary: Modern, extensible Python build backend
License: MIT
URL: https://pypi.org/project/hatchling/
Source0: https://files.pythonhosted.org/packages/7a/f1/e47b937226ae3b093bbd0132eb0b7ee5bfad12c2b5324afd10ae49946b05/hatchling-1.33.0.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-packaging
BuildRequires: python3-pathspec
BuildRequires: python3-pluggy
BuildRequires: python3-trove-classifiers
BuildRequires: python3-tomlkit
Requires: python3
Requires: python3-packaging
Requires: python3-pathspec
Requires: python3-pluggy
Requires: python3-trove-classifiers
Requires: python3-tomlkit

%description
Modern, extensible Python build backend

%prep
%oreon_sha256
%autosetup -n hatchling-1.33.0

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
PYTHONPATH=%{buildroot}%{python3_sitelib}:%{buildroot}%{python3_sitearch} python3 -c 'import hatchling'

%files -f %{_builddir}/%{name}.files
