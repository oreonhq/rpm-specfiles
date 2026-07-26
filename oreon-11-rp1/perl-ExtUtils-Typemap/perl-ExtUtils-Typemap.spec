%global source0_hash b1b015772dbb068b93a0f6ffa02f5d94822365e6018ac5ed2bc53ca669071fc7

Name:           perl-ExtUtils-Typemap
Version:        1.00
Release:        34%{?dist}
Summary:        Read/Write/Modify Perl/XS typemap files
# README says "as Perl..."
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/ExtUtils-Typemap
Source0:        https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/ExtUtils-Typemap-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::Typemaps)
BuildRequires:  perl(ExtUtils::Typemaps::InputMap)
BuildRequires:  perl(ExtUtils::Typemaps::OutputMap)
BuildRequires:  perl(ExtUtils::Typemaps::Type)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More)

%description
This module exists merely as a compatibility wrapper around
ExtUtils::Typemaps. In a nutshell, ExtUtils::Typemap was renamed to
ExtUtils::Typemaps because the Typemap directory in lib/ could collide with
the typemap file on case-insensitive file systems.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ExtUtils-Typemap-%{version}

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
%{perl_vendorlib}/ExtUtils/Typemap.pm
%{perl_vendorlib}/ExtUtils/Typemap/
%{_mandir}/man3/ExtUtils::Typemap.3*
%{_mandir}/man3/ExtUtils::Typemap::*

%changelog
%autochangelog
