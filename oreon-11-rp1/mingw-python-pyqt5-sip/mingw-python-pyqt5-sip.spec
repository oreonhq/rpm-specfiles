%global source0_hash 71c37db75a0664325de149f43e2a712ec5fa1f90429a21dafbca005cb6767f94
%{?mingw_package_header}
%global mod_name pyqt5-sip
%global pypi_name pyqt5_sip
Name:           mingw-python-%{mod_name}
Summary:        MinGW Python pyqt5_sip library
Version:        12.19.0
Release:        1%{?dist}
BuildArch:      noarch
License:        GPL-2.0-only OR GPL-3.0-only
Url:            https://www.riverbankcomputing.com/software/sip/
Source0:        https://files.pythonhosted.org/packages/source/m/mingw-python-pyqt5-sip/mingw-python-pyqt5-sip-%{version}.tar.gz
# oreon:deps
BuildRequires:  mingw32-dlfcn
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-python3-build
BuildRequires:  mingw64-dlfcn
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-python3-build
# /oreon:deps
%description
MinGW Python %{pypi_name} library.

%package -n mingw32-python3-%{mod_name}
Summary:       MinGW Python 3 %{mod_name} library
Obsoletes:     mingw32-python3-%{pypi_name} < 12.11.0-2
Provides:      mingw32-python3-%{pypi_name} = %{version}-%{release}
%description -n mingw32-python3-%{mod_name}
MinGW Python 3 %{pypi_name} library.

%package -n mingw64-python3-%{mod_name}
Summary:       MinGW Python 3 %{pypi_name} library
Obsoletes:     mingw64-python3-%{pypi_name} < 12.11.0-2
Provides:      mingw64-python3-%{pypi_name} = %{version}-%{release}
%description -n mingw64-python3-%{mod_name}
MinGW Python 3 %{pypi_name} library.

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
%files -n mingw32-python3-pyqt5-sip -f %{oreon_filedir}/mingw32-python3-pyqt5-sip.list
%files -n mingw64-python3-pyqt5-sip -f %{oreon_filedir}/mingw64-python3-pyqt5-sip.list

%changelog

%autochangelog
