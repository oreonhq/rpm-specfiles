%global source0_hash 78abcf413091bc7c1e4e8c10fbbb438d1ac0b5a87436c5b972c3e8253871b6fb
Name:           python-tables
Version:        3.11.1
Release:        1%{?dist}
Summary:        Hierarchical datasets for Python
License:        ...
URL:            http://www.pytables.org
Source0:        https://files.pythonhosted.org/packages/source/t/tables/tables-%{version}.tar.gz
Patch1:         0001-Skip-tests-that-fail-on-s390x.patch
Patch2:         0001-Skip-failing-test.patch
Patch3:         test_basics.diff
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(blosc2) >= 2.3.0
BuildRequires:  python3dist(cython) >= 3.1
BuildRequires:  python3dist(numpy) >= 2
BuildRequires:  python3dist(setuptools) >= 61.0.0
Requires:       python3-tables = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-tables
Summary:        Hierarchical datasets for Python
# oreon:reqs
Requires:       python3dist(blosc2) >= 2.3.0
Requires:       python3dist(numexpr) >= 2.6.2
Requires:       python3dist(numpy) >= 1.20.0
# /oreon:reqs
%description -n python3-tables

%prep
%global oreon_srcdir tables-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-tables usr/lib/python3*/site-packages/tables* usr/lib64/python3*/site-packages/tables* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/tables* usr/lib64/python3*/site-packages/tables* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-tables -f %{oreon_filedir}/python3-tables.list

%changelog

%autochangelog
