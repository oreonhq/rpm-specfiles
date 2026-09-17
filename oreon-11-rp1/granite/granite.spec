%global source0_hash 067d31445da9808a802fca523630c3e4b84d2d7c78ae547ced017cb7f3b9c6b5

%global common_description %{expand:
Granite is a companion library for GTK+ and GLib. Among other things, it
provides complex widgets and convenience functions designed for use in
apps built for elementary.}

Name:           granite
Summary:        elementary companion library for GTK+ and GLib
Version:        6.2.0
Release:        %autorelease
License:        LGPL-3.0-or-later

URL:            https://github.com/elementary/granite
Source0:        %{url}/archive/%{version}/granite-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.48.2
BuildRequires:  vala >= 0.48

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0) >= 2.50
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.50
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(gobject-2.0) >= 2.50
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(gobject-introspection-1.0)

# granite relies on org.gnome.desktop.interface for the clock-format setting
Requires:       gsettings-desktop-schemas

# granite provides and needs some generic icons
Requires:       hicolor-icon-theme

%description %{common_description}

%package        devel
Summary:        Granite Toolkit development headers
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel %{common_description}

This package contains the development headers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n granite-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang granite

%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/io.elementary.granite.demo.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/granite.appdata.xml

%files -f granite.lang
%doc README.md
%license COPYING

%{_libdir}/libgranite.so.6
%{_libdir}/libgranite.so.6.*

%{_libdir}/girepository-1.0/Granite-1.0.typelib

%{_datadir}/icons/hicolor/*/actions/appointment.svg
%{_datadir}/icons/hicolor/*/actions/open-menu.svg
%{_datadir}/icons/hicolor/scalable/actions/open-menu-symbolic.svg

%{_datadir}/metainfo/granite.appdata.xml

%files devel
%{_bindir}/granite-demo

%{_libdir}/libgranite.so
%{_libdir}/pkgconfig/granite.pc

%{_includedir}/granite/

%{_datadir}/applications/io.elementary.granite.demo.desktop
%{_datadir}/gir-1.0/Granite-1.0.gir
%{_datadir}/vala/vapi/granite.deps
%{_datadir}/vala/vapi/granite.vapi

%changelog
%autochangelog
