%global source0_hash f6c4b7865f423b551ea1610b5b0a80b19d7ba221b705e4b61020d8377adfcbb3

%global srcname flake8-builtins

Name:           python-%{srcname}
Version:        3.1.0
Release:        2%{?dist}
Summary:        Check for python builtins being used as variables or parameters

License:        GPL-2.0-only
URL:            https://github.com/gforcada/flake8-builtins
Source0:        https://github.com/gforcada/flake8-builtins/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
Python allows to override builtin names, but although could be useful in some
really specific use cases, the general approach is to not do that as code then
can suddenly break without a clear trace.}

%description %_description

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel

%description -n python%{python3_pkgversion}-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l flake8_builtins

%check
%pytest run_tests.py

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
