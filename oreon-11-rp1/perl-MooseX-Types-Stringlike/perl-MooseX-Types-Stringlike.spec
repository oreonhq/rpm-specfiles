%global source0_hash 2ee349ec5c529a6f347f42ff640e47b245564b93cca305df63c7821f5b55cf19

Name:		perl-MooseX-Types-Stringlike
Summary:	Moose type constraints for strings or string-like objects
Version:	0.003
Release:	34%{?dist}
License:	Apache-2.0
URL:		https://metacpan.org/release/MooseX-Types-Stringlike
Source0:	https://cpan.metacpan.org/modules/by-module/MooseX/MooseX-Types-Stringlike-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.17
# Module Runtime
BuildRequires:	perl(MooseX::Types)
BuildRequires:	perl(MooseX::Types::Moose)
BuildRequires:	perl(overload)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Test::More) >= 0.96
BuildRequires:	perl(version)
# Optional Test Requirements
BuildRequires:	perl(CPAN::Meta)
BuildRequires:	perl(CPAN::Meta::Requirements) >= 2.120900
# Dependencies
# (none)

Provides:       perl(MooseX::Types::Stringlike)
%description
This module provides a more general version of the Str type. If coercions are
enabled, it will accept objects that overload stringification and coerces them
into strings.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n MooseX-Types-Stringlike-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING README
%{perl_vendorlib}/MooseX/
%{_mandir}/man3/MooseX::Types::Stringlike.3*

%changelog
%autochangelog
