%global source0_hash 29aaa007d0dea4a8d8db778cf191eadeca91c4e9883ba4a8e2dc4d54e8ccf20e
Name:           perl-Email-Find
Version:        0.10
Release:        1%{?dist}
Summary:        Find RFC 822 email addresses in plain text
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Email-Find
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Email-Find-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Email::Valid)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Mail::Address)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
