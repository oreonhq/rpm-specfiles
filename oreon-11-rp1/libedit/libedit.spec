# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 21362b00653bbfc1c71f71a7578da66b5b5203559d43134d2dd7719e313ce041
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%global snap 20251016

# Build man pages with mdoc2man.awk to avoid circular dependencies
%bcond bootstrap 0

Summary:	The NetBSD Editline library
Name:		libedit
Version:	3.1
Release:	58.%{snap}cvs%{?dist}

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
Source:        https://www.thrysoee.dk/editline//libedit-20251016-3.1.tar.gz

BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	ncurses-devel

%if %{without bootstrap}
BuildRequires:	groff-base
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
%oreon_verify_sources
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

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.1-58.
- Prepare for Oreon 11 (RP1)
