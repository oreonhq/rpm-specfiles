%global source0_hash db5533b872b18578cdecbc179dea128915d920b570a45ad6ccd005cc061d4c2f

%{?mingw_package_header}

%global vday 02
%global vmonth 12
%global vyear 2004
%global name1 zfstream

Name:           mingw-%{name1}
Version:        %{vyear}%{vmonth}%{vday}
Release:        48%{?dist}
Summary:        MinGW Windows abstraction API for reading and writing compressed files

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.wanderinghorse.net/computing/%{name1}/
Source0:        http://www.wanderinghorse.net/computing/%{name1}/libs11n_%{name1}-%{vyear}.%{vmonth}.%{vday}.tar.gz
# I tried half a day to get the rather peculiar original build system working,
# but I failed, so I decided to simply replace it by autotools.
# This has the further advantage that it knows how to cross-compile.
Source1:        %{name1}-autotools.tar.gz
# The patch has been sent via private mail to the author. The author responded
# that the patch had been integrated into his personal tree, but apparently
# he has not gotten around to release a new version.
Patch1:         %{name1}-zip.patch
# Fix build against minizip-3.0.7
Patch2:         %{name1}-minizip.patch

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-bzip2
BuildRequires:  mingw64-bzip2
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-zlib
BuildRequires:  mingw32-minizip
BuildRequires:  mingw64-minizip
BuildRequires:  libtool
BuildRequires:  automake
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw32-pkg-config
BuildRequires:  mingw64-pkg-config

%description
MinGW zfstream C++ compressed I/O abstraction library

#Mingw32
%package -n mingw32-%{name1}
Summary:        MinGW Windows abstraction API for reading and writing compressed files

%description -n mingw32-%{name1}
MinGW zfstream C++ compressed I/O abstraction library

#Mingw64
%package -n mingw64-%{name1}
Summary:        MinGW Windows abstraction API for reading and writing compressed files

%description -n mingw64-%{name1}
MinGW zfstream C++ compressed I/O abstraction library

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n libs11n_%{name1}-%{vyear}.%{vmonth}.%{vday} -a 1
%patch -P1 -p0 -b .zip
%patch -P2 -p1
touch NEWS README AUTHORS
aclocal
autoconf
autoheader
libtoolize -f
automake -a -c

%build
%{mingw_configure} --disable-static
%{mingw_make} %{?_smp_mflags}

%install
%{mingw_make} install DESTDIR=$RPM_BUILD_ROOT

# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete

%files -n mingw32-%{name1}
%doc LICENSE
%{mingw32_bindir}/libzfstream-0.dll
%{mingw32_includedir}/*
%{mingw32_libdir}/libzfstream.dll.a
%{mingw32_libdir}/pkgconfig/zfstream.pc

%files -n mingw64-%{name1}
%doc LICENSE
%{mingw64_bindir}/libzfstream-0.dll
%{mingw64_includedir}/*
%{mingw64_libdir}/libzfstream.dll.a
%{mingw64_libdir}/pkgconfig/zfstream.pc

%changelog
%autochangelog
