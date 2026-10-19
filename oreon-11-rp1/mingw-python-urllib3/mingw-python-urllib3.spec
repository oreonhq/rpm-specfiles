%global source0_hash 1b62b6884944a57dbe321509ab94fd4d3b307075e0c2eae991ac71ee15ad38ed
%{?mingw_package_header}
%global pypi_name urllib3
Name:          mingw-python-%{pypi_name}
Summary:        MinGW Windows Python urllib3
Version:       2.8.0
Release:        1%{?dist}
BuildArch:     noarch
License:       MIT
URL:           https://urllib3.readthedocs.io/en/latest/
Source0:        https://files.pythonhosted.org/packages/source/m/mingw-python-urllib3/mingw-python-urllib3-%{version}.tar.gz
Patch0:        urllib3-no-hatch.patch
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
%files -n mingw32-python3-urllib3 -f %{oreon_filedir}/mingw32-python3-urllib3.list
%files -n mingw64-python3-urllib3 -f %{oreon_filedir}/mingw64-python3-urllib3.list

%changelog

%autochangelog
