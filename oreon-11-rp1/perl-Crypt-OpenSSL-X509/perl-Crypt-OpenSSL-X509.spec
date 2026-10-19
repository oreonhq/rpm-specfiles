%global source0_hash 3344824f839ea10e941a10a72c2e55f917cfef049914576540dc954d143b3fa6
Name:           perl-Crypt-OpenSSL-X509
Version:        2.0.1
Release:        5%{?dist}
Summary:        Perl interface to OpenSSL for X509
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-OpenSSL-X509
Source0:        https://cpan.metacpan.org/authors/id/J/JO/JONASBN/Crypt-OpenSSL-X509-%{version}.tar.gz
Patch0:         Crypt-OpenSSL-X509-1.914-Do-not-hard-code-CFLAGS.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  perl(Config)
BuildRequires:  perl(Convert::ASN1)
BuildRequires:  perl(Crypt::OpenSSL::Guess)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Crypt::OpenSSL::X509 - Perl extension to OpenSSL's X509 API.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Crypt-OpenSSL-X509-%{version}
%patch -P 0 -p1

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
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
