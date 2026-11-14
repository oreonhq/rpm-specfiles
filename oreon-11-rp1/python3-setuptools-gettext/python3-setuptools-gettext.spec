# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash c82d3748859b83f9dd301ed7f564c5811980ba6ac1ef5cb285cb52d935ec4856
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-setuptools-gettext
Version: 0.1.20
Release: 1%{?dist}
Summary: Setuptools plugin for gettext catalogs
License: GPL-2.0-or-later
URL: https://pypi.org/project/setuptools-gettext/
Source0: https://files.pythonhosted.org/packages/f3/e3/2cd04954149680e8fac9f002bd7a425e4b76495c32b55ae0123d1979282e/setuptools_gettext-0.1.20.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
Requires: python3
Requires: python3-setuptools

%description
Setuptools plugin for gettext catalogs.

%prep
%oreon_sha256
%autosetup -n setuptools_gettext-%{version}

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import setuptools_gettext'

%files -f %{_builddir}/%{name}.files
