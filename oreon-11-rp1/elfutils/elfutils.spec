%global source0_hash fd5cc6b77ad6773cac93cb3f415f9318ac3b3455eecf801f6b4a742c4f6c7209
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: elfutils
Version: 0.196
Release: 4%{?dist}
Summary: ELF and DWARF library
License: GPL-2.0-or-later OR LGPL-3.0-or-later
URL: https://sourceware.org/elfutils/
Source0: https://sourceware.org/elfutils/ftp/%{version}/elfutils-%{version}.tar.bz2

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: m4
BuildRequires: patchelf
BuildRequires: zlib-devel
BuildRequires: bzip2-devel
BuildRequires: xz-devel
BuildRequires: libzstd-devel
BuildRequires: pkgconf
BuildRequires: gettext

Requires: elfutils-libs%{?_isa} = %{version}-%{release}
Requires: elfutils-libelf%{?_isa} = %{version}-%{release}

%description
Tools for handling ELF objects and DWARF debugging information.

%package libs
Summary: Libraries to handle compiled objects
Requires: elfutils-libelf%{?_isa} = %{version}-%{release}

%description libs
The libdw and libasm libraries from elfutils.

%package libelf
Summary: Library to read and write ELF files

%description libelf
The libelf library from elfutils.

%package libelf-devel
Summary: Development files for libelf
Requires: elfutils-libelf%{?_isa} = %{version}-%{release}

%description libelf-devel
Headers, pkg-config file, and man pages for libelf.

%package devel
Summary: ELF and DWARF library
Requires: elfutils-libs%{?_isa} = %{version}-%{release}
Requires: elfutils-libelf-devel%{?_isa} = %{version}-%{release}

%description devel
Headers and pkg-config file for libdw and libasm.

%prep
%oreon_sha256
%autosetup -n elfutils-0.196 -p1

%build
%oreon_configure --disable-debuginfod --disable-libdebuginfod
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f")
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
%find_lang elfutils

%ldconfig_scriptlets libs
%ldconfig_scriptlets libelf

%files
%license COPYING
%{_bindir}/eu-*
%{_mandir}/man1/eu-*.1*

%files libs
%license COPYING-LGPLV3
%{_libdir}/libasm-%{version}.so
%{_libdir}/libasm.so.1
%{_libdir}/libdw-%{version}.so
%{_libdir}/libdw.so.1

%files libelf -f elfutils.lang
%license COPYING-LGPLV3
%{_libdir}/libelf-%{version}.so
%{_libdir}/libelf.so.1

%files devel
%{_includedir}/dwarf.h
%{_includedir}/elfutils/
%{_libdir}/libasm.so
%{_libdir}/libdw.so
%{_libdir}/pkgconfig/libdw.pc

%files libelf-devel
%{_includedir}/gelf.h
%{_includedir}/libelf.h
%{_includedir}/nlist.h
%{_libdir}/libelf.so
%{_libdir}/pkgconfig/libelf.pc
%{_mandir}/man3/*.3*
