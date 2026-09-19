%global source0_hash 39a0cf1ecc7e282d1d30f36594ebd55c9fae1fda8a2622cee5d100430628f88c

%{?mingw_package_header}

%global pypi_name pyproj

Name:           mingw-python-%{pypi_name}
Summary:        MinGW Python %{pypi_name} library
Version:        3.7.2
Release:        2%{?dist}
BuildArch:      noarch

License:        MIT
Url:            https://github.com/jswhit/%{pypi_name}
Source0:        %{pypi_source %pypi_name}
# Don't pass runtime_library_dirs to ext_options in setup.py
Patch0:         pyproj-runtime-library-dirs.patch

BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-dlfcn
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-proj
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-python3-build
BuildRequires:  mingw32-python3-Cython

BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-dlfcn
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-proj
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-python3-build
BuildRequires:  mingw64-python3-Cython

%description
MinGW Python %{pypi_name} library.

%package -n mingw32-python3-%{pypi_name}
Summary:       MinGW Python 3 %{pypi_name} library

%description -n mingw32-python3-%{pypi_name}
MinGW Python 3 %{pypi_name} library.

%package -n mingw64-python3-%{pypi_name}
Summary:       MinGW Python 3 %{pypi_name} library

%description -n mingw64-python3-%{pypi_name}
MinGW Python 3 %{pypi_name} library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%build
(
export PROJ_DIR=%{mingw32_prefix}
export PROJ_INCDIR=%{mingw32_includedir}
export PROJ_LIBDIR=%{mingw32_libdir}
export PROJ_VERSION=`mingw32-pkg-config --modversion proj`
%mingw32_py3_build_wheel
)
(
export PROJ_DIR=%{mingw64_prefix}
export PROJ_INCDIR=%{mingw64_includedir}
export PROJ_LIBDIR=%{mingw64_libdir}
export PROJ_VERSION=`mingw64-pkg-config --modversion proj`
%mingw64_py3_build_wheel
)

%install
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel

%files -n mingw32-python3-%{pypi_name}
%license LICENSE
%{mingw32_bindir}/pyproj
%{mingw32_python3_sitearch}/%{pypi_name}/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}.dist-info/

%files -n mingw64-python3-%{pypi_name}
%license LICENSE
%{mingw64_bindir}/pyproj
%{mingw64_python3_sitearch}/%{pypi_name}/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}.dist-info/

%changelog
%autochangelog
