%global source0_hash 6ffab915f323f60089e3ebf852b9b9707d6917266df8afd7370fac04bfdfee4e
Name:           perl-Starman
Version:        0.4017
Release:        1%{?dist}
Summary:        High-performance preforking PSGI/Plack web server
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Starman
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Starman-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Parser::XS)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Net::Server::PreFork)
BuildRequires:  perl(Net::Server::SIG)
BuildRequires:  perl(Net::Server::SS::PreFork)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Plack::Loader)
BuildRequires:  perl(Plack::Request)
BuildRequires:  perl(Plack::TempBuffer)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Plack::Test::Suite)
BuildRequires:  perl(Plack::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::TCP)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(subs)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Starman is a PSGI perl web server that has unique features such as high
performance, preforking, use of signals and a small memory footprint. It is PSGI
compatible and offers HTTP/1.1 support.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Starman-%{version}

%build

/usr/bin/perl Build.PL --installdirs vendor
./Build
%install
./Build install --destdir $RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
