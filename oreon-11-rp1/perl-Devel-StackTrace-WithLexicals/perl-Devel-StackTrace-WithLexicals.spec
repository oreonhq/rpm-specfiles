%global source0_hash 693d6e7c7d77833b5288d2378555abd0127bb3f139201e7573e8780d3f6455c6

Name:           perl-Devel-StackTrace-WithLexicals
Version:        2.01
Release:        33%{?dist}
Summary:        Generate stack traces with lexical variables
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-StackTrace-WithLexicals
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SARTAK/Devel-StackTrace-WithLexicals-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::GithubMeta)
BuildRequires:  perl(Module::Install::WriteAll)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Devel::StackTrace) >= 2.00
BuildRequires:  perl(Devel::StackTrace::Frame)
BuildRequires:  perl(PadWalker) >= 1.98
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(bytes)
BuildRequires:  perl(overload)
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(Devel::StackTrace) >= 2.00
Requires:       perl(PadWalker) >= 1.98

# filter bogus requires on internal Devel::StackTrace package
%?perl_default_filter
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Devel::StackTrace\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(PadWalker\\)$

%description
Devel::StackTrace is pretty good at generating stack traces.

PadWalker is pretty good at the inspection and modification of your callers'
lexical variables.

Devel::StackTrace::WithLexicals is pretty good at generating stack traces with
all your callers' lexical variables.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Devel-StackTrace-WithLexicals-%{version}
# Remove bundled modules
rm -rf inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
