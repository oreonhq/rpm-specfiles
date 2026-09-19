%global source0_hash ff58fd19c32df5196a6936a4c96dca488b3578165af99ae76560b2cdc02086a2

Name:           perl-POE-Component-Server-SOAP
Version:        1.14
Release:        47%{?dist}
Summary:        Publish POE event handlers via SOAP over HTTP
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Component-Server-SOAP
Source0:        https://cpan.metacpan.org/authors/id/A/AP/APOCAL/POE-Component-Server-SOAP-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(POE)
BuildRequires:  perl(POE::Component::Server::SimpleHTTP)
BuildRequires:  perl(POE::Component::Server::SimpleHTTP::Response)
BuildRequires:  perl(POE::Session)
BuildRequires:  perl(SOAP::Constants)
BuildRequires:  perl(SOAP::Lite)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
This module makes serving SOAP/1.1 requests a breeze in POE.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n POE-Component-Server-SOAP-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
# fix a non-UTF-8 issue....
cd blib/man3
iconv --from=ISO-8859-1 --to=UTF-8 POE::Component::Server::SOAP.3pm > new
mv new POE::Component::Server::SOAP.3pm

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc README Changes examples/ t/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
