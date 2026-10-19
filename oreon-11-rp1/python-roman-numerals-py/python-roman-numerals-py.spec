%global source0_hash f5d7b2b4ca52dd855ef7ab8eb3590f428c0b1ea480736ce32b01fef2a5f8daf9
Name:           python-roman-numerals-py
Version:        4.1.0
Release:        1%{?dist}
Summary:        This package is deprecated, switch to roman-numerals.
License:        0BSD OR CC0-1.0
URL:            https://github.com/AA-Turner/roman-numerals/
Source0:        https://files.pythonhosted.org/packages/source/r/roman_numerals_py/roman_numerals_py-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-roman-numerals-py = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-roman-numerals-py
Summary:        This package is deprecated, switch to roman-numerals.
# oreon:reqs
Requires:       python3dist(roman-numerals) == 4.1.0
# /oreon:reqs
%description -n python3-roman-numerals-py

%prep
%global oreon_srcdir roman_numerals_py-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-roman-numerals-py usr/lib/python3*/site-packages/roman_numerals_py* usr/lib64/python3*/site-packages/roman_numerals_py* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/roman_numerals_py* usr/lib64/python3*/site-packages/roman_numerals_py* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-roman-numerals-py -f %{oreon_filedir}/python3-roman-numerals-py.list

%changelog

%autochangelog
