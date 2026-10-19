%global source0_hash 1af8b147eb1405d5839e78aeb93131690495fe9da5c91856cb33ad55a7f1e5b2
Name:           python-roman-numerals
Version:        4.1.0
Release:        3%{?dist}
Summary:        Manipulate well-formed Roman numerals
License:        0BSD
URL:            https://github.com/AA-Turner/roman-numerals/
Source0:        https://files.pythonhosted.org/packages/source/r/roman_numerals/roman_numerals-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.12
Requires:       python3-roman-numerals = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-roman-numerals-py
Summary:        Manipulate well-formed Roman numerals
Provides:       python3.14dist(roman-numerals-py) = %{version}
Provides:       python3dist(roman-numerals-py) = %{version}
%description -n python3-roman-numerals-py

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir roman_numerals-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-roman-numerals-py usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pyproject_check_import
%pytest
%files
%files -n python3-roman-numerals-py -f %{oreon_filedir}/python3-roman-numerals-py.list

%changelog

%autochangelog
