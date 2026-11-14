# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 0895cfa3b5531fc65fe439c05eb65144f123bf7a394fcaa56aa423548d8e45c0

Name: python3-hpack
Version: 4.2.0
Release: 1%{?dist}
Summary: HTTP/2 header compression for Python
License: MIT
URL: https://github.com/python-hyper/hpack
Source0: https://files.pythonhosted.org/packages/26/5b/fcabf6028144a8723726318b07a32c2f3314acdff6265743cf08a344b18e/hpack-%{version}.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
BuildRequires: python3-wheel
BuildRequires: python3-pytest
BuildRequires: python3-hypothesis

Requires: python3
Provides: python3dist(hpack) = %{version}

%description
HPACK header compression implementation for HTTP/2 in Python.

%prep
%oreon_sha256
%autosetup -n hpack-%{version}

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} \
  python3 -m pytest -v -k 'not test_get_by_index_out_of_range'

%files -f %{_builddir}/%{name}.files
%license LICENSE

%changelog
%autochangelog
