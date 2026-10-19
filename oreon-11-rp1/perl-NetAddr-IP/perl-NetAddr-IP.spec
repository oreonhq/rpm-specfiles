%global source0_hash ec5a82dfb7028bcd28bb3d569f95d87dd4166cc19867f2184ed3a59f6d6ca0e7
Name:           perl-NetAddr-IP
Version:        4.079
Release:        1%{?dist}
Summary:        Manages IPv4 and IPv6 addresses and subnets
License:        GPL-2.0-or-later AND (GPL-2.0-or-later OR Artistic-1.0-Perl)
URL:            https://metacpan.org/release/NetAddr-IP
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIKER/NetAddr-IP-%{version}.tar.gz
Requires:       perl(Math::BigInt)
%global __provides_exclude ^(perl\\(NetAddr::IP(::(InetBase|Util(PP)?))?\\)$|Util\\.so)
Provides:       perl(NetAddr::IP)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Pod::Text)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides an object-oriented abstraction on top of IP addresses
or IP subnets, that allows for easy manipulations.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n NetAddr-IP-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PERLLOCAL=1 NO_PACKLIST=1
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.079-35
- Prepare for Oreon 11 (RP1)
