%global source0_hash fd5cc6b77ad6773cac93cb3f415f9318ac3b3455eecf801f6b4a742c4f6c7209
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: elfutils
Version: 0.196
Release: 1%{?dist}
Summary: ELF and DWARF library
License: GPL-2.0-or-later OR LGPL-3.0-or-later
URL: https://sourceware.org/elfutils/
Source0: https://sourceware.org/elfutils/ftp/%{version}/elfutils-%{version}.tar.bz2

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
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
%endif

%description
ELF and DWARF library

%package devel
Summary: ELF and DWARF library
Requires: elfutils%{?_isa} = %{version}-%{release}

%description devel
ELF and DWARF library

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
%oreon_filelist_devel

%files -f %{_builddir}/%{name}.files
%license COPYING-LGPLV3

%files devel -f %{_builddir}/%{name}-devel.files
