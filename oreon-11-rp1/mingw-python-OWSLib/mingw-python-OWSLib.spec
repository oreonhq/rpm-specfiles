%global source0_hash b1ea352ee84f37a1a8ae44122b13cbd3b5b7bf9af0f74d84fe9ed7d9613b9543
%{?mingw_package_header}
%global mod_name owslib
Name:          mingw-python-OWSLib
Summary:        MinGW Windows Python OWSLib library
Version:       0.36.0
Release:        1%{?dist}
BuildArch:     noarch
License:       BSD-3-Clause
URL:           https://geopython.github.io/OWSLib
Source0:        https://files.pythonhosted.org/packages/source/o/owslib/owslib-%{version}.tar.gz
# oreon:deps
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-python3-build
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-python3-build
# /oreon:deps
%description
MinGW Windows Python OWSLib library.

%package -n mingw32-python3-%{mod_name}
Summary:       MinGW Windows Python3 %{pypi_name} library
%description -n mingw32-python3-%{mod_name}
MinGW Windows Python3 OWSLib library.

%package -n mingw64-python3-%{mod_name}
Summary:       MinGW Windows Python3 OWSLib library
%description -n mingw64-python3-%{mod_name}
MinGW Windows Python3 OWSLib library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{mod_name}-%{version}

%build

%mingw32_py3_build_wheel
%mingw64_py3_build_wheel
%install
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-python3-owslib -f %{oreon_filedir}/mingw32-python3-owslib.list
%files -n mingw64-python3-owslib -f %{oreon_filedir}/mingw64-python3-owslib.list

%changelog

%autochangelog
