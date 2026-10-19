%global source0_hash f4ddfb4dd6ac5013df8341bfa734d9c9ee0f10e2e71215ec8fe5bf780b7c9127
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
Summary:        Encrypt Data with Cipher Block Chaining Mode
Name:           perl-Crypt-CBC
Version:        3.07
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-CBC
Source0:        https://www.cpan.org/modules/by-module/Crypt/Crypt-CBC-%{version}.tar.gz
Source1:        cbctest1.pl
Source2:        Crypt-CBC-GH6.pl
BuildArch:      noarch
Requires:       perl(Crypt::Cipher::AES)
Requires:       perl(Scalar::Util)
Recommends:     perl(Math::Int128)
Provides:       perl(Crypt::CBC)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Crypt::Cipher::AES)
BuildRequires:  perl(Crypt::IDEA)
BuildRequires:  perl(Crypt::PBKDF2)
BuildRequires:  perl(Crypt::URandom)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
