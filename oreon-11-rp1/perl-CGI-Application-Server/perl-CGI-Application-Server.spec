%global source0_hash 90c4f750f2117394dc800573c0a6a686fdb22d1f8fb9be112192bcef07be3f0e

Name:           perl-CGI-Application-Server
Version:        0.063
Release:        37%{?dist}
Summary:        Simple HTTP server for developing with CGI::Application
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/CGI-Application-Server
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/CGI-Application-Server-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Carp) >= 0.01
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(CGI::Application::Dispatch)
BuildRequires:  perl(CGI::Application::Plugin::Redirect)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Server::Simple) >= 0.18
BuildRequires:  perl(HTTP::Server::Simple::CGI)
BuildRequires:  perl(HTTP::Server::Simple::Static) >= 0.02
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(lib)
BuildRequires:  perl(Scalar::Util) >= 1.18
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::HTTP::Server::Simple)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::WWW::Mechanize)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
This is a simple HTTP server for for use during development with
CGI::Application. At this moment, it serves our needs in a very basic way.
The plan is to release early and release often, and add features when we
need them. That said, we welcome any and all patches, tests and feature
requests (the ones with which are accompanied by failing tests will get
priority).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Application-Server-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
