%global source0_hash 63b13680793a83b4c0e0f7744439f44e3a5b4f2569c31e598ed93d7907567524
Name:           perl-SVG-TT-Graph
Version:        1.04
Release:        18%{?dist}
Summary:        Base object for generating SVG Graphs
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/SVG-TT-Graph
Source0:        https://cpan.metacpan.org/authors/id/L/LL/LLAP/SVG-TT-Graph-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Template)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
This package can be used as a base for creating SVG graphs with
Template Toolkit.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n SVG-TT-Graph-%{version}
# Remove bundled libraries
find . -type f -exec chmod 644 {} \;
sed -i '1s,#!.*perl,#!/usr/bin/perl,' script/timeseries.pl
# chmod +x script/*.pl

%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build} %{?_smp_mflags}
%install
%{make_install} DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
