# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash f25c6ab51548a73a75558742fb031e0625d6485fe5f9155949d6486a2408ab66

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
BuildRequires: oreon-rpm-macros
Summary: GNU macro processor
Name: m4
Version:        1.4.21
Release:        1%{?dist}
License: GPL-3.0-or-later AND GFDL-1.3-or-later AND FSFULLR AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND GPL-3.0-or-later WITH Texinfo-exception AND GPL-2.0-or-later WITH Autoconf-exception-generic AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND MIT
Source0:        https://mirror.cs.odu.edu/gnu/m4/m4-%{version}.tar.xz
Source1:        m4-1.4.21.tar.xz.sig
# Fix SIGSEGV in gnulib posix_spawn_file_actions_addchdir tests
# https://lists.gnu.org/archive/html/bug-gnulib/2026-07/msg00165.html
Patch0:        m4-1.4.21-gnulib-posix_addchdr.patch
URL: https://www.gnu.org/software/m4/
BuildRequires: make
BuildRequires: gcc autoconf automake
BuildRequires: gettext
%ifarch ppc ppc64
BuildRequires: texinfo
BuildRequires:  oreon-rpm-macros
%endif
# Gnulib is not versioned, see m4 ChangeLog for approximate date of Gnulib copy
Provides: bundled(gnulib)

%description
A GNU implementation of the traditional UNIX macro processor.  M4 is
useful for writing text files which can be logically parsed, and is used
by many programs as part of their build process.  M4 has built-in
functions for including files, running shell commands, doing arithmetic,
etc.  The autoconf program needs m4 for generating configure scripts, but
not for running configure scripts.

Install m4 if you need a macro processor.

%prep
%oreon_sha256

%setup -q
%patch -P0 -p1
autoreconf
chmod 644 COPYING

%build
%configure
%make_build

%install
%make_install
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
%find_lang %{name}

%check
make %{?_smp_mflags} check

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%{_bindir}/m4
%{_infodir}/*
%{_mandir}/man1/m4.1*

