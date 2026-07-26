%global source0_hash 879f07130ac64792ddb9fd758e6673119283bda37d75573787ae22af8684a240

Name:		keybinder
Version:	0.3.1
Release:	33%{?dist}
Summary:	A library for registering global keyboard shortcuts
# python-keybinder/__init__.py	unused
# SPDX confirmed
License:	MIT
URL:		https://github.com/engla/keybinder
Source0:	%url/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	gtk2-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	/usr/bin/gtkdocize
Obsoletes:		python2-%{name} < 0.3.1-16

%description
keybinder is a library for registering global keyboard shortcuts. 
Keybinder works with GTK-based applications using the X Window System.

The library contains:
- A C library, libkeybinder
- An examples directory with programs in C, Lua, and Vala.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
This package contains the development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}
sed -i -e 's@-rpath @@g' libkeybinder/Makefile.in \
	lua-keybinder/Makefile.in python-keybinder/Makefile.in
autoreconf -fiv

%build
PY2_STATUS=disable
%configure --disable-static --${PY2_STATUS}-python --disable-lua \
	--disable-silent-rules
%make_build

%install
%make_install

#Remove libtool archives.
find %{buildroot} -name '*.la'| xargs rm -f

%ldconfig_scriptlets

%files
%doc NEWS
%doc AUTHORS
%doc README
%license COPYING
%{_libdir}/libkeybinder.so.0{,.*}
%{_libdir}/girepository-1.0/Keybinder-*.typelib
%{_datadir}/gir-1.0/Keybinder-*.gir

%files devel
%{_includedir}/keybinder.h
%{_libdir}/pkgconfig/keybinder.pc
%{_libdir}/libkeybinder.so
%{_datadir}/gtk-doc/html/%{name}

%changelog
%autochangelog
