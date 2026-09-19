%global source0_hash 6f6cdf7b8053f553b907e0c88a6064eb48cf2751852eb24323dcf027792334c8

%bcond_without bdb
%bcond_without ldap
%bcond_without mysql
%bcond_without postgres
%bcond_without mdb
%ifarch %{java_arches}
%bcond_without java
%else
%bcond_with java
%endif

%global apiver  5.0
%global libgda4_obsoletes_version 1:4.2.13-3
%global upstream libgda

Name:           libgda5
Epoch:          1
Version:        5.2.10
Release:        27%{?dist}
Summary:        Library for writing gnome database programs

License:        LGPL-2.1-or-later
URL:            http://www.gnome-db.org/
Source:         http://ftp.gnome.org/pub/GNOME/sources/%{upstream}/5.2/%{upstream}-%{version}.tar.xz

# Patches for building against mdbtools >= 0.9.0
# https://gitlab.gnome.org/GNOME/libgda/-/merge_requests/178
Patch1:         0001-mdb-provider-Remove-no-op-mdb_init-and-mdb_exit-call.patch
Patch2:         0002-mdb-provider-Store-filename-used-to-open-the-DB-in-o.patch
Patch3:         0003-mdb-provider-Pass-MdbHandle-to-the-mdb_set_date_fmt-.patch
# Upstream fix commit 9859479884fad5f39e6c37e8995e57c28b11b1b9
Patch4:         libgda-5.2.10-mysql-bool-fix.patch
Patch5:         bebdffb4de586fb43fd07ac549121f4b22f6812d.patch
Patch6:         libgda5-configure-c99.patch
Patch7:         libgda5-gtksourceview-c99.patch
Patch8:         libgda5-configure-c99-2.patch
Patch9:         libgda5-c99-2.patch
Patch10:        libgda5-c99-3.patch
Patch11:        libgda5-c99-4.patch
Patch12:        pointer-types.patch
Patch13:        types.patch
Patch14:        gettext.patch

BuildRequires:    gcc
BuildRequires:    gcc-c++
BuildRequires:    pkgconfig >= 0.8
BuildRequires:    glade-devel
BuildRequires:    glib2-devel >= 2.28.0
BuildRequires:    gtk3-devel >= 3.0.0
BuildRequires:    gtksourceview3-devel
BuildRequires:    goocanvas2-devel
BuildRequires:    graphviz-devel >= 2.26.0
BuildRequires:    iso-codes-devel
BuildRequires:    itstool
BuildRequires:    libxslt-devel >= 1.0.9
BuildRequires:    sqlite-devel >= 3.10.2
BuildRequires:    libgcrypt-devel
BuildRequires:    libgee-devel
BuildRequires:    gobject-introspection-devel >= 0.6.5
BuildRequires:    libxml2-devel readline-devel json-glib-devel
BuildRequires:    gtk-doc intltool gettext-devel flex bison perl(XML::Parser)
BuildRequires:    libsecret-devel
BuildRequires:    libsoup-devel
BuildRequires:    openssl-devel
BuildRequires:    yelp-tools
BuildRequires:    vala
BuildRequires:    make
BuildRequires:    gnome-common
%{?with_bdb:BuildRequires:    libdb-devel}
%{?with_ldap:BuildRequires:    openldap-devel}
%{?with_mysql:BuildRequires:    mariadb-connector-c-devel}
%{?with_postgres:BuildRequires:    libpq-devel}
%{?with_mdb:BuildRequires:    mdbtools-devel}
%{?with_java:BuildRequires:    java-devel >= 1:1.6.0}

%description
%{upstream} is a library that eases the task of writing Gtk3-based database
programs.

%package        devel
Summary:        Development files for %{upstream}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:      libgda-java-devel < %{libgda4_obsoletes_version}
Obsoletes:      libgda-ldap-devel < %{libgda4_obsoletes_version}
Obsoletes:      libgda-mdb-devel < %{libgda4_obsoletes_version}
Obsoletes:      libgda-mysql-devel < %{libgda4_obsoletes_version}
Obsoletes:      libgda-postgres-devel < %{libgda4_obsoletes_version}
Obsoletes:      libgda-sqlcipher-devel < %{libgda4_obsoletes_version}
Obsoletes:      libgda-sqlite-devel < %{libgda4_obsoletes_version}
Obsoletes:      libgda-web-devel < %{libgda4_obsoletes_version}

%description    devel
The %{upstream}-devel package contains libraries and header files for
developing applications that use %{upstream}.

%package ui
Summary:         UI extensions for %{upstream}
Requires:        %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description ui
%{upstream}-ui extends %{upstream} providing graphical widgets (Gtk+).

%package        ui-devel
Summary:        Development files for %{upstream}-ui
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       %{name}-ui%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       gtk3-devel%{?_isa} >= 3.0.0

%description    ui-devel
The %{upstream}-ui-devel package contains libraries and header files for
developing applications that use %{upstream}-ui.

%package tools
Summary:         Graphical tools for %{upstream}
Requires:        %{name}-ui%{?_isa} = %{epoch}:%{version}-%{release}

%description tools
This %{upstream}-tools package provides graphical tools for %{upstream}.

%package sqlite
Summary:        SQLite provider for %{upstream}
Requires:       %{name}%{?isa} = %{epoch}:%{version}-%{release}
Requires:       sqlite-libs%{?isa} >= 3.10.2

%description sqlite
This %{upstream}-sqlite includes the %{upstream} SQLite provider.

%if 0%{with bdb}
%package bdb
Summary:        Berkeley DB provider for %{upstream}
Requires:       %{name}%{?isa} = %{epoch}:%{version}-%{release}

%description bdb
This %{upstream}-bdb includes the %{upstream} Berkeley DB provider.
%endif

%if 0%{with ldap}
%package ldap
Summary:        Ldap provider for %{upstream}
Requires:       %{name}%{?isa} = %{epoch}:%{version}-%{release}

%description ldap
This %{upstream}-ldap includes the %{upstream} Ldap provider.
%endif

%package sqlcipher
Summary:        SQLiteCipher provider for %{upstream}
Requires:       %{name}%{?isa} = %{epoch}:%{version}-%{release}

%description sqlcipher
This %{upstream}-sqlcipher includes the %{upstream} SQLiteCipher provider.
%package web
Summary:        Web provider for %{upstream}
Requires:       %{name}%{?isa} = %{epoch}:%{version}-%{release}

%description web
This %{upstream}-web includes the %{upstream} Web provider.

%if 0%{with mysql}
%package mysql
Summary:        Mysql provider for %{upstream}
Requires:       %{name}%{?isa} = %{epoch}:%{version}-%{release}

%description mysql
This %{upstream}-mysql includes the %{upstream} Mysql provider.
%endif

%if 0%{with postgres}
%package postgres
Summary:        Postgres provider for %{upstream}
Requires:       %{name}%{?isa} = %{epoch}:%{version}-%{release}

%description postgres
This %{upstream}-postgres includes the %{upstream} PostgreSQL provider.
%endif

%if 0%{with mdb}
%package mdb
Summary:        Mdb provider for %{upstream}
Requires:       %{name}%{?isa} = %{epoch}:%{version}-%{release}

%description mdb
This %{upstream}-mdb includes the %{upstream} Mdb provider.
%endif

%if 0%{with java}
%package java
Summary:        Java provider for %{upstream}
Requires:       %{name}%{?isa} = %{epoch}:%{version}-%{release}

%description java
This %{upstream}-java includes the %{upstream} Java JDBC provider.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{upstream}-%{version}
# Workaround to detect JRE 17 (java 17)
sed -i.java m4/java.m4 \
	-e 's|JRE11\.0\.|JRE[[1-9]][[0-9]]|' -e 's|Sun JRE 11.0|Sun \$JVERSION|'
NOCONFIGURE=1 srcdir=. gnome-autogen.sh

# AUTHORS not in UTF-8
iconv --from=ISO-8859-1 --to=UTF-8 AUTHORS > AUTHORS.new && \
touch -r AUTHORS AUTHORS.new && mv AUTHORS.new AUTHORS

%build
# set LD_LIBRARY_PATH manually since it fails to find libjvm with java7
%if 0%{with java}
# this list should match the setup in java-1.7.0-openjdk.spec
# or getsp.java should be fixed
%ifarch x86_64
%global archinstall amd64
%endif
%ifarch %{ix86}
%global archinstall i386
%endif
%ifarch ppc
%global archinstall ppc
%endif
%ifarch ppc64
%global archinstall ppc64
%endif
%ifarch ppc64le
%global archinstall ppc64le
%endif
%ifarch ia64
%global archinstall ia64
%endif
%ifarch s390
%global archinstall s390
%endif
%ifarch s390x
%global archinstall s390x
%endif
%ifarch %{arm}
%global archinstall arm
%endif
# 32 bit sparc, optimized for v9
%ifarch sparcv9
%global archinstall sparc
%endif
# 64 bit sparc
%ifarch sparc64
%global archinstall sparcv9
%endif
%ifarch aarch64
%global archinstall aarch64
%endif
export LD_LIBRARY_PATH=%{_jvmdir}/java/jre/lib/%{archinstall}/server:$LD_LIBRARY_PATH
%endif
export CFLAGS="$CFLAGS -std=gnu17"
export CXXFLAGS="$CXXFLAGS -std=gnu17"
%configure --disable-static --enable-vala \
           --with-libsoup  --with-gnome-keyring \
           --with-ui --with-gtksourceview \
           --with-goocanvas --with-graphviz \
           --enable-system-sqlite=yes \
           %{?with_bdb:--with-bdb=%{_prefix} --with-bdb-libdir-name=%{_lib}} \
           %{!?with_ldap:--with-ldap=no} \
           %{!?with_mysql:--with-mysql=no} \
           %{!?with_postgres:--with-postgresql=no} \
           %{!?with_mdb:--with-mdb=no} \
           %{!?with_java:--with-java=no}
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm %{buildroot}/%{_sysconfdir}/%{upstream}-%{apiver}/sales_test.db

%find_lang libgda-5.0
%find_lang gda-browser --with-gnome

%files -f libgda-5.0.lang
%license COPYING
%doc AUTHORS ChangeLog README NEWS
%dir %{_sysconfdir}/%{upstream}-%{apiver}/
%config(noreplace) %{_sysconfdir}/%{upstream}-%{apiver}/config
%{_libdir}/%{upstream}-%{apiver}.so.*
%{_libdir}/%{upstream}-report-%{apiver}.so.*
%{_libdir}/%{upstream}-xslt-%{apiver}.so.*
%dir %{_libdir}/%{upstream}-%{apiver}/
%dir %{_libdir}/%{upstream}-%{apiver}/plugins/
%dir %{_libdir}/%{upstream}-%{apiver}/providers/
%{_libdir}/girepository-1.0/Gda-%{apiver}.typelib
%{_mandir}/man1/*
%dir %{_datadir}/%{upstream}-%{apiver}/
%dir %{_datadir}/%{upstream}-%{apiver}/dtd/
%{_datadir}/%{upstream}-%{apiver}/dtd/libgda-*.dtd
%{_datadir}/%{upstream}-%{apiver}/import_encodings.xml
%{_datadir}/%{upstream}-%{apiver}/information_schema.xml

%files devel
%dir %{_datadir}/gtk-doc/
%dir %{_datadir}/gtk-doc/html/
%doc %{_datadir}/gtk-doc/html/%{upstream}-%{apiver}
%{_datadir}/gir-1.0/Gda-%{apiver}.gir
%dir %{_includedir}/%{upstream}-%{apiver}/
%{_includedir}/%{upstream}-%{apiver}/%{upstream}
%{_includedir}/%{upstream}-%{apiver}/%{upstream}-xslt
%{_includedir}/%{upstream}-%{apiver}/%{upstream}-report
%{_libdir}/%{upstream}-%{apiver}.so
%{_libdir}/%{upstream}-report-%{apiver}.so
%{_libdir}/%{upstream}-xslt-%{apiver}.so
%{_libdir}/pkgconfig/%{upstream}-%{apiver}.pc
%{_libdir}/pkgconfig/%{upstream}-*-%{apiver}.pc
%exclude %{_libdir}/pkgconfig/%{upstream}-ui-%{apiver}.pc
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libgda-%{apiver}.vapi

%files ui
%{_libdir}/%{upstream}-ui-%{apiver}.so.*
%{_libdir}/%{upstream}-%{apiver}/plugins/*.xml
%{_libdir}/%{upstream}-%{apiver}/plugins/%{upstream}-ui-plugins.so
%{_libdir}/girepository-1.0/Gdaui-%{apiver}.typelib
%{_datadir}/%{upstream}-%{apiver}/pixmaps
%{_datadir}/%{upstream}-%{apiver}/dtd/gdaui-layout.dtd
%{_datadir}/%{upstream}-%{apiver}/ui/
%{_datadir}/%{upstream}-%{apiver}/icons/
%{_datadir}/%{upstream}-%{apiver}/server_operation.glade
%{_datadir}/%{upstream}-%{apiver}/language-specs/gda-sql.lang

%files ui-devel
%{_includedir}/%{upstream}-%{apiver}/%{upstream}-ui
%{_libdir}/%{upstream}-ui-%{apiver}.so
%{_bindir}/gdaui-demo-%{apiver}
%{_libdir}/pkgconfig/%{upstream}-ui-%{apiver}.pc
%{_datadir}/%{upstream}-%{apiver}/demo/
%{_datadir}/gir-1.0/Gdaui-%{apiver}.gir
%{_datadir}/glade/
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libgda-ui-%{apiver}.vapi

%files tools -f gda-browser.lang
%doc %{_datadir}/gtk-doc/html/gda-browser/
%{_bindir}/gda-*
%{_datadir}/%{upstream}-%{apiver}/gda_trml2html
%{_datadir}/%{upstream}-%{apiver}/gda_trml2pdf
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/gda-browser-%{apiver}.desktop
%{_datadir}/applications/gda-control-center-%{apiver}.desktop
%{_datadir}/pixmaps/gda-browser-5.0.png
%{_datadir}/icons/hicolor/*

%files sqlite
%{_libdir}/%{upstream}-%{apiver}/providers/%{upstream}-sqlite.so
%{_datadir}/%{upstream}-%{apiver}/sqlite_specs*.xml

%if 0%{with bdb}
%files bdb
%{_libdir}/libgda-%{apiver}/providers/libgda-bdb.so
%{_datadir}/%{upstream}-%{apiver}/bdb_specs*.xml
%endif

%if 0%{with ldap}
%files ldap
%{_libdir}/%{upstream}-%{apiver}/providers/%{upstream}-ldap.so
%{_datadir}/%{upstream}-%{apiver}/ldap_specs*.xml
%endif

%files sqlcipher
%{_libdir}/%{upstream}-%{apiver}/providers/%{upstream}-sqlcipher.so
%{_datadir}/%{upstream}-%{apiver}/sqlcipher_specs*.xml

%files web
%{_libdir}/%{upstream}-%{apiver}/providers/%{upstream}-web.so
%{_datadir}/%{upstream}-%{apiver}/php/
%{_datadir}/%{upstream}-%{apiver}/web/
%{_datadir}/%{upstream}-%{apiver}/web_specs*.xml

%if 0%{with mysql}
%files mysql
%{_libdir}/libgda-%{apiver}/providers/libgda-mysql.so
%{_datadir}/%{upstream}-%{apiver}/mysql_specs*.xml
%endif

%if 0%{with postgres}
%files postgres
%{_libdir}/libgda-%{apiver}/providers/libgda-postgres.so
%{_datadir}/%{upstream}-%{apiver}/postgres_specs*.xml
%endif

%if 0%{with mdb}
%files mdb
%{_libdir}/libgda-%{apiver}/providers/libgda-mdb.so
%{_datadir}/%{upstream}-%{apiver}/mdb_specs*.xml
%endif

%if 0%{with java}
%files java
%{_libdir}/libgda-%{apiver}/providers/%{upstream}-jdbc.so
%{_libdir}/libgda-%{apiver}/providers/gdaprovider-%{apiver}.jar
%{_datadir}/%{upstream}-%{apiver}/jdbc_specs*.xml
%endif

%changelog
%autochangelog
