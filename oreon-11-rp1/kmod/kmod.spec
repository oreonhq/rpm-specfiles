%global source0_hash 985554de49c21a58abd68c6cda2251384e1e5bb08b3b14c7f02b51f4c90c2958
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: kmod
Version: 34.3
Release: 2%{?dist}
Summary: Linux kernel module management utilities
License: GPL-2.0-or-later AND LGPL-2.1-or-later
URL: https://git.kernel.org/pub/scm/utils/kernel/kmod/kmod.git
Source0: https://mirrors.edge.kernel.org/pub/linux/utils/kernel/kmod/kmod-%{version}.tar.xz
Source1: kmod-%{version}.tar.sign
Source2: kmod-key.asc
Provides: module-init-tools = 4.0-1
Obsoletes: module-init-tools < 4.0-1

BuildRequires: oreon-rpm-macros
BuildRequires: gnupg2
BuildRequires: xz
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: pkgconf
BuildRequires: patchelf
BuildRequires: openssl-devel
BuildRequires: xz-devel
BuildRequires: zlib-devel
BuildRequires: libzstd-devel
Requires: kmod-libs%{?_isa} = %{version}-%{release}

%description
kmod provides tools to insert, remove, list, check properties and resolve
dependencies of Linux kernel modules, and the libkmod library.

%package devel
Summary: Development files for libkmod
Requires: kmod-libs%{?_isa} = %{version}-%{release}

%description devel
Headers and libraries for developing against libkmod.

%package libs
Summary: Library to manage Linux kernel modules
License: LGPL-2.1-or-later
Obsoletes: kmod < 34.3-2

%description libs
libkmod provides an API for insertion, removal, listing and dependency
resolution of Linux kernel modules.

%prep
%oreon_sha256
xz -dc %{SOURCE0} > %{_builddir}/kmod-%{version}.tar
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{_builddir}/kmod-%{version}.tar
rm -f %{_builddir}/kmod-%{version}.tar
%autosetup -n kmod-%{version} -p1

%build
%oreon_meson -Dmanpages=false -Ddocs=false -Dbuild-tests=false \
  -Dopenssl=enabled -Dxz=enabled -Dzlib=enabled -Dzstd=enabled \
  -Dbashcompletiondir=%{_datadir}/bash-completion/completions \
  -Dfishcompletiondir=%{_datadir}/fish/vendor_completions.d \
  -Dzshcompletiondir=%{_datadir}/zsh/site-functions
%oreon_meson_build

%install
%oreon_meson_install
mkdir -p %{buildroot}%{_sysconfdir}/depmod.d %{buildroot}%{_sysconfdir}/modprobe.d
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f" 2>/dev/null || true)
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done

%files
%license COPYING
%{_bindir}/depmod
%{_bindir}/insmod
%{_bindir}/kmod
%{_bindir}/lsmod
%{_bindir}/modinfo
%{_bindir}/modprobe
%{_bindir}/rmmod
%{_datadir}/pkgconfig/kmod.pc
%{_datadir}/bash-completion/completions/*
%{_datadir}/fish/vendor_completions.d/*
%{_datadir}/zsh/site-functions/*
%dir %{_sysconfdir}/depmod.d
%dir %{_sysconfdir}/modprobe.d

%ldconfig_scriptlets libs

%files libs
%license COPYING
%{_libdir}/libkmod.so.2
%{_libdir}/libkmod.so.2.*

%files devel
%{_includedir}/libkmod.h
%{_libdir}/libkmod.so
%{_libdir}/pkgconfig/libkmod.pc
