%global source0_hash 9d4f7873009d2e31b8b1ec762606b12bee5526e1fe75de48e9495382bfef2bea
Name: rarian
Version: 0.8.6
Release:        1%{?dist}
License: LGPL-2.1-or-later AND Zlib
Summary:        Documentation meta-data library
URL: http://rarian.freedesktop.org/
Source0:        https://gitlab.freedesktop.org/rarian/rarian/-/releases/%{version}/downloads/assets/rarian-%{version}.tar.bz2
Source1: scrollkeeper-omf.dtd
Requires(post): libxml2
Requires(postun): libxml2
Requires: libxslt
Requires: coreutils, util-linux, gawk
# oreon:deps
BuildRequires:  check-devel
BuildRequires:  gcc-c++
BuildRequires:  info
BuildRequires:  make
BuildRequires:  man-db
BuildRequires:  man-pages
BuildRequires:  tinyxml2-devel
# /oreon:deps
%description
Rarian is a documentation meta-data library that allows access to documents,
man pages and info pages.  It was designed as a replacement for scrollkeeper.

%package compat
License: GPL-2.0-or-later
Summary: Extra files for compatibility with scrollkeeper
Requires: rarian = %{version}-%{release}
Requires(post): rarian
Provides: scrollkeeper = 0.4
Obsoletes: scrollkeeper <= 0.3.14
%description compat
This package contains files needed to maintain backward-compatibility with
scrollkeeper.

%package devel
Summary: Development files for Rarian
License: LGPL-2.1-or-later AND Zlib
Requires: rarian = %{version}-%{release}
Requires: pkgconfig
%description devel
This package contains files required to develop applications that use the
Rarian library ("librarian").

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

%configure --disable-skdb-update
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%check

make VERBOSE=1 check
%install
%make_install
mkdir -p %buildroot%{_datadir}/xml/scrollkeeper/dtds
cp %{SOURCE1} %buildroot%{_datadir}/xml/scrollkeeper/dtds
rm -rf %buildroot%{_libdir}/librarian.a
rm -rf %buildroot%{_libdir}/librarian.la
%ldconfig_scriptlets
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post compat

%{_bindir}/rarian-sk-update
CATALOG=/etc/xml/catalog
/usr/bin/xmlcatalog --noout --add "rewriteSystem" \
  "http://scrollkeeper.sourceforge.net/dtds/scrollkeeper-omf-1.0/scrollkeeper-omf.dtd" \
  "/usr/share/xml/scrollkeeper/dtds/scrollkeeper-omf.dtd" $CATALOG >& /dev/null || :
/usr/bin/xmlcatalog --noout --add "rewriteURI" \
  "http://scrollkeeper.sourceforge.net/dtds/scrollkeeper-omf-1.0/scrollkeeper-omf.dtd" \
  "/usr/share/xml/scrollkeeper/dtds/scrollkeeper-omf.dtd" $CATALOG >& /dev/null || :
%postun compat

if [ $1 = 0 ]; then
  CATALOG=/etc/xml/catalog
  /usr/bin/xmlcatalog --noout --del \
    "/usr/share/xml/scrollkeeper/dtds/scrollkeeper-omf.dtd" $CATALOG >& /dev/null || :
fi
%files -f %{oreon_filedir}/main.list
%files -n rarian-compat -f %{oreon_filedir}/rarian-compat.list
%files -n rarian-devel -f %{oreon_filedir}/rarian-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.8.6-1
- Prepare for Oreon 11 (RP1)
