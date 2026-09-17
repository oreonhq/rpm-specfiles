%global source0_hash 513f68066ed192ace630f601984c565b5c1d1c81d98c6478ebe4edb3a15be03a

Summary: A library implementing algorithms related to the Unicode Standard
Name: courier-unicode
Version: 2.2.6
Release: 9%{?dist}
License: GPL-3.0-only
URL: http://www.courier-mta.org/unicode/
Source0: https://downloads.sourceforge.net/project/courier/%{name}/%{version}/%{name}-%{version}.tar.bz2
Source1: https://downloads.sourceforge.net/project/courier/%{name}/%{version}/%{name}-%{version}.tar.bz2.sig
Source2: pubkey.maildrop

BuildRequires: gcc-c++
BuildRequires: gcc
BuildRequires: gnupg
BuildRequires: perl-interpreter
BuildRequires: make

%description
This library implements several algorithms related to the Unicode Standard:

* Look up uppercase, lowercase, and titlecase equivalents of a unicode character.
* Implementation of grapheme and work breaking rules.
* Implementation of line breaking rules.

Several ancillary functions, like looking up the unicode character that
corresponds to some HTML 4.0 entity (such as “&amp;”, for example), and
determining the normal width or a double-width status of a unicode character.
Also, an adaptation of the iconv(3) API for this unicode library.

This library also implements C++ bindings for these algorithms.
The current release of the Courier Unicode library is based on the Unicode 8.0.0 standard.

%package devel
Summary: Development tools for programs which will use the libcourier-unicode library
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The courier-unicode-devel package includes the header files and documentation
necessary for developing programs which will use the libcourier-unicode library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q

%build
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%makeinstall

# We don't ship .la files.
rm %{buildroot}%{_libdir}/*.la

%check
%{__make} check

%files
%license COPYING
%doc README ChangeLog AUTHORS
%{_libdir}/libcourier-unicode.so.7
%{_libdir}/libcourier-unicode.so.7.0.0

%files devel
%{_includedir}/courier-unicode.h
%{_includedir}/courier-unicode-categories-tab.h
%{_includedir}/courier-unicode-script-tab.h
%{_libdir}/libcourier-unicode.so
%{_datadir}/aclocal/courier-unicode.m4
%{_datadir}/aclocal/courier-unicode-version.m4
%{_mandir}/man3/*
%{_mandir}/man7/*

%changelog
%autochangelog
