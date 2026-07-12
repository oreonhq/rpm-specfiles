%global source0_hash cd2c59d58061ce1a4975a313160df7186f62eea2655b85d520e5e24e9eeb0fe9

Name:           perl-constant-boolean
Version:        0.02
Release:        44%{?dist}
Summary:        Define TRUE and FALSE constants
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/constant-boolean
Source0:        https://cpan.metacpan.org/authors/id/D/DE/DEXTER/constant-boolean-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol::Util)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More) >= 0.88
# Dependencies
Requires:       perl(Symbol::Util)

Provides:       perl(constant::boolean)
%description
Defines TRUE and FALSE constants in caller's namespace. You could use
simple values like empty string or zero for false, or any non-empty and non-
zero string value as true, but the TRUE and FALSE constants are more
descriptive.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n constant-boolean-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
%{make_build} test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/constant/
%{_mandir}/man3/constant::boolean.3*

%changelog
%autochangelog
