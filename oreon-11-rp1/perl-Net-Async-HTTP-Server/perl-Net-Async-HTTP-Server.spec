%global source0_hash 43f1ef13eeae1132266578372837c4e4bdfb0556b1f4b45d7f5d97d4ce9fe99a

Name:           perl-Net-Async-HTTP-Server
Version:        0.15
Release:        3%{?dist}
Summary:        Serve HTTP with IO::Async
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Net-Async-HTTP-Server
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Net-Async-HTTP-Server-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter perl-generators coreutils
BuildRequires:  perl(:VERSION) >= 5.14.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(IO::Async) >= 0.54
BuildRequires:  perl(IO::Async::Listener) >= 0.61
BuildRequires:  perl(IO::Async::Loop)
BuildRequires:  perl(IO::Async::SSL)
BuildRequires:  perl(IO::Async::Stream)
BuildRequires:  perl(IO::Async::Test)
BuildRequires:  perl(IO::Socket::UNIX)
BuildRequires:  perl(Metrics::Any) >= 0.05
BuildRequires:  perl(Module::Build) >= 0.4004
BuildRequires:  perl(Net::Async::HTTP)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test2::V0) >= 0.000147
BuildRequires:  perl(Test::Metrics::Any)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(URI::QueryParam)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
Recommends:     perl(IO::Async::SSL)
Recommends:     perl(IO::Socket::UNIX)

%description
This module allows a program to respond asynchronously to HTTP requests, as
part of a program based on IO::Async. An object in this class listens on a
single port and invokes the on_request callback or subclass method whenever
an HTTP request is received, allowing the program to respond to it.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-Async-HTTP-Server-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes examples README
%license LICENSE
%dir %{perl_vendorlib}/Net
%dir %{perl_vendorlib}/Net/Async
%dir %{perl_vendorlib}/Net/Async/HTTP
%{perl_vendorlib}/Net/Async/HTTP/Server*
%dir %{perl_vendorlib}/Plack
%dir %{perl_vendorlib}/Plack/Handler
%dir %{perl_vendorlib}/Plack/Handler/Net
%dir %{perl_vendorlib}/Plack/Handler/Net/Async
%dir %{perl_vendorlib}/Plack/Handler/Net/Async/HTTP
%{perl_vendorlib}/Plack/Handler/Net/Async/HTTP/Server.pm
%{_mandir}/man3/Net::Async::HTTP*
%{_mandir}/man3/Plack::Handler::Net::Async::HTTP*

%changelog
%autochangelog
