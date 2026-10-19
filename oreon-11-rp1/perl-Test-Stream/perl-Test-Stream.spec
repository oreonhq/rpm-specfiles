%global source0_hash e6d3e163dd658dd1f54859833390c820c07bc2ca9318686cbf06e4d78ffea7fb
Name:           perl-Test-Stream
Version:        1.302027
Release:        1%{?dist}
Summary:        Successor to Test::More and Test::Builder
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Stream
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Test-Stream-%{version}.tar.gz
BuildArch:      noarch
%if !%{defined perl_bootstrap}
%endif
Requires:       perl(utf8)
Suggests:       perl(Sub::Name) >= 0.11
Suggests:       perl(Sub::Util) >= 1.40
Suggests:       perl(Term::ReadKey) >= 2.03
Suggests:       perl(Unicode::GCString) >= 2013.10
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(PerlIO)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Sub::Util)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Trace::Mask)
BuildRequires:  perl(Trace::Mask::Reference)
BuildRequires:  perl(Unicode::GCString)
BuildRequires:  perl(base)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
