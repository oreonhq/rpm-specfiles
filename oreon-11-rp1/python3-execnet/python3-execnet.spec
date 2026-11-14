# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 63d83bfdd9a23e35b9c6a3261412324f964c2ec8dcd8d3c6916ee9373e0befcd
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-execnet
Version: 2.1.2
Release: 1%{?dist}
Summary: execnet: rapid multi-Python deployment
License: MIT License
URL: https://pypi.org/project/execnet/
Source0: https://files.pythonhosted.org/packages/bf/89/780e11f9588d9e7128a3f87788354c7946a9cbb1401ad38a48c4db9a4f07/execnet-2.1.2.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-hatchling
BuildRequires: python3-hatch-vcs
BuildRequires: python3-hatch-vcs
Requires: python3

%description
execnet: rapid multi-Python deployment

%prep
%oreon_sha256
%autosetup -n execnet-2.1.2

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import execnet'

%files -f %{_builddir}/%{name}.files
