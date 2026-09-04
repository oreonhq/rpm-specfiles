%global source0_hash 65f266143752f734b0a7cc83c46f4618af75b8c5911b00ccb61d0ac9b6da0360

%global pypi_name decorator

Name:           python-%{pypi_name}
Version:        5.3.1
Release:        %autorelease
Summary:        Module to simplify usage of decorators

License:        BSD-2-Clause
URL:            https://github.com/micheles/decorator
Source0:        https://files.pythonhosted.org/packages/source/d/decorator/decorator-5.2.1.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%description
The aim of the decorator module is to simplify the usage of decorators for
the average programmer, and to popularize decorators usage giving examples
of useful decorators, such as memoize, tracing, redirecting_stdout, locked,
etc.  The core of this module is a decorator factory called decorator.

%package -n python3-decorator
Summary:        Module to simplify usage of decorators in python3
%{?python_provide:%python_provide python3-decorator}

%description -n python3-decorator
The aim of the decorator module is to simplify the usage of decorators for
the average programmer, and to popularize decorators usage giving examples
of useful decorators, such as memoize, tracing, redirecting_stdout, locked,
etc.  The core of this module is a decorator factory called decorator.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l decorator

%check
%{py3_test_envvars} %{python3} -m unittest tests/test.py

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst CHANGES.md
%license LICENSE.txt

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.2.1-1
- Prepare for Oreon 11 (RP1)
