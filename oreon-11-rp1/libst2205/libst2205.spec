%global source0_hash 5a57a4ff52c1c1e2b92d5d4f3d08e23356314140c70c9b61e0e8e5848da8a53f
Name:           libst2205
Version:        1.4.3
Release:        35%{?dist}
Summary:        Library for accessing the display of hacked st2205 photo frames
License:        GPL-3.0-or-later
URL:            http://picframe.spritesserver.nl/wiki/index.php
Source0:        http://www.neophob.com/files/st2205tool-1.4.3.tar.gz
Patch0:         st2205tool-1.4.3-no-exit.patch
Patch1:         st2205tool-1.4.3-width-height-swap.patch
Patch2:         libst2205-c99.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gd-devel
BuildRequires:  make
# /oreon:deps
%description
It is possible to flash digital photo frames with the st2205 chip-sets with
a modified firmware, which allows one to display real time images on the
display of the frame from a PC. This package contains a library for accessing
the display from the PC, for st2205 frames with the hacked firmware.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tools
Summary:        Tools for %{name}
Requires:       %{name} = %{version}-%{release}
%description tools
This package contains the st2205 set picture utility which can be used to
display a (properly sized) PNG file on a supported picture frames display.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n st2205tool
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build

make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -fPIC -D_GNU_SOURCE" -C libst2205
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -I../libst2205" -C setpic
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}
install -m 755 setpic/setpic $RPM_BUILD_ROOT%{_bindir}/st2205-setpic
install -m 755 libst2205/libst2205.so $RPM_BUILD_ROOT%{_libdir}/libst2205.so.1
ln -s libst2205.so.1 $RPM_BUILD_ROOT%{_libdir}/libst2205.so
install -p -m 644 libst2205/st2205.h $RPM_BUILD_ROOT%{_includedir}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libst2205-devel -f %{oreon_filedir}/libst2205-devel.list
%files -n libst2205-tools -f %{oreon_filedir}/libst2205-tools.list

%changelog

%autochangelog
