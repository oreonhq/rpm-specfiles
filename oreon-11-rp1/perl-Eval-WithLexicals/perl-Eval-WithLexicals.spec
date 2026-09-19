%global source0_hash 66f127e69451cc3ae44c49143a70bbe11e1adb8120bf3ef8ecac908301ae0974

Name:           perl-Eval-WithLexicals
Version:        1.003006
Release:        25%{?dist}
Summary:        Pure Perl eval with persistent lexical variables
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Eval-WithLexicals
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/Eval-WithLexicals-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(B)
BuildRequires:  perl(Moo) >= 0.009006
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Sub::Quote)
# Tests
BuildRequires:  perl(lib)
BuildRequires:  perl(strictures) >= 1
BuildRequires:  perl(Test::More) >= 0.94
Requires:       perl(Moo) >= 0.009006

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Moo\\)$

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Eval-WithLexicals-%{version}
perl -MConfig -i -pe 's{^#!.*perl}{$Config{startperl}}' bin/tinyrepl

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
%autochangelog
