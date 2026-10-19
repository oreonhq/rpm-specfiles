%global source0_hash f157db7a33ef5d05dd6c0b4e211435586c02b712eaa9f592d078895193aac449
Name:           igt-gpu-tools
Version:        2.5
Release:        1%{?dist}
Summary:        Test suite and tools for DRM drivers
License:        (MIT AND ISC) AND (GPL-1.0-or-later WITH Linux-syscall-note) AND (GPL-2.0-only OR MIT) AND (GPL-2.0-only WITH Linux-syscall-note OR MIT) AND GPL-2.0-or-later WITH Linux-syscall-note AND HPND-sell-variant AND ICU AND ISC AND (MIT AND LGPL-3.0-or-later) AND X11
URL:            https://gitlab.freedesktop.org/drm/igt-gpu-tools
%if 0%{?gitdate}
Source0:        https://gitlab.freedesktop.org/drm/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
%else
%endif
%global provobs_version 2.99.917-42.20180618
Provides:       xorg-x11-drv-intel-devel = %{provobs_version}
Provides:       intel-gpu-tools = %{provobs_version}
Obsoletes:      xorg-x11-drv-intel-devel < %{provobs_version}
Obsoletes:      intel-gpu-tools < %{provobs_version}
# oreon:deps
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  kernel-headers
BuildRequires:  meson
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libdw)
BuildRequires:  pkgconfig(libkmod)
BuildRequires:  pkgconfig(liboping)
BuildRequires:  pkgconfig(libproc2)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  pkgconfig(pciaccess)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(valgrind)
BuildRequires:  pkgconfig(xmlrpc)
BuildRequires:  pkgconfig(xmlrpc_client)
BuildRequires:  pkgconfig(xmlrpc_util)
BuildRequires:  pkgconfig(xv)
BuildRequires:  python3-docutils
# /oreon:deps
%description
igt-gpu-tools (formerly known as intel-gpu-tools) is the standard for writing
test cases for DRM drivers. It also includes a handful of useful tools for
various drivers, such as Intel's GPU tools for i915.

%package docs
Summary:        Documentation for igt-gpu-tools
%description docs
gtk-doc generated documentation package for igt-gpu-tools.

%package devel
Summary:        Development files for igt-gpu-tools
%description devel
Development files for compiling against certain tools provided by
igt-gpu-tools, such as i915-perf.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir igt-gpu-tools-v%{version}
%oreon_prep
%build

%global with_libunwind enabled
CFLAGS="%{build_cflags} -Wno-array-bounds"
%meson \
        -Db_ndebug=false \
        -Dc_link_args="-z lazy" \
        -Doverlay=disabled \
        -Dlibunwind=%{with_libunwind}
%meson_build
ninja -C %{_vpath_builddir} igt-gpu-tools-doc
%install
%meson_install
rm %{buildroot}/%{_libdir}/pkgconfig/intel-gen4asm.pc
rm %{buildroot}/%{_libdir}/libigt.so
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ifarch %{ix86} x86_64
%meson_test --timeout-multiplier 16
%endif
%files -f %{oreon_filedir}/main.list
%files -n igt-gpu-tools-docs -f %{oreon_filedir}/igt-gpu-tools-docs.list
%files -n igt-gpu-tools-devel -f %{oreon_filedir}/igt-gpu-tools-devel.list

%changelog

%autochangelog
