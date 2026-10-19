%global source0_hash 2ee349ec5c529a6f347f42ff640e47b245564b93cca305df63c7821f5b55cf19
Name:		perl-MooseX-Types-Stringlike
Summary:        Moose type constraints for strings or string-like objects
Version:	0.003
Release:        34%{?dist}
License:	Apache-2.0
URL:		https://metacpan.org/release/MooseX-Types-Stringlike
Source0:        https://cpan.metacpan.org/modules/by-module/MooseX/MooseX-Types-Stringlike-%{version}.tar.gz
BuildArch:	noarch
Provides:       perl(MooseX::Types::Stringlike)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
