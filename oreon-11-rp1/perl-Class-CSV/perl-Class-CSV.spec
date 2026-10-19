%global source0_hash bce148284947a2cf7375eac13260fbfe23cb6b8c215970e3af7049b36de5e354
Name:           perl-Class-CSV
Version:        1.03
Release:        1%{?dist}
Summary:        Class based CSV parser/writer
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-CSV
Source0:        https://cpan.metacpan.org/authors/id/D/DJ/DJR/Class-CSV-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Class::Accessor) >= 0.18
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Class::Accessor\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test)
BuildRequires:  perl(Text::CSV_XS)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
