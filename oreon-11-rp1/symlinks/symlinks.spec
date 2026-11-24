# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 596fa828d6425c47aa1a11418139cc572dae07a96c87eb1b9c70acf0c1836cd3
%global source1_hash d6272a58ec1ada3e95032936cc42396f2ed1b7b1e4c781f083eb2e73630c62a4
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Summary: A utility which maintains a system's symbolic links
Name: symlinks
URL: http://ibiblio.org/pub/Linux/utils/file/
Version: 1.7
Release: 1%{?dist}
License: Symlinks
Source0: http://ibiblio.org/pub/Linux/utils/file/%{name}-%{version}.tar.gz
Source1: symlinks-LICENSE.txt
BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: make
%description
The symlinks utility performs maintenance on symbolic links.  Symlinks
checks for symlink problems, including dangling symlinks which point
to nonexistent files.  Symlinks can also automatically convert
absolute symlinks to relative symlinks.

Install the symlinks package if you need a program for maintaining
symlinks on your system.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%setup -q
cp %{SOURCE1} .

%build
make CFLAGS="$RPM_OPT_FLAGS $(getconf LFS_CFLAGS) %{build_ldflags}" %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 755 symlinks $RPM_BUILD_ROOT%{_bindir}
install -m 644 symlinks.1 $RPM_BUILD_ROOT%{_mandir}/man1

%files
%doc symlinks-LICENSE.txt
%{_bindir}/symlinks
%{_mandir}/man1/symlinks.1*

%changelog
%autochangelog
