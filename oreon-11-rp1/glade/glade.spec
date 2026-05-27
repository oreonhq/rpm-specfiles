%global source0_hash 31c9adaea849972ab9517b564e19ac19977ca97758b109edc3167008f53e3d9c

Name:           glade
Version:        3.40.0
Release:        14%{?dist}
Summary:        User Interface Designer for GTK+

# - /usr/bin/glade is GPLv2+
# - /usr/bin/glade-previewer is LGPLv2+
# - libgladeui-2.so, libgladegtk.so, and libgladepython.so all combine
#   GPLv2+ and LGPLv2+ code, so the resulting binaries are GPLv2+
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            https://glade.gnome.org/
Source0:        https://download.gnome.org/sources/glade/3.40/glade-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gjs-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk3-devel
BuildRequires:  gtk-doc
BuildRequires:  itstool
BuildRequires:  libxml2-devel
BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-devel
BuildRequires:  webkit2gtk4.1-devel
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/xsltproc

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
Glade is a RAD tool to enable quick and easy development of user interfaces for
the GTK+ toolkit and the GNOME desktop environment.

The user interfaces designed in Glade are saved as XML, which can be used in
numerous programming languages including C, C++, C#, Vala, Java, Perl, Python,
and others.


%package libs
Summary:        Widget library for Glade UI designer

%description    libs
The %{name}-libs package consists of the widgets that compose the Glade GUI as
a separate library to ease the integration of Glade into other applications.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use Glade widget library.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1
# glade does not use libsoup, no other porting necessary
sed -i -e 's/webkit2gtk-4.0/webkit2gtk-4.1/' meson.build


%build
%meson -Dgtk_doc=true
%meson_build


%install
%meson_install

%find_lang glade --with-gnome


%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/org.gnome.Glade.appdata.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Glade.desktop


%files -f glade.lang
%license COPYING*
%doc AUTHORS NEWS
%{_bindir}/glade
%{_bindir}/glade-previewer
%{_datadir}/applications/org.gnome.Glade.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Glade.svg
%{_datadir}/icons/hicolor/symbolic/apps/glade-brand-symbolic.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Glade-symbolic.svg
%{_datadir}/metainfo/org.gnome.Glade.appdata.xml
%{_mandir}/man1/glade.1*
%{_mandir}/man1/glade-previewer*

%files libs
%license COPYING*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Gladeui-2.0.typelib
%dir %{_libdir}/glade/
%dir %{_libdir}/glade/modules/
%{_libdir}/glade/modules/libgladegjs.so
%{_libdir}/glade/modules/libgladegtk.so
%{_libdir}/glade/modules/libgladepython.so
%{_libdir}/glade/modules/libgladewebkit2gtk.so
%{_libdir}/libgladeui-2.so.13*
%{_datadir}/glade/

%files devel
%{_includedir}/libgladeui-2.0/
%{_libdir}/libgladeui-2.so
%{_libdir}/pkgconfig/gladeui-2.0.pc
%dir %{_datadir}/gettext
%dir %{_datadir}/gettext/its
%{_datadir}/gettext/its/glade-catalog.its
%{_datadir}/gettext/its/glade-catalog.loc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Gladeui-2.0.gir
%doc %{_datadir}/gtk-doc/


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.40.0-14
- Prepare for Oreon 11 (RP1)
