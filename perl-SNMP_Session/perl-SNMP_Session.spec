Name:           perl-SNMP_Session
Version:        1.16
Release:        8%{?dist}
Summary:        SNMP support for Perl 5

License:        Artistic-2.0
URL:            https://github.com/sleinen/snmp-session/
Source0:        https://github.com/sleinen/snmp-session/archive/v%{version}/SNMP_Session-%{version}.tar.gz
Patch0:         SNMP_Session-1.13-fix_ivp6.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(IO::Socket::INET6)
Requires:       perl(Socket6)

%description
Pure Perl SNMP v1 and SNMP v2 support for Perl 5.

The SNMP operations currently supported are "get", "get-next", "get-bulk"
and "set", as well as trap generation and reception. 


%prep
%setup -q -n SNMP_Session-%{version}
%patch -P 0 -p1
%{__perl} -pi -e 's{^#!/usr/local/bin/perl\b}{#!%{__perl}}' test/*
chmod -c 644 test/*


%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}


%install
%{make_install}
%{_fixperms} %{buildroot}/*


%check
make test


%files
%license Artistic
%doc README README.SNMP_util index.html test/
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.16-8
- Prepare for Oreon 11 (RP1)
