# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash e9d912827f872c029017a53f0ef2180b327c3f7fd23c87229f7a8e8b70031d4d
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-sphinxcontrib-serializinghtml
Version: 2.0.0
Release: 1%{?dist}
Summary: sphinxcontrib-serializinghtml is a sphinx extension which outputs "...
License: BSD License
URL: https://pypi.org/project/sphinxcontrib-serializinghtml/
Source0: https://files.pythonhosted.org/packages/3b/44/6716b257b0aa6bfd51a1b31665d1c205fb12cb5ad56de752dfa15657de2f/sphinxcontrib_serializinghtml-2.0.0.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-flit-core
Requires: python3

%description
sphinxcontrib-serializinghtml is a sphinx extension which outputs "...

%prep
%oreon_sha256
%autosetup -n sphinxcontrib_serializinghtml-2.0.0

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import sphinxcontrib.serializinghtml'

%files -f %{_builddir}/%{name}.files
