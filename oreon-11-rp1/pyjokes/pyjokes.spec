%global source0_hash a6d06a5428dd8f316a3f8784cac0180067b6530121d9cf3976d5f903db264c86
%global pypi_name pyjokes
%global with_tests 0
%global global_desc One line jokes for programmers (jokes as a service)
Name:           %{pypi_name}
Version:        0.6.0
Release:        1%{?dist}
Summary:        One line jokes for programmers (jokes as a service)
License:        LicenseRef-Callaway-BSD
URL:            http://pyjok.es/
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz
BuildArch:      noarch
%if 0%{?with_tests}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyjokes = %{version}-%{release}
# /oreon:deps
%description
%{global_desc}.

%package     -n python3-%{pypi_name}
Summary: %{global_desc}. This package includes a commandline interface.
%{?python_provide:%python_provide python3-%{pypi_name}}
%description -n python3-%{pypi_name}
%{global_desc}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pypi_name}-%{version}

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/pyjokes* usr/lib64/python3*/site-packages/pyjokes* usr/bin/*

%check

%files
%files -n python3-pyjokes -f %{oreon_filedir}/python3-pyjokes.list

%changelog

%autochangelog
