%global source0_hash 6c22d069f5a57ac206d4659b28b8869bb9270640bb955efddd451dcc58cdb391

Name:           perl-Plack-Middleware-FixMissingBodyInRedirect
Version:        0.12
Release:        32%{?dist}
Summary:        Plack::Middleware which sets body for redirect response, if it's not already set
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Plack-Middleware-FixMissingBodyInRedirect
Source0:        https://cpan.metacpan.org/modules/by-module/Plack/Plack-Middleware-FixMissingBodyInRedirect-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(parent)
BuildRequires:  perl(Plack::Builder)
BuildRequires:  perl(Plack::Middleware)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Plack::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

%description
This module sets body in redirect response, if it's not already set.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Plack-Middleware-FixMissingBodyInRedirect-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
