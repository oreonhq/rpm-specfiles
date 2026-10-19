%global source0_hash 3c4fd64f453e8f40cf862420a70da95a71b6487ace75e8e0cf85d73707db6065
%{?mingw_package_header}
%global pypi_name ephem
Name:          mingw-python-%{pypi_name}
Summary:        MinGW Windows Python ephem
Version:       4.2.1
Release:        1%{?dist}
BuildArch:     noarch
License:       MIT
URL:           http://rhodesmill.org/pyephem/
Source0:        https://files.pythonhosted.org/packages/source/m/mingw-python-ephem/mingw-python-ephem-%{version}.tar.gz
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
MinGW Windows Python %{pypi_name}.

%package -n mingw32-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name}
%description -n mingw32-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name}.

%package -n mingw64-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name}
%description -n mingw64-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name}.

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
%files -n mingw32-python3-ephem -f %{oreon_filedir}/mingw32-python3-ephem.list
%files -n mingw64-python3-ephem -f %{oreon_filedir}/mingw64-python3-ephem.list

%changelog

%autochangelog
