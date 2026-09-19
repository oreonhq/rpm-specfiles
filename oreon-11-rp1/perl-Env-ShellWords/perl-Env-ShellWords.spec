%global source0_hash f2de23e05cbcd0c2ba95f113a9a789f548d5aaa3cd395a7e75914a024b191844

Name:           perl-Env-ShellWords
Version:        0.02
Release:        25%{?dist}
Summary:        Environment variables for arguments as a Perl array
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Env-ShellWords
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Env-ShellWords-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Text::ParseWords)
# Tests:
BuildRequires:  perl(Config)
BuildRequires:  perl(Test2::V0) >= 0.000060
# Optional tests:
# Test::More not helpful
Requires:       perl(Carp)

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

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
