%global source0_hash bce148284947a2cf7375eac13260fbfe23cb6b8c215970e3af7049b36de5e354

Name:           perl-Class-CSV
Version:        1.03
Release:        50%{?dist}
Summary:        Class based CSV parser/writer
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-CSV
Source0:        https://cpan.metacpan.org/authors/id/D/DJ/DJR/Class-CSV-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor) >= 0.18
BuildRequires:  perl(constant)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
BuildRequires:  perl(Text::CSV_XS) >= 0.23
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Requires:       perl(Class::Accessor) >= 0.18

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Class::Accessor\\)$

%description
This module can be used to create objects from CSV files, or to create CSV
files from objects. Text::CSV_XS is used for parsing and creating CSV file
lines, so any limitations in Text::CSV_XS will of course be inherant in
this module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-CSV-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
