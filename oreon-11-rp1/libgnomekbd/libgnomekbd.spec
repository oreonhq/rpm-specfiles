%global source0_hash none

Name:           libgnomekbd
Version:        3.28.1
Release:        9%{?dist}
Summary:        A keyboard configuration library

License:        LGPL-2.0-or-later
URL:            http://gswitchit.sourceforge.net
Source0:        https://download.gnome.org/sources/libgnomekbd/3.28/libgnomekbd-%{version}.tar.xz

BuildRequires:  gettext-devel
BuildRequires:  gtk3-devel >= 3.0.0
BuildRequires:  cairo-devel
BuildRequires:  libxklavier-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gobject-introspection-devel
BuildRequires:  meson

%description
The libgnomekbd package contains a GNOME library which manages
keyboard configuration and offers various widgets related to
keyboard configuration.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description    devel
The libgnomekbd-devel package contains libraries and header files for
developing applications that use libgnomekbd.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name}


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/gkbd-keyboard-display.desktop


%files -f %{name}.lang
%license COPYING.LIB
%{_libdir}/libgnomekbd.so.8*
%{_libdir}/libgnomekbdui.so.8*
%{_datadir}/libgnomekbd
%{_datadir}/glib-2.0/schemas/org.gnome.libgnomekbd*.gschema.xml
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Gkbd-3.0.typelib
%{_bindir}/gkbd-keyboard-display
%{_datadir}/applications/gkbd-keyboard-display.desktop
%{_datadir}/GConf/gsettings/libgnomekbd.convert

%files devel
%{_includedir}/*
%{_libdir}/libgnomekbd.so
%{_libdir}/libgnomekbdui.so
%{_libdir}/pkgconfig/*
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Gkbd-3.0.gir


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.28.1-9
- Import
