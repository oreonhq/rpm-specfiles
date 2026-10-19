%global source0_hash 22080b2b94f222132da0d2d800437cf1ccd5e078df415e69771ad1070ac8487b
%global build_type_safety_c 2
Summary:        An Enchanting Spell Checking Library
Name: enchant
Version: 1.6.0
Release:        1%{?dist}
Epoch: 1
License: LicenseRef-Callaway-LGPLv2+
Source0:        https://github.com/rrthomas/enchant/archive/refs/tags/enchant-1-6-0.tar.gz#/enchant-%{version}.tar.gz
URL: https://github.com/rrthomas/enchant
Provides: enchant-aspell = 1.6.0-37
Obsoletes: enchant-aspell < 1.6.0-37
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  glib2-devel
BuildRequires:  hunspell-devel
BuildRequires:  libtool
BuildRequires:  libvoikko-devel
BuildRequires:  make
# /oreon:deps
%description
A library that wraps other spell checking backends.

%package voikko
Summary: Integration with voikko for libenchant
Requires: enchant = %{epoch}:%{version}-%{release}
%description voikko
Libraries necessary to integrate applications using libenchant with voikko.

%package devel
Summary: Support files necessary to compile applications with libenchant.
Requires: enchant = %{epoch}:%{version}-%{release}
Requires: glib2-devel
%description devel
Libraries, headers, and support files necessary to compile applications using libenchant.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n enchant-enchant-1-6-0
autoreconf -fiv

%build

%configure --enable-myspell --with-myspell-dir=/usr/share/hunspell --disable-static --disable-ispell --disable-hspell --disable-zemberek --disable-aspell
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT/%{_libdir}/enchant/*.la
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n enchant-voikko -f %{oreon_filedir}/enchant-voikko.list
%files -n enchant-devel -f %{oreon_filedir}/enchant-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:1.6.0-41
- Import
