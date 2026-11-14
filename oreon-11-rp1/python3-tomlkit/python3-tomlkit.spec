# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 83e32755ba1d20d9340bd069ee97e9f6232ba2346b63ffcba425de01f7e327a6
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-tomlkit
Version: 0.15.2
Release: 1%{?dist}
Summary: Style preserving TOML library
License: MIT
URL: https://pypi.org/project/tomlkit/
Source0: https://files.pythonhosted.org/packages/08/72/fc01563df95c189a9f65850096bdc205bc2fe37da6c740cd64afaf18d07e/tomlkit-0.15.2.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-poetry-core
Requires: python3

%description
Style preserving TOML library.

%prep
%oreon_sha256
%autosetup -n tomlkit-%{version}

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import tomlkit'

%files -f %{_builddir}/%{name}.files
