%global source0_hash 507e8eb0c4fad1f69dfaeaf7f7a9e55e4646f10961a434ed93de7ab4339b8bb9

Name:           perl-Email-Received
Summary:        Parse an email Received: header
Version:        1.00
Release:        37%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Email-Received
Source0:        https://cpan.metacpan.org/authors/id/S/SI/SIMON/Email-Received-%{version}.tar.gz

BuildArch:      noarch

BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(Email::Simple)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Balanced)

%description
This module is a Perl Email Project rewrite of SpamAssassin's email header
parser. We did this so that the great work they did in analyzing pretty
much every possible Received header format could be used in applications
other than SpamAssassin itself.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Email-Received-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{_mandir}/man3/Email::Received.3pm*
%{perl_vendorlib}/Email

%changelog
%autochangelog
