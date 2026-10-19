%global source0_hash 304636d4eccd81a14b6914d07b84c79ebb815288c76fe027b9ebff6ff24d5705
Name:      hyphen
Summary:        A text hyphenation library
Version:   2.8.8
Release:        1%{?dist}
Source0:        https://downloads.sourceforge.net/hunspell/hyphen-%{version}.tar.gz
URL:       http://hunspell.sf.net
License:   GPL-2.0-only OR LGPL-2.1-or-later OR MPL-1.1
%ifarch %{valgrind_arches}
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  patch
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Hyphen is a library for high quality hyphenation and justification.

%package devel
Requires: hyphen = %{version}-%{release}
Summary: Files for developing with hyphen
%description devel
Includes and definitions for developing with hyphen

%package en
Requires: hyphen
Summary: English hyphenation rules
BuildArch: noarch
%description en
English hyphenation rules.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

%configure --disable-static
make %{?_smp_mflags}
%check

make check
%ifarch %{valgrind_arches}
VALGRIND=memcheck make check
%endif
%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la
pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen/
en_US_aliases="en_AG en_AU en_BS en_BW en_BZ en_CA en_DK en_GB en_GH en_HK en_IE en_IN en_JM en_MW en_NA en_NZ en_PH en_SG en_TT en_ZA en_ZM en_ZW"
for lang in $en_US_aliases; do
        ln -s hyph_en_US.dic hyph_$lang.dic
done
popd
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n hyphen-devel -f %{oreon_filedir}/hyphen-devel.list
%files -n hyphen-en -f %{oreon_filedir}/hyphen-en.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.8.8-28
- Import
