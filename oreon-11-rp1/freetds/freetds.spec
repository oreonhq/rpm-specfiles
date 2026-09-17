%global source0_hash 6b2c8b93b9ee7c83855daf745de5878790032f14dbaee553d83a9d211b84dd4b

Summary:        Libraries for talking to Microsoft SQL Server and Sybase databases
Name:           freetds
Version:        1.5.18
Release:        1%{?dist}
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://www.freetds.org/
Source0:        https://www.freetds.org/files/stable/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(openssl)
BuildRequires:  krb5-devel
BuildRequires:  unixODBC >= 2.0.0
BuildRequires:  unixODBC-devel >= 2.0.0

%description
FreeTDS is a set of libraries that allows Unix and Linux programs to
natively talk to Microsoft SQL Server and Sybase databases using the
Tabular Data Stream (TDS) protocol, via DB-Lib, CT-Lib, and ODBC call
level interfaces. Pulled in here as a BuildRequires of qt5-qtbase's Qt
SQL TDS driver plugin.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Headers and shared-object symlinks for building software against FreeTDS
(libsybdb, libct).

%package unixodbc
Summary:        FreeTDS ODBC driver for unixODBC
Requires:       unixODBC%{?_isa} >= 2.0.0
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description unixodbc
ODBC driver module for unixODBC (libtdsodbc).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{version}

%build
%configure \
        --disable-static \
        --with-tdsver=auto \
        --enable-krb5 \
        --with-openssl \
        --with-unixodbc
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete
rm -rf %{buildroot}%{_defaultdocdir}/freetds

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post unixodbc
echo "[FreeTDS]
Description = FreeTDS unixODBC Driver
Driver = %{_libdir}/libtdsodbc.so
Setup = %{_libdir}/libtdsodbc.so" | odbcinst -i -d -r > /dev/null 2>&1 || :
echo "[SQL Server]
Description = FreeTDS unixODBC Driver
Driver = %{_libdir}/libtdsodbc.so
Setup = %{_libdir}/libtdsodbc.so" | odbcinst -i -d -r > /dev/null 2>&1 || :

%preun unixodbc
odbcinst -u -d -n 'FreeTDS' > /dev/null 2>&1 || :
odbcinst -u -d -n 'SQL Server' > /dev/null 2>&1 || :

%files
%license COPYING.txt COPYING_LIB.txt
%doc AUTHORS.md NEWS.md README.md
%{_bindir}/*
%{_mandir}/man?/*
%{_libdir}/libct.so.*
%{_libdir}/libsybdb.so.*
%config(noreplace) %{_sysconfdir}/freetds.conf
%config(noreplace) %{_sysconfdir}/locales.conf
%config(noreplace) %{_sysconfdir}/pool.conf

%files devel
%{_libdir}/libct.so
%{_libdir}/libsybdb.so
%{_includedir}/*.h

%files unixodbc
%{_libdir}/libtdsodbc.so

%changelog
%autochangelog
