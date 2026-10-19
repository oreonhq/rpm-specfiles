%global source0_hash 8999580c13889955a7901b8a5ed00c20797922e1e7679082e38e38fae8e1cefc
Summary:        Libraries to provide access to RTAS calls and RTAS events
Name:    librtas
Version: 2.0.7
Release:        1%{?dist}
URL:     https://github.com/ibm-power-utilities/librtas
License: LGPL-2.0-or-later
Source0:        https://github.com/ibm-power-utilities/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
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
ExclusiveArch: %{power64}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

./autogen.sh
%configure --disable-silent-rules --disable-static
%make_build CFLAGS="$CFLAGS"
%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -f  %{buildroot}/%{_docdir}/librtas/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{oreon_filedir}/main.list
%files -n librtas-devel -f %{oreon_filedir}/librtas-devel.list

%changelog

%autochangelog
