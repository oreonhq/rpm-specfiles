%global source0_hash b7349a9fa926d503472998d1e0b8c3a7fcae0edc7ce30ada4ee756cdb252a37c
Name:           perl-match-simple
Version:        0.012
Release:        1%{?dist}
Summary:        Simplified clone of smartmatch operator
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            http://search.cpan.org/dist/match-simple/
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/match-simple-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Carp)
Requires:       perl(Exporter::Tiny) >= 0.026
Requires:       perl(overload)
Requires:       perl(Sub::Infix) >= 0.004
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Exporter::Tiny\\)$
Provides:       perl(match::simple)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter::Tiny)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Infix)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::RefHash)
BuildRequires:  perl(if)
BuildRequires:  perl(overload)
BuildRequires:  perl(overloading)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
match::simple provides a simple match operator |M| that acts like a sane
subset of the (as of Perl 5.18) deprecated smart match operator. Unlike
smart match, the behaviour of the match is determined entirely by the
operand on the right hand side.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n match-simple-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
%make_build
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

unset MATCH_SIMPLE_IMPLEMENTATION
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
