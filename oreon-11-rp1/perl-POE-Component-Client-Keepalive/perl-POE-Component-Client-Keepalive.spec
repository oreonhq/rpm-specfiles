%global source0_hash 8c0819100f859fbfe0a13454773ee3b6f47cd7e85a317ad62ec35507cb3c36cb

Name:           perl-POE-Component-Client-Keepalive
%global real_ver 0.272
# Keep four digits to stay above the unfortunate 0.0901,
# so that epoch need not be changed.
Version:        %{real_ver}0
Release:        34%{?dist}
Summary:        Manages and keeps alive client connections
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Component-Client-Keepalive
Source0:        https://cpan.metacpan.org/authors/id/R/RC/RCAPUTO/POE-Component-Client-Keepalive-%{real_ver}.tar.gz
# Fix a race in t/10_resolver.t, bug #1136851, CPAN RT#98644
Patch0:         POE-Component-Client-Keepalive-0.272-Fix-a-race-in-t-10_resolver.t.patch
BuildArch:      noarch
# Build
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Net::IP::Minimal) >= 0.02
BuildRequires:  perl(POE) >= 1.311
BuildRequires:  perl(POE::Component::Resolver) >= 0.917
BuildRequires:  perl(POE::Component::Server::TCP)
# Unused BuildRequires:  perl(POE::Component::SSLify)
BuildRequires:  perl(POE::Wheel::ReadWrite)
BuildRequires:  perl(POE::Wheel::SocketFactory)
BuildRequires:  perl(Socket)
# Tests
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(lib)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More) >= 0.94
Requires:       perl(Net::IP::Minimal) >= 0.02
Requires:       perl(POE) >= 1.311
Requires:       perl(POE::Component::Resolver) >= 0.917
# Satisfy automaticly generated requires that want this module >= 0.0901
# (So the package has this provide in two versions, oh well.)
Provides:       perl(POE::Component::Client::Keepalive) = %{version}

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:__requires_exclude|^}perl\\(Net::IP::Minimal\\)$
%global __requires_exclude %__requires_exclude|^perl\\(POE\\)$
%global __requires_exclude %__requires_exclude|^perl\\(POE::Component::Resolver\\)$

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

%check
# I'm leaving all tests active for now, even though 09_timeout.t runs a test
# which is _supposed_ to timeout against google.com.  This may or may not
# work inside the buildsys; if it doesn't the cure should be as easy as nixing
# this one test.
unset RELEASE_TESTING
make test

%files
%license LICENSE
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
