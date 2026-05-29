%global source0_hash ec5a82dfb7028bcd28bb3d569f95d87dd4166cc19867f2184ed3a59f6d6ca0e7

Name:           perl-NetAddr-IP
Version:        4.079
Release:        35%{?dist}
Summary:        Manages IPv4 and IPv6 addresses and subnets
# Lite/Util/Util.xs is GPL-2.0-or-later
# Other files are (GPL-2.0-or-later OR Artistic-1.0-Perl)
License:        GPL-2.0-or-later AND (GPL-2.0-or-later OR Artistic-1.0-Perl)
URL:            https://metacpan.org/release/NetAddr-IP
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIKER/NetAddr-IP-4.079.tar.gz
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Pod::Text)
# Module Runtime
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(overload)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
# Runtime
Requires:       perl(Math::BigInt)

# Don't "provide" private Perl libs or redundant unversioned provides
%global __provides_exclude ^(perl\\(NetAddr::IP(::(InetBase|Util(PP)?))?\\)$|Util\\.so)

%description
This module provides an object-oriented abstraction on top of IP addresses
or IP subnets, that allows for easy manipulations.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n NetAddr-IP-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PERLLOCAL=1 NO_PACKLIST=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}

%check
make test

%files
%license Artistic Copying
%doc About-NetAddr-IP.txt Changes TODO docs/rfc1884.txt
%{perl_vendorarch}/auto/NetAddr/
%{perl_vendorarch}/NetAddr/
%{_mandir}/man3/NetAddr::IP.3*
%{_mandir}/man3/NetAddr::IP::InetBase.3*
%{_mandir}/man3/NetAddr::IP::Lite.3*
%{_mandir}/man3/NetAddr::IP::Util.3*
%{_mandir}/man3/NetAddr::IP::UtilPP.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.079-35
- Prepare for Oreon 11 (RP1)
