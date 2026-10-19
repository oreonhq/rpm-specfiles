%global source0_hash d94f520804e2541b1cd20e73366720a973caf5dd2d2623838fc8d6398afd7edb
Name:           perl-Net-Patricia
Version:        1.24
Release:        1%{?dist}
Summary:        Patricia Trie perl module for fast IP address lookups
License:        GPL-2.0-or-later AND LicenseRef-Callaway-BSD
URL:            https://metacpan.org/release/Net-Patricia
Source0:        https://cpan.metacpan.org/modules/by-module/Net/Net-Patricia-%{version}.tar.gz
Requires:       perl(DynaLoader)
Requires:       perl(Exporter)
Requires:       perl(Net::CIDR::Lite) >= 0.20
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Net::CIDR::Lite)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Socket6)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(diagnostics)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module uses a Patricia Trie data structure to quickly perform IP
address prefix matching for applications such as IP subnet, network or
routing table lookups.  The data structure is based on a radix tree using a
radix of two, so sometimes you see patricia implementations called "radix"
as well.  The term "Trie" is derived from the word "retrieval" but is
pronounced like "try".  Patricia stands for "Practical Algorithm to
Retrieve Information Coded as Alphanumeric", and was first suggested for
routing table lookups by Van Jacobsen.  Patricia Trie performance
characteristics are well-known as it has been employed for routing table
lookups within the BSD kernel since the 4.3 Reno release.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Net-Patricia-%{version}
%oreon_prep
%build

%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
%make_build
%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
