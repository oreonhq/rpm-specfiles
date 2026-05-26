Name:           zchunk
Version:        1.5.1
Release:        4%{?dist}
Summary:        Compressed file format that allows easy deltas
License:        BSD-2-Clause AND MIT
URL:            https://github.com/zchunk/zchunk
Source0:        https://github.com/zchunk/zchunk/archive/1.5.1/zchunk-1.5.1.tar.gz
# oreon url source checksums begin
%global source0_sha256 2c187055e2206e62cef4559845e7c2ec6ec5a07ce1e0a6044e4342e0c5d7771d
%global source0_file zchunk-1.5.1.tar.gz
# oreon url source checksums end
BuildRequires:  gcc
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  meson
Requires:       %{name}-libs%{_isa} = %{version}-%{release}
Provides:       bundled(buzhash-urlblock) = 0.1

%description
zchunk is a compressed file format that splits the file into independent
chunks.  This allows you to only download the differences when downloading a
new version of the file, and also makes zchunk files efficient over rsync.
zchunk files are protected with strong checksums to verify that the file you
downloaded is in fact the file you wanted.

%package libs
Summary: Zchunk library

%description libs
zchunk is a compressed file format that splits the file into independent
chunks.  This allows you to only download the differences when downloading a
new version of the file, and also makes zchunk files efficient over rsync.
zchunk files are protected with strong checksums to verify that the file you
downloaded is in fact the file you wanted.

This package contains the zchunk library, libzck.

%package devel
Summary: Headers for building against zchunk
Requires: %{name}-libs%{_isa} = %{version}-%{release}

%description devel
zchunk is a compressed file format that splits the file into independent
chunks.  This allows you to only download the differences when downloading a
new version of the file, and also makes zchunk files efficient over rsync.
zchunk files are protected with strong checksums to verify that the file you
downloaded is in fact the file you wanted.

This package contains the headers necessary for building against the zchunk
library, libzck.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/zchunk-1.5.1.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "2c187055e2206e62cef4559845e7c2ec6ec5a07ce1e0a6044e4342e0c5d7771d" || { echo "oreon: Source0 SHA256 mismatch for zchunk-1.5.1.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup
# Remove bundled sha libraries
rm -rf src/lib/hash/sha*

%build
%meson -Dwith-openssl=enabled -Dwith-zstd=enabled
%meson_build

%install
%meson_install
mkdir -p %{buildroot}%{_libexecdir}
install contrib/gen_xml_dictionary %{buildroot}%{_libexecdir}/zck_gen_xml_dictionary

%check
%meson_test

%ldconfig_scriptlets libs

%files
%doc README.md contrib
%{_bindir}/zck*
%{_bindir}/unzck
%{_libexecdir}/zck_gen_xml_dictionary
%{_mandir}/man1/*.gz

%files libs
%license LICENSE
%doc README.md
%{_libdir}/libzck.so.*

%files devel
%doc zchunk_format.txt
%{_libdir}/libzck.so
%{_libdir}/pkgconfig/zck.pc
%{_includedir}/zck.h

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.1-4
- Prepare for Oreon 11 (RP1)
