%global source0_hash 0ee6a0ac32d733fdf0e2394c9760cd4563bacd28b6a8e1fa4e63c671ff77c827
Name:           perl-Net-Async-WebSocket
Version:        0.14
Release:        1%{?dist}
Summary:        Use WebSockets with IO::Async
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Net-Async-WebSocket
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Net-Async-WebSocket-%{version}.tar.gz
BuildArch:      noarch
Recommends:     perl(IO::Async::SSL)
Requires:       perl(Protocol::WebSocket) >= 0.22
Requires:       perl(URI::wss)
Requires:       perl(IO::Async::Listener) >= 0.61
Requires:       perl(IO::Async::Stream) >= 0.34
%global __requires_exclude ^perl\\(IO::Async::(Listener|Stream)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(IO::Async::Listener)
BuildRequires:  perl(IO::Async::Loop)
BuildRequires:  perl(IO::Async::Notifier)
BuildRequires:  perl(IO::Async::OS)
BuildRequires:  perl(IO::Async::Stream)
BuildRequires:  perl(IO::Async::Test)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Protocol::WebSocket)
BuildRequires:  perl(Protocol::WebSocket::Frame)
BuildRequires:  perl(Protocol::WebSocket::Handshake::Client)
BuildRequires:  perl(Protocol::WebSocket::Handshake::Server)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::wss)
BuildRequires:  perl(base)
BuildRequires:  perl(meta)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This distribution provides modules that implement the WebSocket protocol,
and allows either servers or clients to be written based on IO::Async.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-Async-WebSocket-%{version}

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
