%global source0_hash be9ad9a276f4305ab7dd2f5225c8be1ff54352f565ff4dede9628c1aaa7dec57
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: util-linux
Version: 2.41.1
Release: 1%{?dist}
Summary: Low-level system utilities and libraries
License: GPL-2.0-or-later
URL: https://github.com/util-linux/util-linux
Source0: https://mirrors.edge.kernel.org/pub/linux/utils/util-linux/v2.41/util-linux-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: pkgconf
BuildRequires: ncurses-devel
BuildRequires: zlib-devel
BuildRequires: readline-devel
BuildRequires: pam-devel
BuildRequires: libcap-devel
BuildRequires: libselinux-devel
BuildRequires: patchelf
%endif

%description
util-linux provides libmount, libblkid, libfdisk and libsmartcols.

%package devel
Summary: Low-level system utilities and libraries
Requires: util-linux%{?_isa} = %{version}-%{release}

%description devel
util-linux provides libmount, libblkid, libfdisk and libsmartcols.

%prep
%oreon_sha256
%autosetup -n util-linux-%{version} -p1

%build
%oreon_configure \
  --disable-static \
  --with-systemd=no \
  --without-python \
  --with-ncursesw \
  --enable-libuuid \
  --enable-libblkid \
  --enable-libmount \
  --enable-libfdisk \
  --enable-libsmartcols
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
%license COPYING

%files devel -f %{_builddir}/%{name}-devel.files
