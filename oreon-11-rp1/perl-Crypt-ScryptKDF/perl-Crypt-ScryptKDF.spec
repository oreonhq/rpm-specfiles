%global source0_hash 7d16ee95cce3eb54c174673a7299f4c086fba3ac85f847d0e134feed5f776017

Name:           perl-Crypt-ScryptKDF
Version:        0.010
Release:        35%{?dist}
Summary:        Scrypt password based key derivation function
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-ScryptKDF
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIK/Crypt-ScryptKDF-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# Run-time
BuildRequires:  perl(Exporter) >= 5.59
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(XSLoader)

# Testing
BuildRequires:  perl(Crypt::OpenSSL::Random)
BuildRequires:  perl(Test::More)

# a strong PRNG required, the simplest one
Requires:       perl(Crypt::OpenSSL::Random)

%description
Scrypt is a password-based key derivation function (like for example
PBKDF2). Scrypt was designed to be "memory-hard" algorithm in order to make
it expensive to perform large scale custom hardware attacks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Crypt-ScryptKDF-%{version}

%build
perl Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%{!?_licensedir:%global license %doc}
%license LICENSE
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Crypt*
%{_mandir}/man3/*

%changelog
%autochangelog
