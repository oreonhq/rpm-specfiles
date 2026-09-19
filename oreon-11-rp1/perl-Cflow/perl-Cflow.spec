%global source0_hash e387ef5737d052de33c3589748fa8dad368fc0b010c71dd865dcfb830976659e

Name:           perl-Cflow
Version:        1.053
Release:        65%{?dist}
Summary:        Find flows in raw IP flow files
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://pages.cs.wisc.edu/~plonka/Cflow/
Source0:        http://pages.cs.wisc.edu/~plonka/Cflow/Cflow-%{version}.tar.gz
# Respect Perl's ccflags, bug #1459766,
# <http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=628522>
Patch0:         perl-Cflow-ccflags.patch
# Use system flow-tools
Patch1:         perl-Cflow-flow-tools.patch

BuildRequires:  findutils
BuildRequires:  flow-tools-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
# Run-time:
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
# English not used at tests
BuildRequires:  perl(Exporter)
# File::Basename not used at tests
# Getopt::Std not used at tests
# IO::File not used at tests
BuildRequires:  perl(POSIX)
# Socket not used at tests
BuildRequires:  perl(strict)
# Tests:
BuildRequires:  perl(Socket)

%{?perl_default_filter}

%description
Cflow with flow-tools support.  This module implements an API for
processing IP flow accounting information which as been collected from
routers and written into flow files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Cflow-%{version}
%patch -P0 -p1
%patch -P1 -p1 -b .flow-tools

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"

make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%license COPYING
%doc README Changes
%{_bindir}/flowdumper
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Cflow.pm
%{_mandir}/man1/flowdumper.1.gz
%{_mandir}/man3/*.3*

%changelog
%autochangelog
