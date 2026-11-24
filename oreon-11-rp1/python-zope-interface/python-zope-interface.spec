# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 0b47b62e8d0d99b24bcdd32f4f2120425e5019c3bee2ad69a0e1d75737487a96
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%if 0%{?oreon}
%bcond docs 0
%else
%bcond docs %{undefined rhel}
%endif
%bcond tests 1

%global _docdir_fmt %{name}

Name:		python-zope-interface
Version:	8.7
Release:        %{autorelease}
Summary:	Zope 3 Interface Infrastructure
License:	ZPL-2.1
URL:		https://pypi.io/project/zope.interface
Source0:	%{pypi_source zope_interface}

%description
Interfaces are a mechanism for labeling objects as conforming to a given API
or contract.

This is a separate distribution of the zope.interface package used in Zope 3.

%package -n python3-zope-interface
Summary:	Zope 3 Interface Infrastructure

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  make
BuildRequires:  python3-devel

%description -n python3-zope-interface
Interfaces are a mechanism for labeling objects as conforming to a given API
or contract.

This is a separate distribution of the zope.interface package used in Zope 3.

%if %{with docs}
%package doc
Summary:        Documentation for zope.interface
BuildArch:      noarch
BuildRequires:  python3-docs

%description doc
Documentation for %{name}.
%endif

%prep
%oreon_sha256
%autosetup -n zope_interface-%{version} -p1

sed -i '/setuptools/s/<.*"/"/' pyproject.toml

sed -i "s/'default'/'classic'/" docs/conf.py

sed -i "s|\('https://docs\.python\.org/': \)None|\1'%{_docdir}/python3-docs/html/objects.inv'|" docs/conf.py

sed -i "/coverage/d" setup.py

%generate_buildrequires
%pyproject_buildrequires %{?with_docs: -x docs} %{?with_tests: -x test}

%build
%pyproject_wheel

%if %{with docs}
PYTHONPATH=$PWD/src make -C docs html
rm -f docs/_build/html/.buildinfo
%endif

%install
%pyproject_install
%pyproject_save_files -l zope

%check
%py3_check_import zope.interface
%if %{with tests}
pushd %{buildroot}%{python3_sitearch}
PURE_PYTHON=1 python3 -m unittest discover -vv -s zope/interface -t .
popd
%endif

%files -n python3-zope-interface -f %{pyproject_files}
%doc README.rst CHANGES.rst
%license COPYRIGHT.txt
%exclude %{python3_sitearch}/zope/interface/tests/
%exclude %{python3_sitearch}/zope/interface/common/tests/
%exclude %{python3_sitearch}/zope/interface/*.c

%if %{with docs}
%files doc
%doc docs/_build/html/
%endif

%changelog
%autochangelog
