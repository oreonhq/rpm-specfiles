%global source0_hash 23ef065897821337bdd16487e65e2a3798383348225c72cd762bb3741ad009b5

Name:           perl-MIME-EncWords
Version:        1.015.0
Release:        5%{?dist}
Summary:        Deal with RFC 2047 encoded words (improved)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MIME-EncWords
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEZUMI/MIME-EncWords-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
# MIME::Charset::USE_ENCODE is "Encode" on recent Perl
BuildRequires:  perl(Encode) >= 1.98
BuildRequires:  perl(Encode::Encoding)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(MIME::Base64) >= 2.13
BuildRequires:  perl(MIME::Charset) >= 1.10.1
# MIME::Charset::_Compat not used
BuildRequires:  perl(strict)
# Unicode::String not used
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(charnames)
# Encode::CN not used
# Encode::JP not used
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00
# MIME::Charset::USE_ENCODE is "Encode" on recent Perl
Requires:       perl(Encode) >= 1.98
Requires:       perl(MIME::Base64) >= 2.13
Requires:       perl(MIME::Charset) >= 1.10.1

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((MIME::Base64|MIME::Charset)\\)$

%description
MIME::EncWords is aimed to be another implementation of MIME::Words so that it
will achieve more exact conformance with RFC 2047 (former RFC 1522)
specifications. Additionally, it contains some improvements. Following synopsis
and descriptions are inherited from its inspirer, then added descriptions on
improvements (**) or changes and clarifications (*).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MIME-EncWords-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PERLLOCAL=1 NO_PACKLIST=1
%make_build

%install
%make_install
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc ARTISTIC Changes GPL README
%{perl_vendorlib}/Encode/
%{perl_vendorlib}/MIME/
%{perl_vendorlib}/POD2/
%{_mandir}/man3/Encode::MIME::EncWords.3pm*
%{_mandir}/man3/MIME::EncWords.3pm*
%{_mandir}/man3/POD2::JA::Encode::MIME::EncWords.3pm*
%{_mandir}/man3/POD2::JA::MIME::EncWords.3pm*

%changelog
%autochangelog
