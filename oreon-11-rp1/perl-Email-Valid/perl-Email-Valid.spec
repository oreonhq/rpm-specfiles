%global source0_hash 1c37a9b1bc76304859572b150a82c26bd4f12ec63d2d0b76505ac392104cb47f

Name:           perl-Email-Valid
Version:        1.204
Release:        5%{?dist}
Summary:        Check validity of internet email address
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Email-Valid
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Email-Valid-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  bind-utils
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Mail::Address)
BuildRequires:  perl(Scalar::Util)
# Tests
BuildRequires:  perl(Test::More)
# Optional tests
BuildRequires:  perl(Net::DNS)
BuildRequires:  perl(Net::Domain::TLD)

%description
This module determines whether an email address is well-formed, and optionally,
whether a mail host exists for the domain or whether the top level domain of 
the email address is valid.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Email-Valid-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/Email/
%{_mandir}/man3/*.3*

%changelog
%autochangelog
