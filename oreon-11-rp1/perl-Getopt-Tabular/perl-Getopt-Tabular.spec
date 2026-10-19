%global source0_hash 9bdf067633b5913127820f4e8035edc53d08372faace56ba6bfa00c968a25377
Name:           perl-Getopt-Tabular
Version:        0.3
Release:        1%{?dist}
Summary:        Table-driven argument parsing for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Getopt-Tabular
Source0:        https://cpan.metacpan.org/authors/id/G/GW/GWARD/Getopt-Tabular-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(Getopt::Tabular)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Getopt::Tabular is a Perl module for table-driven argument parsing,
vaguely inspired by John Ousterhout's Tk_ParseArgv.  All you really need
to do to use the package is set up a table describing all your command-line
options, and call &GetOptions.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Getopt-Tabular-%{version}
sed -i 's#/usr/local/bin/perl5#%{__perl}#' demo
chmod a-x demo

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
