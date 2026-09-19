%global source0_hash 63b13680793a83b4c0e0f7744439f44e3a5b4f2569c31e598ed93d7907567524

Name:           perl-SVG-TT-Graph
Version:        1.04
Release:        18%{?dist}
Summary:        Base object for generating SVG Graphs
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/SVG-TT-Graph
Source0:        https://cpan.metacpan.org/authors/id/L/LL/LLAP/SVG-TT-Graph-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Template)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

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

%check
%{make_build} test

%files
%doc Changes README script
%license LICENSE
%{perl_vendorlib}/SVG*
%{_mandir}/man3/SVG*

%changelog
%autochangelog
