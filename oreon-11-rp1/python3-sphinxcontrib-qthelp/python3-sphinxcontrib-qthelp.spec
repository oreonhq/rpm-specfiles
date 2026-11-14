# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 4fe7d0ac8fc171045be623aba3e2a8f613f8682731f9153bb2e40ece16b9bbab
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-sphinxcontrib-qthelp
Version: 2.0.0
Release: 1%{?dist}
Summary: sphinxcontrib-qthelp is a sphinx extension which outputs QtHelp doc...
License: BSD License
URL: https://pypi.org/project/sphinxcontrib-qthelp/
Source0: https://files.pythonhosted.org/packages/68/bc/9104308fc285eb3e0b31b67688235db556cd5b0ef31d96f30e45f2e51cae/sphinxcontrib_qthelp-2.0.0.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-flit-core
Requires: python3

%description
sphinxcontrib-qthelp is a sphinx extension which outputs QtHelp doc...

%prep
%oreon_sha256
%autosetup -n sphinxcontrib_qthelp-2.0.0

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import sphinxcontrib.qthelp'

%files -f %{_builddir}/%{name}.files
