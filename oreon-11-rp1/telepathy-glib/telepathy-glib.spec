%global source0_hash b0a374d771cdd081125f38c3abd079657642301c71a543d555e2bf21919273f0
%global	dbus_ver	0.95
%global	dbus_glib_ver	0.90
%global	glib_ver	2.36.0
%global	gobj_ver	1.30
%global	vala_ver	0.16.0
Name:           telepathy-glib
Version:        0.24.2
Release:        1%{?dist}
Summary:        GLib bindings for Telepathy
License:        LGPL-2.1-or-later
URL:            http://telepathy.freedesktop.org/wiki/FrontPage
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
Patch0:         telepathy-glib-pr3-test-cm-with-newer-glib.patch
Patch1:         telepathy-glib-prXXX-function-type-cast.patch
# oreon:deps
BuildRequires:  /usr/bin/valac
BuildRequires:  /usr/bin/vapigen
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  dbus-daemon
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gtk-doc
BuildRequires:  make
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  python3
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n telepathy-glib-vala -f %{oreon_filedir}/telepathy-glib-vala.list
%files -n telepathy-glib-devel -f %{oreon_filedir}/telepathy-glib-devel.list

%changelog

%autochangelog

