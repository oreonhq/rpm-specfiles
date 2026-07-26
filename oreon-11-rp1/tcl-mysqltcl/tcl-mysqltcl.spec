%global source0_hash 5b6e04430b80fd4af54599551503bae681232be0bae3c55c1a93adeb66702007

%{!?tcl_version: %global tcl_version %((echo '8.6'; echo 'puts $tcl_version' | tclsh 2>/dev/null) | tail -1)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}

%define real_name mysqltcl

Summary:        MySQL interface for Tcl
Name:           tcl-mysqltcl
Version:        3.052
Release:        28%{?dist}

License:        MIT
Source:         http://www.xdobry.de/mysqltcl/%{real_name}-%{version}.tar.gz
URL:            http://www.xdobry.de/mysqltcl

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  tcl-devel
Requires:       tcl(abi) = %{tcl_version}
Provides:       %{real_name} = %{version}-%{release}

# Patch for Tcl 9 support - not upstreamed
# https://bugzilla.redhat.com/show_bug.cgi?id=2337778
Patch: 0001-use-tcl9-datastructures.patch

%description
Mysqltcl is an extension to the Tool Command Language (Tcl) that
provides high-level access to a MySQL database server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n mysqltcl-%{version}
chmod -x generic/mysqltcl.c
chmod 644 README ChangeLog COPYING AUTHORS README-msqltcl doc/mysqltcl.html

%build
%configure --with-tcl=%{_libdir} \
           --with-mysql-lib=%{_libdir} \
           --enable-threads \
           --enable-symbols
make %{?_smp_mflags}

%install
rm -Rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{tcl_sitearch}
mv $RPM_BUILD_ROOT%{_libdir}/%{real_name}-%{version} $RPM_BUILD_ROOT%{tcl_sitearch}/%{real_name}-%{version}

%files
%doc README ChangeLog COPYING AUTHORS README-msqltcl doc/mysqltcl.html
%{tcl_sitearch}/%{real_name}-%{version}
%{_mandir}/mann/*

%changelog
%autochangelog
