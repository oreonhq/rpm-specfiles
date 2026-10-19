%global source0_hash 675b5fd8b1cfe62b13229f42e6282ce0d61c8fd4574af9a2c3aaad75617a6fc3
Name:           perl-WWW-DuckDuckGo
Version:        0.016
Release:        33%{?dist}
Summary:        Access to the DuckDuckGo APIs
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/WWW-DuckDuckGo
Source0:        https://cpan.metacpan.org/modules/by-module/WWW/WWW-DuckDuckGo-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(JSON) >= 2.50
Requires:       perl(Moo) >= 0.009007
Requires:       perl(URI) >= 1.58
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(JSON\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Moo\\)$
%global __requires_exclude %__requires_exclude|^perl\\(URI\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(JSON)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::QueryParam)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
