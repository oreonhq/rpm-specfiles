%global source0_hash 96292d29edf85eca10724a00e0af509c40b17b9b5638c00332d703599b6f3b74
Name:           perl-Data-Printer
Version:        1.002001
Release:        1%{?dist}
Summary:        Pretty printer for Perl data structures
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-Printer
Source0:        https://cpan.metacpan.org/modules/by-module/Data/Data-Printer-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(B)
Requires:       perl(B::Deparse)
Requires:       perl(File::HomeDir) >= 0.91
Requires:       perl(Hash::Util::FieldHash)
Requires:       perl(mro)
Requires:       perl(Package::Stash) >= 0.3
Requires:       perl(Term::ANSIColor) >= 3
Requires:       perl(version) >= 0.77
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\((File::HomeDir|Term::ANSIColor)\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Package::Stash\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(B)
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Cpanel::JSON::XS)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Date::Handler::Delta)
BuildRequires:  perl(Date::Pcalc::Object)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Incomplete)
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(DateTime::Tiny)
BuildRequires:  perl(Devel::Size)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::HomeDir::Test)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Hash::Util::FieldHash)
BuildRequires:  perl(Package::Stash)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sort::Naturally)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(charnames)
BuildRequires:  perl(if)
BuildRequires:  perl(mro)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Data::Printer is a Perl module to pretty-print Perl data structures and
objects in full color. It is meant to display variables on screen, properly
formatted to be inspected by a human.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-Printer-%{version}

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
