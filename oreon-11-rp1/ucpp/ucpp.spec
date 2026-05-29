%global source0_hash 6765412754337b919ee5df2c23ccb17436bf2703e2cda7dfdccc7bdcd406a56c

Summary: Embeddable, quick, light and fully compliant ISO C99 preprocessor
Name: ucpp
Version: 1.3.5
Release: 17%{?dist}
URL: https://gitlab.com/scarabeusiv/ucpp
Source0:        https://gitlab.com/scarabeusiv/ucpp/-/archive/1.3.5/ucpp-1.3.5.tar.bz2
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
BuildRequires: make
BuildRequires: libtool
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
A C preprocessor is a part of a C compiler responsible for macro replacement,
conditional compilation and inclusion of header files. It is often found as
a stand-alone program on Unix systems.

ucpp is such a preprocessor; it is designed to be quick and light, but anyway
fully compliant to the ISO standard 9899:1999, also known as C99. ucpp can be
compiled as a stand-alone program, or linked to some other code; in the latter
case, ucpp will output tokens, one at a time, on demand, as an integrated lexer.

%package libs
Summary: Library for preprocessing C code compliant with ISO-C99

%description libs
libucpp is an ISO standard 9899:1999 compliant preprocessing library for C
code. It will output tokens, one at a time, on demand, as an integrated lexer.

%package devel
Summary: Development files for libucpp Library
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
libucpp is an ISO standard 9899:1999 compliant preprocessing library for C
code. It will output tokens, one at a time, on demand, as an integrated lexer.

This package contains the development files for the library.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q
# convert README to UTF-8
iconv -f iso8859-1 -t utf8 README >README.utf8 && \
 touch -r README.utf8 README && \
 mv README.utf8 README
autoreconf -vif

%build
%configure \
           --disable-silent-rules \
           --disable-static \
           --disable-werror \

%make_build

%install
%make_install
rm %{buildroot}%{_libdir}/libucpp.la

%files
%{_bindir}/ucpp
%{_mandir}/man1/ucpp.1*

%files libs
%doc AUTHORS ChangeLog* COPYING README
%{_libdir}/libucpp.so.13*

%files devel
%{_includedir}/libucpp
%{_libdir}/libucpp.so
%{_libdir}/pkgconfig/libucpp.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.5-17
- Prepare for Oreon 11 (RP1)
