# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 180224db6aed87ba9ce1f2781ebcd5826253de8ff637112090e24b84502bbf9f

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-markdown
Version: 3.11
Release: 1%{?dist}
Summary: Markdown implementation in Python
License: BSD-3-Clause
URL: https://python-markdown.github.io/
Source0: https://files.pythonhosted.org/packages/source/m/markdown/markdown-%{version}.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-pyyaml
BuildRequires: python3-setuptools

Requires: python3

Provides: python3dist(markdown) = %{version}
Provides: python-markdown = %{version}-%{release}

%description
This is a Python implementation of John Gruber's Markdown. It is
almost completely compliant with the reference implementation, though
there are a few very minor differences.

%prep
%oreon_sha256
%autosetup -p1 -n markdown-%{version}

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist
PYTHONPATH=%{buildroot}%{python3_sitelib} \
    %{buildroot}%{_bindir}/markdown_py LICENSE.md > LICENSE.html

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} python3 -m unittest discover tests

%files -f %{_builddir}/%{name}.files
%license LICENSE.html LICENSE.md

%changelog
%autochangelog
