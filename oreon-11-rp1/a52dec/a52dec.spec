%global source0_hash a21d724ab3b3933330194353687df82c475b5dfb997513eef4c25de6c865ec33
Summary:        Small test program for liba52
Name:       a52dec
Version:    0.7.4
Release:        54%{?dist}
License:    GPL-2.0-only
URL:        http://liba52.sourceforge.net
Source0:        https://deb.debian.org/debian/pool/main/a/a52dec/a52dec_0.7.4.orig.tar.gz
Patch0:     a52dec-configure-optflags.patch
Patch2:     liba52-silence.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%package -n liba52
Summary:    A free ATSC A/52 stream decoder, also known as AC-3 or AC3
Obsoletes:  a52dec < 0.7.4-25
Obsoletes:  a52dec-libs < 0.7.4-25
Provides:   a52dec-libs = %{version}-%{release}
%package -n liba52-devel
Summary:    Development files for liba52
Requires:   liba52%{?_isa} = %{version}-%{release}
Provides:   %{name}-devel = %{version}-%{release}
Obsoletes:  %{name}-devel < 0.7.4-25
%description

Small test program for liba52.

%description -n liba52

liba52 is a free library for decoding ATSC A/52 streams. The A/52
standard is used in a variety of applications, including digital
television and DVD. It is also known as AC-3 or AC3

%description -n liba52-devel

The liba52-devel package contains libraries and header files for
developing applications that use liba52-devel.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

sed -i -e 's/-prefer-non-pic/-prefer-pic/' liba52/configure.incl

# regenerate autotools
autoreconf -fiv

# Convert to utf-8
for file in AUTHORS; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done

%build

%configure --enable-shared --disable-static
%make_build
%install
%make_install
%ldconfig_scriptlets -n liba52
%oreon_autofiles liba52 usr/*/lib*.so.*
%oreon_autofiles liba52-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n liba52 -f %{oreon_filedir}/liba52.list
%files -n liba52-devel -f %{oreon_filedir}/liba52-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.4-53
- Prepare for Oreon 11 (RP1)
