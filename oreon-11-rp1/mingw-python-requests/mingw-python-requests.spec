%global source0_hash dbba0bac56e100853db0ea71b82b4dfd5fe2bf6d3754a8893c3af500cec7d7cf
%{?mingw_package_header}
%global pypi_name requests
Name:          mingw-python-%{pypi_name}
Summary:        MinGW Windows Python requests library
Version:       2.34.2
Release:        1%{?dist}
BuildArch:     noarch
License:       Apache-2.0
URL:           https://requests.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/m/mingw-python-requests/mingw-python-requests-%{version}.tar.gz
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
Requires:      mingw32-python3-certifi
%description -n mingw32-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name}.

%package -n mingw64-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name}
Requires:      mingw64-python3-certifi
%description -n mingw64-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

# Strip env shebang in nonexecutable file
sed -i '/#!\/usr\/.*python/d' src/requests/certs.py

%build

%mingw32_py3_build_wheel
%mingw64_py3_build_wheel
%install
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-python3-requests -f %{oreon_filedir}/mingw32-python3-requests.list
%files -n mingw64-python3-requests -f %{oreon_filedir}/mingw64-python3-requests.list

%changelog

%autochangelog
