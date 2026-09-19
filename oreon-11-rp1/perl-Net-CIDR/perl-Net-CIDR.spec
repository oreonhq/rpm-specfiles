%global source0_hash 9e950fef4422264dc8efab30dbbd3ce2be125e61b3f5c50111d15506d3b570e3

Name:           perl-Net-CIDR
Version:        0.27
Release:        2%{?dist}
Summary:        Manipulate IPv4/IPv6 netblocks in CIDR notation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Net-CIDR
Source0:        https://cpan.metacpan.org/modules/by-module/Net/Net-CIDR-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
# Test Suite
BuildRequires:  perl(Test::More) >= 1
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Dependencies
# (no additional dependencies)

%description
The Net::CIDR package contains functions that manipulate lists of IP netblocks
expressed in CIDR notation. The Net::CIDR functions handle both IPv4 and IPv6
addresses.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-CIDR-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
%{make_build} test

%files
%license COPYING
%doc ChangeLog README
%{perl_vendorlib}/Net/
%{_mandir}/man3/Net::CIDR.3*

%changelog
%autochangelog
