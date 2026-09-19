%global source0_hash 0aac3458f78b115e661a51610b631c46f27c8b6a4446e4dafb9a13b5ddb5d5e7

%global pypi_name jsonpath-rw

Name:           python-%{pypi_name}
Version:        1.4.0
Release:        %autorelease
Summary:        Extended implementation of JSONPath for Python

License:        Apache-2.0
URL:            https://github.com/kennknowles/python-jsonpath-rw
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
This library provides a robust and significantly extended implementation of
JSONPath for Python, with a clear AST for meta-programming.

This library differs from other JSONPath implementations in that it is a full
language implementation, meaning the JSONPath expressions are first class
objects, easy to analyze, transform, parse, print, and extend.

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-ply
BuildRequires:  python3-decorator
BuildRequires:  python3-six
BuildRequires:  python-pytest

%description -n python3-%{pypi_name}
This library provides a robust and significantly extended implementation of
JSONPath for Python, with a clear AST for meta-programming.

This library differs from other JSONPath implementations in that it is a full
language implementation, meaning the JSONPath expressions are first class
objects, easy to analyze, transform, parse, print, and extend.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l jsonpath_rw

%check
%pyproject_check_import

%{pytest} -v

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%{_bindir}/jsonpath.py

%changelog
%autochangelog
