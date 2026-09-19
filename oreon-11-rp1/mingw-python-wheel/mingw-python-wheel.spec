%global source0_hash e3e79874b07d776c40bd6033f8ddf76a7dad46a7b8aa1b2787a83083519a1803

%{?mingw_package_header}

%global pypi_name wheel

Name:          mingw-python-%{pypi_name}
Summary:       MinGW Windows Python %{pypi_name} library
Version:       0.46.3
Release:       1%{?dist}
BuildArch:     noarch

License:       MIT AND (Apache-2.0 OR BSD-2-Clause)
URL:           https://pypi.python.org/pypi/%{pypi_name}
Source0:       %{pypi_source %{pypi_name} %{version}}

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-setuptools

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-setuptools

# Don't scan */bin/wheel for requires, it would generate a Requires: pythonX.Y
%global __requires_exclude_from ^.*/bin/wheel$

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
%mingw32_py3_build
%mingw64_py3_build
%mingw32_py3_build_host
%mingw64_py3_build_host

%install
%mingw32_py3_install
%mingw64_py3_install
%mingw32_py3_install_host
%mingw64_py3_install_host

%files -n mingw32-python3-%{pypi_name}
%license LICENSE.txt
%{mingw32_bindir}/wheel
%{mingw32_python3_sitearch}/%{pypi_name}/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}-py%{mingw32_python3_version}.egg-info/
%{_prefix}/%{mingw32_target}/bin/wheel
%{mingw32_python3_hostsitearch}/%{pypi_name}/
%{mingw32_python3_hostsitearch}/%{pypi_name}-%{version}-py%{mingw32_python3_version}.egg-info/

%files -n mingw64-python3-%{pypi_name}
%license LICENSE.txt
%{mingw64_bindir}/wheel
%{mingw64_python3_sitearch}/%{pypi_name}/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}-py%{mingw64_python3_version}.egg-info/
%{_prefix}/%{mingw64_target}/bin/wheel
%{mingw64_python3_hostsitearch}/%{pypi_name}/
%{mingw64_python3_hostsitearch}/%{pypi_name}-%{version}-py%{mingw64_python3_version}.egg-info/

%changelog
%autochangelog
