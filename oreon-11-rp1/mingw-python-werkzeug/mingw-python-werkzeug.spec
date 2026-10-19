%global source0_hash cd3cd98b1b92dc3b7b3995038826c68097dcb16f9baa63abe35f20eafeb9fe5e
%{?mingw_package_header}
%global mod_name werkzeug
%global pypi_name werkzeug
Name:          mingw-python-%{mod_name}
Summary:        MinGW Windows Python werkzeug library
Version:       3.1.8
Release:        1%{?dist}
BuildArch:     noarch
License:       BSD-3-Clause
URL:           https://palletsprojects.com/p/werkzeug/
Source0:        https://files.pythonhosted.org/packages/source/m/mingw-python-werkzeug/mingw-python-werkzeug-%{version}.tar.gz
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

%autosetup -p1 -n %{pypi_name}-%{version}

%build

%mingw32_py3_build_wheel
%mingw64_py3_build_wheel
%install
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-python3-werkzeug -f %{oreon_filedir}/mingw32-python3-werkzeug.list
%files -n mingw64-python3-werkzeug -f %{oreon_filedir}/mingw64-python3-werkzeug.list

%changelog

%autochangelog
