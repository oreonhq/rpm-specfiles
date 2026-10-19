%global source0_hash 01320b279648ab5b13263f8d260bc5958be599e1eaac77c4503598dfcf96c8bb
%global xfceversion 4.20
%bcond x11 %[%{undefined rhel} || 0%{?rhel} < 10]
%global glib2_minver 2.68.0
%global gtk3_minver 3.24.10
%global gdk_pixbuf_minver 2.40.8
%global wl_minver 1.20
%global api_majorver 0
Name:           libxfce4windowing
Version:        4.20.7
Release:        1%{?dist}
Summary:        Windowing concept abstraction library for X11 and Wayland
License:        LGPL-2.1-or-later
URL:            https://docs.xfce.org/xfce/libxfce4windowing/start
Source0:        http://archive.xfce.org/src/xfce/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2
%if %{with x11}
%endif
Requires: gdk-pixbuf2-modules-extra
# oreon:deps
BuildRequires:  bzip2
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  meson
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdk-wayland-3.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(vapigen)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wlr-protocols)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  tar
BuildRequires:  xfce4-dev-tools
# /oreon:deps
%description
Libxfce4windowing is an abstraction library that attempts to present
windowing concepts (screens, toplevel windows, workspaces, etc.) in a
windowing-system-independent manner.

Currently, X11 is fully supported, via libwnck.  Wayland is partially
supported, through various Wayland protocol extensions.  However, the
full range of operations available on X11 is not available on Wayland,
due to missing features in these protocol extensions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git_am

%conf
%meson %{!?with_x11:-Dx11=disabled}

%build

%meson_build
%install
%meson_install
%find_lang %{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libxfce4windowing-devel -f %{oreon_filedir}/libxfce4windowing-devel.list

%changelog

%autochangelog
