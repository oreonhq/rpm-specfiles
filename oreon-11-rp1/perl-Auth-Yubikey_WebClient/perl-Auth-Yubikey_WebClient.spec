%global source0_hash 776fb87529261caf5c9ee7027425e36889fab1996a501cb5030b67b3c9c67bfe

Name:           perl-Auth-Yubikey_WebClient
Version:        4.02
Release:        4%{?dist}
Summary:        Authenticating the Yubikey against the Yubico Web API
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            http://metacpan.org/dist/Auth-Yubikey_WebClient/
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MASSYN/Auth-Yubikey_WebClient-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Digest::HMAC_SHA1) >= 1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(LWP::UserAgent) >= 1
BuildRequires:  perl(MIME::Base64) >= 1
BuildRequires:  perl(URI::Escape) >= 1
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
BuildRequires:  perl(Test::Pod) >=  1.22

%description
Authenticate against the Yubico server via the Web API in Perl.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# 4.0.2 tarball is malformed
#setup -q -n Auth-Yubikey_WebClient-%%{version}
%setup -q -n Auth-Yubikey_WebClient-master

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Auth
%{_mandir}/man3/Auth::Yubikey_WebClient.3pm*

%changelog
%autochangelog
