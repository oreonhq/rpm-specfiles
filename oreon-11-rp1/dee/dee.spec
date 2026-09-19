%global source0_hash 1bf0336ce684aa0f48d6eae2469628c1a9b43695a77443bc31a5790aa673bf8a

# gtk2 deps aren't C23 clean, can't build here with that until they are (if they ever are)
%global optflags %{optflags} -std=gnu17

Summary:	Model to synchronize multiple instances over DBus
Name:		dee
Version:	1.2.7
Release:	65%{?dist}
# GPLv3-licensed tests and examples are in the tarball, but not installed
License:	LGPL-3.0-only
URL:		https://launchpad.net/dee
Source0:	http://launchpad.net/dee/1.0/%{version}/+download/%{name}-%{version}.tar.gz
Patch0:		dee-1.2.7-gcc6-fixes.patch
Patch1:		dee-1.2.7-deprecated-g_type_class_add_private.patch
# https://salsa.debian.org/debian/dee/-/blob/master/debian/patches/vapi-skip-properties.patch
Patch2:		vapi-skip-properties.patch
# Skip duplicates flagged by vala 0.5X
Patch3:		dee-1.2.7-fix-duplicates-vala-0.5X.patch
# Fix issue where g_string_free was not storing the return value
Patch4:		dee-1.2.7-fix-g_string_free-usage.patch
BuildRequires:	vala
BuildRequires:	gtk-doc
BuildRequires:	dbus-glib-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	libicu-devel >= 4.6
BuildRequires:	python3-devel
BuildRequires:	autoconf, automake, libtool
BuildRequires: make
# For %%{python3_sitearch}/gi/overrides directory
Requires:	python3-gobject-base

%description
Libdee is a library that uses DBus to provide objects allowing you to
create Model-View-Controller type programs across DBus. It also
consists of utility objects which extend DBus allowing for peer-to-peer
discoverability of known objects without needing a central registrar.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .gcc6
%patch -P1 -p1 -b .dep
%patch -P2 -p1
%patch -P3 -p1 -b .dupes
%patch -P4 -p1 -b .freefix
autoupdate
autoreconf -ifv .

%build
export CFLAGS="%{optflags} -Wno-error=maybe-uninitialized"
export PYTHON="/usr/bin/python3"
%configure --disable-static
make %{?_smp_mflags} V=1

%install
make DESTDIR=%{buildroot} install
find %{buildroot} -regex ".*\.la$" | xargs rm -f --

%ldconfig_scriptlets

%files
%license COPYING
%{_bindir}/dee-tool
%{_libdir}/girepository-1.0/*.typelib
%{_libdir}/libdee*.so.*
%{python3_sitearch}/gi/overrides/*

%files devel
%license COPYING
%{_includedir}/dee-1.0
%{_libdir}/libdee*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/gtk-doc/html/dee-1.0
%{_datadir}/vala/vapi/*.vapi
%{_datadir}/vala/vapi/*.deps

%changelog
%autochangelog
