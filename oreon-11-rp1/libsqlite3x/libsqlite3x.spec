%global source0_hash 9cf0ded40a9f1481b61f25e40837023d862389fc5e8e2704d2d8164b565ae73f
%global veryear 2007
%global vermon  10
%global verday  18
%global namesq3 libsq3
Name:           libsqlite3x
Version:        %{veryear}%{vermon}%{verday}
Release:        1%{?dist}
Summary:        A C++ Wrapper for the SQLite3 embeddable SQL database engine
License:        zlib
URL:            http://www.wanderinghorse.net/computing/sqlite/
Source0:        http://www.wanderinghorse.net/computing/sqlite/%{name}-%{veryear}.%{vermon}.%{verday}.tar.gz
Source1:        libsqlite3x-autotools.tar.gz
Patch1:         libsqlite3x-prep.patch
Patch2:         libsqlite3x-includes.patch
# oreon:deps
BuildRequires:  automake
BuildRequires:  dos2unix
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  sqlite-devel
# /oreon:deps
%description
sqlite3 is a slick embedded SQL server written in C. It's easy to use,
powerful, and quite fast. sqlite3x is a C++ wrapper API for working
with sqlite3 databases that uses exceptions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       sqlite-devel pkgconfig
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n     %{namesq3}
Summary:        A C++ Wrapper for the SQLite3 embeddable SQL database engine
Requires:       %{namesq3} = %{version}-%{release}
%description -n %{namesq3}
sqlite3 is a slick embedded SQL server written in C. It's easy to use,
powerful, and quite fast. sq3 is a C++ wrapper API for working
with sqlite3 databases that does not use exceptions.

%package -n     %{namesq3}-devel
Summary:        Development files for %{name}
Requires:       %{namesq3} = %{version}-%{release}
Requires:       sqlite-devel pkgconfig
%description -n %{namesq3}-devel
The %{namesq3}-devel package contains libraries and header files for
developing applications that use %{namesq3}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{veryear}.%{vermon}.%{verday} -a 1
dos2unix *.hpp *.cpp
%patch -P1 -p0 -b .prep
%patch -P2 -p0 -b .incl

iconv -f iso8859-1 -t utf-8  <README >R && mv R README

%build

aclocal
libtoolize -f
autoheader
autoconf
automake -a -c
%configure --disable-static
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
make
make doc
make doc-sq3
%install
%{__rm} -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%ldconfig_scriptlets
%ldconfig_scriptlets -n %{namesq3}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libsqlite3x-devel -f %{oreon_filedir}/libsqlite3x-devel.list
%files -n libsq3 -f %{oreon_filedir}/libsq3.list
%files -n libsq3-devel -f %{oreon_filedir}/libsq3-devel.list

%changelog

%autochangelog
