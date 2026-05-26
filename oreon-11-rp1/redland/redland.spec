# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 de1847f7b59021c16bdc72abb4d8e2d9187cd6124d69156f3326dd34ee043681
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           redland
Version:        1.0.17
Release:        41%{?dist}
Summary:        RDF Application Framework

License:        LGPL-2.1-or-later OR Apache-2.0
URL:            http://librdf.org/
Source0:        http://download.librdf.org/source/%{name}-%{version}.tar.gz

Patch1:         0001-rhbz-1936659-stub-deprecated.patch

BuildRequires:  make
BuildRequires:  curl-devel
BuildRequires:  gcc-c++
BuildRequires:  gtk-doc
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  libxml2-devel >= 2.4.0
BuildRequires:  perl-interpreter
BuildRequires:  raptor2-devel 
BuildRequires:  rasqal-devel >= 0.9.26
BuildRequires:  sqlite-devel

%if ! 0%{?rhel}
BuildRequires:  libpq-devel
BuildRequires:  mariadb-connector-c-devel
%endif

%if 0%{?rhel}
Obsoletes: redland-mysql < 1.0.17-24
Obsoletes: redland-pgsql < 1.0.17-24
%endif
# can probably omit soon (f28 or f29?) -- rex
Obsoletes: redland-virtuoso < 1.0.17-8

%description
Redland is a library that provides a high-level interface for RDF
(Resource Description Framework) implemented in an object-based API.
It is modular and supports different RDF/XML parsers, storage
mechanisms and other elements. Redland is designed for applications
developers to provide RDF support in their applications as well as
for RDF developers to experiment with the technology.

%package         devel
Summary:         Libraries and header files for programs that use Redland
Requires:        %{name}%{?_isa} = %{version}-%{release}
%description     devel
Header files for development with Redland.

%if ! 0%{?rhel}
%package         mysql
Summary:         MySQL storage support for Redland
Requires:        %{name}%{?_isa} = %{version}-%{release}
%description     mysql
This package provides Redland's storage support for graphs in memory and
persistently with MySQL files or URIs.

%package         pgsql
Summary:         PostgreSQL storage support for Redland
Requires:        %{name}%{?_isa} = %{version}-%{release}
%description     pgsql
This package provides Redland's storage support for graphs in memory and
persistently with PostgreSQL files or URIs.
%endif

%prep
%oreon_verify_sources
%setup -q
%if 0%{?rhel}
%patch -P1 -p1 -b .stub-deprecated
%endif

NOCONFIGURE=1 ./autogen.sh

# hack to nuke rpaths
%if "%{_libdir}" != "/usr/lib"
sed -i -e 's|"/lib /usr/lib|"/%{_lib} %{_libdir}|' configure
%endif


%build

%if 0%{?rhel}
%define distrooptions --disable-digests --without-mysql --without-postgresql
%else
# fedora
%define distrooptions --with-mysql --with-postgresql
%endif

export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%configure \
  --enable-release \
  --disable-static \
  --with-sqlite \
  --without-bdb \
  --without-threestone \
  --without-virtuoso \
  %{distrooptions} \

%make_build


%install
%make_install

#unpackaged files
find $RPM_BUILD_ROOT -name \*.la -exec rm -v {} \;


%check
make check


%ldconfig_scriptlets

%files
%doc AUTHORS NEWS README
%doc NOTICE TODO
%doc FAQS.html LICENSE.html NEWS.html README.html TODO.html
%license COPYING COPYING.LIB LICENSE.txt LICENSE-2.0.txt
%{_libdir}/librdf.so.0*
%{_bindir}/rdfproc
%{_bindir}/redland-db-upgrade
%dir %{_datadir}/redland
%{_mandir}/man1/redland-db-upgrade.1*
%{_mandir}/man1/rdfproc.1*
%{_mandir}/man3/redland.3*
%dir %{_libdir}/redland
%{_libdir}/redland/librdf_storage_sqlite.so
%if ! 0%{?rhel}
%{_datadir}/redland/mysql-v1.ttl
%{_datadir}/redland/mysql-v2.ttl
%endif

%if ! 0%{?rhel}
%files mysql
%{_libdir}/redland/librdf_storage_mysql.so

%files pgsql
%{_libdir}/redland/librdf_storage_postgresql.so
%endif

%files devel
%doc ChangeLog RELEASE.html
%{_bindir}/redland-config
%{_datadir}/redland/Redland.i
%{_datadir}/gtk-doc/
%{_includedir}/redland.h
%{_includedir}/librdf.h
%{_includedir}/rdf_*.h
%{_libdir}/librdf.so
%{_libdir}/pkgconfig/redland.pc
%{_mandir}/man1/redland-config.1*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.17-41
- Prepare for Oreon 11 (RP1)
