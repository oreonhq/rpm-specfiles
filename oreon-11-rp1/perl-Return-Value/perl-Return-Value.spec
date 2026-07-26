%global source0_hash 8e2260a96531e93686200b9c8850ebe005d88ce369ff6bc70ff1a7405b7550ac

Name:           perl-Return-Value
Version:        1.666005
Release:        30%{?dist}
Summary:        Polymorphic Return Values
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Return-Value
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Return-Value-%{version}.tar.gz
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker), perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Perl::Critic), perl(Test::More)
BuildArch:      noarch

%description
This module provides polymorphic return values with a simple API that should 
get you what you're looking for in each context a return value is used in.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Return-Value-%{version}

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
make test PERL_TEST_CRITIC=1

%files
%doc README LICENSE
%{perl_vendorlib}/Return/
%{_mandir}/man3/*.3*

%changelog
%autochangelog
