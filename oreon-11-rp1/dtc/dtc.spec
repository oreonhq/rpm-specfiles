%global source0_hash 23526015a6f1550e0541a53fe7acea1b5a11e3697cdf3a3bdc076abc38f6045d

%global with_mingw 0

%if 0%{?fedora}
%global with_mingw 1
%endif

%undefine _auto_set_build_flags

Name:          dtc
Version:       1.8.1
Release:       1%{?dist}
Summary:       Device Tree Compiler
License:       GPL-2.0-or-later
URL:           https://devicetree.org/
Source0:       https://www.kernel.org/pub/software/utils/%{name}/%{name}-%{version}.tar.xz

# Replace removed Python 2 C API macros with Python 3 equivalents
# for compatibility with SWIG 4.5.0
Patch0:        dtc-swig45.patch

BuildRequires: gcc
BuildRequires: meson
BuildRequires: python3-devel
BuildRequires: libyaml-devel
BuildRequires: swig bison flex
BuildRequires: valgrind-devel

%if %{with_mingw}
BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
%endif

%description
Devicetree is a data structure for describing hardware. Rather than hard coding
every detail of a device into an operating system, many aspects of the hardware
can be described in a data structure that is passed to the operating system at
boot time. The devicetree is used by OpenFirmware, OpenPOWER Abstraction Layer
(OPAL), Power Architecture Platform Requirements (PAPR) and in the standalone
Flattened Device Tree (FDT) form.

%package -n libfdt
Summary: Device tree library

%description -n libfdt
libfdt is a library to process Open Firmware style device trees on various
architectures.

%package -n libfdt-devel
Summary: Development headers for device tree library
Requires: libfdt = %{version}-%{release}

%description -n libfdt-devel
This package provides development files for libfdt

%package -n libfdt-static
Summary: Static version of device tree library
Requires: libfdt-devel = %{version}-%{release}

%description -n libfdt-static
This package provides the static library of libfdt

%package -n python3-libfdt
Summary: Python 3 bindings for device tree library
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n python3-libfdt
This package provides python3 bindings for libfdt

%if %{with_mingw}
%package -n mingw32-libfdt
Summary: MinGW Device tree library
BuildArch: noarch

%description -n mingw32-libfdt
libfdt is a library to process Open Firmware style device trees on various
architectures.

%package -n mingw32-libfdt-static
Summary: Static version of MinGW Device tree library
Requires: mingw32-libfdt = %{version}-%{release}
BuildArch: noarch

%description -n mingw32-libfdt-static
This package provides the static library of mingw32-libfdt

%package -n mingw64-libfdt
Summary: MinGW Device tree library
BuildArch: noarch

%description -n mingw64-libfdt
libfdt is a library to process Open Firmware style device trees on various
architectures.

%package -n mingw64-libfdt-static
Summary: Static version of MinGW Device tree library
Requires: mingw64-libfdt = %{version}-%{release}
BuildArch: noarch

%description -n mingw64-libfdt-static
This package provides the static library of mingw64-libfdt

%{?mingw_debug_package}
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires --pyproject-dependencies

%build
%meson -Dtools=true -Dpython=disabled
%meson_build
%pyproject_wheel

%if %{with_mingw}
%mingw_meson -Dtools=false -Dtests=false
%mingw_ninja
%endif


%install
%meson_install
%pyproject_install
%pyproject_save_files libfdt _libfdt

%if %{with_mingw}
%mingw_ninja_install
%mingw_debug_install_post
%endif


%check
%meson_test
%pyproject_check_import


%ldconfig_scriptlets -n libfdt


%files
%license GPL
%doc Documentation/manual.txt
%{_bindir}/convert-dtsv0
%{_bindir}/dtc
%{_bindir}/dtdiff
%{_bindir}/fdt*

%files -n libfdt
%license GPL
%{_libdir}/libfdt.so.1*

%files -n libfdt-static
%{_libdir}/libfdt.a

%files -n libfdt-devel
%{_libdir}/libfdt.so
%{_libdir}/pkgconfig/libfdt.pc
%{_includedir}/*fdt*

%files -n python3-libfdt -f %{pyproject_files}

%if %{with_mingw}
%files -n mingw32-libfdt
%license GPL
%{mingw32_bindir}/libfdt-1.dll
%{mingw32_includedir}/*fdt*.h
%{mingw32_libdir}/libfdt.dll.a
%{mingw32_libdir}/pkgconfig/libfdt.pc

%files -n mingw32-libfdt-static
#%{mingw32_libdir}/libfdt.a

%files -n mingw64-libfdt
%license GPL
%{mingw64_bindir}/libfdt-1.dll
%{mingw64_includedir}/*fdt*.h
%{mingw64_libdir}/libfdt.dll.a
%{mingw64_libdir}/pkgconfig/libfdt.pc

%files -n mingw64-libfdt-static
#%{mingw64_libdir}/libfdt.a
%endif

%changelog
%autochangelog
