%global source0_hash 93941f85a1e7bd593fa94f299233cb5dfc91cd144fd9a78a6ceb75001c5b03be
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libpsl
Version: 0.23.3
Release: 2%{?dist}
Summary: C library for the Public Suffix List
License: MIT
URL: https://github.com/rockdaboot/libpsl
Source0: https://github.com/rockdaboot/libpsl/releases/download/%{version}/libpsl-%{version}.tar.gz
Source1: libpsl-%{version}.tar.gz.sig
Source2: libpsl-key.asc
Requires: publicsuffix-list

BuildRequires: oreon-rpm-macros
BuildRequires: gnupg2
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: patchelf
BuildRequires: libidn2-devel
BuildRequires: libunistring-devel
BuildRequires: publicsuffix-list
BuildRequires: pkgconf
BuildRequires: python3

%description
libpsl is a C library to handle the Public Suffix List.

%package devel
Summary: Development files for libpsl
Requires: libpsl%{?_isa} = %{version}-%{release}
Provides: pkgconfig(libpsl)

%description devel
Headers and libraries for developing against libpsl.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -n libpsl-%{version} -p1
sed -i '1s|^#!.*python$|#!/usr/bin/python3|' src/psl-make-dafsa

%build
%oreon_configure --disable-static --disable-gtk-doc --disable-man --enable-runtime=libidn2 --disable-builtin \
  --with-psl-file=%{_datadir}/publicsuffix/public_suffix_list.dat --with-psl-testfile=no
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f" 2>/dev/null || true)
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
%oreon_filelist_devel

%files -f %{_builddir}/%{name}.files
%license COPYING

%files devel -f %{_builddir}/%{name}-devel.files
