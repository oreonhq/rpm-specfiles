# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 55ca7c70a75689be937aa27f8ff4b018f06ff4838fc73045560bf0f5a1291060
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-werkzeug
Version: 3.1.9
Release: 1%{?dist}
Summary: The comprehensive WSGI web application library
License: BSD-3-Clause
URL: https://pypi.org/project/werkzeug/
Source0: https://files.pythonhosted.org/packages/a4/34/4dd12fc8bb7d61c91467ec3efe415ffa7d5456f799954b40c5bbaeae470e/werkzeug-3.1.9.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-flit-core
BuildRequires: python3-markupsafe
Requires: python3
Requires: python3-markupsafe

%description
The comprehensive WSGI web application library

%prep
%oreon_sha256
%autosetup -n werkzeug-3.1.9

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import werkzeug'

%files -f %{_builddir}/%{name}.files
