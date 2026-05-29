%global source0_hash 6f0ab25325afad69fbdd1637f78a9e5cbdd6887fea66e751880ba2609eebf1fa

Name:           perl-SNMP_Session
Version:        1.16
Release:        8%{?dist}
Summary:        SNMP support for Perl 5

License:        Artistic-2.0
URL:            https://github.com/sleinen/snmp-session/
Source0:        https://github.com/sleinen/snmp-session/archive/v1.16/SNMP_Session-1.16.tar.gz
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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
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
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.16-8
- Import
