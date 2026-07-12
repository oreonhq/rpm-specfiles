%global source0_hash efe5e2be70425efc123a4e57f4b96b2d23beb03200c8326495b5b433b6b77158

Name:           perl-DateTime-Format-Strptime
Epoch:          1
Version:        1.80
Release:        2%{?dist}
Summary:        Parse and format strptime and strftime patterns
License:        Artistic-2.0
URL:            https://metacpan.org/release/DateTime-Format-Strptime
Source0:        https://cpan.metacpan.org/modules/by-module/DateTime/DateTime-Format-Strptime-%{version}.tar.gz



BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(DateTime) >= 1.00
BuildRequires:  perl(DateTime::Locale) >= 1.30
BuildRequires:  perl(DateTime::Locale::Base)
BuildRequires:  perl(DateTime::TimeZone) >= 2.09
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Params::ValidationCompiler)
BuildRequires:  perl(parent)
BuildRequires:  perl(Specio) >= 0.33
BuildRequires:  perl(Specio::Declare)
BuildRequires:  perl(Specio::Exporter)
BuildRequires:  perl(Specio::Library::Builtins)
BuildRequires:  perl(Specio::Library::String)
BuildRequires:  perl(strict)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(utf8)
# Optional Tests
BuildRequires:  perl(CPAN::Meta) >= 2.120900
BuildRequires:  perl(CPAN::Meta::Prereqs)
# Dependencies
# (none)

Provides:       perl(DateTime::Format::Strptime)
%description
This module implements most of strptime(3), the POSIX function that is the
reverse of strftime(3), for DateTime. While strftime takes a DateTime and a
pattern and returns a string, strptime takes a string and a pattern and
returns the DateTime object associated.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n DateTime-Format-Strptime-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%{perl_vendorlib}/DateTime/
%{_mandir}/man3/DateTime::Format::Strptime.3*
%{_mandir}/man3/DateTime::Format::Strptime::Types.3*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:1.80-2
- Import
