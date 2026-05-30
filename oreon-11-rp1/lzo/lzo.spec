%global source0_hash c0f892943208266f9b6543b3ae308fab6284c5c90e627931446fb49b4221a072

Name:           lzo
Version:        2.10
Release:        16%{?dist}
Summary:        Data compression library with very fast (de)compression
License:        gpl-2.0-or-later
URL:            http://www.oberhumer.com/opensource/lzo/

Source0:        http://www.oberhumer.com/opensource/lzo/download/%{name}-%{version}.tar.gz
Patch0:         lzo-2.08-configure.patch
Patch1:         lzo-2.08-rhbz1309225.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  zlib-devel

%description
LZO is a portable lossless data compression library written in ANSI C.
It offers pretty fast compression and very fast decompression.
Decompression requires no memory. In addition there are slower
compression levels achieving a quite competitive compression ratio
while still decompressing at this very high speed.


%package minilzo
Summary:        Mini version of lzo for apps which don't need the full version

%description minilzo
A small (mini) version of lzo for embedding into applications which don't need
full blown lzo compression support.


%package devel
Summary:        Development files for the lzo library
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-minilzo = %{version}-%{release}
Requires:       zlib-devel

%description devel
LZO is a portable lossless data compression library written in ANSI C.
It offers pretty fast compression and very fast decompression.
This package contains development files needed for lzo.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1
# mark asm files as NOT needing execstack
for i in asm/i386/src_gas/*.S; do
  echo '.section .note.GNU-stack,"",@progbits' >> $i
done


%build
%configure --disable-dependency-tracking --disable-static --enable-shared
%{make_build} CFLAGS+=-fno-strict-aliasing

# build minilzo too (bz 439979)
gcc %{optflags} -fpic -Iinclude/lzo -o minilzo/minilzo.o -c minilzo/minilzo.c
gcc -g -shared -Wl,-z,now -o libminilzo.so.0 -Wl,-soname,libminilzo.so.0 minilzo/minilzo.o


%install
%{make_install}
find $RPM_BUILD_ROOT -name '*.la' -delete

install -m 755 libminilzo.so.0 $RPM_BUILD_ROOT%{_libdir}
ln -s libminilzo.so.0 $RPM_BUILD_ROOT%{_libdir}/libminilzo.so
install -p -m 644 minilzo/minilzo.h $RPM_BUILD_ROOT%{_includedir}/lzo

#Remove doc
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/lzo

%check
make check test


%ldconfig_scriptlets
%ldconfig_scriptlets minilzo


%files
%license COPYING
%doc AUTHORS THANKS NEWS
%{_libdir}/liblzo2.so.*

%files minilzo
%license COPYING
%doc minilzo/README.LZO
%{_libdir}/libminilzo.so.0

%files devel
%doc doc/LZOAPI.TXT doc/LZO.FAQ doc/LZO.TXT
%{_includedir}/lzo
%{_libdir}/lib*lzo*.so
%{_libdir}/pkgconfig/lzo2.pc


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.10-16
- Prepare for Oreon 11 (RP1)
