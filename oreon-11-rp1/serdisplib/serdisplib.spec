%global source0_hash fe82ebe72731e91509083569dfe41a09e21632cc1211cdc4f76274f83ed218fa
Name:           serdisplib
Version:        1.97.9
Release:        1%{?dist}
Summary:        Library to drive serial displays with built-in controllers
License:        GPL-2.0-or-later
URL:            http://serdisplib.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         serdisplib-configure-c99.patch
Patch1:         serdisplib-1.97.9-build-fix.patch
# oreon:deps
BuildRequires:  SDL-devel
BuildRequires:  gcc
BuildRequires:  gd-devel
BuildRequires:  libusb-compat-0.1-devel
BuildRequires:  make
# /oreon:deps
%description
serdisplib started as a library to drive serial displays with built-in
controllers. beginning with version 1.95 support was added for parallel driven
displays. anyhow: the name 'serdisplib' will not change.

The serial in "serial display" characterizes the way of how the data is
transferred to the display controller: data is sent bit by bit using a single
input line. several (few) other lines are controlling things like timing
(clock), data or command, ... 

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tools
Summary:        Serdisplib tools (testserdisp, multidisplay)
Requires:       %{name} = %{version}-%{release}
%description tools
This package contains the tools for serdisplib

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --enable-libusb --enable-libSDL --disable-statictools
make %{?_smp_mflags} STATIC_LDFLAGS="$RPM_LD_FLAGS -lusb -lSDL -lpthread"
%install
%makeinstall
rm $RPM_BUILD_ROOT%{_libdir}/libserdisp.a
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n serdisplib-devel -f %{oreon_filedir}/serdisplib-devel.list
%files -n serdisplib-tools -f %{oreon_filedir}/serdisplib-tools.list

%changelog

%autochangelog
