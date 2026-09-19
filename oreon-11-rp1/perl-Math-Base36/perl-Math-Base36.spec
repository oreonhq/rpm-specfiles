%global source0_hash eedcc8cb22b8f6b6c07742e55931f6e9d03771d221d0b76639f18a3b7d19f47f

# Perform optional tests
%bcond_without perl_Math_Base36_enables_optional_test

Name:           perl-Math-Base36
Version:        0.14
Release:        32%{?dist}
Summary:        Encoding and decoding of base36 strings
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Math-Base36
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRICAS/Math-Base36-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(inc::Module::Install) >= 1.00
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
%if %{with perl_Math_Base36_enables_optional_test}
# Optional tests only
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
%endif

%{?perl_default_filter}

%description
This module converts to and from Base36 numbers (0..9 - A..Z).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Math-Base36-%{version}
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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
