%global source0_hash 87c85c6edffcea4f96e6b4800f6f9512aeab19eb8d3b348301a721331bcb8580
Name:           perl-GraphViz2
Version:        2.67
Release:        1%{?dist}
Summary:        GraphViz2 Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/GraphViz2
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETJ/GraphViz2-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  graphviz
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  perl(Config)
BuildRequires:  perl(Config::Tiny)
BuildRequires:  perl(Data::Section::Simple)
BuildRequires:  perl(Date::Simple)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Graph::Directed)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Snapshot)
BuildRequires:  perl(Text::Xslate)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides a Perl interface to the amazing Graphviz, an open
source graph visualization tool from AT&T. It is called GraphViz2 so
that preexisting code using (the Perl module) GraphViz continues to work.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n GraphViz2-%{version}

%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
