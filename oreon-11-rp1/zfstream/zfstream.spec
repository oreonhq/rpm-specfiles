%global source0_hash 32640618af7347728b11c7d64f56afad95cc336ba1c37f9cba4ffca48ae72476

%global vday 02
%global vmonth 12
%global vyear 2004

Name:           zfstream
Version:        %{vyear}%{vmonth}%{vday}
Release:        44%{?dist}
Summary:        Library for reading and writing compressed and non-compressed files

License:        LGPL-2.1-or-later
URL:            http://www.wanderinghorse.net/computing/%{name}/
Source0:        http://www.wanderinghorse.net/computing/%{name}/libs11n_%{name}-%{vyear}.%{vmonth}.%{vday}.tar.gz
# I tried half a day to get the rather peculiar original build system working,
# but I failed, so I decided to simply replace it by autotools.
# This has the further advantage that it knows how to cross-compile,
# as evidenced by the mingw32-zfstream package also under review.
Source1:        %{name}-autotools.tar.gz
# The patch has been sent via private mail to the author. The author responded
# that the patch had been integrated into his personal tree, but apparently
# he has not gotten around to release a new version.
Patch1:         %{name}-zip.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  bzip2-devel
BuildRequires:  libtool
BuildRequires:  minizip-ng-compat-devel

%description
zfstream is a small C++ library which provides an abstraction API for reading
and writing compressed and non-compressed files using the same API. It supports
libz and libbz2 compression schemes. The library is trivial to use and provides
client applications with a unified interface for reading and writing files
without having to know whether they are compressed or not.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
Requires:       bzip2-devel
Requires:       zlib-devel 

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n libs11n_%{name}-%{vyear}.%{vmonth}.%{vday} -a 1
%patch -P1 -p0 -b .zip
aclocal
autoconf
autoheader
libtoolize -f
touch NEWS README AUTHORS
automake -a -c

%build
%configure --disable-static
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%{_libdir}/*.so.*

%files devel
%doc ChangeLog
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
