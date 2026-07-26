%global source0_hash 63dfd45c5b90fba94be958254b8545cba4e5a7a5de06db62529cd990d18563ea

# Perform optional tests
%bcond_without perl_MooseX_Types_DateTime_enables_optional_test

Name:       perl-MooseX-Types-DateTime
Version:    0.14
Release:    2%{?dist}
# see, e.g., lib/MooseX/Types/DateTime.pm
License:    GPL-1.0-or-later OR Artistic-1.0-Perl

Summary:    DateTime related constraints and coercions for Moose
Source:     https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Types-DateTime-%{version}.tar.gz
Url:        https://metacpan.org/release/MooseX-Types-DateTime
BuildArch:  noarch

BuildRequires: coreutils
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl-macros
BuildRequires: perl(Module::Build::Tiny) >= 0.034
# Run-time:
BuildRequires: perl(DateTime) >= 0.43
BuildRequires: perl(DateTime::Duration) >= 0.43
BuildRequires: perl(DateTime::Locale) >= 0.40
BuildRequires: perl(DateTime::TimeZone) >= 0.95
BuildRequires: perl(if)
BuildRequires: perl(Moose) >= 0.41
BuildRequires: perl(MooseX::Types) >= 0.30
BuildRequires: perl(MooseX::Types::Moose) >= 0.30
BuildRequires: perl(namespace::autoclean)
BuildRequires: perl(namespace::clean) >= 0.19
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
# Tests:
BuildRequires: perl(File::Spec)
BuildRequires: perl(Module::Metadata)
BuildRequires: perl(Moose::Util::TypeConstraints)
BuildRequires: perl(ok)
BuildRequires: perl(Term::ANSIColor)
BuildRequires: perl(Test::Fatal)
BuildRequires: perl(Test::More) >= 0.88
BuildRequires: perl(Test::Warnings)
BuildRequires: perl(ok)
%if %{with perl_MooseX_Types_DateTime_enables_optional_test}
# Optional tests:
BuildRequires: perl(Locale::Maketext)
%endif
# Clamp version to decimal 2 digits
Requires:   perl(DateTime) >= 0.43
Requires:   perl(DateTime::Duration) >= 0.43
Requires:   perl(DateTime::Locale) >= 0.40
Requires:   perl(namespace::autoclean)

%{?perl_default_filter}

# Remove over-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(DateTime[:)].*\\.[0-9]{3,}$

%description
This module packages several type constraints (Moose::Util::TypeConstraints)
and coercions designed to work with the DateTime suite of objects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Types-DateTime-%{version}

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes t
%license LICENCE
%{perl_vendorlib}/MooseX*
%{_mandir}/man3/MooseX*.3*

%changelog
%autochangelog
