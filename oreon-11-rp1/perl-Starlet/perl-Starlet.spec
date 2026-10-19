%global source0_hash b9603b8e62880cb4582f6a7939eafec65e6efd3d900f2c7dd342e5f4c68d62d8
Name:           perl-Starlet
Version:        0.31
Release:        28%{?dist}
Summary:        Simple, high-performance PSGI/Plack HTTP server
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Starlet
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAZUHO/Starlet-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  /usr/bin/make
BuildRequires:  /usr/bin/perl
BuildRequires:  /usr/bin/start_server
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Install::ReadmeFromPod)
BuildRequires:  perl(Net::EmptyPort)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Parallel::Prefork)
BuildRequires:  perl(Plack)
BuildRequires:  perl(Plack::HTTPParser)
BuildRequires:  perl(Plack::Loader)
BuildRequires:  perl(Plack::TempBuffer)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Plack::Util)
BuildRequires:  perl(Server::Starter)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::TCP)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
# /oreon:deps
%description
Starlet is a standalone HTTP/1.0 server with support for keep-alive, prefork,
graceful shutdown, hot deploy, fast HTTP processing, and is suitable for
running HTTP application servers behind a reverse proxy.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Starlet-%{version}
rm -r inc/
sed -i -e '/^inc\/.*$/d' MANIFEST

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{__make} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
