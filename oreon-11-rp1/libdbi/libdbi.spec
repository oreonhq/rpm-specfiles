%global source0_hash none

Summary: Database Independent Abstraction Layer for C
Name: libdbi
Version: 0.9.0
Release: 29%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL: http://libdbi.sourceforge.net/

Source: http://prdownloads.sourceforge.net/libdbi/%{name}-%{version}.tar.gz

# add support for aarch64 to the shipped old automake files
# -> fixed in upstream (see http://sourceforge.net/p/libdbi/mailman/message/31868578/)
#    but upstream haven't realeased new version yet
Patch1: libdbi-aarch64.patch

BuildRequires: openjade docbook-style-dsssl
BuildRequires: gcc
BuildRequires: make
Conflicts: libdbi-dbd-mysql < 0.8
Conflicts: libdbi-dbd-pgsql < 0.8

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

# we will include generated documentation in -devel subpackage,
# so we need to remove it from builddir, since it would be included
# automatically otherwise
rm -rf ${RPM_BUILD_ROOT}%{_docdir}/%{name}-%{version}

%ldconfig_scriptlets

%files
%doc AUTHORS
%doc ChangeLog
%doc README
%doc NEWS
%license COPYING
%{_libdir}/libdbi.so.*

%files devel
%doc TODO
%{_includedir}/dbi/
%{_libdir}/libdbi.so
%{_libdir}/pkgconfig/dbi.pc

%files doc
%license COPYING
%doc doc/programmers-guide.pdf
%doc doc/programmers-guide/
%doc doc/driver-guide.pdf
%doc doc/driver-guide/

%changelog
%autochangelog

