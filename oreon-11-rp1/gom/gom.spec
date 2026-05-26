Name:           gom
Version:        0.5.6
Release:        1%{?dist}
Summary:        GObject to SQLite object mapper library

# documentation is GFDL-1.1-or-later
License:        LGPL-2.1-or-later AND GFDL-1.1-or-later
URL:            https://wiki.gnome.org/Projects/Gom
Source0:        https://download.gnome.org/sources/gom/0.5/gom-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 4d7a5e268698c8e7e40603e36e9e3a2b76133931ce1b637c1136301491b54cc3
%global source0_file gom-0.5.6.tar.xz
# oreon url source checksums end

BuildRequires:  gobject-introspection-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-base
BuildRequires:  /usr/bin/gi-docgen

%description
Gom provides an object mapper from GObjects to SQLite. It helps you write
applications that need to store structured data as well as make complex queries
upon that data.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/gom-0.5.6.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "4d7a5e268698c8e7e40603e36e9e3a2b76133931ce1b637c1136301491b54cc3" || { echo "oreon: Source0 SHA256 mismatch for gom-0.5.6.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1

%build
%meson -Denable-gtk-doc=true
%meson_build

%install
%meson_install

%ldconfig_scriptlets

%files
%license COPYING
%doc NEWS README
%{_libdir}/girepository-1.0/Gom-1.0.typelib
%{_libdir}/libgom-1.0.so.0*
%dir %{python3_sitelib}/gi
%dir %{python3_sitelib}/gi/overrides
%{python3_sitelib}/gi/overrides/Gom.py
%dir %{python3_sitelib}/gi/overrides/__pycache__
%{python3_sitelib}/gi/overrides/__pycache__/Gom.cpython-*.pyc

%files devel
%{_includedir}/gom-1.0/
%{_libdir}/libgom-1.0.so
%{_libdir}/pkgconfig/gom-1.0.pc
%{_datadir}/gir-1.0/Gom-1.0.gir
%doc %{_docdir}/gom-1.0/

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.5.6-1
- Prepare for Oreon 11 (RP1)
