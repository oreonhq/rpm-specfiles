%global source0_hash fa7fc37acd73ea44ad6caa353b9ac39f8ef01d5befada27ec05ae6232edd7eff

%global pypi_name beautifultable

Name:           python-%{pypi_name}
Version:        1.1.0
Release:        16%{?dist}
Summary:        Print ASCII tables for terminals

License:        MIT
URL:            https://github.com/pri22296/beautifultable
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This package provides the BeautifulTable class for easily printing tabular data
in a visually appealing ASCII format to a terminal.

Features included but not limited to:

- Full customization of the look and feel of the table
- Build the Table as you wish, By adding rows, or by columns or even mixing both
  these approaches
- Full support for colors using ANSI sequences or any library of your choice
- Plenty of predefined styles for multiple use cases and option to create
  custom ones
- Support for Unicode characters

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(wcwidth)
BuildRequires:  python3dist(pytest)
 
%description -n python3-%{pypi_name}
This package provides the BeautifulTable class for easily printing tabular data
in a visually appealing ASCII format to a terminal.

Features included but not limited to:

- Full customization of the look and feel of the table
- Build the Table as you wish, By adding rows, or by columns or even mixing both
  these approaches
- Full support for colors using ANSI sequences or any library of your choice
- Plenty of predefined styles for multiple use cases and option to create
  custom ones
- Support for Unicode characters

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l %{pypi_name}

%check
%{pytest} test.py

%files -n %files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt

%changelog
%autochangelog
