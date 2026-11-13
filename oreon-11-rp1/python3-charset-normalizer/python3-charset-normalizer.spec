# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 39de2a259fc954455c57274dc94c79d5842774e1247a016aff30bc0efed0f4ef
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-charset-normalizer
Version: 3.5.2
Release: 1%{?dist}
Summary: Real first universal charset detector
License: MIT
URL: https://pypi.org/project/charset-normalizer/
Source0: https://files.pythonhosted.org/packages/33/1c/f41d4e74c28ab327ff3acd36053f7ea506c55872d7a90b0fa71aa3ab0c89/charset_normalizer-3.5.2.tar.gz
Patch0: charset-normalizer-setuptools-unbound.patch
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-wheel
BuildRequires: python3-setuptools
Requires: python3

%description
Detects the encoding of text byte streams.

%prep
%oreon_sha256
%autosetup -n charset_normalizer-3.5.2 -p1

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
PYTHONPATH=%{buildroot}%{python3_sitelib}:%{buildroot}%{python3_sitearch} python3 -c 'import charset_normalizer'

%files -f %{_builddir}/%{name}.files
%license LICENSE
