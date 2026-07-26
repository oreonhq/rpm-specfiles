%global source0_hash be4bf804f083a4ce001b5eb7e3c0862479d10f94c936f6c4e5f250aa5ff5bd2d

Name:           python-roman-numerals-py
Version:        3.1.0
Release:        %autorelease
Summary:        Manipulate well-formed Roman numerals

# Upstream says: Zero-Clause BSD license or the CC0 1.0 Universal license
# CC0-1.0 is not allowed for Fedora, hence declaring only 0BSD
License:        0BSD
URL:            https://github.com/AA-Turner/roman-numerals/
Source:         %{pypi_source roman_numerals_py}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This project provides utilities manipulating well-formed Roman numerals,
in various programming languages.}

%description %_description

%package -n     python3-roman-numerals-py
Summary:        %{summary}

%description -n python3-roman-numerals-py %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n roman_numerals_py-%{version}

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L roman_numerals

%check
%pyproject_check_import
%pytest

%files -n python3-roman-numerals-py -f %{pyproject_files}
%license LICENCE.rst
%doc README.rst

%changelog
%autochangelog
