%global source0_hash 08cd4ad238d76b33a156e29e24ecf5f2405191d109ac854d8b47e6b267668c69

Name:           perl-Authen-U2F
Version:        0.003
Release:        10%{?dist}
Summary:        FIDO U2F library
# All but examples/demoserver/u2f-api.js is GPL-1.0-or-later OR Artistic-1.0-Perl
# examples/demoserver/u2f-api.js is BSD-3-Clause
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND BSD-3-Clause
URL:            https://metacpan.org/dist/Authen-U2F
Source0:        https://cpan.metacpan.org/authors/id/R/RO/ROBN/Authen-U2F-%{version}.tar.gz
# https://github.com/robn/Authen-U2F/issues/8
# https://developers.google.com/open-source/licenses/bsd
Source1:        bsd
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(Crypt::OpenSSL::X509) >= 1.806
BuildRequires:  perl(Crypt::PK::ECC)
BuildRequires:  perl(CryptX) >= 0.034
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Exporter::Tiny)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(JSON)
BuildRequires:  perl(Math::Random::Secure)
BuildRequires:  perl(MIME::Base64) >= 3.11
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Type::Params)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(warnings)

%description
This module provides the tools you need to add support for U2F in your
application.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Authen-U2F-%{version}
install -p -m 0644 %{SOURCE1} .

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%make_build test

%files
%doc Changes README
%license LICENSE bsd
%{perl_vendorlib}/Authen/
%{_mandir}/man3/Authen::U2F.3pm*

%changelog
%autochangelog
