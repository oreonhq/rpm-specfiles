%global source0_hash 432b7c83ff88749af128003f5257c573aec1a463418db90ed22843cbbc258b4f

Name:           perl-Email-Date-Format
Version:        1.008
Release:        8%{?dist}
Summary:        Produce RFC 2822 date strings
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Email-Date-Format
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Email-Date-Format-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
BuildRequires:  perl(Time::Local)
BuildArch:      noarch

Provides:       perl(Email::Date::Format)
%description
This module can be used to emit RFC 2822 style date strings.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Email-Date-Format-%{version}

%build
sed -i '/LICENSE/ d' Makefile.PL
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc README LICENSE
%{perl_vendorlib}/Email/
%{_mandir}/man3/*.3*

%changelog
%autochangelog
