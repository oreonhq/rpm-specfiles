%global source0_hash 798dc4b64d46aedb2acf233b09e48fb1c24f25274adfdd888ce7b1ee6e176052
Name:           perl-HTML-Lint
Version:        2.32
Release:        1%{?dist}
Summary:        HTML::Lint Perl module
License:        Artistic-2.0
URL:            https://metacpan.org/release/HTML-Lint
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/HTML-Lint-%{version}.tar.gz
BuildArch:      noarch
Provides:       weblint = %{version}-%{release}
# oreon:deps
BuildRequires:  /usr/bin/make
BuildRequires:  /usr/bin/perl
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(HTML::Tagset)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl-generators
# /oreon:deps
%description
HTML::Lint Perl module, a pure-Perl HTML parser and checker for syntactic
legitmacy.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-Lint-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{__make} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
