Name:           perl-UNIVERSAL-isa
Version:        1.20171012
Release:        25%{?dist}
Summary:        Hack around module authors using UNIVERSAL::isa as a function
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/UNIVERSAL-isa
Source0:        https://cpan.metacpan.org/modules/by-module/UNIVERSAL/UNIVERSAL-isa-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
BuildRequires:  perl(warnings::register)
# Test Suite
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(overload)
# Optional Tests
BuildRequires:  perl(CPAN::Meta) >= 2.120900
# Dependencies
# (none)

%description
Whenever you use "isa" in UNIVERSAL as a function, a kitten using
Test::MockObject dies. Normally, the kittens would be helpless, but
if they use UNIVERSAL::isa (the module whose docs you are reading),
the kittens can live long and prosper.

This module replaces UNIVERSAL::isa with a version that makes sure
that if it's called as a function on objects which override isa,
isa will be called on those objects as a method.

In all other cases the real UNIVERSAL::isa is just called directly.

%prep
%setup -q -n UNIVERSAL-isa-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENCE
%doc Changes CONTRIBUTING README
%{perl_vendorlib}/UNIVERSAL/
%{_mandir}/man3/UNIVERSAL::isa.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.20171012-25
- Prepare for Oreon 11 (RP1)
