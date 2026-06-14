%global source0_hash 1af8b147eb1405d5839e78aeb93131690495fe9da5c91856cb33ad55a7f1e5b2

Name:           python-roman-numerals
Version:        4.1.0
Release:        1%{?dist}
Summary:        Manipulate well-formed Roman numerals

License:        0BSD
URL:            https://github.com/AA-Turner/roman-numerals/
Source0:        https://files.pythonhosted.org/packages/source/r/roman_numerals/roman_numerals-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  pyproject-rpm-macros

%global _description %{expand:
This project provides utilities manipulating well-formed Roman numerals,
in various programming languages.}

%description %_description

%package -n     python3-roman-numerals
Summary:        %{summary}

%py_provides    python3-roman-numerals-py
Obsoletes:      python3-roman-numerals-py < 4~~

%description -n python3-roman-numerals %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n roman_numerals-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L roman_numerals

%check
%pyproject_check_import
%pytest

%files -n python3-roman-numerals -f %{pyproject_files}
%license LICENCE.rst
%doc README.rst
