%global source0_hash 63dfd45c5b90fba94be958254b8545cba4e5a7a5de06db62529cd990d18563ea
%bcond_without perl_MooseX_Types_DateTime_enables_optional_test
Name:       perl-MooseX-Types-DateTime
Version:    0.14
Release:        1%{?dist}
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:        DateTime related constraints and coercions for Moose
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Types-DateTime-%{version}.tar.gz
Url:        https://metacpan.org/release/MooseX-Types-DateTime
BuildArch:  noarch
%if %{with perl_MooseX_Types_DateTime_enables_optional_test}
%endif
Requires:   perl(DateTime) >= 0.43
Requires:   perl(DateTime::Duration) >= 0.43
Requires:   perl(DateTime::Locale) >= 0.40
Requires:   perl(namespace::autoclean)
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(DateTime[:)].*\\.[0-9]{3,}$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Duration)
BuildRequires:  perl(DateTime::Locale)
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Locale::Maketext)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(if)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(ok)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl-macros
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
