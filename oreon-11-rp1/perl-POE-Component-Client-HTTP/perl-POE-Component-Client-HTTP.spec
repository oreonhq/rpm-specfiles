%global source0_hash 339e86075dbb9e8583c45d4000f1f1256102f4865ae9ec25c90f9d15432b5a14
Name:           perl-POE-Component-Client-HTTP
Version:        0.949
Release:        1%{?dist}
Summary:        A non-blocking/parallel web requests engine for POE
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Component-Client-HTTP
Source0:        https://cpan.metacpan.org/authors/id/R/RC/RCAPUTO/POE-Component-Client-HTTP-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(HTTP::Headers) >= 5.810
Requires:       perl(HTTP::Request) >= 5.811
Requires:       perl(HTTP::Request::Common) >= 5.811
Requires:       perl(HTTP::Response) >= 5.813
Requires:       perl(HTTP::Status) >= 5.811
Requires:       perl(Net::HTTP::Methods) >= 5.812
Requires:       perl(POE) >= 1.312
Requires:       perl(POE::Component::Client::Keepalive) >= 0.2710
Requires:       perl(Socket) >= 2.001
Requires:       perl(URI) >= 1.37
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Errno)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(Net::HTTP::Methods)
BuildRequires:  perl(POE)
BuildRequires:  perl(POE::Component::Client::Keepalive)
BuildRequires:  perl(POE::Component::Server::TCP)
BuildRequires:  perl(POE::Driver::SysRW)
BuildRequires:  perl(POE::Filter)
BuildRequires:  perl(POE::Filter::HTTPD)
BuildRequires:  perl(POE::Filter::Line)
BuildRequires:  perl(POE::Filter::Stackable)
BuildRequires:  perl(POE::Filter::Stream)
BuildRequires:  perl(POE::Session)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::POE::Server::TCP)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(URI)
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

%{?!_with_network_tests:rm t/01* t/02*}
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
