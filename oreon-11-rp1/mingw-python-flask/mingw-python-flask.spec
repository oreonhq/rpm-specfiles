%global source0_hash 0ef0e52b8a9cd932855379197dd8f94047b359ca0a78695144304cb45f87c9eb
%{?mingw_package_header}
%global mod_name flask
%global pypi_name flask
Name:          mingw-python-%{mod_name}
Summary:        MinGW Windows Python flask library
Version:       3.1.3
Release:        1%{?dist}
BuildArch:     noarch
License:       BSD-3-Clause
URL:           https://palletsprojects.com/p/itsdangerous/
Source0:        https://files.pythonhosted.org/packages/source/m/mingw-python-flask/mingw-python-flask-%{version}.tar.gz
# oreon:deps
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-python3-build
BuildRequires:  mingw32-python3-flit-core
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-python3-build
BuildRequires:  mingw64-python3-flit-core
# /oreon:deps
%description
MinGW Windows Python %{pypi_name}.

%package -n mingw32-python3-%{mod_name}
Summary:       MinGW Windows Python3 %{pypi_name}
%description -n mingw32-python3-%{mod_name}
MinGW Windows Python3 %{pypi_name}.

%package -n mingw64-python3-%{mod_name}
Summary:       MinGW Windows Python3 %{pypi_name}
%description -n mingw64-python3-%{mod_name}
MinGW Windows Python3 %{pypi_name}.

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
%files -n mingw32-python3-flask -f %{oreon_filedir}/mingw32-python3-flask.list
%files -n mingw64-python3-flask -f %{oreon_filedir}/mingw64-python3-flask.list

%changelog

%autochangelog
