%global source0_hash 995f4b420e666da5c8bac9faf55e7aedbe3789c525d634720a53be3ccf27a670
%global apiver  6.0
Name:           libgda
Epoch:          1
Version:        6.0.0
Release:        14%{?dist}
Summary:        Library for writing gnome database programs
License:        LGPL-2.0-or-later
URL:            http://www.gnome-db.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%{name}/6.0/%{name}-%{version}.tar.xz
Patch0:         mariadb.patch
Patch1:         signed-int.patch
Patch2:         libgda-fix-build-order.patch
Provides: %{name}-bdb%{?_isa} = 1:%{version}-%{release}
Obsoletes: %{name}-bdb <= 1:5.2.10-4
Provides: %{name}-ldap%{?_isa} = 1:%{version}-%{release}
Obsoletes: %{name}-ldap <= 1:5.2.10-4
Provides: %{name}-sqlcipher%{?_isa} = 1:%{version}-%{release}
Obsoletes: %{name}-sqlcipher <= 1:5.2.10-4
Provides: %{name}-mdb%{?_isa} = 1:%{version}-%{release}
Obsoletes: %{name}-mdb <= 1:5.2.10-4
Provides: %{name}-java%{?_isa} = 1:%{version}-%{release}
Obsoletes: %{name}-java <= 1:5.2.10-4
Provides: %{name}-web%{?_isa} = 1:%{version}-%{release}
Obsoletes: %{name}-web <= 1:5.2.10-4
# oreon:deps
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
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
BuildRequires:  libgcrypt-devel
BuildRequires:  libgee-devel
BuildRequires:  libpq-devel
BuildRequires:  libsecret-devel
BuildRequires:  libsoup-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  make
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  meson
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel
BuildRequires:  perl(XML::Parser)
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  sqlcipher-devel
BuildRequires:  sqlite-devel
BuildRequires:  vala
BuildRequires:  yelp-tools
# /oreon:deps
%description
%{name} is a library that eases the task of writing Gtk3-based database
programs.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package ui
Summary:         UI extensions for %{name}
Requires:        %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%description ui
%{name}-ui extends %{name} providing graphical widgets (Gtk+).

%package        ui-devel
Summary:        Development files for %{name}-ui
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       %{name}-ui%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       gtk3-devel%{?_isa} >= 3.0.0
%description    ui-devel
The %{name}-ui-devel package contains libraries and header files for
developing applications that use %{name}-ui.

%package tools
Summary:         Graphical tools for %{name}
Requires:        %{name}-ui%{?_isa} = %{epoch}:%{version}-%{release}
%description tools
This %{name}-tools package provides graphical tools for %{name}.

%package sqlite
Summary:        SQLite provider for %{name}
Requires:       %{name}%{?isa} = %{epoch}:%{version}-%{release}
Requires:       sqlite-libs%{?isa} >= 3.22.0
%description sqlite
This %{name}-sqlite includes the %{name} SQLite provider.

%package sqlcipher
Summary:        SQLiteCipher provider for %{name}
Requires:       %{name}%{?isa} = %{epoch}:%{version}-%{release}
%description sqlcipher
This %{name}-sqlcipher includes the %{name} SQLiteCipher provider.

%package mysql
Summary:        Mysql provider for %{name}
Requires:       %{name}%{?isa} = %{epoch}:%{version}-%{release}
%description mysql
This %{name}-mysql includes the %{name} Mysql provider.

%package postgres
Summary:        Postgres provider for %{name}
Requires:       %{name}%{?isa} = %{epoch}:%{version}-%{release}
%description postgres
This %{name}-postgres includes the %{name} PostgreSQL provider.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
NOCONFIGURE=1 srcdir=. gnome-autogen.sh

# AUTHORS not in UTF-8
iconv --from=ISO-8859-1 --to=UTF-8 AUTHORS > AUTHORS.new && \
touch -r AUTHORS AUTHORS.new && mv AUTHORS.new AUTHORS

%build

%meson -Djson=true -Dldap=true -Ddoc=false -Dexperimental=true -Dhelp=true -Dui=true -Dlibsoup=true -Dlibsecret=true -Dflatpak=false -Dsqlcipher=true -Dgraphviz=true
%meson_build
%install
%meson_install
mkdir -p %{buildroot}%{_sysconfdir}/%{name}-%{apiver}/
install data/config %{buildroot}%{_sysconfdir}/%{name}-%{apiver}/config
install libgda-ui/data/import_encodings.xml %{buildroot}%{_datadir}/%{name}-%{apiver}/import_encodings.xml
%find_lang libgda-6.0
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libgda-devel -f %{oreon_filedir}/libgda-devel.list
%files -n libgda-ui -f %{oreon_filedir}/libgda-ui.list
%files -n libgda-ui-devel -f %{oreon_filedir}/libgda-ui-devel.list
%files -n libgda-tools -f %{oreon_filedir}/libgda-tools.list
%files -n libgda-sqlite -f %{oreon_filedir}/libgda-sqlite.list
%files -n libgda-sqlcipher -f %{oreon_filedir}/libgda-sqlcipher.list
%files -n libgda-mysql -f %{oreon_filedir}/libgda-mysql.list
%files -n libgda-postgres -f %{oreon_filedir}/libgda-postgres.list

%changelog

%autochangelog
