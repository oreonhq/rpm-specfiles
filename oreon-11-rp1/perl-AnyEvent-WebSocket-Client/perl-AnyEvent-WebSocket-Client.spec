%global source0_hash 55cf0ea6f93f8f4932ead5f9a89b027642ed60381a93528411c7e9331dd4c025
Name:           perl-AnyEvent-WebSocket-Client
Version:        0.55
Release:        1%{?dist}
Summary:        WebSocket client for AnyEvent
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/AnyEvent-WebSocket-Client
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/AnyEvent-WebSocket-Client-%{version}.tar.gz
BuildArch:      noarch
BuildConflicts: perl(Crypt::Random::Source) < 0.08
Requires:       perl(AnyEvent::Connector)
Requires:       perl(URI)
Requires:       perl(URI::ws)
Recommends:     perl(PerlX::Maybe::XS)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(AE)
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(AnyEvent::Connector)
BuildRequires:  perl(AnyEvent::Handle)
BuildRequires:  perl(AnyEvent::Socket)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Devel::Cycle)
BuildRequires:  perl(EV)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Mojo::Server::Daemon)
BuildRequires:  perl(Mojolicious)
BuildRequires:  perl(Mojolicious::Lite)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Net::SSLeay)
BuildRequires:  perl(PerlX::Maybe)
BuildRequires:  perl(PerlX::Maybe::XS)
BuildRequires:  perl(Protocol::WebSocket)
BuildRequires:  perl(Protocol::WebSocket::Frame)
BuildRequires:  perl(Protocol::WebSocket::Handshake::Client)
BuildRequires:  perl(Protocol::WebSocket::Handshake::Server)
BuildRequires:  perl(Protocol::WebSocket::Request)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test2::API)
BuildRequires:  perl(Test2::Require)
BuildRequires:  perl(Test2::Require::Module)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::ws)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This class provides an interface to interact with a web server that
provides services via the WebSocket protocol in an AnyEvent context.
It uses Protocol::WebSocket rather than reinventing the wheel. You
could use AnyEvent and Protocol::WebSocket directly if you wanted
finer grain control, but if that is not necessary then this class may
save you some time.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n AnyEvent-WebSocket-Client-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

unset PERL_AE_WS_C_TEST_PROXY_URL PERL_AE_WS_C_TEST_PROXY_ON ANYEVENT_WEBSOCKET_TEST_SKIP_SSL
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
