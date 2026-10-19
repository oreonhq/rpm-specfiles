%global source0_hash 18757189638932b309b34c45bb810aa3e4856e3ed580100017dade65793f46c0
Summary:        The PBKDF2 password hashing algorithm
Name:		perl-Crypt-PBKDF2
Version:	0.261630
Release:        1%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Crypt-PBKDF2
Source0:        https://cpan.metacpan.org/authors/id/A/AR/ARODLAND/Crypt-PBKDF2-%{version}.tar.gz
BuildArch:	noarch
Provides:       perl(Crypt::PBKDF2)
Provides:       perl(Crypt::PBKDF2)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(Carp)
BuildRequires:  perl(Crypt::URandom)
BuildRequires:  perl(Digest)
BuildRequires:  perl(Digest::HMAC)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Digest::SHA3)
BuildRequires:  perl(Encode)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Type::Tiny)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(constant)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(strictures)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test --verbose
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
