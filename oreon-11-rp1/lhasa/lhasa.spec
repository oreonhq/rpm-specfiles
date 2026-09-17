%global source0_hash 1ae8d82d37fc12ec2c52c520b6528ec61268e243f33eca4446b440e182c66d91

Name: lhasa
Summary: Free Software LHA implementation
License: ISC

Version: 0.5.0
Release: 1%{?dist}

URL: https://fragglet.github.io/lhasa/
Source0: https://github.com/fragglet/lhasa/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: doxygen
BuildRequires: gcc
BuildRequires: libtool
BuildRequires: make

# Explicitly require libs in the main package
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

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

# Some bundled JavaScript files are subject to the MIT license
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

%check
%make_build check

%files
%{_bindir}/lha
%{_mandir}/man1/lha.1*

%files libs
%doc AUTHORS NEWS.md
%license COPYING.md
%{_libdir}/liblhasa.so.0*

%files devel
%{_libdir}/liblhasa.so
%{_libdir}/pkgconfig/liblhasa.pc
%{_includedir}/liblhasa-%{version}/

%files doc
%license COPYING.md
%doc %{_pkgdocdir}

%changelog
%autochangelog
