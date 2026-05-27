%global source0_hash 9d7be8a56d1bedda05c425306cc504ba134307e0c09bda4a788c98744ebcd95d

%if ! (0%{?rhel})
%{bcond_without perl_Net_SSLeay_enables_optional_test}
%else
%{bcond_with perl_Net_SSLeay_enables_optional_test}
%endif

# OpenSSL ENGINE support deprecated in Fedora 41 onwards
# https://fedoraproject.org/wiki/Changes/OpensslDeprecateEngine
%if 0%{?fedora} > 40 || 0%{?rhel} > 9
%global _preprocessor_defines %{?_preprocessor_defines} -DOPENSSL_NO_ENGINE
%endif

Name:		perl-Net-SSLeay
Version:	1.94
Release:	12%{?dist}
Summary:	Perl extension for using OpenSSL
License:	Artistic-2.0
URL:		https://metacpan.org/release/Net-SSLeay
Source0:	https://cpan.metacpan.org/authors/id/C/CH/CHRISN/Net-SSLeay-1.94.tar.gz

Patch0:		https://patch-diff.githubusercontent.com/raw/radiator-software/p5-net-ssleay/pull/514.patch
Patch10:	Net-SSLeay-1.90-pkgconfig.patch
# =========== Module Build ===========================
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
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
# =========== Module Runtime =========================
BuildRequires:	perl(AutoLoader)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Errno)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(Socket)
BuildRequires:	perl(vars)
BuildRequires:	perl(XSLoader)
# =========== Test Suite =============================
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
# =========== Optional Tests =========================
%if %{with perl_Net_SSLeay_enables_optional_test}
BuildRequires:	perl(Crypt::OpenSSL::Bignum)
# Test::Kwalitee 1.00 not used
BuildRequires:	perl(Test::Pod) >= 1.41
# Test::Pod::Coverage 1.00 not used
%endif
# =========== Module Dependencies ====================
Requires:	perl(MIME::Base64)
Requires:	perl(XSLoader)

# Don't "provide" private Perl libs or the redundant unversioned perl(Net::SSLeay) provide
%global __provides_exclude ^(perl\\(Net::SSLeay\\)$|SSLeay\\.so)

%description
This module offers some high level convenience functions for accessing
web pages on SSL servers (for symmetry, same API is offered for
accessing http servers, too), a sslcat() function for writing your own
clients, and finally access to the SSL API of SSLeay/OpenSSL package
so you can write servers or clients for more complicated applications.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n Net-SSLeay-%{version}

# Fix for test suite compatibility with OpenSSL 3.4
%patch -P 0 -p 1

# Get libraries to link against from pkg-config
# https://github.com/radiator-software/p5-net-ssleay/pull/127
%patch -P 10

# Fix permissions in examples to avoid bogus doc-file dependencies
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

# Remove script we don't want packaged
rm -f %{buildroot}%{perl_vendorarch}/Net/ptrtstrun.pl

# Remove private key and related script from documentation
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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.94-12
- Prepare for Oreon 11 (RP1)
