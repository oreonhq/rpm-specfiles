%global source0_hash d583bf5dacb4fef19379ab24348bfea230cca97c4e078e1836ad0a421200014e

Name:           perl-Authen-WebAuthn
Version:        0.005
Release:        4%{?dist}
Summary:        Library to add Web Authentication support to server applications
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Authen-WebAuthn
Source0:        https://cpan.metacpan.org/authors/id/M/MB/MBESSON/Authen-WebAuthn-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(CBOR::XS)
BuildRequires:  perl(constant)
BuildRequires:  perl(Crypt::OpenSSL::X509) >= 1.808
BuildRequires:  perl(Crypt::PK::ECC)
BuildRequires:  perl(Crypt::PK::RSA)
BuildRequires:  perl(Crypt::URandom)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Hash::Merge::Simple)
BuildRequires:  perl(JSON)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(Net::SSLeay) >= 1.88
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)

%description
This module lets you validate WebAuthn registration and authentication
responses.

Currently, it does not handle the generation of registration and
authentication requests.
The transmission of requests and responses from the application server to the
user's browser, and interaction with the WebAuthn browser API is also out of
scope and could be handled by a dedicated JS library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Authen-WebAuthn-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc README README.md
%{perl_vendorlib}/Authen
%{_mandir}/man3/Authen::WebAuthn.3*

%changelog
%autochangelog
