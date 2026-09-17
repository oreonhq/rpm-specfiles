%global source0_hash 4f38c8ed86f017b1f51a1fe8d46bcff041766f4744acd2c1bc39896dff605be2

# Force out of source build
%undefine __cmake_in_source_build

# Use ccache
%bcond ccache 0

# Use clang
%bcond clang 0

%if %{with clang}
# Force clang toolchain
%global toolchain clang
# Disable LTO with clang
%global _lto_cflags %{nil}
%endif

# Debug build with extra compile time checks
%bcond debug 0

# Run tests by default on non-s390x
%ifnarch s390x
%bcond run_tests 1
%endif

# Track various library soversions
%global miral_sover 7
%global mircommon_sover 11
%global mircore_sover 2
%global miroil_sover 8
%global mirplatform_sover 34
%global mirserver_sover 66
%global mirwayland_sover 5
%global mirplatformgraphics_sover 23
%global mirplatforminput_sover 10

Name:           mir
Version:        2.25.1
Release:        5%{?dist}
Summary:        Next generation Wayland display server toolkit

# mircommon is LGPL-2.1-only/LGPL-3.0-only, everything else is GPL-2.0-only/GPL-3.0-only
License:        (GPL-2.0-only or GPL-3.0-only) and (LGPL-2.1-only or LGPL-3.0-only)
URL:            https://canonical.com/mir
Source0:        https://github.com/canonical/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
# Add missing headers for GCC 16 build
Patch:          https://github.com/canonical/mir/pull/4609.patch

%if %{with ccache}
BuildRequires:  ccache
%endif
%if %{with clang}
BuildRequires:  clang
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  git-core
BuildRequires:  cmake, ninja-build, doxygen, graphviz, lcov, gcovr
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  boost-devel
BuildRequires:  python3
BuildRequires:  glm-devel
BuildRequires:  glog-devel, lttng-ust-devel, systemtap-sdt-devel
BuildRequires:  gflags-devel
BuildRequires:  python3-pillow

# Everything detected via pkgconfig
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm) >= 9.0.0
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmock) >= 1.8.0
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gtest) >= 1.8.0
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libxml++-2.6)
BuildRequires:  pkgconfig(nettle)
BuildRequires:  pkgconfig(umockdev-1.0) >= 0.6
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(yaml-cpp)
BuildRequires:  pkgconfig(wlcs)

# pkgconfig(egl) is now from glvnd, so we need to manually pull this in for the Mesa specific bits...
BuildRequires:  mesa-libEGL-devel

# For some reason, this doesn't get pulled in automatically into the buildroot
BuildRequires:  libatomic

# For detecting the font for CMake
BuildRequires:  gnu-free-sans-fonts

# For validating the desktop file for mir-demos
BuildRequires:  %{_bindir}/desktop-file-validate

# For the tests
BuildRequires:  dbus-daemon
BuildRequires:  python3-dbusmock
BuildRequires:  xorg-x11-server-Xwayland

# Add architectures as verified to work
%ifarch %{ix86} %{x86_64} %{arm32} %{arm64} riscv64
BuildRequires:  valgrind
%endif

%description
Mir is a Wayland display server toolkit for Linux systems,
with a focus on efficiency, robust operation,
and a well-defined driver model.

%package devel
Summary:       Development files for Mir
Requires:      %{name}-common-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:      %{name}-server-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:      %{name}-lomiri-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:      %{name}-test-libs-static%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
# Documentation can no longer be built properly
Obsoletes:     %{name}-doc < 2.15.0

%description devel
This package provides the development files to create compositors
built on Mir.

%package internal-devel
Summary:       Development files for Mir exposing private internals
Requires:      %{name}-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description internal-devel
This package provides extra development files to create compositors
built on Mir that need access to private internal interfaces.

%package common-libs
Summary:       Common libraries for Mir
License:       LGPL-2.1-only or LGPL-3.0-only
# mirclient is gone...
Obsoletes:     %{name}-client-libs < 2.6.0
# debug extension for mirclient is gone...
Obsoletes:     %{name}-client-libs-debugext < 1.6.0
# mir utils are gone...
Obsoletes:     %{name}-utils < 2.0.0
# Ensure older mirclient doesn't mix in
Conflicts:     %{name}-client-libs < 2.6.0

%description common-libs
This package provides the libraries common to be used
by Mir clients or Mir servers.

%package lomiri-libs
Summary:       Lomiri compatibility libraries for Mir
License:       GPL-2.0-only or GPL-3.0-only
Requires:      %{name}-common-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:      %{name}-server-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description lomiri-libs
This package provides the libraries for Lomiri to use Mir
as a Wayland compositor.

%package server-libs
Summary:       Server libraries for Mir
License:       GPL-2.0-only or GPL-3.0-only
Requires:      %{name}-common-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description server-libs
This package provides the libraries for applications
that use the Mir server.

%package test-tools
Summary:       Testing tools for Mir
License:       GPL-2.0-only or GPL-3.0-only
Requires:      %{name}-server-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Recommends:    %{name}-demos
Recommends:    glmark2
Recommends:    xorg-x11-server-Xwayland
Requires:      wlcs
# mir-perf-framework is no more...
Obsoletes:     python3-mir-perf-framework < 2.6.0
# Ensure mir-perf-framework is not installed
Conflicts:     python3-mir-perf-framework < 2.6.0

%description test-tools
This package provides tools for testing Mir.

%package demos
Summary:       Demonstration applications using Mir
License:       GPL-2.0-only or GPL-3.0-only
Requires:      %{name}-server-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:      inotify-tools
Requires:      hicolor-icon-theme
Requires:      xorg-x11-server-Xwayland
Requires:      xkeyboard-config
# For some of the demos
Requires:      gnu-free-sans-fonts

%description demos
This package provides applications for demonstrating
the capabilities of the Mir display server.

%package test-libs-static
Summary:       Testing framework library for Mir
License:       GPL-2.0-only or GPL-3.0-only
Requires:      %{name}-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description test-libs-static
This package provides the static library for building
Mir unit and integration tests.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git_am

%conf
%cmake	-GNinja \
	%{?with_ccache:-DCMAKE_C_COMPILER_LAUNCHER=ccache -DCMAKE_CXX_COMPILER_LAUNCHER=ccache} \
	%{?with_debug:-DCMAKE_BUILD_TYPE=Debug} \
	%{!?with_debug:-DMIR_FATAL_COMPILE_WARNINGS=OFF} \
	-DMIR_USE_PRECOMPILED_HEADERS=OFF \
	-DCMAKE_INSTALL_LIBEXECDIR="usr/libexec/mir" \
	-DMIR_PLATFORM="atomic-kms;gbm-kms;wayland;x11"

%build
%cmake_build

%install
%cmake_install

%check
%if %{with run_tests}
export XDG_RUNTIME_DIR=$(mktemp -d)
%ctest
rm -rf $XDG_RUNTIME_DIR
%endif
desktop-file-validate %{buildroot}%{_datadir}/applications/miral-shell.desktop

%files devel
%license COPYING.*
%{_bindir}/mir_wayland_generator
%{_libdir}/libmir*.so
%{_libdir}/pkgconfig/mir*.pc
%exclude %{_libdir}/pkgconfig/mir*internal.pc
%{_includedir}/mir*/
%exclude %{_includedir}/mir*internal/

%files internal-devel
%license COPYING.*
%{_libdir}/pkgconfig/mir*internal.pc
%{_includedir}/mir*internal/

%files common-libs
%license COPYING.LGPL*
%doc README.md
%{_libdir}/libmircore.so.%{mircore_sover}
%{_libdir}/libmircommon.so.%{mircommon_sover}
%{_libdir}/libmirplatform.so.%{mirplatform_sover}
%dir %{_libdir}/%{name}

%files lomiri-libs
%license COPYING.GPL*
%doc README.md
%{_libdir}/libmiroil.so.%{miroil_sover}

%files server-libs
%license COPYING.GPL*
%doc README.md
%{_libdir}/libmiral.so.%{miral_sover}
%{_libdir}/libmirserver.so.%{mirserver_sover}
%{_libdir}/libmirwayland.so.%{mirwayland_sover}
%dir %{_libdir}/%{name}/server-platform
%{_libdir}/%{name}/server-platform/graphics-atomic-kms.so.%{mirplatformgraphics_sover}
%{_libdir}/%{name}/server-platform/graphics-gbm-kms.so.%{mirplatformgraphics_sover}
%{_libdir}/%{name}/server-platform/graphics-wayland.so.%{mirplatformgraphics_sover}
%{_libdir}/%{name}/server-platform/input-evdev.so.%{mirplatforminput_sover}
%{_libdir}/%{name}/server-platform/renderer-egl-generic.so.%{mirplatformgraphics_sover}
%{_libdir}/%{name}/server-platform/server-virtual.so.%{mirplatformgraphics_sover}
%{_libdir}/%{name}/server-platform/server-x11.so.%{mirplatformgraphics_sover}

%files test-tools
%license COPYING.GPL*
%{_bindir}/mir-*test*
%{_bindir}/mir_*test*
%dir %{_libdir}/%{name}/tools
%{_libdir}/%{name}/tools/libmirserverlttng.so
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/miral_wlcs_integration.so
%dir %{_libdir}/%{name}/server-platform
%{_libdir}/%{name}/server-platform/graphics-dummy.so.%{mirplatformgraphics_sover}
%{_libdir}/%{name}/server-platform/input-stub.so.%{mirplatforminput_sover}
%{_datadir}/%{name}/expected_wlcs_failures.list

%files test-libs-static
%license COPYING.GPL*
%{_libdir}/libmir-test-assist.a
%{_libdir}/libmir-test-assist-internal.a

%files demos
%license COPYING.GPL*
%doc README.md
%{_bindir}/mir_demo_*
%{_bindir}/mir-x11-kiosk*
%{_bindir}/miral-*
%{_datadir}/applications/miral-shell.desktop
%{_datadir}/icons/hicolor/scalable/apps/spiral-logo.svg

%changelog
%autochangelog
