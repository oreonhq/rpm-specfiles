%global source0_hash cd79f3367bd74b317dda655dc8fcfa304d9eb6e4fb06b7168c5cf27f96e0cd62

%{?mingw_package_header}

%global pypi_name lxml

Name:          mingw-python-%{pypi_name}
Summary:       MinGW Windows Python %{pypi_name} library
Version:       6.0.2
Release:       2%{?dist}
BuildArch:     noarch

# The lxml project is licensed under BSD-3-Clause
# Some code is derived from ElementTree and cElementTree
# thus using the MIT-CMU elementtree license
# .xsl schematron files are under the MIT license
License:       BSD-3-Clause AND MIT-CMU AND MIT
URL:           https://lxml.de/
Source0:       %{pypi_source}
# Don't attempt to link against librt
Patch0:        lxml-rt.patch

BuildRequires: libxslt-devel

BuildRequires: mingw32-dlfcn
BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc
BuildRequires: mingw32-libxml2
BuildRequires: mingw32-libxslt
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-build
BuildRequires: mingw32-python3-Cython

BuildRequires: mingw64-dlfcn
BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc
BuildRequires: mingw64-libxml2
BuildRequires: mingw64-libxslt
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-build
BuildRequires: mingw64-python3-Cython

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

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%build
# FIXME: avoid incompatible-pointer-types errors
export MINGW32_CFLAGS="%{mingw32_cflags} -fpermissive"
export MINGW64_CFLAGS="%{mingw64_cflags} -fpermissive"
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
