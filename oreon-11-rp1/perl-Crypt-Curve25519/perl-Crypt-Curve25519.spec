%global source0_hash 42eb902b44e434abcdc636435739c4e439fd083fdd561fb005cfc5772c2d179e
Name:		perl-Crypt-Curve25519
Version:	0.08
Release:        1%{?dist}
Summary:        Generate shared secret using elliptic-curve Diffie-Hellman function
License:	(GPL-1.0-or-later OR Artistic-1.0-Perl) AND BSD-3-Clause
URL:		https://metacpan.org/release/Crypt-Curve25519
Source0:        https://www.cpan.org/modules/by-module/Crypt/Crypt-Curve25519-%{version}.tar.gz
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Curve25519 is a Diffie-Hellman function suitable for a wide variety of
applications.

Given a user's 32-byte secret key, Curve25519 computes the user's 32-byte
public key. Given the user's 32-byte secret key and another user's 32-byte
public key, Curve25519 computes a 32-byte secret shared by the two users. This
secret can then be used to authenticate and encrypt messages between the two
users.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Crypt-Curve25519-%{version}

%build

perl Makefile.PL \
	INSTALLDIRS=vendor \
	NO_PACKLIST=1 \
	NO_PERLLOCAL=1 \
	OPTIMIZE="%{optflags}"
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
