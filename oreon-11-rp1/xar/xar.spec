%global source0_hash 67c66c3511a34c82e3cfd2ab38fcac24e99fc636961473573bbe8f696e1a5b79

%global subversion 417.1

Name:           xar
Version:        1.8.0.%{subversion}
Release:        17%{?dist}
Summary:        The eXtensible ARchiver
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://opensource.apple.com/source/xar
Source:         https://opensource.apple.com/tarballs/xar/xar-%{subversion}.tar.gz
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  libxml2-devel
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
BuildRequires:  bzip2-devel
BuildRequires:  gawk
BuildRequires:  autoconf

#First 4 patches taken from Gentoo Xar package. To make Xar more suitable for Linux systems
#Copyright Gentoo authors 2019 GPLv2
Patch0:         xar-1.6.1-ext2.patch
Patch1:         xar-1.8-safe_dirname.patch
Patch2:         xar-1.8-arm-ppc.patch
Patch3:         xar-1.8-openssl-1.1.patch

Patch4:         xar-1.8-Add-OpenSSL-To-Configuration.patch
Patch5:         xar-1.8-gnuconfig.patch

%description
The XAR project aims to provide an easily extensible archive format. Important
design decisions include an easily extensible XML table of contents for random
access to archived files, storing the toc at the beginning of the archive to
allow for efficient handling of streamed archives, the ability to handle files
of arbitrarily large sizes, the ability to choose independent encodings for
individual files in the archive, the ability to store checksums for individual
files in both compressed and uncompressed form, and the ability to query the
table of content's rich meta-data.

%package devel
Summary: Development files for the eXtensible ARchiver
Requires: %{name} = %{version}-%{release}

%description devel
Development files for the eXtensible ARchiver.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -n xar-%{subversion}
pushd xar
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
sed 's:-Wl,-rpath,::g' -i configure.ac #No rpath
sed 's:filetree.h:../lib/filetree.h:g' -i src/xar.c #Fix path
sed 's:util.h:../lib/util.h:g' -i src/xar.c #Fix path
popd

%build
pushd xar
env NOCONFIGURE=1 ./autogen.sh
%configure --disable-static
make %{?_smp_mflags}
popd

%install
pushd xar
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/libxar.la #Not needed
popd

%ldconfig_scriptlets

%files
%doc README xar/ChangeLog xar/TODO
%license xar/LICENSE
%{_bindir}/xar
%{_libdir}/libxar.so.*
%{_mandir}/man1/xar.1*

%files devel
%{_includedir}/xar/
%{_libdir}/libxar.so

%changelog
%autochangelog
