%global source0_hash 4d11b1f95137588e46800f21bd87162e749ea8fe6a777b7af8bd2e6464d6bcc6
%{?mingw_package_header}
%global mingw_pkg_name libsqlite3x
%global veryear 2007
%global vermon  10
%global verday  18
Name:           mingw-%{mingw_pkg_name}
Version:        %{veryear}%{vermon}%{verday}
Release:        44%{?dist}
Summary:        MinGW Windows C++ Wrapper for the SQLite3 embeddable SQL database engine
License:        zlib
URL:            http://www.wanderinghorse.net/computing/sqlite/
Source0:        http://www.wanderinghorse.net/computing/sqlite/%{mingw_pkg_name}-%{veryear}.%{vermon}.%{verday}.tar.gz
Source1:        libsqlite3x-autotools.tar.gz
Patch1:         libsqlite3x-prep.patch
Patch2:         libsqlite3x-includes.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  automake
BuildRequires:  dos2unix
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-sqlite
BuildRequires:  mingw32-winpthreads
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-sqlite
BuildRequires:  mingw64-winpthreads
# /oreon:deps
%description
sqlite3 is a slick embedded SQL server written in C. It's easy to use,
powerful, and quite fast. sqlite3x is a C++ wrapper API for working
with sqlite3 databases that uses exceptions.

#Mingw32
%package -n      mingw32-%{mingw_pkg_name}
Summary:         MinGW Windows C++ Wrapper for the SQLite3 embeddable SQL database engine
%description -n mingw32-%{mingw_pkg_name}
sqlite3 is a slick embedded SQL server written in C. It's easy to use,
powerful, and quite fast. sqlite3x is a C++ wrapper API for working
with sqlite3 databases that uses exceptions.

%package -n     mingw32-libsq3
Summary:        MinGW Windows C++ Wrapper for the SQLite3 embeddable SQL database engine
Requires:       mingw32-%{mingw_pkg_name} = %{version}-%{release}
%description -n mingw32-libsq3
sqlite3 is a slick embedded SQL server written in C. It's easy to use,
powerful, and quite fast. sq3 is a C++ wrapper API for working
with sqlite3 databases that does not use exceptions.

#Mingw64
%package -n      mingw64-%{mingw_pkg_name}
Summary:         MinGW Windows C++ Wrapper for the SQLite3 embeddable SQL database engine
%description -n mingw64-%{mingw_pkg_name}
sqlite3 is a slick embedded SQL server written in C. It's easy to use,
powerful, and quite fast. sqlite3x is a C++ wrapper API for working
with sqlite3 databases that uses exceptions.

%package -n     mingw64-libsq3
Summary:        MinGW Windows C++ Wrapper for the SQLite3 embeddable SQL database engine
Requires:       mingw64-%{mingw_pkg_name} = %{version}-%{release}
%description -n mingw64-libsq3
sqlite3 is a slick embedded SQL server written in C. It's easy to use,
powerful, and quite fast. sq3 is a C++ wrapper API for working
with sqlite3 databases that does not use exceptions.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{mingw_pkg_name}-%{veryear}.%{vermon}.%{verday} -a 1
dos2unix *.hpp *.cpp
%patch -P1 -p0 -b .prep
%patch -P2 -p0 -b .incl
aclocal
libtoolize -f
autoheader
autoconf
automake -a -c
%{mingw_configure} --disable-static
iconv -f iso8859-1 -t utf-8  < README > R
mv R README

%build

%{mingw_make}
%install
%{mingw_make} install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%doc AUTHORS README Doxygen-index.txt
%{mingw32_bindir}/libsqlite3x-1.dll
%{mingw32_includedir}/sqlite3x
%{mingw32_libdir}/libsqlite3x.dll.a
%{mingw32_libdir}/pkgconfig/libsqlite3x.pc
%oreon_autofiles mingw32-libsq3 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libsq3 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-libsqlite3x -f %{oreon_filedir}/mingw32-libsqlite3x.list
%files -n mingw32-libsq3 -f %{oreon_filedir}/mingw32-libsq3.list
%files -n mingw64-libsqlite3x -f %{oreon_filedir}/mingw64-libsqlite3x.list
%files -n mingw64-libsq3 -f %{oreon_filedir}/mingw64-libsq3.list

%changelog

%autochangelog
