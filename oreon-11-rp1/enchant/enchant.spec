%global source0_hash none

# avoid incompatible pointer type errors with GCC 14
%global build_type_safety_c 2

Summary: An Enchanting Spell Checking Library
Name: enchant
Version: 1.6.0
Release: 41%{?dist}
Epoch: 1
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
Source:        http://www.abisource.com/downloads/enchant/%{version}/enchant-%{version}.tar.gz
URL: http://www.abisource.com/
BuildRequires:  gcc-c++
BuildRequires: glib2-devel >= 2.6.0
BuildRequires: hunspell-devel
BuildRequires: libvoikko-devel
BuildRequires: automake, libtool
BuildRequires: make

# Drop at or after f44
Provides: enchant-aspell = 1.6.0-37
Obsoletes: enchant-aspell < 1.6.0-37

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q

%build
%configure --enable-myspell --with-myspell-dir=/usr/share/hunspell --disable-static --disable-ispell --disable-hspell --disable-zemberek --disable-aspell
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT/%{_libdir}/enchant/*.la

%files
%doc AUTHORS COPYING.LIB README
%{_bindir}/*
%{_libdir}/lib*.so.*
%dir %{_libdir}/enchant
%{_libdir}/enchant/lib*myspell.so*
%{_mandir}/man1/enchant.1*
%{_datadir}/enchant

%files voikko
%{_libdir}/enchant/lib*_voikko.so*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/enchant.pc
%{_includedir}/enchant

%ldconfig_scriptlets

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:1.6.0-41
- Import
