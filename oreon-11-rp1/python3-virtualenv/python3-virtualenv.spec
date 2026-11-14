# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash c8b65c7d206ca6ef18de9352c160b3f04f66fff9f6b0ec8fd31f14688eba52c4
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-virtualenv
Version: 21.15.6
Release: 1%{?dist}
Summary: Virtual Python environment builder
License: MIT
URL: https://pypi.org/project/virtualenv/
Source0: https://files.pythonhosted.org/packages/b3/bd/e40ad2df6a9efc1f859ea23d63fd7371cff68252833f182ca9af819bb4d3/virtualenv-21.15.6.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-hatchling
BuildRequires: python3-hatch-vcs
BuildRequires: python3-hatch-fancy-pypi-readme
BuildRequires: python3-distlib
BuildRequires: python3-filelock
BuildRequires: python3-packaging
BuildRequires: python3-platformdirs
BuildRequires: python3-python-discovery
Requires: python3
Requires: python3-distlib
Requires: python3-filelock
Requires: python3-packaging
Requires: python3-platformdirs
Requires: python3-python-discovery

%description
Virtual Python environment builder

%prep
%oreon_sha256
%autosetup -n virtualenv-21.15.6

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import virtualenv'

%files -f %{_builddir}/%{name}.files
