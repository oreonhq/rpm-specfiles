%global source0_hash aa4316004a5ffa969cdb927b921d9d9d7114640bba137ce736b5e3b58ed2c0d4
%global upstream_owner    AdaCore
%global upstream_name     gnatcoll-db
%global upstream_version  26.0.0
%global upstream_commit   08413b3c5f18766a3a59c0d0736ac17fa8e6d831
Name:           gnatcoll-db
Epoch:          2
Version:        %{upstream_version}
Release:        2%{?dist}
Summary:        The GNAT Components Collection – database packages
Summary(sv):    GNAT Components Collection – databaspaket
License:        GPL-3.0-or-later WITH GCC-exception-3.1 AND GPL-3.0-or-later AND GPL-2.0-or-later WITH GNAT-exception
URL:            https://github.com/%{upstream_owner}/%{upstream_name}
Source0:        https://github.com/%{upstream_owner}/%{name}/archive/%{upstream_commit}.tar.gz#/%{name}-%{version}.tar.gz
Patch:          %{name}-dborm_python3.patch
ExclusiveArch:  %{GPRbuild_arches}
# oreon:deps
BuildRequires:  fedora-gnat-project-common
BuildRequires:  gcc-gnat
BuildRequires:  gnatcoll-core-devel
BuildRequires:  gnatcoll-iconv-devel
BuildRequires:  gnatcoll-projects-devel
BuildRequires:  gprbuild
BuildRequires:  libpq-devel
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-latex
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  sed
BuildRequires:  sqlite-devel
# /oreon:deps
%description
This is the database module of the GNAT Components Collection.

%description -l sv
Detta är databasmodulen i GNAT Components Collection.

#################
## Subpackages ##
#################

%package devel
Summary:        Development metapackage for the GNAT Components Collection – database packages
Summary(sv):    Metapaket för programmering med GNAT Components Collection – databaspaket
Requires:       gnatcoll-sql-devel      = %{epoch}:%{version}-%{release}
Requires:       gnatcoll-sqlite-devel   = %{epoch}:%{version}-%{release}
Requires:       gnatcoll-postgres-devel = %{epoch}:%{version}-%{release}
Requires:       gnatcoll-xref-devel     = %{epoch}:%{version}-%{release}
Provides:       deprecated()
%description devel
Each database component of the GNAT Components Collection now has its own
development package. This meta-package exists to prevent problems when Fedora
is upgraded. It pulls in the development packages for all of the database
components.

Do not specify this package in any configurations or dependencies. Specify the
packages you actually need.

%description devel -l sv
Varje databaskomponent i GNAT Components Collection har nu ett eget
programmeringspaket. Detta metapaket är till för att undvika problem när Fedora
uppgraderas. Det drar in programmeringspaketen för alla databaskomponenterna.

Ange inte det här paketet i några konfigurationer eller beroenden. Ange paketen
du faktiskt behöver.

%package -n gnatcoll-sql
Summary:        The GNAT Components Collection – SQL component
Summary(sv):    GNAT Components Collection – SQL-komponenten
License:        GPL-3.0-or-later WITH GCC-exception-3.1
%description -n gnatcoll-sql
This is the SQL component of the GNAT Components Collection. It provides an
object-oriented, high-level interface to SQL queries.

%description -n gnatcoll-sql -l sv
Detta är SQL-komponenten i GNAT Components Collection. Den tillhandahåller ett
objektorienterat högnivågränssnitt mot SQL-frågor.

%package -n gnatcoll-sql-devel
Summary:        Development files for the GNAT Components Collection – SQL component
Summary(sv):    Filer för programmering med GNAT Components Collection – SQL-komponenten
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Provides:       gnatcoll_db2ada = %{epoch}:%{version}-%{release}
Provides:       gnatcoll_all2ada = %{epoch}:%{version}-%{release}
Requires:       gnatcoll-sql%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common gnatcoll-core-devel
Requires:       python3
Recommends:     gnatcoll-db-doc
%description -n gnatcoll-sql-devel
This package contains source code and linking information for developing
applications that use the SQL component of the GNAT Components Collection.
It provides an object-oriented, high-level interface to SQL queries.

This package also contains the tool gnatcoll_db2ada, which generates an Ada
package from a description of a database schema.

%description -n gnatcoll-sql-devel -l sv
Detta paket innehåller källkod och länkningsinformation som behövs för att
utveckla program som använder SQL-komponenten i GNAT Components Collection.
Den tillhandahåller ett objektorienterat högnivågränssnitt mot SQL-frågor.

Det här paketet innehåller också verktyget gnatcoll_db2ada som genererar ett
adapaket från en beskrivning av en databasstruktur.

%package -n gnatcoll-sqlite
Summary:        The GNAT Components Collection – SQLite support
Summary(sv):    GNAT Components Collection – stöd för SQLite
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Requires:       gnatcoll-sql%{?_isa} = %{epoch}:%{version}-%{release}
%description -n gnatcoll-sqlite
This component provides support for SQLite to the SQL component of the GNAT
Components Collection.

%description -n gnatcoll-sqlite -l sv
Den här komponenten tillhandahåller stöd för SQLite till SQL-komponenten i
GNAT Components Collection.

%package -n gnatcoll-sqlite-devel
Summary:        Development files for the GNAT Components Collection – SQLite support
Summary(sv):    Filer för programmering med GNAT Components Collection – stöd för SQLite
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Requires:       gnatcoll-sqlite%{?_isa}    = %{epoch}:%{version}-%{release}
Requires:       gnatcoll-sql-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common gnatcoll-core-devel
Recommends:     gnatcoll-db-doc
%description -n gnatcoll-sqlite-devel
This package contains source code and linking information for developing
applications that use SQLite databases through the SQL component of the
GNAT Components Collection.

%description -n gnatcoll-sqlite-devel -l sv
Detta paket innehåller källkod och länkningsinformation som behövs för att
utveckla program som använder SQLite-databaser genom SQL-komponenten i GNAT
Components Collection.

%package -n gnatcoll-postgres
Summary:        The GNAT Components Collection – PostgreSQL support
Summary(sv):    GNAT Components Collection – stöd för PostgreSQL
License:        GPL-3.0-or-later WITH GCC-exception-3.1 AND GPL-2.0-or-later WITH GNAT-exception
Requires:       gnatcoll-sql%{?_isa} = %{epoch}:%{version}-%{release}
%description -n gnatcoll-postgres
This component provides support for PostgreSQL to the SQL component of the GNAT
Components Collection.

%description -n gnatcoll-postgres -l sv
Den här komponenten tillhandahåller stöd för PostgreSQL till SQL-komponenten i
GNAT Components Collection.

%package -n gnatcoll-postgres-devel
Summary:        Development files for the GNAT Components Collection – PostgreSQL support
Summary(sv):    Filer för programmering med GNAT Components Collection – stöd för PostgreSQL
License:        GPL-3.0-or-later WITH GCC-exception-3.1 AND GPL-2.0-or-later WITH GNAT-exception
Requires:       gnatcoll-postgres%{?_isa}  = %{epoch}:%{version}-%{release}
Requires:       gnatcoll-sql-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common gnatcoll-core-devel
Recommends:     gnatcoll-db-doc
%description -n gnatcoll-postgres-devel
This package contains source code and linking information for developing
applications that use PostgreSQL databases through the SQL component of the
GNAT Components Collection.

%description -n gnatcoll-postgres-devel -l sv
Detta paket innehåller källkod och länkningsinformation som behövs för att
utveckla program som använder PostgreSQL-databaser genom SQL-komponenten i GNAT
Components Collection.

%package -n gnatcoll-xref
Summary:        The GNAT Components Collection – cross-referencing
Summary(sv):    GNAT Components Collection – korshänvisning
License:        GPL-3.0-or-later
Provides:       gnatinspect = %{epoch}:%{version}-%{release}
Requires:       gnatcoll-sql%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       gnatcoll-sqlite%{?_isa} = %{epoch}:%{version}-%{release}
%description -n gnatcoll-xref
This is the Xref component of the GNAT Components Collection. It provides
support for parsing the .ali and .gli files that are generated by GNAT and GCC.
In particular, those files contain information that can be used to do cross-
references for entities (going from references to their declaration for
instance).

This package also contains Gnatinspect, a command-line tool for building and
querying a database of cross-reference information.

%description -n gnatcoll-xref -l sv
Detta är komponenten Xref i GNAT Components Collection. Den analyserar .ali-
och .gli-filerna som GNAT och GCC producerar. I de filerna finns uppgifter som
kan användas till korshänvisning (till exempel att hitta en deklaration utifrån
en referens).

Det här paketet innehåller också Gnatinspect, ett kommandoradsverktyg för att
bygga och söka i en databas över korshänvisningar.

%package -n gnatcoll-xref-devel
Summary:        Development files for the GNAT Components Collection – cross-referencing
Summary(sv):    Filer för programmering med GNAT Components Collection – korshänvisning
License:        GPL-3.0-or-later
Requires:       gnatcoll-xref%{?_isa}         = %{epoch}:%{version}-%{release}
Requires:       gnatcoll-sql-devel%{?_isa}    = %{epoch}:%{version}-%{release}
Requires:       gnatcoll-sqlite-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common gnatcoll-core-devel gnatcoll-iconv-devel
Recommends:     gnatcoll-db-doc
%description -n gnatcoll-xref-devel
This package contains source code and linking information for developing
applications that use the Xref component of the GNAT Components Collection.
It provides support for parsing the .ali and .gli files that are generated by
GNAT and GCC. In particular, those files contain information that can be used
to do cross-references for entities (going from references to their declaration
for instance).

%description -n gnatcoll-xref-devel -l sv
Detta paket innehåller källkod och länkningsinformation som behövs för att
utveckla program som använder komponenten Xref i GNAT Components Collection.
Den analyserar .ali- och .gli-filerna som GNAT och GCC producerar. I de filerna
finns uppgifter som kan användas till korshänvisning (till exempel att hitta en
deklaration utifrån en referens).

%package doc
Summary:        Documentation for the GNAT Components Collection – database packages
Summary(sv):    Dokumentation till GNAT Components Collection – databaspaket
BuildArch:      noarch
License:        AdaCore-doc AND MIT AND BSD-2-Clause AND GPL-3.0-or-later WITH GCC-exception-3.1
Requires:       font(fontawesome)
Requires:       font(lato)
Requires:       font(robotoslab)
%description doc
This package contains the documentation for the database and Xref components of
the GNAT Components Collection.

%description doc -l sv
Detta paket innehåller dokumentationen till GNAT Components Collections
databaskomponenter och Xref.

#############
## Prepare ##
#############

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{upstream_name}-%{upstream_commit}

# Delete the bundled SQLite to be extra sure that the packaged version is used.
rm --recursive sqlite/amalgamation

###########
## Build ##
###########

%build

echo '%{version}' > ./version_information
export GNATCOLL_VERSION=%{version}
export BUILD=PROD
export LIBRARY_TYPE=relocatable
export GNATCOLL_SQLITE=external
mkdir stage  # without --parents to avoid clobbering any existing directory
for component in sql sqlite postgres xref ; do
    gprbuild %{GPRbuild_flags} \
             -aP stage%{_GNAT_project_dir} \
             -P ${component}/gnatcoll_${component}.gpr
    gprinstall --create-missing-dirs --no-manifest --no-build-var \
               --prefix=${PWD}/stage%{_prefix} \
               --sources-subdir=${PWD}/stage%{_includedir}/gnatcoll-${component} \
               --project-subdir=${PWD}/stage%{_GNAT_project_dir} \
               --ali-subdir=${PWD}/stage%{_libdir}/gnatcoll-${component} \
               --lib-subdir=${PWD}/stage%{_libdir} \
               --no-lib-link \
               -aP stage%{_GNAT_project_dir} \
               -P ${component}/gnatcoll_${component}.gpr
    ln --symbolic --force libgnatcoll_${component}.so.%{version} \
       stage%{_libdir}/libgnatcoll_${component}.so
done
gprbuild -cargs -fPIE %{GPRbuild_flags} -aP stage%{_GNAT_project_dir} \
         -P gnatinspect/gnatinspect.gpr
gprbuild -cargs -fPIE %{GPRbuild_flags} -aP stage%{_GNAT_project_dir} \
         -P gnatcoll_db2ada/gnatcoll_all2ada.gpr
make -C docs html latexpdf
%install
cp --archive stage/* --target-directory=%{buildroot}
mkdir --parents %{buildroot}%{_bindir} %{buildroot}%{_libexecdir}/gnatcoll
cp gnatinspect/obj/gnatinspect gnatcoll_db2ada/obj/gnatcoll_all2ada \
   --target-directory=%{buildroot}%{_bindir}
cp --preserve=timestamps gnatcoll_db2ada/dborm.py \
   --target-directory=%{buildroot}%{_libexecdir}/gnatcoll
%{py3_shebang_fix} %{buildroot}%{_libexecdir}/gnatcoll/dborm.py
mkdir --parents %{buildroot}%{_pkgdocdir}/html
cp --preserve=timestamps --recursive \
   docs/_build/html/* --target-directory=%{buildroot}%{_pkgdocdir}/html
mkdir --parents %{buildroot}%{_pkgdocdir}/pdf
cp --preserve=timestamps \
   docs/_build/latex/*.pdf --target-directory=%{buildroot}%{_pkgdocdir}/pdf
ln --symbolic gnatcoll_all2ada %{buildroot}%{_bindir}/gnatcoll_db2ada
for component in sql sqlite postgres xref ; do
    sed --regexp-extended --in-place \
        '--expression=1i with "directories";' \
        '--expression=/^--  This project has been generated/d' \
        '--expression=/package Linker is/,/end Linker/d' \
        '--expression=s|^( *for +Source_Dirs +use +).*;$|\1(Directories.Includedir \& "/'gnatcoll-${component}'");|i' \
        '--expression=s|^( *for +Library_Dir +use +).*;$|\1Directories.Libdir;|i' \
        '--expression=s|^( *for +Library_ALI_Dir +use +).*;$|\1Directories.Libdir \& "/'gnatcoll-${component}'";|i' \
        %{buildroot}%{_GNAT_project_dir}/gnatcoll_${component}.gpr
done
mkdir --parents %{buildroot}%{_pkgdocdir}/xref
cp --preserve=timestamps xref/README.md \
   --target-directory=%{buildroot}%{_pkgdocdir}/xref
cp --preserve=timestamps --recursive examples \
   --target-directory=%{buildroot}%{_pkgdocdir}
mkdir --parents %{buildroot}%{_licensedir}/%{name}
cp --preserve=timestamps COPYING3 COPYING.RUNTIME \
   --target-directory=%{buildroot}%{_licensedir}/%{name}
%oreon_autofiles gnatcoll-sql usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles gnatcoll-sql-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles gnatcoll-sqlite usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles gnatcoll-sqlite-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles gnatcoll-postgres usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles gnatcoll-postgres-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles gnatcoll-xref usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles gnatcoll-xref-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gnatcoll-db-devel -f %{oreon_filedir}/gnatcoll-db-devel.list
%files -n gnatcoll-sql -f %{oreon_filedir}/gnatcoll-sql.list
%files -n gnatcoll-sql-devel -f %{oreon_filedir}/gnatcoll-sql-devel.list
%files -n gnatcoll-sqlite -f %{oreon_filedir}/gnatcoll-sqlite.list
%files -n gnatcoll-sqlite-devel -f %{oreon_filedir}/gnatcoll-sqlite-devel.list
%files -n gnatcoll-postgres -f %{oreon_filedir}/gnatcoll-postgres.list
%files -n gnatcoll-postgres-devel -f %{oreon_filedir}/gnatcoll-postgres-devel.list
%files -n gnatcoll-xref -f %{oreon_filedir}/gnatcoll-xref.list
%files -n gnatcoll-xref-devel -f %{oreon_filedir}/gnatcoll-xref-devel.list
%files -n gnatcoll-db-doc -f %{oreon_filedir}/gnatcoll-db-doc.list

%changelog

%autochangelog
