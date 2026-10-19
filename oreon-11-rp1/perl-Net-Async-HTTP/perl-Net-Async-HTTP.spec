%global source0_hash 39206d069495d1b86aee37aa8ad3c9334d36e59cce6cf79cd386ac0cf3798cdb
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
Name:           perl-Net-Async-HTTP
Version:        0.49
Release:        9%{?dist}
Summary:        Use HTTP with IO::Async
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Net-Async-HTTP
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Net-Async-HTTP-%{version}.tar.gz
BuildArch:      noarch
%if !0%{?perl_bootstrap}
%endif
Recommends:     perl(Compress::Bzip2) >= 2.010
Recommends:     perl(Compress::Raw::Zlib) >= 2.057
Recommends:     perl(IO::Async::SSL) >= 0.12
Recommends:     perl(Net::Async::SOCKS) >= 0.003
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Bzip2)
BuildRequires:  perl(Compress::Raw::Zlib)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Future)
BuildRequires:  perl(Future::Utils)
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(IO::Async::Loop)
BuildRequires:  perl(IO::Async::Notifier)
BuildRequires:  perl(IO::Async::SSL)
BuildRequires:  perl(IO::Async::Stream)
BuildRequires:  perl(IO::Async::Test)
BuildRequires:  perl(IO::Async::Timer::Countdown)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Metrics::Any)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Net::Async::HTTP::Server)
BuildRequires:  perl(Net::Async::SOCKS)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Struct::Dumb)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Metrics::Any)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(URI)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This object class implements an asynchronous HTTP user agent. It sends
requests to servers, returning Future instances to yield responses when
they are received. The object supports multiple concurrent connections to
servers, and allows multiple requests in the pipeline to any one
connection. Normally, only one such object will be needed per program to
support any number of requests.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-Async-HTTP-%{version}

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

unset NET_ASYNC_HTTP_MAXCONNS
./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
