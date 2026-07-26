%global source0_hash d07fa580529beac6a9c8274c6bf220b4c3aade685df65c1669d53339bf6ef1e8

Name:           perl-Time-Period
Version:        1.25
Release:        30%{?dist}
Summary:        A Perl module to deal with time periods

# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Time-Period
Source0:        https://cpan.metacpan.org/authors/id/P/PB/PBOYD/Time-Period-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Exporter)
# Tests:
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)

%description
Period.pm is a Perl module that contains code to deal with time periods.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Time-Period-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc LICENSE README
# For noarch packages: vendorlib
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
