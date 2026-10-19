%global source0_hash a367fc74cbcfe9bedc626fff79ce6c5c3ea404c04414f80746cb3ab36acfbb71
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%global gap_pkgname    browse
%global gap_upname     Browse
%global gap_makedoc    makedocrel.g
%global gap_skip_check 1
%bcond bootstrap 0
Name:           gap-pkg-%{gap_pkgname}
Version:        1.8.23
Release:        1%{?dist}
Summary:        GAP browser for 2-dimensional arrays of data
License:        GPL-3.0-or-later
URL:            https://www.math.rwth-aachen.de/~Browse/
Source0:        https://www.math.rwth-aachen.de/~%{gap_upname}//%{gap_upname}-%{version}.tar.bz2
ExcludeArch:    %{ix86}
BuildSystem:    gap
BuildOption(build): --packagedirs ..
BuildOption(install): app bibl bin lib tst version
BuildOption(check): tst/testall.g
%if %{without bootstrap}
%endif
Requires:       gap-core%{?_isa}
Recommends:     gap-pkg-atlasrep
Recommends:     gap-pkg-io%{?_isa}
Recommends:     gap-pkg-tomlib
%global __provides_exclude_from ncurses\\.so
# oreon:deps
BuildRequires:  GAPDoc-doc
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-atlasrep-doc
BuildRequires:  gap-pkg-ctbllib-doc
BuildRequires:  gap-pkg-io-doc
BuildRequires:  gap-pkg-tomlib
BuildRequires:  gcc
BuildRequires:  ghostscript
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  netpbm-progs
BuildRequires:  pkgconfig(ncurses)
# /oreon:deps
%description
The motivation for this package was to develop functions for an interactive
display of two-dimensional arrays of data, for example character tables.  They
should be displayed with labeled rows and columns, the display should allow
some markup for fonts or colors, it should be possible to search for entries,
to sort rows or columns, to hide and unhide information, to bind commands to
keys, and so on.

To achieve this our package now provides three levels of functionality, where
in particular the first level may also be used for completely other types of
applications:
- A low level interface to ncurses: This may be interesting for all kinds of
  applications which want to display text with some markup and colors, maybe
  in several windows, using the available capabilities of a terminal.
- A medium level interface to a generic function NCurses.BrowseGeneric: We
  introduce a new operation Browse which is meant as an interactive version of
  Display for GAP objects.  Then we provide a generic function for browsing
  two-dimensional arrays of data, handles labels for rows and columns,
  searching, sorting, binding keys to actions, etc.  This is for users who
  want to implement new methods for browsing two-dimensional data.
- Applications of these interfaces: We provide some applications of the
  ncurses interface and of the function NCurses.BrowseGeneric.  These may be
  interesting for end users, and also as examples for programmers of further
  applications.  This includes a method for browsing character tables, several
  games, and an interface for demos.

%package doc
License:        GPL-3.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Gap browser documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       GAPDoc-doc
Requires:       gap-pkg-io-doc
%if %{without bootstrap}
Requires:       gap-pkg-atlasrep-doc
Requires:       gap-pkg-ctbllib-doc
%endif
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%conf
# Give an executable script a shebang
sed -i '1i#!/bin/sh' bibl/getnewestbibfile

%build -p

./configure %{gap_archdir}
%make_build
%build -a

rm tst/*~
sed -i "s,$PWD/\.\./pkg,..,g" doc/*.html
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-browse-doc -f %{oreon_filedir}/gap-pkg-browse-doc.list

%changelog

%autochangelog
