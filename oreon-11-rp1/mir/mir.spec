%global source0_hash 9ef7d7fb1d05938cc30341cb4a3cf5dd6e9f84a8fe8d309481ee382b2bebaae1
%undefine __cmake_in_source_build
%bcond ccache 0
%bcond clang 0
%if %{with clang}
%global toolchain clang
%global _lto_cflags %{nil}
%endif
%bcond debug 0
%ifnarch s390x
%bcond run_tests 1
%endif
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
Version:        2.29.0
Release:        1%{?dist}
Summary:        Next generation Wayland display server toolkit
License:        (GPL-2.0-only or GPL-3.0-only) and (LGPL-2.1-only or LGPL-3.0-only)
URL:            https://canonical.com/mir
Source0:        https://github.com/canonical/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Patch:          https://github.com/canonical/mir/pull/4609.patch
%if %{with ccache}
%endif
%if %{with clang}
%else
%endif
%ifarch %{ix86} %{x86_64} %{arm32} %{arm64} riscv64
%endif
# oreon:deps
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  dbus-daemon
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gcovr
BuildRequires:  gflags-devel
BuildRequires:  git-core
BuildRequires:  glm-devel
BuildRequires:  glog-devel
BuildRequires:  gnu-free-sans-fonts
BuildRequires:  graphviz
BuildRequires:  lcov
BuildRequires:  libatomic
BuildRequires:  lttng-ust-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmock)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libxml++-2.6)
BuildRequires:  pkgconfig(nettle)
BuildRequires:  pkgconfig(umockdev-1.0)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wlcs)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(yaml-cpp)
BuildRequires:  python3
BuildRequires:  python3-dbusmock
BuildRequires:  python3-pillow
BuildRequires:  systemtap-sdt-devel
BuildRequires:  xorg-x11-server-Xwayland
# /oreon:deps
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
Obsoletes:     %{name}-client-libs < 2.6.0
Obsoletes:     %{name}-client-libs-debugext < 1.6.0
Obsoletes:     %{name}-utils < 2.0.0
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
Obsoletes:     python3-mir-perf-framework < 2.6.0
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with run_tests}
export XDG_RUNTIME_DIR=$(mktemp -d)
%ctest
rm -rf $XDG_RUNTIME_DIR
%endif
desktop-file-validate %{buildroot}%{_datadir}/applications/miral-shell.desktop
%files -f %{oreon_filedir}/main.list
%files -n mir-devel -f %{oreon_filedir}/mir-devel.list
%files -n mir-internal-devel -f %{oreon_filedir}/mir-internal-devel.list
%files -n mir-common-libs -f %{oreon_filedir}/mir-common-libs.list
%files -n mir-lomiri-libs -f %{oreon_filedir}/mir-lomiri-libs.list
%files -n mir-server-libs -f %{oreon_filedir}/mir-server-libs.list
%files -n mir-test-tools -f %{oreon_filedir}/mir-test-tools.list
%files -n mir-demos -f %{oreon_filedir}/mir-demos.list
%files -n mir-test-libs-static -f %{oreon_filedir}/mir-test-libs-static.list

%changelog

%autochangelog
