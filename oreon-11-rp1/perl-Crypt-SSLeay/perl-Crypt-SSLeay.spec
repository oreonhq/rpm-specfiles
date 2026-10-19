%global source0_hash f5d34f813677829857cf8a0458623db45b4d9c2311daaebe446f9e01afa9ffe8
%bcond_with perl_Crypt_SSLeay_enables_network_test
Name:           perl-Crypt-SSLeay
Summary:        OpenSSL glue that provides LWP with HTTPS support
Version:        0.72
Release:        1%{?dist}
License:        Artistic-2.0
URL:            https://metacpan.org/release/Crypt-SSLeay
Source0:        https://cpan.metacpan.org/authors/id/N/NA/NANIS/Crypt-SSLeay-%{version}.tar.gz
Patch0:         Crypt-SSLeay-0.72-Do-not-use-SSLv2_client_method-with-OpenSSL-1.1.0.patch
Patch1:         Crypt-SSLeay-0.72-Fix-building-on-Perl-without-dot-in-INC.patch
Patch2:         Crypt-SSLeay-0.72-Use-ExtUtils-PkgConfig-to-discover-OpenSSL-if-availa.patch
Patch3:         Crypt-SSLeay-0.72-Use_TLS_client_method-with-OpenSSL-1.1.1.patch
%if %{with perl_Crypt_SSLeay_enables_network_test}
%endif
Requires:       /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem
Requires:       perl(XSLoader)
%global __provides_exclude %{?__provides_exclude:__provides_exclude|}^perl\\(DB\\)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(openssl)
# /oreon:deps
%description
These Perl modules provide support for the HTTPS protocol under the World-Wide
Web library for Perl (LWP), so that a LWP::UserAgent can make HTTPS GET, HEAD,
and POST requests.

This package contains Net::SSL module which is automatically loaded by
LWP::Protocol::https on HTTPS requests, and provides the necessary SSL glue
for that module to work.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Crypt-SSLeay-%{version} 
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

# Placate rpmlint
chmod -c -x lib/Net/SSL.pm

%build

perl Makefile.PL \
    --%{!?with_perl_Crypt_SSLeay_enables_network_test:no-}live-tests \
    INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}" \
    </dev/null
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -a -size 0 -delete
%{_fixperms} %{buildroot}
chmod -R u+w %{buildroot}/*
chmod -R 644 eg/*
chmod -R 644 certs/*
rm certs/ca-bundle.crt
ln -s /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem certs/ca-bundle.crt
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
