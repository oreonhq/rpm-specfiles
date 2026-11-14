# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash c9e2916ace8aad64cc13a0d233ee22317f2b9025b9cf3295249fa985cc7082e9
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-sphinxcontrib-htmlhelp
Version: 2.1.0
Release: 1%{?dist}
Summary: sphinxcontrib-htmlhelp is a sphinx extension which renders HTML hel...
License: BSD License
URL: https://pypi.org/project/sphinxcontrib-htmlhelp/
Source0: https://files.pythonhosted.org/packages/43/93/983afd9aa001e5201eab16b5a444ed5b9b0a7a010541e0ddfbbfd0b2470c/sphinxcontrib_htmlhelp-2.1.0.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-flit-core
Requires: python3

%description
sphinxcontrib-htmlhelp is a sphinx extension which renders HTML hel...

%prep
%oreon_sha256
%autosetup -n sphinxcontrib_htmlhelp-2.1.0

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import sphinxcontrib.htmlhelp'

%files -f %{_builddir}/%{name}.files
