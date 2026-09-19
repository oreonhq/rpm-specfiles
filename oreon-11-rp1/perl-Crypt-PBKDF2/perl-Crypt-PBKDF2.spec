%global source0_hash 18757189638932b309b34c45bb810aa3e4856e3ed580100017dade65793f46c0

Summary:	The PBKDF2 password hashing algorithm
Name:		perl-Crypt-PBKDF2
Version:	0.261630
Release:	1%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Crypt-PBKDF2
Source0:	https://cpan.metacpan.org/authors/id/A/AR/ARODLAND/Crypt-PBKDF2-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Module::Build::Tiny) >= 0.034
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Crypt::URandom)
BuildRequires:	perl(Digest) >= 1.16
BuildRequires:	perl(Digest::HMAC) >= 1.01
BuildRequires:	perl(Digest::SHA)
BuildRequires:	perl(Digest::SHA3) >= 0.22
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(Module::Runtime)
BuildRequires:	perl(Moo) >= 2
BuildRequires:	perl(Moo::Role) >= 2
BuildRequires:	perl(namespace::autoclean)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(strictures) >= 2
BuildRequires:	perl(Try::Tiny) >= 0.04
BuildRequires:	perl(Type::Tiny)
BuildRequires:	perl(Types::Standard) >= 1.000005
# Test Suite
BuildRequires:	perl(constant)
BuildRequires:	perl(Encode)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More)
# Dependencies
# (none)

Provides:       perl(Crypt::PBKDF2)
Provides:       perl(Crypt::PBKDF2)
%description
PBKDF2 is a secure password hashing algorithm that uses the techniques of "key
strengthening" to make the complexity of a brute-force attack arbitrarily high.
PBKDF2 uses any other cryptographic hash or cipher (by convention, usually
HMAC-SHA2, but Crypt::PBKDF2 is fully pluggable), and allows for an arbitrary
number of iterations of the hashing function, and a nearly unlimited output
hash size (up to 2**32-1 times the size of the output of the backend hash).
The hash is salted, as any password hash should be, and the salt may also be of
arbitrary size.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Crypt-PBKDF2-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test --verbose

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Crypt/
%{_mandir}/man3/Crypt::PBKDF2.3*
%{_mandir}/man3/Crypt::PBKDF2::Hash.3*
%{_mandir}/man3/Crypt::PBKDF2::Hash::DigestHMAC.3*
%{_mandir}/man3/Crypt::PBKDF2::Hash::HMACSHA1.3*
%{_mandir}/man3/Crypt::PBKDF2::Hash::HMACSHA2.3*
%{_mandir}/man3/Crypt::PBKDF2::Hash::HMACSHA3.3*

%changelog
%autochangelog
