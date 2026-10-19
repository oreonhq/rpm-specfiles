%global source0_hash 5b6e04430b80fd4af54599551503bae681232be0bae3c55c1a93adeb66702007
%{!?tcl_version: %global tcl_version %((echo '8.6'; echo 'puts $tcl_version' | tclsh 2>/dev/null) | tail -1)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}
%define real_name mysqltcl
Summary:        MySQL interface for Tcl
Name:           tcl-mysqltcl
Version:        3.052
Release:        1%{?dist}
License:        MIT
Source0:        http://www.xdobry.de/%{real_name}/%{real_name}-%{version}.tar.gz
URL:            http://www.xdobry.de/mysqltcl
Requires:       tcl(abi) = %{tcl_version}
Provides:       %{real_name} = %{version}-%{release}
Patch: 0001-use-tcl9-datastructures.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  tcl-devel
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
