# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 2ce4765fd49df6693771ef2941f81e33d8ee14b94a81a5c7b369aa3b137b85a5
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: pam
Version: 1.7.3
Release: 3%{?dist}
Summary: Pluggable authentication modules
License: BSD-3-Clause
URL: https://github.com/linux-pam/linux-pam
Source0: https://github.com/linux-pam/linux-pam/releases/download/v%{version}/Linux-PAM-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: flex
BuildRequires: libxcrypt-devel
BuildRequires: pkgconfig(audit)
BuildRequires: pkgconfig(libcap-ng)
BuildRequires: pkgconfig(libeconf)
BuildRequires: pkgconfig(libselinux)
BuildRequires: pkgconfig(libnsl)
BuildRequires: pkgconfig(libtirpc)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: gettext-devel
BuildRequires: gdbm-devel
BuildRequires: pkgconfig
BuildRequires: patchelf

Provides: pam-libs = %{version}-%{release}
Provides: pam-libs%{?_isa} = %{version}-%{release}

%description
PAM is the pluggable authentication library.

%package devel
Summary: Pluggable authentication modules
Requires: pam%{?_isa} = %{version}-%{release}

%description devel
PAM is the pluggable authentication library.

%prep
%oreon_sha256
%autosetup -n Linux-PAM-%{version} -p1

%build
%oreon_meson -Ddocs=disabled -Delogind=disabled -Ddb=gdbm
%oreon_meson_build

%install
%oreon_meson_install
rm -f %{buildroot}%{_sysconfdir}/environment
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

%changelog
%autochangelog
