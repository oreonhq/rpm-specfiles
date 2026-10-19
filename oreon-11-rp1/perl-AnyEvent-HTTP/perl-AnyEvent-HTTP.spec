%global source0_hash 5cfa53416124176f6f4cd32b00ea8ca79a2d5df51258683989cd04fe86e25013
Name:      perl-AnyEvent-HTTP
Version:   2.25
Release:        1%{?dist}
Summary:        Simple but non-blocking HTTP/HTTPS client
License:   GPL-1.0-or-later OR Artistic-1.0-Perl
URL:       https://metacpan.org/release/AnyEvent-HTTP
Source0:        https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/AnyEvent-HTTP-%{version}.tar.gz
BuildArch: noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(AnyEvent::Handle)
BuildRequires:  perl(AnyEvent::Impl::Perl)
BuildRequires:  perl(AnyEvent::Socket)
BuildRequires:  perl(AnyEvent::Util)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(URI)
BuildRequires:  perl(base)
BuildRequires:  perl(common::sense)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module is an AnyEvent user, you need to make sure that you use and
run a supported event loop.

This module implements a simple, stateless and non-blocking HTTP client.
It supports GET, POST and other request methods, cookies and more, all
on a very low level. It can follow redirects supports proxies and
automatically limits the number of connections to the values specified
in the RFC.

It should generally be a "good client" that is enough for most HTTP
tasks. Simple tasks should be simple, but complex tasks should still be
possible as the user retains control over request and response headers.

The caller is responsible for authentication management, cookies (if the
simplistic implementation in this module doesn't suffice), referrer and
other high-level protocol details for which this module offers only
limited support.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n AnyEvent-HTTP-%{version}

%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
