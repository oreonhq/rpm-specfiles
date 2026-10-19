%global source0_hash f93bfef2c0e869750e094bb0c29d5b1652704b09272c6406842688cf634e1584
Name:           libvpl-tools
Version:        1.5.0
Release:        1%{?dist}
Summary:        Intel Video Processing Library (Intel VPL) Tools
License:        MIT
URL:            https://intel.github.io/libvpl
ExclusiveArch:  x86_64
Source0:        https://github.com/intel/libvpl-tools/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-use-system-gtest.patch
Patch1:         %{name}-versioned-library.patch
Patch2:         %{name}-gcc13.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  libvpl-devel
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(gtkmm-4.0)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(libva-x11)
BuildRequires:  pkgconfig(pciaccess)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-dri3)
BuildRequires:  pkgconfig(xcb-present)
# /oreon:deps
%description
Intel Video Processing Library (Intel VPL) tools provide access to hardware
accelerated video decode, encode, and frame processing capabilities on Intel
GPUs from the command line.

The tools require the Intel VPL base library and a runtime library installed.
Current runtime implementations:

- Intel VPL GPU Runtime for use on Intel Iris Xe graphics and newer
- Intel Media SDK for use on legacy Intel graphics

%package devel
Summary:	Development files for %{name}
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains library and header files for development

%package libs
Summary:	%{name} runtime library
Requires:	%{name} = %{version}-%{release}
%description libs
Runtime library for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# delete bundled googletest
rm -rf ext/*

%build

%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_SHARED_LIBS=ON \
    -DBUILD_TESTS=ON \
    -DTOOLS_ENABLE_OPENCL=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n libvpl-tools-devel -f %{oreon_filedir}/libvpl-tools-devel.list
%files -n libvpl-tools-libs -f %{oreon_filedir}/libvpl-tools-libs.list

%changelog

%autochangelog
