%global source0_hash e387ef5737d052de33c3589748fa8dad368fc0b010c71dd865dcfb830976659e
Name:           perl-Cflow
Version:        1.053
Release:        1%{?dist}
Summary:        Find flows in raw IP flow files
License:        GPL-2.0-or-later
URL:            http://pages.cs.wisc.edu/~plonka/Cflow/
Source0:        http://pages.cs.wisc.edu/~plonka/Cflow/Cflow-%{version}.tar.gz
Patch0:         perl-Cflow-ccflags.patch
Patch1:         perl-Cflow-flow-tools.patch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  findutils
BuildRequires:  flow-tools-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
