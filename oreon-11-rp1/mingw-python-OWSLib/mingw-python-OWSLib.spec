%global source0_hash 0182f377bb30d25b78284bbaf82a12dece97902ed844cee88791ff38665b9b00

%{?mingw_package_header}

%global mod_name owslib

Name:          mingw-python-OWSLib
Summary:       MinGW Windows Python OWSLib library
Version:       0.35.0
Release:       2%{?dist}
BuildArch:     noarch

License:       BSD-3-Clause
URL:           https://geopython.github.io/OWSLib
Source0:       %{pypi_source owslib}

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-build

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-build

%description
MinGW Windows Python OWSLib library.

%package -n mingw32-python3-%{mod_name}
Summary:       MinGW Windows Python3 %{pypi_name} library

%description -n mingw32-python3-%{mod_name}
MinGW Windows Python3 OWSLib library.

%package -n mingw64-python3-%{mod_name}
Summary:       MinGW Windows Python3 OWSLib library

%description -n mingw64-python3-%{mod_name}
MinGW Windows Python3 OWSLib library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{mod_name}-%{version}

%build
%mingw32_py3_build_wheel
%mingw64_py3_build_wheel

%install
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel

%files -n mingw32-python3-%{mod_name}
%license LICENSE
%{mingw32_python3_sitearch}/%{mod_name}/
%{mingw32_python3_sitearch}/%{mod_name}-%{version}.dist-info/

%files -n mingw64-python3-%{mod_name}
%license LICENSE
%{mingw64_python3_sitearch}/%{mod_name}/
%{mingw64_python3_sitearch}/%{mod_name}-%{version}.dist-info/

%changelog
%autochangelog
