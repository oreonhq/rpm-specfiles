%global source0_hash 964d31caf728e217c697ff77ea69c2ba0865fa41ec20bb00f0977e62fdcc52e3
%{?mingw_package_header}
%global pypi_name psycopg2
Name:          mingw-python-%{pypi_name}
Summary:        MinGW Windows Python psycopg2 library
Version:       2.9.13
Release:        1%{?dist}
BuildArch:     noarch
License:	LGPL-3.0-or-later WITH openvpn-openssl-exception
URL:           https://www.psycopg.org/
Source0:        https://files.pythonhosted.org/packages/source/m/mingw-python-psycopg2/mingw-python-psycopg2-%{version}.tar.gz
Patch0:        psycopg2_mingw.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  mingw32-dlfcn
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-postgresql
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-python3-build
BuildRequires:  mingw64-dlfcn
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-postgresql
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-python3-build
# /oreon:deps
%description
MinGW Windows Python %{pypi_name} library.

%package -n mingw32-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name} library
%description -n mingw32-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name} library.

%package -n mingw64-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name} library
%description -n mingw64-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name} library.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%build

%mingw32_py3_build_wheel
%mingw64_py3_build_wheel
%install
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-python3-psycopg2 -f %{oreon_filedir}/mingw32-python3-psycopg2.list
%files -n mingw64-python3-psycopg2 -f %{oreon_filedir}/mingw64-python3-psycopg2.list

%changelog

%autochangelog
