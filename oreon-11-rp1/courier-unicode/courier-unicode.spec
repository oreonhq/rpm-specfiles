%global source1_hash 704858d602e0445bfb447fb2f35f33772d42f8201a829e81c04eec29974d0537
%global source0_hash 0aed2349c5b62de0d33ccf8c23527aae41daf95a03c8054c88de4faef8da8a08
Summary:        A library implementing algorithms related to the Unicode Standard
Name: courier-unicode
Version: 2.6.0
Release:        1%{?dist}
License: GPL-3.0-only
URL: http://www.courier-mta.org/unicode/
Source0:        https://downloads.sourceforge.net/project/courier/%{name}/%{version}/%{name}-%{version}.tar.bz2
Source1: https://downloads.sourceforge.net/project/courier/%{name}/%{version}/%{name}-%{version}.tar.bz2.sig
Source2: pubkey.maildrop
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gnupg
BuildRequires:  make
BuildRequires:  perl-interpreter
# /oreon:deps
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
rm %{buildroot}%{_libdir}/*.la
%oreon_autofiles courier-unicode-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%{__make} check
%files -f %{oreon_filedir}/main.list
%files -n courier-unicode-devel -f %{oreon_filedir}/courier-unicode-devel.list

%changelog

%autochangelog
