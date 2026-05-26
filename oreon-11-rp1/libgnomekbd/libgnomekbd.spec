# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 22dc59566d73c0065350f5a97340e62ecc7b08c4df19183804bb8be24c8fe870
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

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
%oreon_verify_sources
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
