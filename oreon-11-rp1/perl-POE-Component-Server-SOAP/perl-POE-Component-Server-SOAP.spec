%global source0_hash ff58fd19c32df5196a6936a4c96dca488b3578165af99ae76560b2cdc02086a2
Name:           perl-POE-Component-Server-SOAP
Version:        1.14
Release:        1%{?dist}
Summary:        Publish POE event handlers via SOAP over HTTP
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Component-Server-SOAP
Source0:        https://cpan.metacpan.org/authors/id/A/AP/APOCAL/POE-Component-Server-SOAP-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(POE)
BuildRequires:  perl(POE::Component::Server::SimpleHTTP)
BuildRequires:  perl(POE::Component::Server::SimpleHTTP::Response)
BuildRequires:  perl(POE::Session)
BuildRequires:  perl(SOAP::Constants)
BuildRequires:  perl(SOAP::Lite)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module makes serving SOAP/1.1 requests a breeze in POE.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n POE-Component-Server-SOAP-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
cd blib/man3
iconv --from=ISO-8859-1 --to=UTF-8 POE::Component::Server::SOAP.3pm > new
mv new POE::Component::Server::SOAP.3pm
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
