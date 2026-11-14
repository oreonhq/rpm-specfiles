# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash fcc3c0cb8bfe7f4b3bb0e231c04b15dbad068cb3c2515f343d8fde4dce93bd5d
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-filelock
Version: 4.2.10
Release: 1%{?dist}
Summary: A platform independent file lock
License: Unlicense
URL: https://pypi.org/project/filelock/
Source0: https://files.pythonhosted.org/packages/a1/cf/05bcdacabdc0aec7dc8e19d76281bd82325df62dae3b6430e9ba57397689/filelock-4.2.10.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-hatchling
BuildRequires: python3-hatch-vcs
BuildRequires: python3-hatch-fancy-pypi-readme
BuildRequires: python3-sbom
Requires: python3

%description
A platform independent file lock

%prep
%oreon_sha256
%autosetup -n filelock-4.2.10

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import filelock'

%files -f %{_builddir}/%{name}.files
