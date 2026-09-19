%global source0_hash 29aaa007d0dea4a8d8db778cf191eadeca91c4e9883ba4a8e2dc4d54e8ccf20e

Name:           perl-Email-Find
Version:        0.10
Release:        49%{?dist}
Summary:        Find RFC 822 email addresses in plain text

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Email-Find
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Email-Find-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Email::Valid)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Mail::Address)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(Test::More)

%description
Email::Find is a module for finding a *subset* of RFC 822 email
addresses in arbitrary text (see the section on "CAVEATS"). The
addresses it finds are not guaranteed to exist or even actually be email
addresses at all (see the section on "CAVEATS"), but they will be valid
RFC 822 syntax.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Email-Find-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
