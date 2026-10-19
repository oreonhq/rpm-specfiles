%global source0_hash 6444b13b9ec5b6f9de8f72513a00870325779e3b05bfcf554edb1ab0c90f5962
%define abi_major 0
%define abi_minor 1
Name:           pnglite
Version:        0.1.17
Release:        1%{?dist}
Summary:        A lightweight C library for loading PNG images
License:        zlib
URL:            http://www.danielkarling.se/stuff/pnglite/
Source0:        http://downloads.sourceforge.net/pnglite/%{name}-%{version}.zip
Patch0:         pnglite-0.1.17-zlib.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  zlib-devel
# /oreon:deps
%description
pnglite is a C library for loading PNG images. It was created as a
substitute for libpng in situations when libpng is more than enough. It
currently requires zlib for inflate and crc checking and it can read the
most common types of PNG images. The library has a small and simple to use
interface.

%package devel
Summary:        Files needed to build and link programs with pnglite
Requires:       pnglite = %{version}
%description devel
This contains a header file and a link to library for the linker
to link against pnglite.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c
%patch -P0 -p1 -b .zlib
sed 's/\r//' -i pnglite.h

%build

gcc %{optflags} -shared -fPIC -Wl,--soname,libpnglite.so.%{abi_major} \
       -o libpnglite.so.%{abi_major}.%{abi_minor} pnglite.c
%install
install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_includedir}
install -pm 0644 pnglite.h %{buildroot}%{_includedir}
install libpnglite.so.%{abi_major}.%{abi_minor} %{buildroot}%{_libdir}
ln -s libpnglite.so.%{abi_major}.%{abi_minor} %{buildroot}%{_libdir}/libpnglite.so.%{abi_major}
ln -s libpnglite.so.%{abi_major}.%{abi_minor} %{buildroot}%{_libdir}/libpnglite.so
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n pnglite-devel -f %{oreon_filedir}/pnglite-devel.list

%changelog

%autochangelog
