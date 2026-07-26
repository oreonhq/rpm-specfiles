%global source0_hash 96292d29edf85eca10724a00e0af509c40b17b9b5638c00332d703599b6f3b74

Name:           perl-Data-Printer
Version:        1.002001
Release:        5%{?dist}
Summary:        Pretty printer for Perl data structures
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-Printer
Source0:        https://cpan.metacpan.org/modules/by-module/Data/Data-Printer-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(B)
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Devel::Size)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Hash::Util::FieldHash)
# Hash::Util::FieldHash::Compat not used
BuildRequires:  perl(if)
BuildRequires:  perl(mro)
# MRO::Compat not used
BuildRequires:  perl(Package::Stash) >= 0.3
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sort::Naturally)
BuildRequires:  perl(Term::ANSIColor) >= 3
BuildRequires:  perl(charnames)
BuildRequires:  perl(overload)
BuildRequires:  perl(version) >= 0.77
# Win32::Console::ANSI not used
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(File::HomeDir::Test)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More) >= 0.88
# Optional tests:
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Cpanel::JSON::XS)
BuildRequires:  perl(Date::Handler::Delta)
BuildRequires:  perl(Date::Pcalc::Object)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Tiny)
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(DateTime::Incomplete)
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

%check
%{make_build} test

%files
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
