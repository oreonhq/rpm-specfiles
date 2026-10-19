%global source0_hash 23526015a6f1550e0541a53fe7acea1b5a11e3697cdf3a3bdc076abc38f6045d
%global with_mingw 0
%undefine _auto_set_build_flags
Name:          dtc
Version:       1.8.1
Release:        1%{?dist}
Summary:        Device Tree Compiler
License:       GPL-2.0-or-later
URL:           https://devicetree.org/
Source0:        https://www.kernel.org/pub/software/utils/%{name}/%{name}-%{version}.tar.xz
Patch0:        dtc-swig45.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-dtc = %{version}-%{release}
# /oreon:deps
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

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Dtools=true -Dpython=disabled
%meson_build
%pyproject_wheel
%mingw_meson -Dtools=false -Dtests=false
%mingw_ninja
%install
%meson_install
%pyproject_install
%mingw_ninja_install
%mingw_debug_install_post
%oreon_autofiles libfdt usr/*/lib*.so.*
%oreon_autofiles libfdt-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libfdt-static usr/*/lib*.so.*
%oreon_autofiles python3-libfdt usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-libfdt usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-libfdt-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libfdt usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libfdt-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
%pyproject_check_import
%ldconfig_scriptlets -n libfdt
%files
%files -n libfdt -f %{oreon_filedir}/libfdt.list
%files -n libfdt-devel -f %{oreon_filedir}/libfdt-devel.list
%files -n libfdt-static -f %{oreon_filedir}/libfdt-static.list
%files -n python3-libfdt -f %{oreon_filedir}/python3-libfdt.list
%files -n mingw32-libfdt -f %{oreon_filedir}/mingw32-libfdt.list
%files -n mingw32-libfdt-static -f %{oreon_filedir}/mingw32-libfdt-static.list
%files -n mingw64-libfdt -f %{oreon_filedir}/mingw64-libfdt.list
%files -n mingw64-libfdt-static -f %{oreon_filedir}/mingw64-libfdt-static.list

%changelog

%autochangelog
