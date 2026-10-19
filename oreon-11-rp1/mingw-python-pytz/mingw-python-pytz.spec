%global source0_hash 360b9e3dbb49a209c21ad61809c7fb453643e048b38924c765813546746e81c3
%{?mingw_package_header}
%global pypi_name pytz
Name:          mingw-python-%{pypi_name}
Summary:        MinGW Windows Python pytz library
Version:       2026.3.post1
Release:        1%{?dist}
BuildArch:     noarch
License:       MIT
URL:           https://github.com/stub42/pytz
Source0:        https://files.pythonhosted.org/packages/source/m/mingw-python-pytz/mingw-python-pytz-%{version}.tar.gz
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
%files -n mingw32-python3-pytz -f %{oreon_filedir}/mingw32-python3-pytz.list
%files -n mingw64-python3-pytz -f %{oreon_filedir}/mingw64-python3-pytz.list

%changelog

%autochangelog
