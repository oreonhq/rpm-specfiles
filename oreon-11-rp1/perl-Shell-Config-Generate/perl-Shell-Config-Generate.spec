%global source0_hash 84f451f22215dd68e9c18aa3f7ddb03a82007d166cfada003d0f166f571e0562
Name:           perl-Shell-Config-Generate
Version:        0.34
Release:        18%{?dist}
Summary:        Portably generate configuration for any shell
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Shell-Config-Generate
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Shell-Config-Generate-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Shell::Guess) >= 0.02
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Shell::Guess\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Env)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Shell::Guess)
BuildRequires:  perl(Test2::API)
BuildRequires:  perl(Test2::Mock)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This Perl module provides an interface for specifying shell configurations for
different shell environments without having to worry about the arcane
differences between shells such as csh, sh, cmd.exe and command.com.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Shell-Config-Generate-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
