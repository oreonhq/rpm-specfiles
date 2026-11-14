# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 01932bc4f7e4c15f6b57b208224e78490d3f4af777869aaeb877a965637c8095
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: breezy
Version: 3.3.25
Release: 1%{?dist}
Summary: Friendly distributed version control system
License: GPL-2.0-or-later
URL: https://pypi.org/project/breezy/
Source0: https://files.pythonhosted.org/packages/e4/31/8b72e0d4588dac3b0c09fb31844bddf51c512be445f733fa55c640c46fa5/breezy-3.3.25.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
BuildRequires: python3-cython
BuildRequires: python3-setuptools-rust
BuildRequires: python3-setuptools-gettext
BuildRequires: rust
BuildRequires: cargo
BuildRequires: gcc
BuildRequires: python3-catalogus
BuildRequires: python3-configobj
BuildRequires: python3-fastbencode
BuildRequires: python3-patiencediff
BuildRequires: python3-merge3
BuildRequires: python3-dulwich
BuildRequires: python3-urllib3
BuildRequires: python3-pyyaml
BuildRequires: python3-vcsgraph
Requires: python3
Requires: python3-catalogus
Requires: python3-configobj
Requires: python3-fastbencode
Requires: python3-patiencediff
Requires: python3-merge3
Requires: python3-dulwich
Requires: python3-urllib3
Requires: python3-pyyaml
Requires: python3-vcsgraph

%description
Friendly distributed version control system

%prep
%oreon_sha256
%autosetup -n breezy-3.3.25

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
ln -s brz %{buildroot}%{_bindir}/bzr
%oreon_filelist
sed -i '\|/bin/bzr$|d;\|/bin/brz$|d' %{_builddir}/%{name}.files

%check
python3 -c 'import breezy'

%files -f %{_builddir}/%{name}.files
%{_bindir}/brz
%{_bindir}/bzr
