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
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%{upstream}/5.2/%{upstream}-%{version}.tar.xz
Patch1:         0001-mdb-provider-Remove-no-op-mdb_init-and-mdb_exit-call.patch
Patch2:         0002-mdb-provider-Store-filename-used-to-open-the-DB-in-o.patch
Patch3:         0003-mdb-provider-Pass-MdbHandle-to-the-mdb_set_date_fmt-.patch
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
%{?with_bdb:BuildRequires:    libdb-devel}
%{?with_ldap:BuildRequires:    openldap-devel}
%{?with_mysql:BuildRequires:    mariadb-connector-c-devel}
%{?with_postgres:BuildRequires:    libpq-devel}
%{?with_mdb:BuildRequires:    mdbtools-devel}
%{?with_java:BuildRequires:    java-devel >= 1:1.6.0}
# oreon:deps
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  glade-devel
BuildRequires:  glib2-devel
BuildRequires:  gnome-common
BuildRequires:  gobject-introspection-devel
BuildRequires:  goocanvas2-devel
BuildRequires:  graphviz-devel
BuildRequires:  gtk-doc
BuildRequires:  gtk3-devel
BuildRequires:  gtksourceview3-devel
BuildRequires:  intltool
BuildRequires:  iso-codes-devel
BuildRequires:  itstool
BuildRequires:  json-glib-devel
BuildRequires:  libdb-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libgee-devel
BuildRequires:  libpq-devel
BuildRequires:  libsecret-devel
BuildRequires:  libsoup-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  make
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  mdbtools-devel
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel
BuildRequires:  perl(XML::Parser)
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  sqlite-devel
BuildRequires:  vala
BuildRequires:  yelp-tools
# /oreon:deps
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

%if 0%{with java}
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
%ifarch sparcv9
%global archinstall sparc
%endif
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libgda5-devel -f %{oreon_filedir}/libgda5-devel.list
%files -n libgda5-ui -f %{oreon_filedir}/libgda5-ui.list
%files -n libgda5-ui-devel -f %{oreon_filedir}/libgda5-ui-devel.list
%files -n libgda5-tools -f %{oreon_filedir}/libgda5-tools.list
%files -n libgda5-sqlite -f %{oreon_filedir}/libgda5-sqlite.list
%files -n libgda5-bdb -f %{oreon_filedir}/libgda5-bdb.list
%files -n libgda5-ldap -f %{oreon_filedir}/libgda5-ldap.list
%files -n libgda5-sqlcipher -f %{oreon_filedir}/libgda5-sqlcipher.list
%files -n libgda5-web -f %{oreon_filedir}/libgda5-web.list
%files -n libgda5-mysql -f %{oreon_filedir}/libgda5-mysql.list
%files -n libgda5-postgres -f %{oreon_filedir}/libgda5-postgres.list
%files -n libgda5-mdb -f %{oreon_filedir}/libgda5-mdb.list

%changelog

%autochangelog
