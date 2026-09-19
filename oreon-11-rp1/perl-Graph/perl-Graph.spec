%global source0_hash 5c9a51f89efe7a36db288590bf66753f2417afd41b82363e39f2f3101d498065

%global cpan_version 0.9735

Name:           perl-Graph
# Keep 2-digit precision
Version:        %(echo '%{cpan_version}' | sed 's/\(\...\)\(.\)/\1.\2/')
Release:        2%{?dist}
Summary:        Perl module for dealing with graphs, the abstract data structures

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Graph
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETJ/Graph-%{cpan_version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time
BuildRequires:  perl(B::Deparse) >= 0.61
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Heap::Fibonacci) >= 0.80
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(overload)
BuildRequires:  perl(Safe)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Set::Object) >= 1.40
BuildRequires:  perl(Storable) >= 2.05
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(lib)
BuildRequires:  perl(Math::Complex)
BuildRequires:  perl(Test::More) >= 0.82
BuildRequires:  perl(Text::Abbrev)
# Optional tests
BuildRequires:  perl(Devel::Cycle)
Requires:       perl(Carp)
Requires:       perl(Data::Dumper)
Requires:       perl(Heap::Fibonacci)
Requires:       perl(Safe)
Requires:       perl(Set::Object) >= 1.40

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

%check
make test

%files
%doc README RELEASE DESIGN Changes TODO util
%{perl_vendorlib}/Graph*
%{_mandir}/man3/Graph*.3*

%changelog
%autochangelog
