%global source0_hash 8f77e8a7ced5301af6e22f47302fdbc3b1ff41f2b83c43c77ae5ca041771ddbf

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Summary: Cross platform C library for parsing GNU style command line arguments
Name: argtable
Version: 2.13
Release: 34%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
Url: http://argtable.sourceforge.net/
Source: http://prdownloads.sourceforge.net/argtable/%{name}2-13.tar.gz
Patch0: argtable-c99.patch
BuildRequires:  gcc
BuildRequires: pkgconfig
BuildRequires: make

%description
Argtable is an ANSI C library for parsing GNU style command line
arguments. It enables a program's command line syntax to be defined in
the source code as an array of argtable structs. The command line is
then parsed according to that specification and the resulting values
are returned in those same structs where they are accessible to the main
program. Both tagged (-v, --verbose, --foo=bar) and untagged arguments
are supported, as are multiple instances of each argument.
Syntax error handling is automatic.

%package devel
Summary: Development package that includes the argtable header files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Header and development files for using argtable

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}2-13

%build
%configure --disable-static --docdir=%{_pkgdocdir}
make %{?_smp_mflags} 

%install
make DESTDIR=${RPM_BUILD_ROOT} install
rm -f ${RPM_BUILD_ROOT}/%{_libdir}/*.la
install -pm 644 AUTHORS ChangeLog COPYING README ${RPM_BUILD_ROOT}%{_pkgdocdir}

%files
%dir %{_pkgdocdir}
%{_pkgdocdir}/AUTHORS
%{_pkgdocdir}/ChangeLog
%{_pkgdocdir}/COPYING
%{_pkgdocdir}/README
%{_libdir}/libargtable2.so.*

%files devel
%{_libdir}/libargtable2.so
%{_includedir}/argtable2.h
%{_libdir}/pkgconfig/argtable2.pc

%doc %{_mandir}/man3/*
%{_pkgdocdir}/*
%exclude %{_pkgdocdir}/AUTHORS
%exclude %{_pkgdocdir}/ChangeLog
%exclude %{_pkgdocdir}/COPYING
%exclude %{_pkgdocdir}/README

%ldconfig_scriptlets

%changelog
%autochangelog
