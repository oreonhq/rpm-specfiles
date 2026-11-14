# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-3.0-or-later

%global source0_hash 3a7fd28378cb5416f8de2c9e77196ec915145d44e30ff4e0ee8beb3fe6211c91

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: source-highlight
Version: 3.1.9
Release: 1%{?dist}
Summary: Produces a document with syntax highlighting
License: GPL-3.0-or-later
URL: https://www.gnu.org/software/src-highlite/
Source0: https://ftp.gnu.org/gnu/src-highlite/source-highlight-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: boost-devel
BuildRequires: help2man

%description
GNU Source-highlight takes a source file and produces a document with
syntax highlighting.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: source-highlight-devel%{?_isa} = %{version}-%{release}
Provides: pkgconfig(source-highlight) = %{version}

%description devel
Headers and libraries for %{name}.

%prep
%oreon_sha256
%autosetup -p1

%build
%configure --with-boost-libdir=%{_libdir}
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete

%check
make check

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%{_bindir}/source-highlight
%{_bindir}/source-highlight-settings
%{_bindir}/src-hilite-lesspipe.sh
%{_libdir}/libsource-highlight.so.*
%{_datadir}/source-highlight/
%{_mandir}/man1/source-highlight.1*
%{_mandir}/man1/source-highlight-settings.1*
%{_infodir}/source-highlight.info*
%{_infodir}/source-highlight-lib.info*

%files devel
%{_libdir}/libsource-highlight.so
%{_includedir}/source-highlight/
%{_libdir}/pkgconfig/source-highlight.pc

%changelog
%autochangelog
