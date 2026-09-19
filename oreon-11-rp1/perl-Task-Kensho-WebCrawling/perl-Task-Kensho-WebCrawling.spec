%global source0_hash e6dcee9f897b69c6eb64a46634ef6336a36c6818023cc51f39acb501534645ef

Name:           perl-Task-Kensho-WebCrawling
Version:        0.41
Release:        13%{?dist}
Summary:        Glimpse at an Enlightened Perl (Web Crawling)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Task-Kensho-WebCrawling
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Task-Kensho-WebCrawling-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6.0
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
# No run-time dependency is needed for tests.
# Tests
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
Requires:       perl(Attean)
Requires:       perl(HTTP::BrowserDetect)
Requires:       perl(HTTP::Thin)
Requires:       perl(HTTP::Tiny)
Requires:       perl(LWP::Simple)
Requires:       perl(LWP::UserAgent)
Requires:       perl(Mojo::UserAgent)
Requires:       perl(WWW::Mechanize)
Requires:       perl(WWW::Mechanize::TreeBuilder)
Requires:       perl(WWW::Selenium)

%description
Task::Kensho is a list of recommended modules for Enlightened Perl
development. CPAN is wonderful, but there are too many wheels and you have
to pick and choose amongst the various competing technologies.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Task-Kensho-WebCrawling-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENCE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
