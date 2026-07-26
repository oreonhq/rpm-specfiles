%global source0_hash 3446e1d71abdeb98d41e252777e67e1909b186496fda59f98f67032f7fbcd955

Name:           mdbtools
Version:        1.0.0
Release:        9%{?dist}
Summary:        Access data stored in Microsoft Access databases
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/mdbtools/mdbtools/
Source0:        https://github.com/mdbtools/mdbtools/releases/download/v%{version}/mdbtools-%{version}.tar.gz
Patch1:         mdbtools-0.9.3-mdb-sql-compile-fix.patch
Patch2:         mdbtools-1.0.0-s390x-build-fix.patch
BuildRequires:  make gcc
BuildRequires:  libxml2-devel glib2-devel unixODBC-devel readline-devel gettext-devel
BuildRequires:  bison flex txt2man rarian-compat bash-completion
BuildRequires:  libtool autoconf automake
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# No provides this is here because starting with 0.9.y upstream has dropped gmdb2
Obsoletes:      %{name}-gui <= 0.7.1-99

%description
MDB Tools is a suite of programs for accessing data stored in Microsoft
Access databases.

%package libs
Summary:        Library for accessing data stored in Microsoft Access databases
License:        LGPLv2+

%description libs
This package contains the MDB Tools library, which can be used by applications
to access data stored in Microsoft Access databases.

%package        devel
Summary:        Development files for %{name}
License:        LGPLv2+
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}, glib2-devel, pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        odbc
Summary:        MDB Unix-ODBC driver
License:        LGPLv2+
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    odbc
The mdbtools-odbc package contains a Unix-ODBC driver using
the mdbtools SQL front-end for MDB files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
autoreconf -vif

%build
%configure --disable-static --with-unixodbc="%{_prefix}"
%make_build V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete

%ldconfig_scriptlets libs

%files
%license COPYING
%{_bindir}/mdb-*
%{_mandir}/man1/mdb-*.1.gz
%{_datadir}/bash-completion

%files libs
%doc AUTHORS NEWS README.md
%license COPYING.LIB
%{_libdir}/libmdb*.so.*

%files devel
%doc HACKING.md
%{_libdir}/libmdb*.so
%{_libdir}/pkgconfig/libmdb*.pc
%{_includedir}/mdb*.h

%files odbc
%{_libdir}/odbc

%changelog
%autochangelog
