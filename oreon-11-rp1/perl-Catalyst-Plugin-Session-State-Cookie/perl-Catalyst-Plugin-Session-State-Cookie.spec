%global source0_hash e9b1c7b2b96c194f87a5f77e1449717077c70ffc67a4bfc29f026c9ee2e07bea
Name:           perl-Catalyst-Plugin-Session-State-Cookie
Summary:        Maintain session IDs using cookies
Version:        0.18
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/Catalyst-Plugin-Session-State-Cookie-%{version}.tar.gz
URL:            https://metacpan.org/release/Catalyst-Plugin-Session-State-Cookie
BuildArch:      noarch
Requires:       perl(Catalyst) >= 5.80005
Requires:       perl(Catalyst::Plugin::Session) >= 0.27
Requires:       perl(Catalyst::Plugin::Session::State)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Catalyst)
BuildRequires:  perl(Catalyst::Controller)
BuildRequires:  perl(Catalyst::Plugin::Session)
BuildRequires:  perl(Catalyst::Plugin::Session::State)
BuildRequires:  perl(Catalyst::Test)
BuildRequires:  perl(Catalyst::Utils)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
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
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
