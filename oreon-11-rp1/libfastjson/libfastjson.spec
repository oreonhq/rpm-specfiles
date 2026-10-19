%global source0_hash 7cd6f78c1c07f4140f6976a9a0e0048bcaa7292329c6ac2c0e070383d83d8edd
Name:		libfastjson
Version:	1.2609.0
Release:        1%{?dist}
Summary:        A JSON implementation in C
License:	MIT
URL:		https://github.com/rsyslog/libfastjson
Source0:        http://download.rsyslog.com/libfastjson/libfastjson-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
LIBFASTJSON implements a reference counting object
model that allows you to easily construct JSON
objects in C, output them as JSON formatted strings
and parse JSON formatted strings back into the
C representation of JSON objects.

%package	devel
Summary:	Development files for libfastjson
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description	devel
This package contains libraries and header files for
developing applications that use libfastjson.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

for doc in ChangeLog; do
 iconv -f iso-8859-1 -t utf8 $doc > $doc.new &&
 touch -r $doc $doc.new &&
 mv $doc.new $doc
done

%build

autoreconf -iv
export CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE" # temporary workaround for EPEL5, fixed upstream
%configure --enable-shared --disable-static
%install
make V=1 DESTDIR=%{buildroot} install
find %{buildroot} -name '*.la' -delete -print
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make V=1 check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libfastjson-devel -f %{oreon_filedir}/libfastjson-devel.list

%changelog

%autochangelog
