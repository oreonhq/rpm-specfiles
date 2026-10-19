%global source0_hash dafb6cdca524c628df832b6dd0bf8fabceb103248edb21762c02d3068fca4503
Summary:        Database Independent Abstraction Layer for C
Name: libdbi
Version: 0.9.0
Release:        29%{?dist}
License: LicenseRef-Callaway-LGPLv2+
URL: http://libdbi.sourceforge.net/
Source0:        http://prdownloads.sourceforge.net/libdbi/%{name}-%{version}.tar.gz
Patch1: libdbi-aarch64.patch
Conflicts: libdbi-dbd-mysql < 0.8
Conflicts: libdbi-dbd-pgsql < 0.8
# oreon:deps
BuildRequires:  docbook-style-dsssl
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openjade
# /oreon:deps
%description
libdbi implements a database-independent abstraction layer in C, similar to the
DBI/DBD layer in Perl. Writing one generic set of code, programmers can
leverage the power of multiple databases and multiple simultaneous database
connections by using this framework.

The libdbi package contains just the libdbi framework.  To make use of
libdbi you will also need one or more plugins from libdbi-drivers, which
contains the plugins needed to interface to specific database servers.

%package devel
Summary: Development files for libdbi (Database Independent Abstraction Layer for C)
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
The libdbi-devel package contains the header files and documentation
needed to develop applications with libdbi.

%package doc
Summary: Documentation for libdbi (Database Independent Abstraction Layer for C)
BuildArch: noarch
%description doc
The libdbi-doc package contains guides for development of applications with libdbi.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

%patch -P1 -p1

%build

%configure
make %{?_smp_mflags}
%install
make DESTDIR=$RPM_BUILD_ROOT install
rm -f ${RPM_BUILD_ROOT}%{_libdir}/libdbi.a
rm -f ${RPM_BUILD_ROOT}%{_libdir}/libdbi.la
rm -rf ${RPM_BUILD_ROOT}%{_docdir}/%{name}-%{version}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libdbi-devel -f %{oreon_filedir}/libdbi-devel.list
%files -n libdbi-doc -f %{oreon_filedir}/libdbi-doc.list

%changelog

%autochangelog

