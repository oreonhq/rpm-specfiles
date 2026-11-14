# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 0b48f17296f869db89221c3bde463fdff35152a4cb99ae4aaa42b0b64333fc6c

Name: python3-gssapi
Version: 1.12.0
Release: 1%{?dist}
Summary: Python GSSAPI bindings
License: ISC
URL: https://github.com/pythongssapi/python-gssapi
Source0: https://files.pythonhosted.org/packages/6b/fb/9492eb37b5786369b7e96fff2cf4040713acb33b96124813e058cbbd4356/gssapi-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: krb5-devel
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
BuildRequires: python3-cython
BuildRequires: python3-decorator

Requires: krb5-libs
Requires: python3
Requires: python3-decorator
Provides: python3dist(gssapi) = %{version}

%description
Python bindings for the Generic Security Service Application Program
Interface.

%prep
%oreon_sha256
%autosetup -n gssapi-%{version}

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
PYTHONPATH=%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib} \
  python3 -c 'import gssapi; from gssapi.raw import NameType'

%files -f %{_builddir}/%{name}.files
%license LICENSE.txt
%doc README.txt

%changelog
%autochangelog
