%global source0_hash 427c47527f11d157380d90e33c86535a3a0e8eb5c7e2cf0278bd6dbfe733fcee
Name: lhasa
Summary:        Free Software LHA implementation
License: ISC
Version: 0.6.0
Release:        1%{?dist}
URL: https://fragglet.github.io/lhasa/
Source0:        https://github.com/fragglet/lhasa/archive/v%{version}/%{name}-v%{version}.tar.gz
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
Lhasa is a library for parsing LHA (.lzh) archives and a free replacement
for the Unix LHA tool.

Currently it is only possible to read from (i.e. decompress) archives;
generating (compressing) LHA archives may be an enhancement for future
versions. The aim is to be compatible with as many different variants
of the LHA file format as possible, including LArc (.lzs) and PMarc (.pma).

The command line tool aims to be interface-compatible with the non-free
Unix LHA tool (command line syntax and output), for backwards compatibility
with tools that expect particular output.

%package libs
Summary: Free Software LHA implementation
%description libs
Lhasa is a library for parsing LHA (.lzh) archives. Currently it is only
possible to read from (i.e. decompress) archives; generating (compressing)
LHA archives may be an enhancement for future versions. The aim is to be
compatible with as many different variants of the LHA file format as possible,
including LArc (.lzs) and PMarc (.pma).

%package devel
Summary: Development files for Lhasa
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
This package provides files required to develop programs using Lhasa,
the free software LHA implementation library.

%package doc
Summary: Documentation for Lhasa
BuildArch: noarch
License: ISC AND MIT
Provides: bundled(js-jquery)
%description doc
This package provides developer documentation (in HTML format)
for Lhasa, the free software LHA implementation library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
sed -i configure.ac \
	-e 's|TEST_CFLAGS="-DTEST_BUILD"|TEST_CFLAGS="$CFLAGS -DTEST_BUILD"|g'

%build

%global _configure ./autogen.sh
%configure --enable-static=no
%make_build
pushd doc
%make_build html
popd
%install
%make_install
install -m 755 -d %{buildroot}%{_pkgdocdir}
cp -a doc/html %{buildroot}%{_pkgdocdir}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%make_build check
%files -f %{oreon_filedir}/main.list
%files -n lhasa-libs -f %{oreon_filedir}/lhasa-libs.list
%files -n lhasa-devel -f %{oreon_filedir}/lhasa-devel.list
%files -n lhasa-doc -f %{oreon_filedir}/lhasa-doc.list

%changelog

%autochangelog
