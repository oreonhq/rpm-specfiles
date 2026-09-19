%global source0_hash e0050c0b7da1eea53ffaf149c0cfbb5c6e2e2b69c4bef22c81fa6eb73e5f6173

%{?mingw_package_header}

%global pypi_name itsdangerous

Name:          mingw-python-%{pypi_name}
Summary:       MinGW Windows Python %{pypi_name} library
Version:       2.2.0
Release:       4%{?dist}
BuildArch:     noarch

License:       BSD-3-Clause
URL:           http://pythonhosted.org/itsdangerous/
Source0:       %{pypi_source}

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-build
BuildRequires: mingw32-python3-flit-core

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-build
BuildRequires: mingw64-python3-flit-core

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

%files -n mingw32-python3-%{pypi_name}
%license LICENSE.txt
%{mingw32_python3_sitearch}/%{pypi_name}/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}.dist-info/

%files -n mingw64-python3-%{pypi_name}
%license LICENSE.txt
%{mingw64_python3_sitearch}/%{pypi_name}/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}.dist-info/

%changelog
%autochangelog
