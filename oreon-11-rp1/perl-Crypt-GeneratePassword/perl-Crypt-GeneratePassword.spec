%global source0_hash d69f3756bcfd79a9b9985fadef33909f62989590322a21163f93d75293019b66

Name:           perl-Crypt-GeneratePassword
Version:        0.05
Release:        30%{?dist}
Summary:        Generate secure random pronounceable passwords
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-GeneratePassword
Source0:        https://cpan.metacpan.org/modules/by-module/Crypt/Crypt-GeneratePassword-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Test::More)

%description
Crypt::GeneratePassword generates random passwords that are (more or less)
pronounceable. Unlike Crypt::RandPasswd, it doesn't use the FIPS-181 NIST
standard, which is proven to be insecure. It does use a similar interface,
so it should be a drop-in replacement in most cases.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Crypt-GeneratePassword-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Crypt*
%{_mandir}/man3/Crypt*

%changelog
%autochangelog
