%global source0_hash 1a813dbdc05c3fbd9dd39dbcfd85e2cfb0ba3d0f652cf6b26ec83ab8146ddc77

Name:           perl-Authen-OATH
Version:        2.0.1
Release:        27%{?dist}
Summary:        OATH One Time Passwords
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Authen-OATH
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/Authen-OATH-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(Digest::HMAC)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Moo) >= 2.002004
BuildRequires:  perl(Types::Standard)
# Tests only:
BuildRequires:  perl(Digest::SHA)
# Pod::Coverage::TrustPod not used
# Pod::Wordlist not used
# Test::CPAN::Changes not used
# Test::Code::TidyAll 0.24 not used
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Needs)
# Test::Spelling not used
# Test::Synopsis not used
# Optional tests:
BuildRequires:  perl(bignum)
BuildRequires:  perl(Pod::Coverage) >= 0.18
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
# Default digest algorithm, also SHA1 is needed by HOTP specification.
Requires:       perl(Digest::SHA)

%description
Implementation of the HOTP and TOTP One Time Password algorithms as defined by
OATH (http://www.openauthentication.org).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Authen-OATH-%{version}
for F in Changes; do
    sed -e 's/\r//' <"$F" >"${F}.unix"
    touch -r "$F" "${F}.unix"
    mv "${F}.unix" "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTORS README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
