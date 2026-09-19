%global source0_hash 09ff5367e83a752f1279f31d8ac05b62360222bb438dc58a71f7e39506298c70

Name:           perl-Mail-Procmail
Version:        1.08
Release:        39%{?dist}
Summary:        Procmail-like facility for creating easy mail filters
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Mail-Procmail
Source0:        https://cpan.metacpan.org/authors/id/J/JV/JV/Mail-Procmail-%{version}.tar.gz
# pm_report display,summing fixes [rt.cpan.org #83152]
Patch0:         pm_report.patch
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(LockFile::Simple)
BuildRequires:  perl(Mail::Internet)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)

%{?perl_default_filter}

%description
procmail is a great mail filter program, but it has weird recipe
format. It's pattern matching capabilities are basic and often
insufficient. This module provides flexibility to filter your
mail using the power of Perl.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Mail-Procmail-%{version}
%patch -P0 -p1 -b .pm_report

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
