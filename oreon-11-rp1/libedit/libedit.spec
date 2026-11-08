# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 432d5e7ea8b0116dd39f2eca7bc11d0eed77faa6b77ea526ace89907c23ea4a0

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global snap 20260512

# Build man pages with mdoc2man.awk to avoid circular dependencies
%bcond bootstrap 0

Summary:	The NetBSD Editline library
Name:		libedit
Version:        3.1
Release:        1%{?dist}

# The project as a whole is BSD-3-Clause.
# These files are BSD-2-Clause:
# - doc/editline.3.roff
# - doc/editrc.5.roff
# - src/chartype.{c,h}
# - src/editline/readline.h
# - src/eln.c
# - src/filecomplete.{c,h}
# - src/getline.c [not linked into final library]
# - src/literal.{c,h}
# - src/read.h
# - src/readline.c
# - src/reallocarr.c
# This file is both BSD-3-Clause and BSD-2-Clause:
# - src/vis.c
# These files are ISC:
# - doc/editline.7.roff
# - src/strlcat.c
# - src/strlcpy.c
License:	BSD-3-Clause AND BSD-2-Clause AND ISC
URL:		https://www.thrysoee.dk/editline/
Source0:        https://www.thrysoee.dk/editline//libedit-20260512-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	ncurses-devel

%if %{without bootstrap}
BuildRequires:	groff-base
BuildRequires:  oreon-rpm-macros
%endif

%description
Libedit is an autotool- and libtoolized port of the NetBSD Editline library.
It provides generic line editing, history, and tokenization functions, similar
to those found in GNU Readline.

%package devel
Summary:	Development files for %{name}

Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	ncurses-devel%{?_isa}

%description devel
This package contains development files for %{name}.

%prep
%oreon_sha256

%autosetup -n %{name}-%{snap}-%{version}

%conf
# Fix unused direct shared library dependencies.
sed -i "s/lncurses/ltinfo/" configure

%build
%configure --disable-static --disable-silent-rules

%make_build

%install
%make_install

%files
%license COPYING
%doc ChangeLog THANKS
%{_mandir}/man5/editrc.5*
%{_libdir}/%{name}.so.0{,.*}

%files devel
%doc examples/fileman.c examples/tc1.c examples/wtc1.c
%{_mandir}/man3/editline.3*
%{_mandir}/man3/el_*.3*
%{_mandir}/man7/editline.7*
%{_includedir}/histedit.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%dir %{_includedir}/editline
%{_includedir}/editline/readline.h

