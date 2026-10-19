%global source0_hash efe5e2be70425efc123a4e57f4b96b2d23beb03200c8326495b5b433b6b77158
Name:           perl-DateTime-Format-Strptime
Epoch:          1
Version:        1.80
Release:        1%{?dist}
Summary:        Parse and format strptime and strftime patterns
License:        Artistic-2.0
URL:            https://metacpan.org/release/DateTime-Format-Strptime
Source0:        https://cpan.metacpan.org/modules/by-module/DateTime/DateTime-Format-Strptime-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(DateTime::Format::Strptime)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Locale)
BuildRequires:  perl(DateTime::Locale::Base)
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Params::ValidationCompiler)
BuildRequires:  perl(Specio)
BuildRequires:  perl(Specio::Declare)
BuildRequires:  perl(Specio::Exporter)
BuildRequires:  perl(Specio::Library::Builtins)
BuildRequires:  perl(Specio::Library::String)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:1.80-2
- Import
