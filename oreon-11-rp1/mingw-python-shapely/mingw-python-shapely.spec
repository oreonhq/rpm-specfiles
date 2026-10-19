%global source0_hash 2ed4ecb28320a433db18a5bf029986aa8afcfd740745e78847e330d5d94922a9
%{?mingw_package_header}
%global mod_name shapely
%global pypi_name shapely
Name:          mingw-python-%{mod_name}
Summary:        MinGW Windows Python shapely library
Version:       2.1.2
Release:        1%{?dist}
BuildArch:     noarch
License:       BSD-3-Clause
URL:           https://github.com/Toblerity/Shapely
Source0:        https://files.pythonhosted.org/packages/source/m/mingw-python-shapely/mingw-python-shapely-%{version}.tar.gz
# oreon:deps
BuildRequires:  mingw32-dlfcn
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-geos
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-python3-Cython
BuildRequires:  mingw32-python3-build
BuildRequires:  mingw32-python3-numpy
BuildRequires:  mingw64-dlfcn
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-geos
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-python3-Cython
BuildRequires:  mingw64-python3-build
BuildRequires:  mingw64-python3-numpy
# /oreon:deps
%description
MinGW Windows Python %{pypi_name} library.

%package -n mingw32-python3-%{mod_name}
Summary:       MinGW Windows Python3 %{pypi_name} library
Requires:      mingw32(libgeos_c-1.dll)
%description -n mingw32-python3-%{mod_name}
MinGW Windows Python3 %{pypi_name} library.

%package -n mingw64-python3-%{mod_name}
Summary:       MinGW Windows Python3 %{mod_name} library
Requires:      mingw64(libgeos_c-1.dll)
%description -n mingw64-python3-%{mod_name}
MinGW Windows Python3 %{pypi_name} library.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

# We don’t need the “oldest supported numpy” in the RPM build, and the
# metapackage in question (https://pypi.org/project/oldest-supported-numpy/) is
# not packaged. Just depend on numpy.
sed -r -i \
    -e 's/oldest-supported-(numpy)/\1/' \
    pyproject.toml

%build

export GEOS_INCLUDE_PATH=%{mingw32_includedir}/geos
export GEOS_LIBRARY_PATH=%{mingw32_libdir}
%mingw32_py3_build_wheel
export GEOS_INCLUDE_PATH=%{mingw64_includedir}/geos
export GEOS_LIBRARY_PATH=%{mingw64_libdir}
%mingw64_py3_build_wheel
%install
export NO_GEOS_CONFIG=1
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-python3-shapely -f %{oreon_filedir}/mingw32-python3-shapely.list
%files -n mingw64-python3-shapely -f %{oreon_filedir}/mingw64-python3-shapely.list

%changelog

%autochangelog
