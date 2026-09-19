%global source0_hash 476b3ab3b47d534e4d6a0f4990021d5d34c69ec937ac0716e66ce8a7bc879958

Name:           perl-Test-WWW-Mechanize-PSGI
Version:        0.39
Release:        21%{?dist}
Summary:        Test PSGI programs using WWW::Mechanize
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-WWW-Mechanize-PSGI
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/Test-WWW-Mechanize-PSGI-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__perl}
BuildRequires:  %{__make}

BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(CGI::Cookie)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Message::PSGI)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::WWW::Mechanize)
BuildRequires:  perl(Try::Tiny)

BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%description
PSGI is a specification to decouple web server environments from web
application framework code. Test::WWW::Mechanize is a subclass of
WWW::Mechanize that incorporates features for web application testing. The
Test::WWW::Mechanize::PSGI module meshes the two to allow easy testing of
PSGI applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-WWW-Mechanize-PSGI-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}

%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
