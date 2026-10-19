%global source0_hash 879f07130ac64792ddb9fd758e6673119283bda37d75573787ae22af8684a240
Name:		keybinder
Version:	0.3.1
Release:        1%{?dist}
Summary:        A library for registering global keyboard shortcuts
License:	MIT
URL:		https://github.com/engla/keybinder
Source0:        https://github.com/engla/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Obsoletes:		python2-%{name} < 0.3.1-16
# oreon:deps
BuildRequires:  /usr/bin/gtkdocize
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(gobject-introspection-1.0)
# /oreon:deps
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
find %{buildroot} -name '*.la'| xargs rm -f
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n keybinder-devel -f %{oreon_filedir}/keybinder-devel.list

%changelog

%autochangelog
