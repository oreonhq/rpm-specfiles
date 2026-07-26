%global source0_hash e9b1c7b2b96c194f87a5f77e1449717077c70ffc67a4bfc29f026c9ee2e07bea

Name:           perl-Catalyst-Plugin-Session-State-Cookie
Summary:        Maintain session IDs using cookies
Version:        0.18
Release:        16%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/Catalyst-Plugin-Session-State-Cookie-%{version}.tar.gz
URL:            https://metacpan.org/release/Catalyst-Plugin-Session-State-Cookie
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  sed
# Run-time:
# This is a Catalyst plugin
BuildRequires:  perl(Catalyst) >= 5.80005
# This is a Catalyst::Plugin::Session extension
BuildRequires:  perl(Catalyst::Plugin::Session) >= 0.27
BuildRequires:  perl(Catalyst::Plugin::Session::State)
BuildRequires:  perl(Catalyst::Utils)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(namespace::autoclean)
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(Catalyst::Controller)
BuildRequires:  perl(Catalyst::Test)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
# This is a Catalyst plugin
Requires:       perl(Catalyst) >= 5.80005
# This is a Catalyst::Plugin::Session extension
Requires:       perl(Catalyst::Plugin::Session) >= 0.27
Requires:       perl(Catalyst::Plugin::Session::State)

%{?perl_default_filter}

%description
In order for Catalyst::Plugin::Session to work the session ID needs to
be stored on the client, and the session data needs to be stored on
the server.  This plugin provides a way to store the session ID on the
client, through a cookie.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Plugin-Session-State-Cookie-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%{make_build} test

%files
%license LICENSE
%doc Changes README t/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
