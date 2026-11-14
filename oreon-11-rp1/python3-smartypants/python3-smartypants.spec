# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 39d64ce1d7cc6964b698297bdf391bc12c3251b7f608e6e55d857cd7c5f800c6

Name: python3-smartypants
Version: 2.0.2
Release: 1%{?dist}
Summary: Python typography conversion library
License: BSD-3-Clause
URL: https://github.com/leohemsted/smartypants.py
Source0: https://files.pythonhosted.org/packages/source/s/smartypants/smartypants-%{version}.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3
BuildRequires: python3-build
BuildRequires: python3-docutils
BuildRequires: python3-installer
BuildRequires: python3-setuptools

Requires: python3
Provides: python3dist(smartypants) = %{version}

%description
Smartypants converts straight quotes, dashes and ellipses into
typographically correct characters.

%prep
%oreon_sha256
%autosetup -n smartypants-%{version}

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} python3 -m unittest discover

%files -f %{_builddir}/%{name}.files
%license COPYING
%doc CHANGES.rst README.rst

%changelog
%autochangelog
