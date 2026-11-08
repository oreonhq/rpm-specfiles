# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 4c5c6136540384e5455b250f768e7ca11b03fdba1a8efc2341ee0f1111e57612

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
Name:     scdoc
Version:        1.11.3
Release:        1%{?dist}
Summary:  Tool for generating roff manual pages

License:  MIT
URL:      https://git.sr.ht/~sircmpwn/%{name}
Source0:        https://git.sr.ht/~sircmpwn/scdoc/archive/%{version}.tar.gz#/scdoc-%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc
BuildRequires: sed
BuildRequires:  oreon-rpm-macros

%description
scdoc is a tool designed to make the process of writing man pages more
friendly. It reads scdoc syntax from stdin and writes roff to stdout, suitable
for reading with man.

%prep
%oreon_sha256

%autosetup -p1

# Disable static linking
sed -i '/-static/d' Makefile

# Use INSTALL provided by the make_install macro
sed -i 's/\tinstall/\t$(INSTALL)/g' Makefile

%build
make PREFIX=%{_prefix} %{?_smp_mflags}

%install
%make_install PREFIX=%{_prefix}

%check
make check

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}.5*
# Not shipped in a -devel package since scdoc is a development tool not
# installed in a user runtime.
%{_datarootdir}/pkgconfig/%{name}.pc

