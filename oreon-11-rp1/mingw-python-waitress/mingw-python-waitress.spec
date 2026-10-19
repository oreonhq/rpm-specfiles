%global source0_hash 6136f3ee4128b704abb654d0c767b27d6412896d0dee16973e86fd703cec5ec9
%{?mingw_package_header}
%global mod_name waitress
%global pypi_name waitress
Name:          mingw-python-%{mod_name}
Summary:        MinGW Windows Python waitress library
Version:       3.0.2
Release:        1%{?dist}
BuildArch:     noarch
License:       ZPL-2.1
URL:           https://github.com/Pylons/waitress
Source0:        waitress-%{version}-nodocs.tar.xz
Source1:       waitress-tarball-nodocs.sh
# oreon:deps
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-python3-build
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-python3-build
# /oreon:deps
%description
MinGW Windows Python %{pypi_name} library.

%package -n mingw32-python3-%{mod_name}
Summary:       MinGW Windows Python3 %{pypi_name} library
%description -n mingw32-python3-%{mod_name}
MinGW Windows Python3 %{pypi_name} library.

%package -n mingw64-python3-%{mod_name}
Summary:       MinGW Windows Python3 %{pypi_name} library
%description -n mingw64-python3-%{mod_name}
MinGW Windows Python3 %{pypi_name} library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}-nodocs

%build

%mingw32_py3_build_wheel
%mingw64_py3_build_wheel
%install
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-python3-waitress -f %{oreon_filedir}/mingw32-python3-waitress.list
%files -n mingw64-python3-waitress -f %{oreon_filedir}/mingw64-python3-waitress.list

%changelog

%autochangelog
