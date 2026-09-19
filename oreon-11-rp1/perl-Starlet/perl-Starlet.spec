%global source0_hash b9603b8e62880cb4582f6a7939eafec65e6efd3d900f2c7dd342e5f4c68d62d8

Name:           perl-Starlet
Version:        0.31
Release:        28%{?dist}
Summary:        Simple, high-performance PSGI/Plack HTTP server
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Starlet
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAZUHO/Starlet-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__perl}
BuildRequires:  %{__make}
BuildRequires:  /usr/bin/start_server
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.59

BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(LWP::UserAgent) >= 5.8
BuildRequires:  perl(Net::EmptyPort)
BuildRequires:  perl(Parallel::Prefork) >= 0.17
BuildRequires:  perl(Plack) >= 0.992
BuildRequires:  perl(Plack::HTTPParser)
BuildRequires:  perl(Plack::Loader)
BuildRequires:  perl(Plack::TempBuffer)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Plack::Util)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Server::Starter) >= 0.06
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::TCP) >= 2.1
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(warnings)

# Eliminate inc/*
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::ReadmeFromPod)

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

%check
%{__make} test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
