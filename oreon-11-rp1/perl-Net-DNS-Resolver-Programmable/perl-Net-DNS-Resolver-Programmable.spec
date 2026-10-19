%global source0_hash 8080a2ab776629585911af1179bdb7c4dc2bebfd4b5efd77b11d1dac62454bf8
Name:           perl-Net-DNS-Resolver-Programmable
Version:        0.009
Release:        24%{?dist}
Summary:        Programmable DNS resolver class for offline emulation of DNS
License:        GPL-2.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-DNS-Resolver-Programmable
Source0:        https://cpan.metacpan.org/modules/by-module/Net/Net-DNS-Resolver-Programmable-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(Net::DNS::Resolver::Programmable)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Net::DNS)
BuildRequires:  perl(Net::DNS::Packet)
BuildRequires:  perl(Net::DNS::Resolver)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Net::DNS::Resolver::Programmable is a Net::DNS::Resolver descendant class
that allows a virtual DNS to be emulated instead of querying the real DNS.
A set of static DNS records may be supplied, or arbitrary code may be
specified as a means for retrieving DNS records, or even generating them
on the fly.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Net-DNS-Resolver-Programmable-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.009-24
- Prepare for Oreon 11 (RP1)
