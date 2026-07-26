%global source0_hash 6943166668fa30efc73662b65a6fd468dcc66979b34177fe3ad0af344be30bb7

%global pypi_name biscuits

Name:           python-%{pypi_name}
Version:        0.3.1
Release:        9%{?dist}
Summary:        Fast and tasty cookies handling

License:        MIT
URL:            https://github.com/pyrates/%{pypi_name}
Source0:        https://github.com/pyrates/%{pypi_name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3dist(setuptools)

%description
Low level API for handling cookies.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Low level API for handling cookies.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# makefile is hard coded to python
sed -i 's/python /python3 /g' Makefile

%build
make compile
%py3_build

%install
%py3_install

%check
%pytest

%files -n python3-%{pypi_name}
%doc README.md
%{python3_sitearch}/biscuits.cpython-%{python3_version_nodots}*.so
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
