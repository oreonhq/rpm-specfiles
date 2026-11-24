# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 00c7c1aaa88358b9c765b6d3000c6eec0ba42abca5351b095321aef446081da3
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global modname ply

%bcond_without tests

Name:           python-%{modname}
Summary:        Python Lex-Yacc
Version:        3.11
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.dabeaz.com/ply/
Source0:        http://www.dabeaz.com/ply/%{modname}-%{version}.tar.gz
Patch0:		262.patch
Patch1:		python-ply-py315-fix.patch
Patch2:   CVE-2025-56005.patch
BuildArch:      noarch

%description
PLY is a straightforward lex/yacc implementation. Here is a list of its 
essential features:
* It is implemented entirely in Python.
* It uses LR-parsing which is reasonably efficient and well suited for larger 
  grammars.
* PLY provides most of the standard lex/yacc features including support 
  for empty productions, precedence rules, error recovery, and support 
  for ambiguous grammars.
* PLY is straightforward to use and provides very extensive error checking.
* PLY doesn't try to do anything more or less than provide the basic lex/yacc 
  functionality. In other words, it's not a large parsing framework or a 
  component of some larger system. 

%package -n python3-%{modname}
Summary:        Python Lex-Yacc
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires: oreon-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{modname}
PLY is a straightforward lex/yacc implementation. Here is a list of its 
essential features:
* It is implemented entirely in Python.
* It uses LR-parsing which is reasonably efficient and well suited for larger 
  grammars.
* PLY provides most of the standard lex/yacc features including support 
  for empty productions, precedence rules, error recovery, and support 
  for ambiguous grammars.
* PLY is straightforward to use and provides very extensive error checking.
* PLY doesn't try to do anything more or less than provide the basic lex/yacc 
  functionality. In other words, it's not a large parsing framework or a 
  component of some larger system.

Python 3 version.

%prep
%oreon_sha256
%setup -n %{modname}-%{version}
%patch -P0 -p1 -b .262
%patch -P1 -p1 -b .py315
%patch -P2 -p1 -b .CVE-2025-56005
find example/ -type f -executable -exec chmod -x {} ';'
find example/ -type f -name '*.py' -exec sed -i \
  -e '1{\@^#!/usr/bin/env python@d}' -e '1{\@^#!/usr/local/bin/python@d}' \
  {} ';'
rm -rf *.egg-info
grep -B1000 "POSSIBILITY OF SUCH DAMAGE" README.md > LICENSE

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l %{modname}

%if %{with tests}
%check
pushd test
  ./cleanup.sh
  %{__python3} testlex.py
  %{__python3} testyacc.py
popd
%endif

%files -n python3-%{modname} -f %{pyproject_files}
%doc CHANGES README.md
%license LICENSE

%changelog
%autochangelog
