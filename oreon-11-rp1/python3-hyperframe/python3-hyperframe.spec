# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash f630908a00854a7adeabd6382b43923a4c4cd4b821fcb527e6ab9e15382a3b08

Name: python3-hyperframe
Version: 6.1.0
Release: 1%{?dist}
Summary: HTTP/2 framing layer for Python
License: MIT
URL: https://github.com/python-hyper/hyperframe
Source0: https://files.pythonhosted.org/packages/02/e7/94f8232d4a74cc99514c13a9f995811485a6903d48e5d952771ef6322e30/hyperframe-%{version}.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
BuildRequires: python3-wheel
BuildRequires: python3-pytest

Requires: python3
Provides: python3dist(hyperframe) = %{version}

%description
Hyperframe provides pure-Python HTTP/2 frame encoding and decoding.

%prep
%oreon_sha256
%autosetup -n hyperframe-%{version}

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
