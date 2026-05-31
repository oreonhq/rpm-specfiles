%global source0_hash 92d8ca769805ae1f176204230438fe52808f4e1c7944053c9eec0e649b237539

%global with_mingw 0

%if 0%{?fedora}
%global with_mingw 1
%endif

%undefine _auto_set_build_flags

Name:          dtc
Version:       1.7.2
Release:       9%{?dist}
Summary:       Device Tree Compiler
License:       GPL-2.0-or-later
URL:           https://devicetree.org/

Source0:        https://www.kernel.org/pub/software/utils/%{name}/%{name}-%{version}.tar.xz
Patch0001:     0001-build-fix-Dtools-false-build.patch
Patch0002:     dtc-Fix-discarded-const-qualifiers.patch

BuildRequires: gcc make
BuildRequires: flex bison swig
BuildRequires: python3-devel
BuildRequires: python3-pip
BuildRequires: python3-setuptools
BuildRequires: python3-setuptools_scm

%if %{with_mingw}
BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++

BuildRequires: meson

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
%{?python_provide:%python_provide python2-libfdt}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n python3-libfdt
This package provides python2 bindings for libfdt

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
# to prevent setuptools from installing an .egg, we need to pass --root to setup.py install
# since $(PREFIX) already contains %%{buildroot}, we set root to /
# .eggs are going to be deprecated, see https://github.com/pypa/pip/issues/11501
sed -i 's@--prefix=$(PREFIX)@--prefix=$(PREFIX) --root=/@' pylibfdt/Makefile.pylibfdt


%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%{make_build} EXTRA_CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}"

%if %{with_mingw}
%mingw_meson -Dtools=false -Dtests=false
%mingw_ninja
%endif

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%{make_install} V=1 DESTDIR=%{buildroot} PREFIX=%{buildroot}/%{_prefix} \
                LIBDIR=%{_libdir} BINDIR=%{_bindir} INCLUDEDIR=%{_includedir}

%if %{with_mingw}
%mingw_ninja_install
%mingw_debug_install_post
%endif

%ldconfig_scriptlets -n libfdt

%files
%license GPL
%doc Documentation/manual.txt
%{_bindir}/*

%files -n libfdt
%license GPL
%{_libdir}/libfdt.so.1*

%files -n libfdt-static
%{_libdir}/libfdt.a

%files -n libfdt-devel
%{_libdir}/libfdt.so
%{_includedir}/*fdt*

%files -n python3-libfdt
%{python3_sitearch}/libfdt-%{version}-py%{python3_version}.egg-info/
%{python3_sitearch}/_libfdt%{python3_ext_suffix}
%pycached %{python3_sitearch}/libfdt.py

%if %{with_mingw}
%files -n mingw32-libfdt
%license GPL
%{mingw32_bindir}/libfdt-1.dll
%{mingw32_includedir}/*fdt*.h
%{mingw32_libdir}/libfdt.dll.a
%{mingw32_libdir}/pkgconfig/libfdt.pc

%files -n mingw32-libfdt-static
%{mingw32_libdir}/libfdt.a

%files -n mingw64-libfdt
%license GPL
%{mingw64_bindir}/libfdt-1.dll
%{mingw64_includedir}/*fdt*.h
%{mingw64_libdir}/libfdt.dll.a
%{mingw64_libdir}/pkgconfig/libfdt.pc

%files -n mingw64-libfdt-static
%{mingw64_libdir}/libfdt.a
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.7.2-9
- Prepare for Oreon 11 (RP1)
