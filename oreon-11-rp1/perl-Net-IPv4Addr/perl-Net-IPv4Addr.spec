%global source0_hash 3845de4f30b17c842b192cace8879dbb6214de9692cfa70f0aaf0981422a63fe

Name:           perl-Net-IPv4Addr
Version:        0.10
Release:        51%{?dist}
Summary:        Perl extension for manipulating IPv4 addresses
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-IPv4Addr
Source0:        https://cpan.metacpan.org/authors/id/F/FR/FRAJULAC/Net-IPv4Addr-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
# Getopt::Long not used at tests
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(Test)
Requires:       perl(AutoLoader)
Requires:       perl(Exporter)
Obsoletes:      perl-Network-IPv4Addr < 0.10-1

%description
Net::IPv4Addr provides functions for parsing IPv4 addresses both in traditional
address/netmask format and in the new CIDR format. There are also methods for
calculating the network and broadcast address and also to see check if a given
address is in a specific network.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-IPv4Addr-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc ChangeLog NEWS README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man?/*

%changelog
%autochangelog
