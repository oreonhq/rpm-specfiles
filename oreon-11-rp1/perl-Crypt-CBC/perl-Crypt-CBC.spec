%global source0_hash f4ddfb4dd6ac5013df8341bfa734d9c9ee0f10e2e71215ec8fe5bf780b7c9127

Summary:        Encrypt Data with Cipher Block Chaining Mode
Name:           perl-Crypt-CBC
Version:        3.07
Release:        2%{?dist}
# Upstream confirms that they're under the same license as perl.
# Wording in CBC.pm is less than clear, but still.
# https://github.com/cpan-authors/Lib-Crypt-CBC/issues/14
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-CBC
Source0:        https://www.cpan.org/modules/by-module/Crypt/Crypt-CBC-%{version}.tar.gz
Source1:        cbctest1.pl
Source2:        Crypt-CBC-GH6.pl
BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Crypt::Cipher::AES)
BuildRequires:  perl(Crypt::PBKDF2)
BuildRequires:  perl(Crypt::URandom)
BuildRequires:  perl(Digest::MD5) >= 2.00
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(File::Basename)
# Not available on 32-bit platforms (#1948957)
#BuildRequires:  perl(Math::Int128)
BuildRequires:  perl(Scalar::Util)
# Test Suite
BuildRequires:  perl(Encode)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More) >= 0.88
# Optional Tests
# Modules used for test suite, skipped when bootstrapping as
# some of these modules use Crypt::CBC themselves
%if 0%{!?perl_bootstrap:1} && ! (0%{?rhel} >= 7)
# Crypt::CAST5 not yet packaged in Fedora
BuildRequires:  perl(Crypt::DES)
BuildRequires:  perl(Crypt::Blowfish)
BuildRequires:  perl(Crypt::Blowfish_PP)
BuildRequires:  perl(Crypt::Rijndael)
%endif
# Crypt::IDEA doesn't need bootstrapping and we get extra test coverage by including it
BuildRequires:  perl(Crypt::IDEA)
# Dependencies
Requires:       perl(Crypt::Cipher::AES)
Requires:       perl(Scalar::Util)
# Optional module needed for CTR mode
Recommends:     perl(Math::Int128)

Provides:       perl(Crypt::CBC)
%description
This is Crypt::CBC, a Perl-only implementation of the cryptographic
cipher block chaining mode (CBC).  In combination with a block cipher
such as Crypt::DES or Crypt::IDEA, you can encrypt and decrypt
messages of arbitrarily long length.  The encrypted messages are
compatible with the encryption format used by SSLeay.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Crypt-CBC-%{version}

chmod -c 644 eg/*.pl

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

# Tests for #2235322, GH#6 (both require Crypt::Blowfish)
%if 0%{!?perl_bootstrap:1} && ! (0%{?rhel} >= 7)
PERL5LIB=%{buildroot}%{perl_vendorlib} perl %{SOURCE1}
PERL5LIB=%{buildroot}%{perl_vendorlib} perl %{SOURCE2}
%endif

%files
%license LICENSE
%doc Changes eg/ README SECURITY.md vulnerabilities.txt
%{perl_vendorlib}/Crypt/
%{_mandir}/man3/Crypt::CBC.3*

%changelog
%autochangelog
