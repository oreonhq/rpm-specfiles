%global source0_hash a75e6f757b975d3da662fe7ea2d985f358f31ad2dede1a222bb4aa403d0dbfd1

Name:           libgringotts
Version:        1.2.1
Release:        44%{?dist}
Summary:        A backend for managing encrypted data files on the disk
Summary(pl):    Zaplecze do zarządzania zaszyfrowanymi plikami danych na dysku

# SPDX confirmed
License:        GPL-2.0-or-later
URL:            http://gringotts.shlomifish.org/
Source0:        http://download.berlios.de/gringotts/%{name}-%{version}.tar.bz2
# Patch for bzip2 algo size fix for big endian
Patch0:         libgringotts-1.2.1-bzip2-algo-bigendian-sizefix.patch

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make

BuildRequires:  bzip2-devel
BuildRequires:  libmcrypt-devel
BuildRequires:  mhash-devel
BuildRequires:  zlib-devel

%description
libGringotts is a small, easy-to-use, thread-safe C library
 originally developed for Gringotts; its purpose is to 
encapsulate data (generic: ASCII, but also binary data) 
in an encrypted and compressed structure, to be written 
in a file or used elseway. It makes use of strong 
encryption algorithms, to ensure the data are as safe 
as possible, and allow the user to have the complete 
control over all the algorithms used in the process.

%description        -l pl
libGringotts to niewielka, łatwa w użyciu biblioteka 
napisana w C, początkowo tworzona dla Gringotts. 
Jej zadaniem jest przechowywanie danych 
(głównie: ASCII, ale równiez binarnych) w zaszyfrowanej 
i skompresowanej strukturze, zapisywanej np. w pliku.
Używa ona silnych algorytmów szyfrujących 
dla maskymalnego bezpieczeństwa danych 
oraz by zapewnić użytkownikowi pełną kontrolę nad nimi.

%package        devel
Summary:        Development files for libgringotts
Summary(pl):    Pliki deweloperskie dla libgringotts
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The libgringotts-devel package contains libraries and header files for
developing applications that use libgringotts.

%description    devel -l pl
Pakiet libgringotts-devel zawiera biblioteki i pliki nagłówków 
niezbędne do tworzenia aplikacji, które używają libgringotts.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .bigendian

# For check
sed -i src/Makefile.am \
	-e 's|\(^[ \t][ \t]*\)@|\1|' \
	-e 's|test.c .libs/libgringotts.a|test.c -L.libs -lgringotts|' \
	-e 's|./libgrgtest|env LD_LIBRARY_PATH=.libs ./libgrgtest|' \
	%{nil}

autoreconf -fi

%build
%configure --disable-static
%make_build

%install
%make_install

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
# Clean up documentation directory
rm -rf $RPM_BUILD_ROOT%{_docdir}

%check
# Some tests e.g. 8) Password quality test (strings) reads /dev/random
# so tests may fail randomly.
# Repeat tests several times to rescue such failure.
test_status=1
for times in $(seq 1 3) ; do
	make check || continue
	test_status=0
	break
done
if test $test_status != 0 ; then exit 1 ; fi

%ldconfig_scriptlets

%files
%license	COPYING
%doc	AUTHORS
%doc	ChangeLog
%doc	NEWS
%doc	README
%doc	TODO

%{_libdir}/%{name}.so.2{,.*}

%files devel
%doc	docs/manual.htm
%{_includedir}/libgringotts.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
