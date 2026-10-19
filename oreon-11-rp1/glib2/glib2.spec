%global source0_hash 17d15cac2af80a33271127408e0abc2748eb297c595c2a26409e81e14e7d1b8f
%global major_minor_version %(echo %{version} | cut -d "." -f 1-2)
Name:           glib2
Version:        2.90.0
Release:        1%{?dist}
Summary:        A library of handy utility functions
License:        LGPL-2.1-or-later
URL:            https://www.gtk.org
Source0:        https://download.gnome.org/sources/glib/%{major_minor_version}/glib-%{version}.tar.xz
Patch:          gnutls-hmac.patch
Patch:          default-terminal.patch
%if 0%{?__isa_bits} == 64
Requires: libgnutls.so.30()(64bit)
%else
Requires: libgnutls.so.30
%endif
Provides: bundled(cmph)
Provides: bundled(dirent)
Provides: bundled(gnulib)
Provides: bundled(gvdb)
Provides: bundled(libcharset)
Provides: bundled(xdgmime)
Conflicts: gobject-introspection < 1.79.1
# oreon:deps
BuildRequires:  /usr/bin/dbus-daemon
BuildRequires:  /usr/bin/g-ir-scanner
BuildRequires:  /usr/bin/rst2man
BuildRequires:  /usr/bin/update-desktop-database
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  glibc-devel
BuildRequires:  gnutls
BuildRequires:  libattr-devel
BuildRequires:  libselinux-devel
BuildRequires:  meson
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(mount)
BuildRequires:  pkgconfig(sysprof-capture-4)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3-devel
BuildRequires:  shared-mime-info
BuildRequires:  systemtap-sdt-devel
BuildRequires:  systemtap-sdt-dtrace
# /oreon:deps
%description
GLib is the low-level core library that forms the basis for projects
such as GTK+ and GNOME. It provides data structure handling for C,
portability wrappers, and interfaces for such runtime functionality
as an event loop, threads, dynamic loading, and an object system.

%package devel
Summary: A library of handy utility functions
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: python3-packaging
Conflicts: gobject-introspection-devel < 1.79.1
%description devel
The glib2-devel package includes the header files for the GLib library.

%package doc
Summary: A library of handy utility functions
Requires: %{name}%{?_isa} = %{version}-%{release}
%description doc
The glib2-doc package includes documentation for the GLib library.

%package static
Summary: glib static
Requires: %{name}-devel = %{version}-%{release}
Requires: pcre2-static
Requires: sysprof-capture-static
%description static
The %{name}-static subpackage contains static libraries for %{name}.

%package tests
Summary: Tests for the glib2 package
Requires: %{name}%{?_isa} = %{version}-%{release}
%description tests
The glib2-tests package contains tests that can be used to verify
the functionality of the installed glib2 package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir glib-%{version}
%oreon_prep
%build

%meson \
    -Dglib_debug=disabled \
    -Ddocumentation=true \
    -Dinstalled_tests=true \
    -Dgnutls=true \
    --default-library=both \
    %{nil}
%meson_build
%install
%meson_install
%py_byte_compile %{python3} %{buildroot}%{_datadir}
mv %{buildroot}%{_bindir}/gio-querymodules %{buildroot}%{_bindir}/gio-querymodules-%{__isa_bits}
sed -i -e "/^gio_querymodules=/s/gio-querymodules/gio-querymodules-%{__isa_bits}/" %{buildroot}%{_libdir}/pkgconfig/gio-2.0.pc
mkdir -p %{buildroot}%{_libdir}/gio/modules
touch %{buildroot}%{_libdir}/gio/modules/giomodule.cache
%find_lang glib20
%transfiletriggerin -- %{_libdir}/gio/modules
gio-querymodules-%{__isa_bits} %{_libdir}/gio/modules &> /dev/null || :
%transfiletriggerpostun -- %{_libdir}/gio/modules
gio-querymodules-%{__isa_bits} %{_libdir}/gio/modules &> /dev/null || :
%transfiletriggerin -- %{_datadir}/glib-2.0/schemas
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
%transfiletriggerpostun -- %{_datadir}/glib-2.0/schemas
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n glib2-devel -f %{oreon_filedir}/glib2-devel.list
%files -n glib2-doc -f %{oreon_filedir}/glib2-doc.list
%files -n glib2-static -f %{oreon_filedir}/glib2-static.list
%files -n glib2-tests -f %{oreon_filedir}/glib2-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.88.0-1
- Prepare for Oreon 11 (RP1)
