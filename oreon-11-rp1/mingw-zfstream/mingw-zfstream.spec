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
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.wanderinghorse.net/computing/%{name1}/
Source0:        http://www.wanderinghorse.net/computing/%{name1}/libs11n_%{name1}-%{vyear}.%{vmonth}.%{vday}.tar.gz
Source1:        %{name1}-autotools.tar.gz
Patch1:         %{name1}-zip.patch
Patch2:         %{name1}-minizip.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-bzip2
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-minizip
BuildRequires:  mingw32-pkg-config
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-bzip2
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-minizip
BuildRequires:  mingw64-pkg-config
BuildRequires:  mingw64-zlib
# /oreon:deps
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
find $RPM_BUILD_ROOT -name "*.la" -delete
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-zfstream -f %{oreon_filedir}/mingw32-zfstream.list
%files -n mingw64-zfstream -f %{oreon_filedir}/mingw64-zfstream.list

%changelog

%autochangelog
