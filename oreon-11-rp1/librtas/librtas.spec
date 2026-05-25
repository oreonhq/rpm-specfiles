Summary: Libraries to provide access to RTAS calls and RTAS events
Name:    librtas
Version: 2.0.6
Release: 6%{?dist}
URL:     https://github.com/ibm-power-utilities/librtas
License: LGPL-2.0-or-later

Source0: https://github.com/ibm-power-utilities/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

# upstream fixes for Lockdown-compatible ABI
Patch1: librtas-01-lockdown-compatible-abi-phase.patch
Patch2: librtas-02-lockdown-compatible-abi-phase.patch
Patch3: librtas-03-lockdown-compatible-abi-phase.patch
Patch4: librtas-04-lockdown-compatible-abi-phase.patch
Patch5: librtas-05-lockdown-compatible-abi-phase.patch
Patch6: librtas-06-lockdown-compatible-abi-phase.patch
Patch7: librtas-07-lockdown-compatible-abi-phase.patch
Patch8: librtas-08-lockdown-compatible-abi-phase.patch
Patch9: librtas-09-end-lockdown-compatible-abi-phase.patch
Patch10: librtas-check-warning-null-pointer.patch
Patch11: librtas-format-mismatch-size_t.patch

BuildRequires: autoconf
BuildRequires: libtool
BuildRequires: make

ExclusiveArch: %{power64}

%description
The librtas shared library provides userspace with an interface
through which certain RTAS calls can be made.  The library uses
either of the RTAS User Module or the RTAS system call to direct
the kernel in making these calls.

The librtasevent shared library provides users with a set of
definitions and common routines useful in parsing and dumping
the contents of RTAS events.

%package devel
Summary:  C header files for development with librtas
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The librtas-devel packages contains the header files necessary for
developing programs using librtas.

%prep
%autosetup -p1

%build
./autogen.sh
%configure --disable-silent-rules --disable-static
%make_build CFLAGS="$CFLAGS"

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -f  %{buildroot}/%{_docdir}/librtas/*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{!?_licensedir:%global license %%doc}
%license COPYING.LESSER
%doc README Changelog
%{_libdir}/librtas.so.*
%{_libdir}/librtasevent.so.*

%files devel
%{_libdir}/librtas.so
%{_libdir}/librtasevent.so
%{_includedir}/librtas.h
%{_includedir}/librtasevent.h
%{_includedir}/librtasevent_v4.h
%{_includedir}/librtasevent_v6.h

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.6-6
- Import
