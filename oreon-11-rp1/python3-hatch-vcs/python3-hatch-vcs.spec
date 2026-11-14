# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 0395fa126940340215090c344a2bf4e2a77bcbe7daab16f41b37b98c95809ff9
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-hatch-vcs
Version: 0.5.0
Release: 1%{?dist}
Summary: Hatch plugin for versioning from a VCS
License: MIT
URL: https://pypi.org/project/hatch-vcs/
Source0: https://files.pythonhosted.org/packages/6b/b0/4cc743d38adbee9d57d786fa496ed1daadb17e48589b6da8fa55717a0746/hatch_vcs-0.5.0.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-hatchling
BuildRequires: python3-setuptools_scm
Requires: python3
Requires: python3-hatchling
Requires: python3-setuptools_scm

%description
Hatch plugin for versioning from a VCS.

%prep
%oreon_sha256
%autosetup -n hatch_vcs-%{version}

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import hatch_vcs'

%files -f %{_builddir}/%{name}.files
