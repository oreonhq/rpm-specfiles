%global source0_hash fc72bfbc532a57984ddd38b549f5e770391aef480443cd26e83ac5ce3a08908c

Name:           perl-CGI-Application-Plugin-DevPopup
Version:        1.08
Release:        37%{?dist}
Summary:        Runtime cgiapp info in a popup window
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/CGI-Application-Plugin-DevPopup
Source0:        https://cpan.metacpan.org/authors/id/R/RH/RHESA/CGI-Application-Plugin-DevPopup-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Application) >= 4.01
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::Template)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(Log::Dispatch::Handle)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Pod)

%{?perl_default_filter}

%description
This module provides a plugin framework for displaying runtime information
about your CGI::Application app in a popup window. A sample Timing plugin
is provided to show how it works.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Application-Plugin-DevPopup-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
