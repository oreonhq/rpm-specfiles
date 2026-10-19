%global source0_hash 6283dbe2197e2f20009cc4b449997742169cdd951bfc44cbc6e62c2a962d3147
Name:           perl-Devel-StackTrace-AsHTML
Summary:        Displays a stack trace in HTML
Version:        0.15
Release:        29%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Devel-StackTrace-AsHTML-%{version}.tar.gz
URL:            https://metacpan.org/release/Devel-StackTrace-AsHTML
BuildArch:      noarch
Requires:       perl(warnings)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  /usr/bin/make
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Devel::StackTrace::AsHTML adds an 'as_html' method to Devel::StackTrace
which displays the stack trace in beautiful HTML, with code snippet
context and function parameters. If you call it on an instance of
Devel::StackTrace::WithLexicals, you even get to see the lexical
variables of each stack frame.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Devel-StackTrace-AsHTML-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

%{__make} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
