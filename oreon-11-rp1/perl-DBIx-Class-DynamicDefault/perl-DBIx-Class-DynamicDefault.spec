%global source0_hash 228f51ab224642584b4dc63db6de2667c5bfae2a894a9376b210a104806a5afb

Name:       perl-DBIx-Class-DynamicDefault 
Version:    0.04
Release:    40%{?dist}
# lib/DBIx/Class/DynamicDefault.pm -> GPL+ or Artistic
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:    Automatically set and update fields 
Url:        https://metacpan.org/release/DBIx-Class-DynamicDefault
Source:     https://cpan.metacpan.org/authors/id/M/MS/MSTROUT/DBIx-Class-DynamicDefault-%{version}.tar.gz
BuildArch:  noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::ExtraTests)
BuildRequires:  perl(Module::Install::Makefile)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(DBIx::Class) >= 0.08127
# Tests:
BuildRequires:  perl(DBICx::TestDatabase)
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(Test::More)
Requires:       perl(DBIx::Class) >= 0.08127

%{?perl_default_filter}
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(DBIx::Class\\)$

%description
Automatically set and update fields with values calculated at run time.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DBIx-Class-DynamicDefault-%{version}
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/DBIx/Class/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
