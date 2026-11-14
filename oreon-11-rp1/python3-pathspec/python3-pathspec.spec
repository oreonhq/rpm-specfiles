# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 17db5ecd524104a120e173814c90367a96a98d07c45b2e10c2f3919fff91bf5a
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-pathspec
Version: 1.1.1
Release: 1%{?dist}
Summary: Utility library for gitignore style pattern matching of file paths.
License: Mozilla Public License 2.0 (MPL 2.0)
URL: https://pypi.org/project/pathspec/
Source0: https://files.pythonhosted.org/packages/5a/82/42f767fc1c1143d6fd36efb827202a2d997a375e160a71eb2888a925aac1/pathspec-1.1.1.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-flit-core
Requires: python3

%description
Utility library for gitignore style pattern matching of file paths.

%prep
%oreon_sha256
%autosetup -n pathspec-1.1.1

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import pathspec'

%files -f %{_builddir}/%{name}.files
