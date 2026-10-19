%global source0_hash d8ab5478f2ecd78af242878415affce761ca6bc54a22a27e026d7c25357c3316
%{?mingw_package_header}
%global pypi_name certifi
Name:          mingw-python-%{pypi_name}
Summary:        MinGW Windows Python certifi library
Version:       2026.7.22
Release:        1%{?dist}
BuildArch:     noarch
License:       MPL-2.0
URL:           https://certifi.io/en/latest/
Source0:        https://files.pythonhosted.org/packages/source/m/mingw-python-certifi/mingw-python-certifi-%{version}.tar.gz
# oreon:deps
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-python3-build
BuildRequires:  mingw64-filesystem
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
%files -n mingw32-python3-certifi -f %{oreon_filedir}/mingw32-python3-certifi.list
%files -n mingw64-python3-certifi -f %{oreon_filedir}/mingw64-python3-certifi.list

%changelog

%autochangelog
