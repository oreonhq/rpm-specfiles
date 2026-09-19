%global source0_hash af19f56747a172512fa509be4883112eb2b41ea31d9713576bc6a63e2c1c1a50

Name:           perl-CGI-Application-Plugin-RequireSSL
Version:        0.04
Release:        42%{?dist}
Summary:        Force SSL in specified pages or modules
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CGI-Application-Plugin-RequireSSL
Source0:        https://cpan.metacpan.org/authors/id/D/DH/DHORNE/CGI-Application-Plugin-RequireSSL-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Attribute::Handlers)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
# Tests
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Application) >= 4.01
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
# Optional tests
BuildRequires:  perl(Test::Pod) >= 1.14

%{?perl_default_filter}

%description
CGI::Application::Plugin::RequireSSL allows individual run modes or whole
modules to be protected by SSL. If a standard HTTP request is received, you
can specify whether an error is raised or if the request should be
redirected to the HTTPS equivalent URL.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Application-Plugin-RequireSSL-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

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
