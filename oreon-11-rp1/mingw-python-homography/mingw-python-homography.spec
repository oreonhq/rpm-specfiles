%global source0_hash 7c63a24064b341498a20b812a9be2f548be6d574b4e38f85f678ba98b1f2caff
%{?mingw_package_header}
%global pypi_name homography
Name:          mingw-python-%{pypi_name}
Summary:        MinGW Windows Python homography library
Version:       0.1.7
Release:        1%{?dist}
BuildArch:     noarch
License:       GPL-3.0-only
URL:           https://github.com/satellogic/%{pypi_name}
Source0:        https://files.pythonhosted.org/packages/source/m/mingw-python-homography/mingw-python-homography-%{version}.tar.gz
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

%package -n mingw32-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name} library
%description -n mingw32-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name} library.

%package -n mingw64-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name} library
%description -n mingw64-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name} library.

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
%files -n mingw32-python3-homography -f %{oreon_filedir}/mingw32-python3-homography.list
%files -n mingw64-python3-homography -f %{oreon_filedir}/mingw64-python3-homography.list

%changelog

%autochangelog
