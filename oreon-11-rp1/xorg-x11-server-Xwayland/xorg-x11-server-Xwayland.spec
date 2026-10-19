%global source0_hash 173aea3d6f79609164c04528e1c8e4c9b60fcd59391c3c9dad4667297d727fb6
%global commit 9a55c402aa803fb10e39ab4fd18a709d0cd06fd4
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global pkgname %{?gitdate:xserver}%{!?gitdate:xwayland}
%global default_font_path "catalogue:/etc/X11/fontpath.d,built-ins"
Summary:        Xwayland
Name:      xorg-x11-server-Xwayland
Version:   24.1.13
Release:        1%{?dist}
URL:       http://www.x.org
%if 0%{?gitdate}
Source0:        https://www.x.org/pub/individual/xserver/xwayland-%{version}.tar.xz
%else
%endif
License:   MIT
Requires: xkeyboard-config
Requires: xkbcomp
Requires: libEGL
Requires: libepoxy >= 1.5.5
%ifarch aarch64 %{arm} hppa ia64 mips ppc ppc64 %{ix86} x86_64
%endif
# oreon:deps
BuildRequires:  audit-libs-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  libselinux-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(fontenc)
BuildRequires:  pkgconfig(libdecor-0)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libei-1.0)
BuildRequires:  pkgconfig(liboeffis-1.0)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(libxcvt)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xdmcp)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xfont2)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xres)
BuildRequires:  pkgconfig(xshmfence)
BuildRequires:  pkgconfig(xtrans)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xv)
BuildRequires:  wayland-devel
BuildRequires:  xorg-x11-proto-devel
# /oreon:deps
%description
Xwayland is an X server for running X clients under Wayland.

%package devel
Summary: Development package
Requires: pkgconfig
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The development package provides the developmental files which are
necessary for developing Wayland compositors using Xwayland.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git_am -n %{pkgname}-%{?gitdate:%{commit}}%{!?gitdate:%{version}}

%build

%meson \
	%{?gitdate:-Dxwayland=true -D{xorg,xnest,xvfb,udev}=false} \
        -Ddefault_font_path=%{default_font_path} \
        -Dbuilder_string="Build ID: %{name} %{version}-%{release}" \
        -Dxkb_output_dir=%{_localstatedir}/lib/xkb \
        -Dserverconfigdir=%{_datadir}/xwayland \
        -Dxcsecurity=true \
        -Dglamor=true \
        -Ddri3=true
%meson_build
%install
%meson_install
rm $RPM_BUILD_ROOT%{_mandir}/man1/Xserver.1*
rm -Rf $RPM_BUILD_ROOT%{_includedir}/xorg
rm -Rf $RPM_BUILD_ROOT%{_datadir}/aclocal
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list
%files -n xorg-x11-server-Xwayland-devel -f %{oreon_filedir}/xorg-x11-server-Xwayland-devel.list

%changelog

%autochangelog
