%global source0_hash 0dc2df2fea9934e3a99e00d417f3d192e9897572f6aff3905bd48f2507d16dff
Summary:        Libraries for talking to Microsoft SQL Server and Sybase databases
Name:           freetds
Version:        1.5.19
Release:        1%{?dist}
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://www.freetds.org/
Source0:        https://www.freetds.org/files/stable/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  gcc
BuildRequires:  krb5-devel
BuildRequires:  make
BuildRequires:  pkgconfig(openssl)
BuildRequires:  unixODBC
BuildRequires:  unixODBC-devel
# /oreon:deps
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
%global oreon_srcdir %{name}-%{version}
%oreon_prep
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

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
%files -f %{oreon_filedir}/main.list
%files -n freetds-devel -f %{oreon_filedir}/freetds-devel.list
%files -n freetds-unixodbc -f %{oreon_filedir}/freetds-unixodbc.list

%changelog

%autochangelog
