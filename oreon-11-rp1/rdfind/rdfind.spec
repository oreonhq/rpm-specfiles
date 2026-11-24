# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 0a2d0d32002cc2dc0134ee7b649bcc811ecfb2f8d9f672aa476a851152e7af35
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:		rdfind
Version:	1.8.0
Release:	1%{?dist}
Summary:	Program that finds duplicate files

License:	GPL-2.0-or-later
URL:		https://rdfind.pauldreik.se/
Source0:	%{url}/%{name}-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires:	clang
BuildRequires:	make
BuildRequires:	nettle-devel
BuildRequires:	xxhash-devel

%description
Rdfind is a program that finds duplicate files. It is useful for compressing
backup directories or just finding duplicate files. It compares files based on
their content, NOT on their file names.

%prep
%oreon_sha256
%autosetup -p1

%build
export CXXFLAGS="%{optflags} -std=c++17"
%configure
%make_build

%install
%make_install

%check
make check

%files
%doc AUTHORS ChangeLog
%license COPYING LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
