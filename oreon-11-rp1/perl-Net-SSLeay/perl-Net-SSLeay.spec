# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash ab213691685fb2a576c669cbc8d9266f8165a31563ad15b7c4030b94adfc0753
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%if ! (0%{?rhel} || 0%{?oreon})
%{bcond_without perl_Net_SSLeay_enables_optional_test}
%else
%{bcond_with perl_Net_SSLeay_enables_optional_test}
%endif

%if 0%{?fedora} > 40 || 0%{?rhel} > 9 || 0%{?oreon}
%global _preprocessor_defines %{?_preprocessor_defines} -DOPENSSL_NO_ENGINE
%endif

Name:		perl-Net-SSLeay
Version:	1.96
Release:	1%{?dist}
Summary:	Perl extension for using OpenSSL
License:	Artistic-2.0
URL:		https://metacpan.org/release/Net-SSLeay
Source0:	https://cpan.metacpan.org/modules/by-module/Net/Net-SSLeay-%{version}.tar.gz
Patch0:		https://patch-diff.githubusercontent.com/raw/radiator-software/p5-net-ssleay/pull/553.patch
Patch10:	Net-SSLeay-1.90-pkgconfig.patch
BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	openssl
BuildRequires:	openssl-devel
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(constant)
BuildRequires:	perl(English)
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(ExtUtils::PkgConfig)
BuildRequires:	perl(ExtUtils::MM)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(Symbol)
BuildRequires:	perl(Text::Wrap)
BuildRequires:	perl(utf8)
BuildRequires:	perl(AutoLoader)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Errno)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(Socket)
BuildRequires:	perl(vars)
BuildRequires:	perl(XSLoader)
BuildRequires:	perl(base)
BuildRequires:	perl(Config)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(HTTP::Tiny)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(IO::Socket::INET)
BuildRequires:	perl(lib)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(SelectSaver)
BuildRequires:	perl(Storable)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(Test::More) >= 0.61
BuildRequires:	perl(threads)
BuildRequires:	perl(warnings)
%if %{with perl_Net_SSLeay_enables_optional_test}
BuildRequires:	perl(Crypt::OpenSSL::Bignum)
BuildRequires:	perl(Test::Pod) >= 1.41
%endif
Requires:	perl(MIME::Base64)
Requires:	perl(XSLoader)

%global __provides_exclude ^(perl\\(Net::SSLeay\\)$|SSLeay\\.so)

%description
This module offers some high level convenience functions for accessing
web pages on SSL servers (for symmetry, same API is offered for
accessing http servers, too), a sslcat() function for writing your own
clients, and finally access to the SSL API of SSLeay/OpenSSL package
so you can write servers or clients for more complicated applications.

%prep
%oreon_sha256
%setup -q -n Net-SSLeay-%{version}

%patch -P0 -p1

%patch -P 10

chmod -c 644 examples/*

%build
unset OPENSSL_PREFIX
PERL_MM_USE_DEFAULT=1 perl Makefile.PL \
	INSTALLDIRS=vendor \
	NO_PACKLIST=1 \
	NO_PERLLOCAL=1 \
	OPTIMIZE="%{optflags}" < /dev/null
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

rm -f %{buildroot}%{perl_vendorarch}/Net/ptrtstrun.pl

rm -f examples/cb-testi.pl
rm -f examples/server_key.pem

%check
unset RELEASE_TESTING
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING.md Credits QuickRef README examples/
%{perl_vendorarch}/auto/Net/
%dir %{perl_vendorarch}/Net/
%{perl_vendorarch}/Net/SSLeay/
%{perl_vendorarch}/Net/SSLeay.pm
%doc %{perl_vendorarch}/Net/SSLeay.pod
%{_mandir}/man3/Net::SSLeay.3*
%{_mandir}/man3/Net::SSLeay::Handle.3*

%changelog
%autochangelog
