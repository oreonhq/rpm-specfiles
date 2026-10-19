%global source0_hash 776fb87529261caf5c9ee7027425e36889fab1996a501cb5030b67b3c9c67bfe
Name:           perl-Auth-Yubikey_WebClient
Version:        4.02
Release:        4%{?dist}
Summary:        Authenticating the Yubikey against the Yubico Web API
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            http://metacpan.org/dist/Auth-Yubikey_WebClient/
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MASSYN/Auth-Yubikey_WebClient-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Digest::HMAC_SHA1)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
