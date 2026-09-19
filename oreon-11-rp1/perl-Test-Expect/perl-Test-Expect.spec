%global source0_hash 2628fcecdda5f649bd25323f646b96a1a07e4557cadcb327c9bad4dc41bbb999

Name:           perl-Test-Expect
Version:        0.34
Release:        27%{?dist}
Summary:        Automated driving and testing of terminal-based programs
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Expect
Source0:        https://cpan.metacpan.org/authors/id/B/BP/BPS/Test-Expect-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Class::Accessor::Chained::Fast)
BuildRequires:  perl(Expect::Simple)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Expect)
BuildRequires:  perl(lib)
BuildRequires:  perl(Term::ReadLine)
BuildRequires:  perl(Test::More)

%description
Test::Expect is a module for automated driving and testing of
terminal-based programs. It is handy for testing interactive programs
which have a prompt, and is based on the same concepts as the Tcl Expect
tool. As in Expect::Simple, the Expect object is made available for
tweaking.

Test::Expect is intended for use in a test script.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Expect-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc CHANGES README
%{perl_vendorlib}/Test/
%{_mandir}/man3/*.3pm*

%changelog
%autochangelog
