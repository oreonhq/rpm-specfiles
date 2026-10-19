%global source0_hash c9fb42b6de9daf475cd229377d0c32d6e87c0f21e874a35e0e679eb201723a67
%bcond_without tests
%global pypi_name vdf
Name:       python-%{pypi_name}
Version:    3.4
Release:        1%{?dist}
Summary:        Package for working with Valve's text and binary KeyValue format
BuildArch:  noarch
License:    MIT
URL:        https://github.com/ValvePython/vdf
Source0:        https://github.com/ValvePython/%{pypi_name}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(setuptools)
# /oreon:deps
%description

%package -n python3-%{pypi_name}
Summary:        Package for working with Valve's text and binary KeyValue format
%{?python_provide:%python_provide python3-%{pypi_name}}
%description -n python3-%{pypi_name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with tests}
%check

%{python3} -m pytest -v \
    %dnl # https://github.com/ValvePython/vdf/issues/33
    --ignore=tests/test_binary_vdf.py
%endif
%files -f %{oreon_filedir}/main.list
%files -n python3-vdf -f %{oreon_filedir}/python3-vdf.list

%changelog

%autochangelog
