%global source0_hash 9d4cffbdca31fb1282615c3575201d94fc3b43ca653821d37b120c95f9cd2e1c
Name:		shelldap
Version:	1.5.2
Release:        1%{?dist}
Summary:        A shell-like interface for browsing LDAP servers
License:	BSD-3-Clause
URL:		https://github.com/mahlonsmith/%{name}
Source0:        https://github.com/mahlonsmith/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch
Recommends:	perl(IO::Socket::SSL) perl(Authen::SASL) perl(Term::ReadLine::Gnu)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(Config)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl-podlators
# /oreon:deps
%description
A handy shell-like interface for browsing LDAP servers and editing their
content. It keeps command history, has sane auto-completion, credential caching,
site-wide and individual configurations.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
/usr/bin/perl -MConfig -i -pe 's{^#!/usr/bin/env perl}{$Config{startperl}}' %{name}

%build

pod2man shelldap > shelldap.1
/usr/bin/perl -n -e 'if(m/^#/){print if($. > 4)}else{exit 0}' shelldap > LICENSE.txt
%install
/usr/bin/mkdir -p %{buildroot}/%{_bindir}
/usr/bin/mkdir -p %{buildroot}/%{_mandir}/man1
/usr/bin/install -p -m 755 shelldap %{buildroot}%{_bindir}/shelldap
/usr/bin/install -p -m 644 shelldap.1 %{buildroot}%{_mandir}/man1/shelldap.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
