%global source0_hash f2de23e05cbcd0c2ba95f113a9a789f548d5aaa3cd395a7e75914a024b191844
Name:           perl-Env-ShellWords
Version:        0.02
Release:        1%{?dist}
Summary:        Environment variables for arguments as a Perl array
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Env-ShellWords
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Env-ShellWords-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Carp)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This Perl module provides an array-like interface to environment variables that
contain flags. For example Autoconf can uses the environment variables like
CFLAGS or LDFLAGS, and this allows you to manipulate those variables
without doing space quoting and other messy mucky stuff.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Env-ShellWords-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
