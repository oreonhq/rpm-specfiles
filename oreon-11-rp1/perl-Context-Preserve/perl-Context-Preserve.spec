%global source0_hash 09914a4c2c7bdb99cab680c183cbf492ec98d6e23fbcc487fcc4ae10567dfd1f

Name:           perl-Context-Preserve
Summary:        Run code after a subroutine call, preserving the context
Version:        0.03
Release:        25%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Context-Preserve-%{version}.tar.gz
URL:            https://metacpan.org/release/Context-Preserve
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
# Tests only
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(ok)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)

%description
Sometimes you need to call a function, get the results, act on the results,
then return the result of the function. This is painful because of contexts;
the original function can behave different if it's called in void, scalar, or
list context. You can ignore the various cases and just pick one, but that's
fragile. To do things right, you need to see which case you're being called
in, and then call the function in that context. This results in 3 code paths,
which is a pain to type in (and maintain).  This module automates the process.
You provide a code reference that is the "original function", and another code
reference to run after running the original. You can modify the return value
(aliased to @_) here, and do whatever else you need to do. 'wantarray' is
correct inside both code references; in "after", though, the return value is
ignored and the value 'wantarray' returns is related to the context that the
original function was called in.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Context-Preserve-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENCE
%doc CONTRIBUTING README Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
