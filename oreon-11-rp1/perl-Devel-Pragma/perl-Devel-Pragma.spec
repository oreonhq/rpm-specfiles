%global source0_hash f93c9b5ac3a7bb17969f5f4a0bdd3c342da163e40996cc78feb7fac706a83ba0
Name:           perl-Devel-Pragma
Version:        1.1.0
Release:        1%{?dist}
Summary:        Helper functions for developers of lexical pragmas
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-Pragma
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHOCOLATE/Devel-Pragma-%{version}.tar.gz
Requires:       perl(Lexical::SealRequireHints) >= 0.010
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude|%__requires_exclude|}^perl\\(Lexical::SealRequireHints\\)$
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Lexical::SealRequireHints)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides helper functions for developers of lexical pragmas.
These can be used both in older versions of perl (from 5.8.1), which have
limited support for lexical pragmas, and in the most recent versions, which
have improved support.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Devel-Pragma-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
