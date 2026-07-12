%global source0_hash ed517bd765948cbee84113358744df2bfff3539badbb37d62037f2b28bbb2557

Name:		perl-DateTime-Calendar-Mayan 
Version:	0.0601 
Release:	48%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:	Mayan Long Count Calendar 
URL:		https://metacpan.org/release/DateTime-Calendar-Mayan
Source0:	https://cpan.metacpan.org/modules/by-module/DateTime/DateTime-Calendar-Mayan-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Module::Build::Compat)
# Runtime
BuildRequires:	perl(constant)
BuildRequires:	perl(DateTime) >= 0.15
BuildRequires:	perl(Params::Validate) >= 0.64
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
# Test Suite
BuildRequires:	perl(DateTime::Duration)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(warnings)
# Dependencies
# (none)

Provides:       perl(DateTime::Calendar::Mayan)
Provides:       perl(DateTime::Calendar::Mayan)
%description
An implementation of the Mayan Long Count, Haab, and Tzolkin calendars
as defined in "Calendrical Calculations The Millennium Edition".
Supplemented by "Frequently Asked Questions about Calendars".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n DateTime-Calendar-Mayan-%{version}

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
%doc Changes README Todo
%{perl_vendorlib}/DateTime/
%{_mandir}/man3/DateTime::Calendar::Mayan.3*

%changelog
%autochangelog
