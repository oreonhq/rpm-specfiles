%global source0_hash 339e86075dbb9e8583c45d4000f1f1256102f4865ae9ec25c90f9d15432b5a14

# Note:  The tests for this perl dist. are disabled by default, as they
# require network access and would thus fail in the buildsys' mock
# environments.  To build locally while enabling tests, either:
#
#   rpmbuild ... --define '_with_network_tests 1' ...
#   rpmbuild ... --with network_tests ...
#   define _with_network_tests 1 in your ~/.rpmmacros

Name:           perl-POE-Component-Client-HTTP
Version:        0.949
Release:        33%{?dist}
Summary:        A non-blocking/parallel web requests engine for POE
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Component-Client-HTTP
Source0:        https://cpan.metacpan.org/authors/id/R/RC/RCAPUTO/POE-Component-Client-HTTP-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Errno)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(HTTP::Headers) >= 5.810
BuildRequires:  perl(HTTP::Request) >= 5.811
BuildRequires:  perl(HTTP::Request::Common) >= 5.811
BuildRequires:  perl(HTTP::Response) >= 5.813
BuildRequires:  perl(HTTP::Status) >= 5.811
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(Net::HTTP::Methods) >= 5.812
BuildRequires:  perl(POE) >= 1.312
# Original perl(POE::Component::Client::Keepalive) >= 0.271 rounded to
# 4 digit precision
BuildRequires:  perl(POE::Component::Client::Keepalive) >= 0.2710
BuildRequires:  perl(POE::Component::Server::TCP)
BuildRequires:  perl(POE::Driver::SysRW)
BuildRequires:  perl(POE::Filter)
BuildRequires:  perl(POE::Filter::HTTPD)
BuildRequires:  perl(POE::Filter::Line)
BuildRequires:  perl(POE::Filter::Stackable)
BuildRequires:  perl(POE::Filter::Stream)
BuildRequires:  perl(POE::Session)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket) >= 2.001
BuildRequires:  perl(strict)
BuildRequires:  perl(URI) >= 1.37
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::POE::Server::TCP) >= 1.14
BuildRequires:  perl(Test::More) > 0.96
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(warnings)
Requires:       perl(HTTP::Headers) >= 5.810
Requires:       perl(HTTP::Request) >= 5.811
Requires:       perl(HTTP::Request::Common) >= 5.811
Requires:       perl(HTTP::Response) >= 5.813
Requires:       perl(HTTP::Status) >= 5.811
Requires:       perl(Net::HTTP::Methods) >= 5.812
Requires:       perl(POE) >= 1.312
# Original perl(POE::Component::Client::Keepalive) >= 0.271 rounded to
# 4 digit precision
Requires:       perl(POE::Component::Client::Keepalive) >= 0.2710
Requires:       perl(Socket) >= 2.001
Requires:       perl(URI) >= 1.37

%{?perl_default_filter}

%description
POE::Component::Client::HTTP is an HTTP user-agent for POE. It lets other
sessions run while HTTP transactions are being processed, and it lets several
HTTP transactions be processed in parallel.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n POE-Component-Client-HTTP-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=true
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*
cd examples
sed -i '/#!perl/d;s/\r//' pcchget.perl

%check
# we don't have network access during the builds; fortunately these look to be
# the only tests requiring it.  Failing that, the entire suite can be
# disabled.
%{?!_with_network_tests:rm t/01* t/02*}
make test

%files
%doc CHANGES* README examples/
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
