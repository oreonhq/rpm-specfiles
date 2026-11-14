# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash e78a29e7766b8b7b354497d08f71a55641abc53675ce1875584781aae35644a1
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: subversion
Version: 1.14.5
Release: 1%{?dist}
Summary: Version control system
License: Apache-2.0
URL: https://subversion.apache.org/
Source0: https://downloads.apache.org/subversion/subversion-%{version}.tar.bz2

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: make
BuildRequires: apr-devel
BuildRequires: apr-util-devel
BuildRequires: sqlite-devel
BuildRequires: zlib-devel
BuildRequires: openssl-devel
BuildRequires: libuuid-devel
BuildRequires: expat-devel
BuildRequires: lz4-devel
BuildRequires: pkgconfig(liblz4)
BuildRequires: patchelf

%description
Subversion version control system.

%prep
%oreon_sha256
%autosetup -n subversion-%{version}

%build
%configure --with-apr=%{_prefix} --with-apr-util=%{_prefix} --with-sqlite=/usr --with-zlib=/usr --with-lz4=%{_prefix} --with-utf8proc=internal
%make_build

%install
%make_install
for f in %{buildroot}%{_bindir}/svn*; do
  r=$(patchelf --print-rpath "$f" 2>/dev/null) || continue
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
%oreon_filelist
sed -i '\|/bin/svn$|d' %{_builddir}/%{name}.files

%check
subversion/svn/svn --version

%files -f %{_builddir}/%{name}.files
%{_bindir}/svn
