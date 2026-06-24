%global source0_hash none

%global	dbus_ver	0.95
%global	dbus_glib_ver	0.90
%global	glib_ver	2.36.0
%global	gobj_ver	1.30
%global	vala_ver	0.16.0

Name:           telepathy-glib
Version:        0.24.2
Release:        15%{?dist}
Summary:        GLib bindings for Telepathy

# LGPL-2.1-or-later: overall
# FSFAP: examples/client/ et al. (not included in the binary)
# FSFAP: tests/contact-search-result.c et al.
# SPDX confirmed
License:        LGPL-2.1-or-later
URL:            http://telepathy.freedesktop.org/wiki/FrontPage
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
# Patch to make testsuite work with newer GLib
# https://gitlab.freedesktop.org/telepathy/telepathy-glib/-/issues/145
# https://gitlab.freedesktop.org/telepathy/telepathy-glib/-/merge_requests/3
# https://gitlab.freedesktop.org/telepathy/telepathy-glib/-/merge_requests/3.patch
Patch0:         telepathy-glib-pr3-test-cm-with-newer-glib.patch
# Patch for -Werror=incompatible-pointer-types
# https://gitlab.freedesktop.org/telepathy/telepathy-glib/-/issues/146
# https://gitlab.freedesktop.org/telepathy/telepathy-glib/-/merge_requests/4
Patch1:         telepathy-glib-prXXX-function-type-cast.patch

BuildRequires:	make
BuildRequires:	gcc
# Tests
BuildRequires:	gcc-c++

BuildRequires:	pkgconfig(dbus-1) >= %{dbus_ver}
BuildRequires:	pkgconfig(dbus-glib-1) >= %{dbus_glib_ver}
BuildRequires:	pkgconfig(glib-2.0) >= %{glib_ver}
BuildRequires:	pkgconfig(gobject-2.0) >= %{glib_ver}
BuildRequires:	pkgconfig(gio-2.0) >= %{glib_ver}
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= %{gobj_ver}

BuildRequires:	gtk-doc >= 1.17
BuildRequires:	/usr/bin/valac
BuildRequires:	/usr/bin/vapigen
BuildRequires:	/usr/bin/xsltproc
BuildRequires:	python3
# For tests/dbus
BuildRequires:	dbus-daemon

%description
Telepathy-glib is the glib bindings for the telepathy unified framework
for all forms of real time conversations, including instant messaging, IRC, 
voice calls and video calls.

%package	vala
Summary:	Vala bindings for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	vala
BuildArch:	noarch

%description vala
Vala bindings for %{name}.

%package 	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	%{name}-vala = %{version}-%{release}
Requires:	telepathy-filesystem

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Explicitly switch to python3
touch timestamp
env LANG=C grep -rl python . | while read f
do
	sed -i $f \
		-e 's|/usr/bin/python$|/usr/bin/python3|'  \
		-e 's|/usr/bin/env[ \t]*python$|/usr/bin/python3|' \
		%{nil}
	# Explicitly set timestamp of the modified files to the same time
	# so that autotool won't be called after configure
	touch -r timestamp $f
done
# Also modify the following timestamp
touch -r timestamp config.h.in

%build
%configure \
	--enable-static=no \
	--disable-silent-rules \
	--enable-introspection=yes \
	--enable-vala-bindings=yes \
	%{nil}

%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -name '*.la' -delete

%check
make check

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/libtelepathy-glib.so.0
%{_libdir}/libtelepathy-glib.so.0.*
%{_libdir}/girepository-1.0/TelepathyGLib-0.12.typelib

%files vala
%{_datadir}/vala/vapi/telepathy-glib.deps
%{_datadir}/vala/vapi/telepathy-glib.vapi

%files devel
%doc %{_datadir}/gtk-doc/html/%{name}/
%{_libdir}/libtelepathy-glib.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/telepathy-1.0/%{name}/
%{_datadir}/gir-1.0/TelepathyGLib-0.12.gir


%changelog
%autochangelog

