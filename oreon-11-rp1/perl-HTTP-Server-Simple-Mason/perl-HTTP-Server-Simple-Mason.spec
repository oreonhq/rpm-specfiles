%global source0_hash b7a49d8e6e55bff0b1f0278d951685466b143243b6f9e59e071f5472ca2a025a
Name: 		perl-HTTP-Server-Simple-Mason
Version: 	0.14
Release:        1%{?dist}
Summary:        HTTP::Server::Simple::Mason Perl module
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL: 		https://metacpan.org/release/HTTP-Server-Simple-Mason
Source0:        https://cpan.metacpan.org/authors/id/J/JE/JESSE/HTTP-Server-Simple-Mason-%{version}.tar.gz
BuildArch: noarch
Requires:	perl(HTTP::Server::Simple::CGI)
# oreon:deps
BuildRequires:  /usr/bin/make
BuildRequires:  /usr/bin/perl
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTML::Mason)
BuildRequires:  perl(HTML::Mason::CGIHandler)
BuildRequires:  perl(HTML::Mason::FakeApache)
BuildRequires:  perl(HTTP::Server::Simple)
BuildRequires:  perl(HTTP::Server::Simple::CGI)
BuildRequires:  perl(Hook::LexWrap)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
# /oreon:deps
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
%oreon_autofiles main

%check

%{__make} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
