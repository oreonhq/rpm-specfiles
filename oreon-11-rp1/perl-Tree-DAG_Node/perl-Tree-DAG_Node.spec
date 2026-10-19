%global source0_hash 27467e3644c8dfbb08e26e6d698a75ef7c1b1a810bda9fca50f922eea5429eb1
Name:           perl-Tree-DAG_Node
Version:        1.35
Release:        1%{?dist}
Summary:        Class for representing nodes in a tree
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Tree-DAG_Node
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSAVAGE/Tree-DAG_Node-%{version}.tgz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Slurper)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
This class encapsulates/makes/manipulates objects that represent nodes in a
tree structure. The tree structure is not an object itself, but is emergent
from the linkages you create between nodes. This class provides the methods
for making linkages that can be used to build up a tree, while preventing you
from ever making any kinds of linkages that are not allowed in a tree (such as
having a node be its own mother or ancestor, or having a node have two
mothers).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Tree-DAG_Node-%{version}

# Fix up shellbangs in example scripts
sed -i -e 's|^#!/usr/bin/env perl|#!/usr/bin/perl|' scripts/*.pl

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
