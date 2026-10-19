%global source0_hash 535d854eed040d4fe96c93bb78454b22a96436a761ab9ea799590a2d3462ad08
%bcond check 1
Name:           perl-Chemistry-Canonicalize
Version:        0.11
Release:        1%{?dist}
Summary:        Number the atoms in a molecule in a unique way
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Chemistry-Canonicalize
Source0:        https://cpan.metacpan.org/authors/id/I/IT/ITUB/Chemistry-Canonicalize-%{version}.tar.gz
%if %{with check}
%endif
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides functions for "canonicalizing" a molecular
structure; that is, to number the atoms in a unique way regardless of
the input order.

The canonicalization algorithm is based on: Weininger, et. al., J. Chem.
Inf. Comp. Sci. 29[2], 97-101 (1989)

This module is part of the PerlMol project.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Chemistry-Canonicalize-%{version}
chmod -x README

%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" \
  NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build
%install
%make_install
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} '%{buildroot}'/*
%oreon_autofiles main
%if %{with check}
%check

make test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
