%global source0_hash 040f16f3066647d761b724a3b70754d28cbd1e6fe5ea01c63ed1cd857117d639

#TODO: BR:/R: perl(IP::Authority) when available

Name:           perl-Net-IP
Version:        1.26
Release:        37%{?dist}
Summary:        Perl module for manipulation of IPv4 and IPv6 addresses
# Some ambiguity here, see http://rt.cpan.org/Ticket/Display.html?id=28689
# HPND (MIT-like) for the IP.pm itself, and "like Perl itself" for all the other
# scripts included.
License:        HPND AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
URL:            https://metacpan.org/release/Net-IP
Source:         https://cpan.metacpan.org/modules/by-module/Net/Net-IP-%{version}.tar.gz
Patch0:         Net-IP-1.26-rt60439.patch
Patch1:         Net-IP-1.26-shellbang.patch
BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Script Run-time:
BuildRequires:  perl(Getopt::Std)
# Tests:
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(lib)
# Dependencies:
# Not yet packaged: IP::Authority

%description
This is the Net::IP module, designed to allow easy manipulation of IPv4 and
IPv6 addresses.

Two applications using the Net::IP module are included: ipcount, an IP address
mini-calculator, which can calculate the number of IP addresses in a prefix or
all the prefixes contained in a given range; and iptab, which prints out a
handy IP "cheat sheet".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-IP-%{version}

# Apply fix for zero networks (#197425, CPAN RT#20265, CPAN RT#60439)
%patch -P 0

# Fix shellbangs in shipped scripts
%patch -P 1

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

# This should work for 0.0.0.0
# https://bugzilla.redhat.com/show_bug.cgi?id=197425
PERL5LIB=%{buildroot}%{perl_vendorlib} ./iptab

%files
%license COPYING
%doc Changes README
# GPL-1.0-or-later OR Artistic-1.0-Perl
%{_bindir}/ipcount
%{_bindir}/iptab
# HPND
%{perl_vendorlib}/Net/
%{_mandir}/man3/Net::IP.3*

%changelog
%autochangelog
