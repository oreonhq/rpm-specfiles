%global source0_hash d488089a64ee4060bce7dbba0291fcca358e7f7ac5230e2ee5b344e7485729c4
%global source3_hash 1217a0212aaa143e44831849d1845b198f248923d7e96634219d3369a6ec8714

%{!?javabuild:%global javabuild 0}
%{!?utils:%global utils 1}
%{!?gcj_support:%global gcj_support 0}
%{!?upgrade:%global upgrade 1}
%{!?upgrade_prev:%global upgrade_prev 0}
%{!?runselftest:%global runselftest 1}
%{!?llvmjit:%global llvmjit 0}

%{!?postgresql_default:%global postgresql_default 1}
%global        pgversion 18

%global        majorversion 3.6
%global        soversion 3
%global        prevmajorversion 2.5
%global        prevversion %{prevmajorversion}.5
%global        so_files postgis postgis_topology rtpostgis
%global        configure_opts --disable-rpath --enable-raster

%global        __provides_exclude_from %{_libdir}/pgsql

Name:          postgresql%{pgversion}-postgis
Version:       3.6.2
Release:       1%{?dist}
Summary:       Geographic Information Systems Extensions to PostgreSQL
License:       GPL-2.0-or-later

URL:           https://www.postgis.net
Source0:        https://download.osgeo.org/postgis/source/postgis-%{version}.tar.gz
Source2:        https://download.osgeo.org/postgis/docs/postgis-%{version}-en.pdf
%if %upgrade_prev
Source3:        https://download.osgeo.org/postgis/source/postgis-2.5.5.tar.gz

# Add proj8 compatibility to postgis-2.x (needed for upgrade package)
Patch1:        postgis2-proj8.patch
Patch2:	       postgis-c99.patch
Patch3:	       postgis-c99-2.patch
%endif

%if %{?postgresql_default}
%global pkgname postgis
%package -n postgis
Summary: Open-source vector similarity search for Postgres
%else
%global pkgname %name
%endif

%if 0%{?fedora}
BuildRequires: SFCGAL-devel
BuildRequires: gtk2-devel
%endif

BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: byacc
BuildRequires: clang
BuildRequires: desktop-file-utils
BuildRequires: docbook-dtds
BuildRequires: flex
BuildRequires: gcc-c++
BuildRequires: gdal-devel >= 1.10.0
BuildRequires: geos-devel >= 3.7.1
BuildRequires: json-c-devel
BuildRequires: libtool
BuildRequires: libxml2-devel
BuildRequires: libxslt
BuildRequires: llvm
BuildRequires: pcre2-devel
BuildRequires: perl-generators
BuildRequires: postgresql%{pgversion}-server-devel
BuildRequires: proj-devel >= 5.2.0
BuildRequires: protobuf-c-devel

%if %upgrade
BuildRequires: postgresql%{pgversion}-upgrade-devel
%endif

%if %runselftest
%if %{?postgresql_default}
BuildRequires: postgresql-test-rpm-macros
%else
BuildRequires: postgresql%{pgversion}-test-rpm-macros
%endif
%endif

%if %llvmjit
Requires:  clang-devel llvm-devel
%endif


%if %{?postgresql_default}
Provides:  postgresql-postgis = %{version}-%{release}
Provides:  %name = %{version}-%{release}
%endif
Provides:  %{pkgname}%{?_isa} = %{version}-%{release}
Provides:  %{pkgname} = %{version}-%{release}
Provides:  postgis-any
Conflicts: postgis-any


%description
PostGIS adds support for geographic objects to the PostgreSQL object-relational
database. In effect, PostGIS "spatially enables" the PostgreSQL server,
allowing it to be used as a backend spatial database for geographic information
systems (GIS), much like ESRI's SDE or Oracle's Spatial extension. PostGIS
follows the OpenGIS "Simple Features Specification for SQL" and has been
certified as compliant with the "Types and Functions" profile.

%description -n %{pkgname}
PostGIS adds support for geographic objects to the PostgreSQL object-relational
database. In effect, PostGIS "spatially enables" the PostgreSQL server,
allowing it to be used as a backend spatial database for geographic information
systems (GIS), much like ESRI's SDE or Oracle's Spatial extension. PostGIS
follows the OpenGIS "Simple Features Specification for SQL" and has been
certified as compliant with the "Types and Functions" profile.


%if %llvmjit
%package -n %{pkgname}-llvmjit
Summary:       Just-in-time compilation support for PostGIS
Requires:      %{pkgname}%{?_isa} = %{version}-%{release}

%description -n %{pkgname}-llvmjit
Just-in-time compilation support for PostGIS.
%endif

%package -n %{pkgname}-docs
Summary:       Extra documentation for PostGIS

%description -n %{pkgname}-docs
The postgis-docs package includes PDF documentation of PostGIS.


%if %javabuild
%package -n %{pkgname}-jdbc
Summary:       The JDBC driver for PostGIS
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:       LicenseRef-Callaway-LGPLv2+
Requires:      %{pkgname}%{?_isa} = %{version}-%{release}
Requires:      postgresql-jdbc
BuildRequires: ant >= 0:1.6.2
BuildRequires: java-devel
BuildRequires: junit >= 0:3.7
BuildRequires: postgresql-jdbc

%if %{gcj_support}
BuildRequires: gcc-java
BuildRequires: java-1.5.0-gcj-devel
Requires(post): %{_bindir}/rebuild-gcj-db
Requires(postun): %{_bindir}/rebuild-gcj-db
%endif

%description -n %{pkgname}-jdbc
The postgis-jdbc package provides the essential jdbc driver for PostGIS.
%endif


%if %utils
%package -n %{pkgname}-utils
Summary:       The utils for PostGIS
Requires:      %{pkgname}%{?_isa} = %{version}-%{release}
Requires:      perl-DBD-Pg

%description -n %{pkgname}-utils
The postgis-utils package provides the utilities for PostGIS.
%endif


%if %upgrade
%package -n %{pkgname}-upgrade
Summary:       Support for upgrading Postgis
Requires:      %{pkgname}%{?_isa} = %{version}-%{release}
Requires:      postgresql%{pgversion}-upgrade
Provides:      bundled(postgis) = %prevversion

%description -n %{pkgname}-upgrade
%if %upgrade_prev
The postgis-upgrade package contains the previous version of Postgis as well as
the current version of Postgis built against the previous version of PostgreSQL
necessary for correct dump of schema from previous version of PostgreSQL.
%else
The postgis-upgrade package contains the current version of Postgis built against
the previous version of PostgreSQL necessary for correct dump of schema from previous
version of PostgreSQL.
%endif
%endif

%if 0%{?fedora}
%package -n %{pkgname}-gui
Summary:       The shp2pgsql-gui utility for PostGIS
Requires:      %{pkgname}%{?_isa} = %{version}-%{release}

%description -n %{pkgname}-gui
The gui package provides shp2pgsql-gui for PostGIS.
%endif

%package -n %{pkgname}-client
Summary:       The CLI clients for PostGIS
Requires:      %{pkgname}%{?_isa} = %{version}-%{release}

%description -n %{pkgname}-client
The client package provides shp2pgsql, raster2pgsql and pgsql2shp for PostGIS.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source3_hash}" = "none" || { f="%{SOURCE3}"; test -f "$f" || { echo "oreon: missing Source3 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source3_hash}" || { echo "oreon: Source3 hash mismatch" >&2; exit 1; }; }
%if %upgrade_prev
%setup -q -n postgis-%{version} -a 3
%else
%setup -q -n postgis-%{version}
%endif

%if %upgrade
(
tar xf %{SOURCE0}

%if %upgrade_prev
cd postgis-%{prevversion}
%patch -P 1 -p1
%patch -P 2 -p2
%patch -P 3 -p1
./autogen.sh
%endif
)
%endif
cp -p %{SOURCE2} .


%build
%configure %configure_opts --with-pgconfig=%{_bindir}/pg_server_config \
%if %llvmjit
	--with-llvm \
%endif
%if 0%{?fedora}
	--with-sfcgal \
	--with-gui
%endif

sed -i 's| -fstack-clash-protection | |' postgis/Makefile
sed -i 's| -fstack-clash-protection | |' raster/rt_pg/Makefile
sed -i 's| -fstack-clash-protection | |' topology/Makefile
sed -i 's| -fstack-clash-protection | |' extensions/address_standardizer/Makefile
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%if %javabuild
export BUILDXML_DIR=%{_builddir}/postgis-%{version}/java/jdbc
JDBC_VERSION_RPM=`rpm -ql postgresql-jdbc| grep 'jdbc2.jar$'|awk -F '/' '{print $5}'`
sed 's/postgresql.jar/'${JDBC_VERSION_RPM}'/g' $BUILDXML_DIR/build.xml > $BUILDXML_DIR/build.xml.new
mv -f $BUILDXML_DIR/build.xml.new $BUILDXML_DIR/build.xml
pushd java/jdbc
ant
popd
%endif

%if %utils
%make_build -C utils
%endif

%if %upgrade
(
cd postgis-%{version}

# Build current Postgis version against the previous PostgreSQL version.  We need only the so names.
# We intentionally don't use %%configure here since there is too many
# pre-defined directories, and not everything from postgis-%%prevversion
# directory respects the `pg_config` output (liblwgeom especially).
./configure %configure_opts \
	--with-pgconfig=%postgresql_upgrade_prefix/bin/pg_config \
	--bindir=%postgresql_upgrade_prefix/bin \
	--libdir=%postgresql_upgrade_prefix/lib \
	--includedir=%postgresql_upgrade_prefix/include \
	--datadir=%postgresql_upgrade_prefix/share \
	--mandir=%postgresql_upgrade_prefix/share/man
sed -i 's| -fstack-clash-protection | |' postgis/Makefile
sed -i 's| -fstack-clash-protection | |' raster/rt_pg/Makefile
sed -i 's| -fstack-clash-protection | |' topology/Makefile
sed -i 's| -fstack-clash-protection | |' extensions/address_standardizer/Makefile
%make_build
)

%if %upgrade_prev
(
cd postgis-%{prevversion}

# Build previous Postgis version against the current PostgreSQL version.  We need only the so names.
%configure %configure_opts
sed -i 's| -fstack-clash-protection | |' postgis/Makefile
sed -i 's| -fstack-clash-protection | |' raster/rt_pg/Makefile
sed -i 's| -fstack-clash-protection | |' topology/Makefile
sed -i 's| -fstack-clash-protection | |' extensions/address_standardizer/Makefile
%make_build
mkdir ../compat-build
for so in %so_files; do
    find -name $so.so -exec cp {} ../compat-build/$so-%{prevmajorversion}.so \;
    find -name $so-%{prevmajorversion}.so -exec cp -t ../compat-build/ {} +
done

# Full build of previous Postgis version against previous PostgreSQL version
# We intentionally don't use %%configure here since there is too many
# pre-defined directories, and not everything from postgis-%%prevversion
# directory respects the `pg_config` output (liblwgeom especially).
./configure %configure_opts \
	--with-pgconfig=%postgresql_upgrade_prefix/bin/pg_config \
	--libdir=%postgresql_upgrade_prefix/lib \
	--includedir=%postgresql_upgrade_prefix/include
sed -i 's| -fstack-clash-protection | |' postgis/Makefile
sed -i 's| -fstack-clash-protection | |' raster/rt_pg/Makefile
sed -i 's| -fstack-clash-protection | |' topology/Makefile
sed -i 's| -fstack-clash-protection | |' extensions/address_standardizer/Makefile
%make_build
)
%endif
%endif


%install
%make_install
%make_install -C utils
%make_install -C extensions

%if %upgrade
(cd postgis-%{version} && %make_install)
%if %upgrade_prev
(cd postgis-%{prevversion} && %make_install)
%endif

# drop unused stuff from upgrade-only installation
/bin/rm -rf %buildroot%postgresql_upgrade_prefix/bin
/bin/rm -rf %buildroot%postgresql_upgrade_prefix/lib/lib*
/bin/rm -rf %buildroot%postgresql_upgrade_prefix/share

# Manually install compat-build binary.
%if %upgrade_prev
for so in %so_files; do
%{__install} -m 644 compat-build/$so-%{prevmajorversion}.so %{buildroot}/%{_libdir}/pgsql
done
%endif
%endif

rm -f  %{buildroot}%{_datadir}/*.sql

%if %javabuild
install -d %{buildroot}%{_javadir}
install -m 755 java/jdbc/postgis-%{version}.jar %{buildroot}%{_javadir}/postgis.jar
%if %{gcj_support}
aot-compile-rpm
%endif
strip %{buildroot}/%{_libdir}/gcj/postgis/*.jar.so
%endif

%if %utils
pushd utils
install -d %{buildroot}%{_datadir}/postgis
install -m 755 create_*.pl repo_revision.pl \
    postgis_restore.pl read_scripts_version.pl \
%if 0%{?fedora}
    profile_intersects.pl test_*.pl \
%endif
    %{buildroot}%{_datadir}/postgis
popd
%endif

find %buildroot \( -name '*.la' -or -name '*.a' \) -delete


%check
%if 0%{?fedora}
desktop-file-validate %{buildroot}/%{_datadir}/applications/shp2pgsql-gui.desktop
%endif
%if %runselftest
%postgresql_tests_run
export PGIS_REG_TMPDIR=`mktemp -d`
if ! LD_LIBRARY_PATH=%{buildroot}%_libdir make check %{_smp_mflags} ; then
    for file in $(find $PGIS_REG_TMPDIR -name '*_diff'); do
	echo "== $file =="
	cat "$file"
    done
fi
%endif


%if %javabuild
%if %gcj_support
%post   jdbc -p %{_bindir}/rebuild-gcj-db
%postun jdbc -p %{_bindir}/rebuild-gcj-db
%endif
%endif


%files -n %{pkgname}
%license COPYING
%doc CREDITS NEWS TODO README.postgis loader/README.* doc/postgis.xml doc/ZMSgeoms.txt

%{_libdir}/pgsql/postgis-%{soversion}.so
%{_datadir}/pgsql/contrib/postgis-%{majorversion}/*.sql
%{_datadir}/pgsql/extension/address_standardizer*.sql
%{_datadir}/pgsql/extension/address_standardizer*.control
%{_datadir}/pgsql/extension/postgis-*.sql
%{_datadir}/pgsql/extension/postgis_raster*.sql
%if 0%{?fedora}
%{_datadir}/pgsql/extension/postgis_sfcgal*.sql
%endif
%{_datadir}/pgsql/extension/postgis_topology*.sql
%{_datadir}/pgsql/extension/postgis.control
%{_datadir}/pgsql/extension/postgis_raster.control
%if 0%{?fedora}
%{_datadir}/pgsql/extension/postgis_sfcgal.control
%endif
%{_datadir}/pgsql/extension/postgis_topology.control
%{_datadir}/pgsql/extension/postgis_tiger_geocoder*.sql
%{_datadir}/pgsql/extension/postgis_tiger_geocoder.control
%{_datadir}/postgis/create_unpackaged.pl
%{_datadir}/postgis/create_skip_signatures.pl
%{_datadir}/postgis/create_spatial_ref_sys_config_dump.pl
%{_datadir}/postgis/create_uninstall.pl
%{_datadir}/postgis/repo_revision.pl
%{_libdir}/pgsql/address_standardizer-%{soversion}.so
%{_libdir}/pgsql/postgis_raster-%{soversion}.so
%if 0%{?fedora}
%{_libdir}/pgsql/postgis_sfcgal-%{soversion}.so
%endif
%{_libdir}/pgsql/postgis_topology-%{soversion}.so

%files -n %{pkgname}-client
%{_bindir}/postgis
%{_bindir}/postgis_restore
%{_bindir}/pgsql2shp
%{_bindir}/raster2pgsql
%{_bindir}/shp2pgsql
%{_bindir}/pgtopo_export
%{_bindir}/pgtopo_import
%{_mandir}/man1/pgsql2shp.1*
%{_mandir}/man1/pgtopo_export.1*
%{_mandir}/man1/pgtopo_import.1*
%{_mandir}/man1/postgis.1*
%{_mandir}/man1/postgis_restore.1*
%{_mandir}/man1/shp2pgsql.1*

%if 0%{?fedora}
%files -n %{pkgname}-gui
%{_bindir}/shp2pgsql-gui
%{_datadir}/applications/shp2pgsql-gui.desktop
%{_datadir}/icons/hicolor/*/apps/shp2pgsql-gui.png
%endif


%if %llvmjit
%files -n %{pkgname}-llvmjit
%{_libdir}/pgsql/bitcode/address_standardizer-*
%{_libdir}/pgsql/bitcode/postgis-*
%{_libdir}/pgsql/bitcode/postgis_raster-*
%if 0%{?fedora}
%{_libdir}/pgsql/bitcode/postgis_sfcgal-*
%endif
%{_libdir}/pgsql/bitcode/postgis_topology-*
%endif


%if %javabuild
%files -n %{pkgname}-jdbc
%license java/jdbc/COPYING_LGPL
%doc java/jdbc/README
%{_javadir}/postgis.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/postgis
%{_libdir}/gcj/postgis/*.jar.so
%{_libdir}/gcj/postgis/*.jar.db
%endif
%endif


%if %upgrade
%files -n %{pkgname}-upgrade
%postgresql_upgrade_prefix/*
%if %upgrade_prev
%{_libdir}/pgsql/*-%{prevmajorversion}.so
%endif
%endif


%if %utils
%files -n %{pkgname}-utils
%doc utils/README
%dir %{_datadir}/postgis/
%doc %{_datadir}/doc/pgsql/extension/README.address_standardizer
%{_datadir}/postgis/create_extension_unpackage.pl
%{_datadir}/postgis/create_or_replace_to_create.pl
%{_datadir}/postgis/create_upgrade.pl
%{_datadir}/postgis/postgis_restore.pl
%{_datadir}/postgis/read_scripts_version.pl
%if 0%{?fedora}
# requires perl(Pg)
%{_datadir}/postgis/profile_intersects.pl
%{_datadir}/postgis/test_estimation.pl
%{_datadir}/postgis/test_geography_estimation.pl
%{_datadir}/postgis/test_geography_joinestimation.pl
%{_datadir}/postgis/test_joinestimation.pl
%endif
%endif


%files -n %{pkgname}-docs
%doc postgis*.pdf


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.6.2-1
- Prepare for Oreon 11 (RP1)
