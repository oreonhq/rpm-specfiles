# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash f0aa004e98032a6e6be4c9da65e7eb7150e36ca3bf508adbcda82b4d003e61ee

Name: python3-typogrify
Version: 2.1.0
Release: 1%{?dist}
Summary: Filters for typographic web content
License: BSD-3-Clause
URL: https://github.com/mintchaos/typogrify
Source0: https://files.pythonhosted.org/packages/source/t/typogrify/typogrify-%{version}.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-pytest
BuildRequires: python3-setuptools
BuildRequires: python3-smartypants

Requires: python3-smartypants
Provides: python3dist(typogrify) = %{version}

%description
Typogrify provides filters that improve typography in HTML content.

%prep
%oreon_sha256
%autosetup -n typogrify-%{version}

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} \
  python3 -m pytest -v typogrify/packages/titlecase/tests.py

%files -f %{_builddir}/%{name}.files
%license LICENSE.txt
%doc README.md

%changelog
%autochangelog
