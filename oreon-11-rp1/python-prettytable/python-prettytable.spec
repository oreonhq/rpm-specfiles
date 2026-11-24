# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 9665594d137fb08a1117518c25551e0ede1687197cf353a4fdc78d27e1073568
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%if 0%{?rhel} || 0%{?oreon}
%bcond lf 0
%else
%bcond lf 1
%endif

%global pypi_name prettytable

Name:           python-%{pypi_name}
Version:        3.10.0
Release:        %{autorelease}
Summary:        Python library to display tabular data in tables

License:        BSD-3-Clause
URL:            https://github.com/jazzband/prettytable
Source0:        prettytable-%{version}.tar.gz

BuildArch:      noarch

BuildRequires: oreon-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  sed
BuildRequires:  python3dist(pytest)
%if %{with lf}
BuildRequires:  python3dist(pytest-lazy-fixtures)
%endif
BuildRequires:  python3dist(wcwidth)

%description
PrettyTable is a simple Python library designed to make it quick and easy to
represent tabular data in visually appealing ASCII tables. It was inspired by
the ASCII tables used in the PostgreSQL shell psql. PrettyTable allows for
selection of which columns are to be printed, independent alignment of columns
(left or right justified or centred) and printing of "sub-tables" by specifying
a row range.

%package -n python3-%{pypi_name}
Summary:	Python library to display tabular data in tables

%description -n python3-%{pypi_name}
PrettyTable is a simple Python library designed to make it quick and easy to
represent tabular data in visually appealing ASCII tables. It was inspired by
the ASCII tables used in the PostgreSQL shell psql. PrettyTable allows for
selection of which columns are to be printed, independent alignment of columns
(left or right justified or centred) and printing of "sub-tables" by specifying
a row range.

%prep
%oreon_sha256
%autosetup -n %{pypi_name}-%{version}
sed -i -e '/^*!\//, 1d' src/prettytable/*.py
%if %{without lf}
sed -i -e 's/from pytest_lazy_fixtures import lf/lf = str/' tests/test_prettytable.py
%endif

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files prettytable

%check
%pytest %{!?with_lf:-k 'not TestBuildEquivalence and not TestMultiPattern'}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md CHANGELOG.md

%changelog
%autochangelog
