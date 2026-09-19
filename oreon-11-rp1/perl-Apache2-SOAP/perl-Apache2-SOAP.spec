%global source0_hash 65f577e698b7e46c24904ee3cc3e27e1101d0a54554ec79a7c0ce4ea0ba0afac

Name:          perl-Apache2-SOAP
Version:       0.73
Release:       49%{?dist}
Summary:       A replacement for Apache::SOAP designed to work with mod_perl 2

License:       GPL-1.0-or-later OR Artistic-1.0-Perl
URL:           https://metacpan.org/release/Apache2-SOAP
Source0:       https://cpan.metacpan.org/authors/id/R/RK/RKOBES/Apache2-SOAP-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: make
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires: mod_perl-devel
# perl(ModPerl::MM) is provided by mod_perl on EL5, by mod_perl-devel on Fedora
#BuildRequires: perl(ModPerl::MM)
# BR for test (disabled)
#BuildRequires: httpd, perl(SOAP::Lite), perl(LWP::UserAgent)
#BuildRequires: perl(Test::More)

%{?perl_default_filter}

%description
This Apache Perl module provides the ability to add support for SOAP
(Simple Object Access Protocol) protocol with easy configuration
(either in .conf or in .htaccess file). This functionality should
give you lightweight option for hosting SOAP services and greatly
simplify configuration aspects. This module inherites functionality
from SOAP::Transport::HTTP2::Apache component of SOAP::Lite module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Apache2-SOAP-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
# Running apache on koji fails
# APACHE_TEST_HTTPD=%%{_sbindir}/httpd make test

%files
%doc Changes README
%{_mandir}/man3/Apache*
%{perl_vendorlib}/Apache2
%{perl_vendorlib}/SOAP/Transport/HTTP2.pm

%changelog
%autochangelog
