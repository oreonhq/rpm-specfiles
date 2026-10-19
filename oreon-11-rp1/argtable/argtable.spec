%global source0_hash 8f77e8a7ced5301af6e22f47302fdbc3b1ff41f2b83c43c77ae5ca041771ddbf
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
Summary:        Cross platform C library for parsing GNU style command line arguments
Name: argtable
Version: 2.13
Release:        1%{?dist}
License: LicenseRef-Callaway-LGPLv2+
Url: http://argtable.sourceforge.net/
Source0:        http://prdownloads.sourceforge.net/argtable/%{name}2-13.tar.gz
Patch0: argtable-c99.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig
# /oreon:deps
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
%global oreon_srcdir %{name}2-13
%oreon_prep
%build

%configure --disable-static --docdir=%{_pkgdocdir}
make %{?_smp_mflags} 
%install
make DESTDIR=${RPM_BUILD_ROOT} install
rm -f ${RPM_BUILD_ROOT}/%{_libdir}/*.la
install -pm 644 AUTHORS ChangeLog COPYING README ${RPM_BUILD_ROOT}%{_pkgdocdir}
%oreon_autofiles argtable-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n argtable-devel -f %{oreon_filedir}/argtable-devel.list

%changelog

%autochangelog
