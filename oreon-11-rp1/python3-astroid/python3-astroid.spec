# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash d515a105722b72098bbe82d430d65e635f742b6cbac3bdfaf8b7c188b87c5e39

Name: python3-astroid
Version: 4.3.4
Release: 1%{?dist}
Summary: Abstract syntax tree with inference support
License: LGPL-2.1-or-later
URL: https://github.com/pylint-dev/astroid
Source0: https://files.pythonhosted.org/packages/source/a/astroid/astroid-%{version}.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools >= 77
BuildRequires: python3-pytest
Requires: python3

%description
Astroid provides a common representation of Python source code for static
analysis with support for safe inference.

%prep
%oreon_sha256
%autosetup -n astroid-%{version}

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -m pytest

%files -f %{_builddir}/%{name}.files
%license LICENSE
%doc README.rst

%changelog
%autochangelog
