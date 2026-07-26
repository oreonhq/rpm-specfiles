%global source0_hash fa88c2d4af0b1126d46401e6355a65496d033cfc2a6a944653011a638adfa75c

Name:           perl-LV
Version:        0.006
Release:        32%{?dist}
Summary:        Perl module to make lvalue subroutines easy and practical
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/LV
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/LV-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Sentinel)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(Variable::Magic)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
This module makes lvalue subroutines easy and practical to use. It's
inspired by the lvalue module which is sadly problematic because of the
existence of another module on CPAN called Lvalue.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n LV-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes CONTRIBUTING COPYRIGHT CREDITS README
%license LICENSE
%{perl_vendorlib}/LV*
%{_mandir}/man3/LV*

%changelog
%autochangelog
