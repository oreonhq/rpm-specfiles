%global source0_hash db467f9ac4bac8f1c4e82667902841fc0957af835c29603d6659a57440b6f8cb

#global prerel pre1
%global xfceversion 4.20

# Disable X11 for RHEL 10+
%bcond x11 %[%{undefined rhel} || 0%{?rhel} < 10]

%global glib2_minver 2.68.0
%global gtk3_minver 3.24.10
%global gdk_pixbuf_minver 2.40.8
%global wl_minver 1.20

%global api_majorver 0

Name:           libxfce4windowing
Version:        4.20.4
Release:        3%{?dist}
Summary:        Windowing concept abstraction library for X11 and Wayland

License:        LGPL-2.1-or-later
URL:            https://docs.xfce.org/xfce/libxfce4windowing/start
#VCS:            git:https://gitlab.xfce.org/xfce/{name}.git
Source0:        http://archive.xfce.org/src/xfce/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2

BuildRequires:  bzip2
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  meson >= 0.56
BuildRequires:  tar
BuildRequires:  xfce4-dev-tools >= 4.19.4
# Generic deps
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_minver}
BuildRequires:  pkgconfig(gobject-2.0) >= %{glib2_minver}
BuildRequires:  pkgconfig(gio-unix-2.0) >= %{glib2_minver}
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= %{gdk_pixbuf_minver}
BuildRequires:  pkgconfig(gdk-3.0) >= %{gtk3_minver}
BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk3_minver}
BuildRequires:  pkgconfig(gtk-doc) >= 1.30
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.66.0
BuildRequires:  pkgconfig(vapigen)
# Wayland deps
BuildRequires:  pkgconfig(gdk-wayland-3.0) >= %{gtk3_minver}
BuildRequires:  pkgconfig(wayland-scanner) >= %{wl_minver}
BuildRequires:  pkgconfig(wayland-client) >= %{wl_minver}
BuildRequires:  pkgconfig(wayland-protocols) >= 1.25
BuildRequires:  pkgconfig(wlr-protocols)
%if %{with x11}
# X11 deps
BuildRequires:  pkgconfig(libdisplay-info) >= 0.1.1
BuildRequires:  pkgconfig(x11) >= 1.6.7
BuildRequires:  pkgconfig(gdk-x11-3.0) >= %{gtk3_minver}
BuildRequires:  pkgconfig(libwnck-3.0) >= 3.14
BuildRequires:  pkgconfig(xrandr) >= 1.5.0
%endif

# Require gdk-pixbuf2-modules-extra for loaders needed for icons
# https://bugzilla.redhat.com/show_bug.cgi?id=2359089
Requires: gdk-pixbuf2-modules-extra

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

%files -f %{name}.lang
%license COPYING
%doc NEWS
%{_libdir}/%{name}*.so.%{api_majorver}{,.*}
%{_libdir}/girepository-1.0/Libxfce4windowing*-%{api_majorver}.0.typelib

%files devel
# Co-own the directory for now
%dir %{_includedir}/xfce4
%{_includedir}/xfce4/%{name}*/
%{_libdir}/%{name}*.so
%{_libdir}/pkgconfig/%{name}*.pc
%{_datadir}/gir-1.0/Libxfce4windowing*-%{api_majorver}.0.gir
%{_datadir}/vala/vapi/libxfce4windowing*

%changelog
%autochangelog
