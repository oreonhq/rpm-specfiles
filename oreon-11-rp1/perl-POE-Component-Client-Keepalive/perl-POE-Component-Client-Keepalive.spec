%global source0_hash 8c0819100f859fbfe0a13454773ee3b6f47cd7e85a317ad62ec35507cb3c36cb
Name:           perl-POE-Component-Client-Keepalive
%global real_ver 0.272
Version:        %{real_ver}0
Release:        34%{?dist}
Summary:        Manages and keeps alive client connections
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Component-Client-Keepalive
Source0:        https://cpan.metacpan.org/authors/id/R/RC/RCAPUTO/POE-Component-Client-Keepalive-%{real_ver}.tar.gz
Patch0:         POE-Component-Client-Keepalive-0.272-Fix-a-race-in-t-10_resolver.t.patch
BuildArch:      noarch
Requires:       perl(Net::IP::Minimal) >= 0.02
Requires:       perl(POE) >= 1.311
Requires:       perl(POE::Component::Resolver) >= 0.917
Provides:       perl(POE::Component::Client::Keepalive) = %{version}
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:__requires_exclude|^}perl\\(Net::IP::Minimal\\)$
%global __requires_exclude %__requires_exclude|^perl\\(POE\\)$
%global __requires_exclude %__requires_exclude|^perl\\(POE::Component::Resolver\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Errno)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(Net::IP::Minimal)
BuildRequires:  perl(POE)
BuildRequires:  perl(POE::Component::Resolver)
BuildRequires:  perl(POE::Component::Server::TCP)
BuildRequires:  perl(POE::Wheel::ReadWrite)
BuildRequires:  perl(POE::Wheel::SocketFactory)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
POE::Component::Client::Keepalive creates and manages connections for other
components. It maintains a cache of kept-alive connections for quick reuse. It
is written specifically for clients that can benefit from kept-alive
connections, such as HTTP clients. Using it for one-shot connections would
probably be silly.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n POE-Component-Client-Keepalive-%{real_ver}
%patch -P0 -p1
chmod -c -x mylib/* t/*
for test in t/release-pod-syntax.t \
            t/release-pod-coverage.t \
            t/000-report-versions.t; do
    perl -MConfig -i -pe 's/#!perl/$Config{startperl}/' ${test}
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

unset RELEASE_TESTING
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
