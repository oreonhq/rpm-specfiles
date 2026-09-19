%global source0_hash 8672f020f2091a1ae9476284c932b4ad8b8ee7b1ec11569efc3dc4b3e753578f

Name:       perl-Data-TreeDumper
Version:    0.43
Release:    1%{?dist}
# see TreeDumper.pm
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:    Improved replacement for Data::Dumper
Source:     https://cpan.metacpan.org/authors/id/N/NK/NKH/Data-TreeDumper-%{version}.tar.gz
Url:        https://metacpan.org/release/Data-TreeDumper
BuildArch:  noarch

BuildRequires: coreutils
BuildRequires: make
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(Carp)
BuildRequires: perl(Check::ISA)
BuildRequires: perl(Class::ISA)
BuildRequires: perl(constant)
BuildRequires: perl(Devel::Size) >= 0.58
BuildRequires: perl(Exporter)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires: perl(Sort::Naturally)
BuildRequires: perl(strict)
BuildRequires: perl(Term::Size) >= 0.2
BuildRequires: perl(Test)
BuildRequires: perl(Text::Wrap) >= 2001.0929
BuildRequires: perl(warnings)

# not automagically picked up
Requires: perl(Term::Size) >= 0.2

%description
Data::Dumper and other modules do a great job of dumping data structures.
Their output, however, often takes more brain power to understand than the
data itself.  When dumping large amounts of data, the output can be
overwhelming and it can be difficult to see the relationship between each
piece of the dumped data.

Data::TreeDumper also dumps data in a tree-like fashion but hopefully in a
format more easily understood.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-TreeDumper-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

# hrm.
find %{buildroot} -name '*.pl' -delete

%check
make test

%files
%doc README Todo *.pl
%{perl_vendorlib}/Data*
%{_mandir}/man3/Data::TreeDumper*.3*

%changelog
%autochangelog
