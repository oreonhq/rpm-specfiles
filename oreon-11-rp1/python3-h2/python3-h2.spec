# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 4e866ffb1a869ae14dd9b5e6beb5c24a13da0495ad72b65925ded182521c1516

Name: python3-h2
Version: 4.4.1
Release: 1%{?dist}
Summary: HTTP/2 protocol stack for Python
License: MIT
URL: https://github.com/python-hyper/h2
Source0: https://files.pythonhosted.org/packages/e7/85/7c366e69d84c17bb778fe41419e1fbcce3033d5b7ce29bbffff0a98b859f/h2-%{version}.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
BuildRequires: python3-wheel
BuildRequires: python3-pytest
BuildRequires: python3-hyperframe >= 6.1
BuildRequires: python3-hpack >= 4.2

Requires: python3
Requires: python3-hyperframe >= 6.1
Requires: python3-hpack >= 4.2
Provides: python3dist(h2) = %{version}

%description
Pure-Python implementation of the HTTP/2 protocol.

%prep
%oreon_sha256
%autosetup -n h2-%{version}

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} python3 -m pytest -v

%files -f %{_builddir}/%{name}.files
%license LICENSE

%changelog
%autochangelog
