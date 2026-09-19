%global source0_hash 27467e3644c8dfbb08e26e6d698a75ef7c1b1a810bda9fca50f922eea5429eb1

Name:           perl-Tree-DAG_Node
Version:        1.35
Release:        3%{?dist}
Summary:        Class for representing nodes in a tree
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Tree-DAG_Node
Source0:        https://cpan.metacpan.org/modules/by-module/Tree/Tree-DAG_Node-%{version}.tgz
BuildArch:      noarch
# Module Build ---------------------------------------------------------------
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  sed
# Module Runtime -------------------------------------------------------------
BuildRequires:  perl(File::Slurper) >= 0.014
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite -----------------------------------------------------------------
BuildRequires:  findutils
BuildRequires:  perl(File::Spec) >= 3.4
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(Test::More) >= 1.001002
BuildRequires:  perl(Test::Pod) >= 1.48
BuildRequires:  perl(utf8)
# Dependencies ---------------------------------------------------------------
# (none)

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

%check
make test
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"

%files
%license LICENSE
%doc Changes README scripts/ SECURITY.md
%{perl_vendorlib}/Tree/
%{_mandir}/man3/Tree::DAG_Node.3*

%changelog
%autochangelog
