%global source0_hash 03bc2471a7e6aa927ba313eda7d73c50820694e801a5bbe2fddcded8f493b67f

Name:		perl-Params-Coerce
Version:	0.15
Release:	16%{?dist}
Summary:	Allows your classes to do coercion of parameters
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Params-Coerce
Source0:	https://cpan.metacpan.org/modules/by-module/Params/Params-Coerce-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Params::Util) >= 0.05
BuildRequires:	perl(Scalar::Util) >= 1.11
BuildRequires:	perl(strict)
# Test Suite
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::More) >= 0.47
BuildRequires:	perl(vars)
BuildRequires:	perl(warnings)
# Dependencies

Provides:       perl(Params::Coerce)
Provides:       perl(Params::Coerce)
%description
A big part of good API design is that we should be able to be flexible in
the ways that we take parameters. Params::Coerce attempts to encourage this,
by making it easier to take a variety of different arguments, while adding
negligible additional complexity to your code.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Params-Coerce-%{version}

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
%{perl_vendorlib}/Params/
%{_mandir}/man3/Params::Coerce.3*

%changelog
%autochangelog
