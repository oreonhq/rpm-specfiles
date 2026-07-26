%global source0_hash e6d3e163dd658dd1f54859833390c820c07bc2ca9318686cbf06e4d78ffea7fb

Name:           perl-Test-Stream
Version:        1.302027
Release:        36%{?dist}
Summary:        Successor to Test::More and Test::Builder
# The license URL in COPYRIGHT POD sections is wrong,
# <https://github.com/Test-More/Test-Stream/issues/66>
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Stream
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Test-Stream-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(B)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
# Optional run-time:
BuildRequires:  perl(Sub::Name) >= 0.11
BuildRequires:  perl(Sub::Util) >= 1.40
BuildRequires:  perl(Term::ReadKey) >= 2.03
BuildRequires:  perl(Unicode::GCString) >= 2013.10
# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(PerlIO)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
# Optional test:
# Break build-cycle: perl-Test-Stream → perl-Trace-Mask → perl-Test-Stream
%if !%{defined perl_bootstrap}
BuildRequires:  perl(Trace::Mask) >= 0.000005
BuildRequires:  perl(Trace::Mask::Reference)
%endif
Requires:       perl(utf8)
# Optional run-time:
Suggests:       perl(Sub::Name) >= 0.11
Suggests:       perl(Sub::Util) >= 1.40
Suggests:       perl(Term::ReadKey) >= 2.03
Suggests:       perl(Unicode::GCString) >= 2013.10

%description
This is a framework for writing and running tests in Perl. Test::Stream is
inspired by Test::Builder, but it provides a much more sane approach. Bundles
and Tools are kept separate, this way you can always use tools without being
forced to adopt the authors ideal bundle.

This distribution is deprecated in favor of Test2.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Stream-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
# README.md duplicates README's content
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
