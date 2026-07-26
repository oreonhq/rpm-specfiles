%global source0_hash b7a49d8e6e55bff0b1f0278d951685466b143243b6f9e59e071f5472ca2a025a

Name: 		perl-HTTP-Server-Simple-Mason
Version: 	0.14
Release: 	43%{?dist}
Summary:	HTTP::Server::Simple::Mason Perl module
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL: 		https://metacpan.org/release/HTTP-Server-Simple-Mason
Source: 	https://cpan.metacpan.org/authors/id/J/JE/JESSE/HTTP-Server-Simple-Mason-%{version}.tar.gz

BuildArch: noarch

BuildRequires:	%{__make}
BuildRequires:	%{__perl}
BuildRequires:	perl-generators
BuildRequires:	perl(base)
BuildRequires:	perl(bytes)
BuildRequires:	perl(Encode)
BuildRequires:	perl(HTML::Mason) >= 1.25
BuildRequires:	perl(HTML::Mason::CGIHandler)
BuildRequires:	perl(HTML::Mason::FakeApache)
BuildRequires:	perl(HTTP::Server::Simple) >= 0.04
BuildRequires:	perl(HTTP::Server::Simple::CGI)
BuildRequires:	perl(Hook::LexWrap)
BuildRequires:	perl(inc::Module::Install)
BuildRequires:	perl(Module::Install::Metadata)
BuildRequires:	perl(Module::Install::WriteAll)
BuildRequires:	perl(strict)

# Required by the tests
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More)
BuildRequires: 	perl(Test::Pod) >= 1.14
BuildRequires: 	perl(Test::Pod::Coverage) >= 1.04

# Improved tests (dynamic requirement of HTML::Mason)
BuildRequires: 	perl(LWP::Simple)

Requires:	perl(HTTP::Server::Simple::CGI)

%description
An abstract baseclass for a standalone mason server

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTTP-Server-Simple-Mason-%{version}
rm -r inc

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes ex
%{perl_vendorlib}/HTTP
%{_mandir}/man3/*

%changelog
%autochangelog
