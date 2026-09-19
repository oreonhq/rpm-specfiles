%global source0_hash 266be8702c5c2ca7d23497f8cada27f017a2192b6d367100d9f7e81b46b841f7

# This file is licensed under the terms of GNU GPLv2+.
Name:           perl-Unicode-Casing
Version:        0.16
Release:        33%{?dist}
Summary:        Perl extension to override system case changing functions
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Unicode-Casing
Source0:        https://cpan.metacpan.org/authors/id/K/KH/KHW/Unicode-Casing-%{version}.tar.gz
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(B::Hooks::OP::Check)
BuildRequires:  perl(B::Hooks::OP::PPAddr)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(if)
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
This module allows overriding the system-defined character case changing
functions. Any time something in its lexical scope would ordinarily call
lc(), lcfirst(), uc(), or ucfirst() the corresponding user-specified
function will instead be called. This applies to direct calls, and indirect
calls via the \L, \l, \U, and \u escapes in double quoted strings and
regular expressions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Unicode-Casing-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Unicode*
%{_mandir}/man3/*

%changelog
%autochangelog
