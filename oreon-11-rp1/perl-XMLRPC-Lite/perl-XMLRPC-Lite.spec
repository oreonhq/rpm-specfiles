%global source0_hash 3a9fa5f2cb1faf8b7c66b4c386eab35cac6088afc4dbc757d4f77d284dab4524

Name:           perl-XMLRPC-Lite
Version:        0.717
Release:        33%{?dist}
Summary:        Client and server implementation of XML-RPC protocol
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XMLRPC-Lite
Source0:        https://cpan.metacpan.org/authors/id/P/PH/PHRED/XMLRPC-Lite-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(SOAP)
BuildRequires:  perl(SOAP::Data)
BuildRequires:  perl(SOAP::Deserializer)
BuildRequires:  perl(SOAP::Lite) >= 0.716
BuildRequires:  perl(SOAP::Serializer)
BuildRequires:  perl(SOAP::Server)
BuildRequires:  perl(SOAP::Server::Parameters)
BuildRequires:  perl(SOAP::SOM)
BuildRequires:  perl(SOAP::Test)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Requires:       perl(MIME::Base64)
Requires:       perl(SOAP)
Requires:       perl(SOAP::Data)
Requires:       perl(SOAP::Deserializer)
Requires:       perl(SOAP::Lite) >= 0.716
Requires:       perl(SOAP::Serializer)
Requires:       perl(SOAP::Server)
Requires:       perl(SOAP::Server::Parameters)
Requires:       perl(SOAP::SOM)
Requires:       perl(SOAP::Transport::HTTP::Apache)
Requires:       perl(SOAP::Transport::HTTP::CGI)
Requires:       perl(SOAP::Transport::HTTP::Daemon)
Requires:       perl(SOAP::Transport::POP3::Server)
Requires:       perl(SOAP::Transport::TCP) >= 0.715
Requires:       perl(SOAP::Transport::TCP::Server)

%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(My::.*\\)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(SOAP::Lite\\)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(SOAP::Transport::TCP\\)

%description
XMLRPC::Lite is a Perl modules which provides a simple interface to the XML-
RPC protocol both on client and server side. Based on SOAP::Lite module, it
gives you access to all features and transports available in that module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n XMLRPC-Lite-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
