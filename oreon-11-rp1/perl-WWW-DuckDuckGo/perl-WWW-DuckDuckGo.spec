%global source0_hash 675b5fd8b1cfe62b13229f42e6282ce0d61c8fd4574af9a2c3aaad75617a6fc3

Name:           perl-WWW-DuckDuckGo
Version:        0.016
Release:        33%{?dist}
Summary:        Access to the DuckDuckGo APIs
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/WWW-DuckDuckGo
Source0:        https://cpan.metacpan.org/modules/by-module/WWW/WWW-DuckDuckGo-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(JSON) >= 2.50
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Moo) >= 0.009007
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.90
BuildRequires:  perl(URI) >= 1.58
BuildRequires:  perl(URI::QueryParam)
BuildRequires:  perl(warnings)
Requires:       perl(JSON) >= 2.50
Requires:       perl(Moo) >= 0.009007
Requires:       perl(URI) >= 1.58

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(JSON\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Moo\\)$
%global __requires_exclude %__requires_exclude|^perl\\(URI\\)$
%description
This distribution gives you an easy access to the DuckDuckGo Zero Click
Info API. It tries to connect via HTTPS first and falls back to HTTP if
there is a failure.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n WWW-DuckDuckGo-%{version}

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
