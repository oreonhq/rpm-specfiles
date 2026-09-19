%global source0_hash 6cd51e3a2192c685a722a38348182eb3084ba1fec842456af3432812f0ec15fa

%global docs_hash 20131007a

Name:		tcl-pgtcl
Version:	2.1.1
Release:	22%{?dist}
Summary:	A Tcl client library for PostgreSQL

URL:		http://sourceforge.net/projects/pgtclng/
# The PostgreSQL license is very similar to other MIT licenses, but the OSI
# recognizes it as an independent license, so we do as well.
License: PostgreSQL

Source0:	http://downloads.sourceforge.net/pgtclng/pgtcl%{version}.tar.gz
# Note that for some reason docs are date-labeled not version-labeled
Source1:	http://downloads.sourceforge.net/pgtclng/pgtcldocs-%{docs_hash}.zip

Patch1:		pgtcl-no-rpath.patch

Provides:	pgtcl = %{version}-%{release}
# pgtcl was originally shipped as a sub-RPM of the PostgreSQL package;
# these Provides/Obsoletes give a migration path.  Note there is no
# intention of changing the version numbers in future.
Provides:	postgresql-tcl = 8.5.0-1
Obsoletes:	postgresql-tcl < 8.5

BuildRequires: make
BuildRequires:  gcc
BuildRequires:	libpq-devel tcl-devel
BuildRequires:	autoconf

Requires:	tcl(abi) >= 8.5

%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}

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
# we don't really need to ship the .h file
rm -f $RPM_BUILD_ROOT%{_includedir}/libpgtcl.h

%files
%{_libdir}/tcl%{tcl_version}/pgtcl%{version}/
%doc Pgtcl-docs/*

%changelog
%autochangelog
