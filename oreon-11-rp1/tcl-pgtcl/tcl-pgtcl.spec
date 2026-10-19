%global source1_hash 6cd51e3a2192c685a722a38348182eb3084ba1fec842456af3432812f0ec15fa
%global source0_hash 1925d7cf9422f0213da725bbe245e065ab570b478881577c87ae714e18078208
%global docs_hash 20131007a
Name:		tcl-pgtcl
Version:	2.1.1
Release:        1%{?dist}
Summary:        A Tcl client library for PostgreSQL
URL:		http://sourceforge.net/projects/pgtclng/
License: PostgreSQL
Source0:        http://downloads.sourceforge.net/pgtclng/pgtcl%{version}.tar.gz
Source1:	http://downloads.sourceforge.net/pgtclng/pgtcldocs-%{docs_hash}.zip
Patch1:		pgtcl-no-rpath.patch
Provides:	pgtcl = %{version}-%{release}
Provides:	postgresql-tcl = 8.5.0-1
Obsoletes:	postgresql-tcl < 8.5
Requires:	tcl(abi) >= 8.5
%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  libpq-devel
BuildRequires:  make
BuildRequires:  tcl-devel
# /oreon:deps
%description
PostgreSQL is an advanced Object-Relational database management system.
The tcl-pgtcl package contains Pgtcl, a Tcl client library for connecting
to a PostgreSQL server.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n pgtcl%{version}

unzip %{SOURCE1}
PGTCLDOCDIR=`basename %{SOURCE1} .zip`
mv $PGTCLDOCDIR Pgtcl-docs

%patch -P1 -p1

autoconf

%build

%configure --libdir=%{tcl_sitearch} --with-tcl=%{_libdir}
make all %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_includedir}/libpgtcl.h
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
