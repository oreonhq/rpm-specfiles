Name:		libfastjson
Version:	1.2304.0
Release:	8%{?dist}
Summary:	A JSON implementation in C
License:	MIT
URL:		https://github.com/rsyslog/libfastjson
Source0:	http://download.rsyslog.com/libfastjson/libfastjson-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 ef30d1e57a18ec770f90056aaac77300270c6203bbe476f4181cc83a2d5dc80c
%global source0_file libfastjson-1.2304.0.tar.gz
# oreon url source checksums end

BuildRequires: autoconf automake libtool
BuildRequires: make

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libfastjson-1.2304.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "ef30d1e57a18ec770f90056aaac77300270c6203bbe476f4181cc83a2d5dc80c" || { echo "oreon: Source0 SHA256 mismatch for libfastjson-1.2304.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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

%check
make V=1 check

%ldconfig_scriptlets

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc AUTHORS ChangeLog README.html
%{_libdir}/libfastjson.so.*

%files devel
%{_includedir}/libfastjson
%{_libdir}/libfastjson.so
%{_libdir}/pkgconfig/libfastjson.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2304.0-8
- Prepare for Oreon 11 (RP1)
