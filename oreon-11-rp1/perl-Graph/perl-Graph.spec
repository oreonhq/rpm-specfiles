%global source0_hash 5c9a51f89efe7a36db288590bf66753f2417afd41b82363e39f2f3101d498065
%global cpan_version 0.9735
Name:           perl-Graph
Version:        %(echo '%{cpan_version}' | sed 's/\(\...\)\(.\)/\1.\2/')
Release:        1%{?dist}
Summary:        Perl module for dealing with graphs, the abstract data structures
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Graph
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETJ/Graph-%{cpan_version}.tar.gz
BuildArch:      noarch
Requires:       perl(Carp)
Requires:       perl(Data::Dumper)
Requires:       perl(Heap::Fibonacci)
Requires:       perl(Safe)
Requires:       perl(Set::Object) >= 1.40
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Cycle)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Heap::Fibonacci)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Math::Complex)
BuildRequires:  perl(Safe)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Set::Object)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Abbrev)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
This is Graph, a Perl module for dealing with graphs, the abstract
data structures. 
 
This is a full rewrite of the Graph module 0.2xx series as discussed
in the book "Mastering Algorithms with Perl", written by Jarkko
Hietaniemi (the undersigned), John Macdonald, and Jon Orwant,
and published by O'Reilly and Associates.  This rewrite is not
fully compatible with the 0.2xx series.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Graph-%{cpan_version}

# avoid extra dependencies
chmod 644 util/cover.sh

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
