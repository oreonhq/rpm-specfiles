%global source0_hash ab213691685fb2a576c669cbc8d9266f8165a31563ad15b7c4030b94adfc0753
%{bcond_with perl_Net_SSLeay_enables_optional_test}
Name:		perl-Net-SSLeay
Version:	1.96
Release:        1%{?dist}
Summary:        Perl extension for using OpenSSL
License:	Artistic-2.0
URL:		https://metacpan.org/release/Net-SSLeay
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHRISN/Net-SSLeay-%{version}.tar.gz
Patch10:	Net-SSLeay-1.90-pkgconfig.patch
%if %{with perl_Net_SSLeay_enables_optional_test}
%endif
Requires:	perl(MIME::Base64)
Requires:	perl(XSLoader)
%global __provides_exclude ^(perl\\(Net::SSLeay\\)$|SSLeay\\.so)
Provides:       perl(Net::SSLeay)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(English)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MM)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(SelectSaver)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module offers some high level convenience functions for accessing
web pages on SSL servers (for symmetry, same API is offered for
accessing http servers, too), a sslcat() function for writing your own
clients, and finally access to the SSL API of SSLeay/OpenSSL package
so you can write servers or clients for more complicated applications.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Net-SSLeay-%{version}

# Fix for test suite compatibility with OpenSSL 3.4

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
rm -f %{buildroot}%{perl_vendorarch}/Net/ptrtstrun.pl
rm -f examples/cb-testi.pl
rm -f examples/server_key.pem
%oreon_autofiles main

%check

unset RELEASE_TESTING
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
