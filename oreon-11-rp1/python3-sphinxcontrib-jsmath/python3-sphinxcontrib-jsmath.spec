# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 551f780cf9687f9c3c74f0cf9f18aca06e0d6958853453f3803fe4d357c5b924
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-sphinxcontrib-jsmath
Version: 2.0.0
Release: 1%{?dist}
Summary: sphinxcontrib-jsmath is a sphinx extension which renders displayed...
License: BSD License
URL: https://pypi.org/project/sphinxcontrib-jsmath/
Source0: https://files.pythonhosted.org/packages/59/02/4f334c7fc3e54c51d2364575a41cd2fae6847e7f53001949f0be5f32e18b/sphinxcontrib_jsmath-2.0.0.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-flit-core
Requires: python3

%description
sphinxcontrib-jsmath is a sphinx extension which renders displayed...

%prep
%oreon_sha256
%autosetup -n sphinxcontrib_jsmath-2.0.0

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import sphinxcontrib.jsmath'

%files -f %{_builddir}/%{name}.files
