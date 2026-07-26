%global source0_hash adb4d72b09e93cff7f400160957684d27b78b4c7b836aec894887ddb1eebd752

Name:           perl-ExtUtils-TBone
Version:        1.124
Release:        32%{?dist}
Summary:        Skeleton for writing t/*.t Perl test files
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/ExtUtils-TBone
Source0:        https://cpan.metacpan.org/authors/id/E/ER/ERYQ/ExtUtils-TBone-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)

%description
This module is intended for folks who release CPAN modules with t/*.t
tests. It makes it easy for you to output syntactically correct test-output
while at the same time logging all test activity to a log file. Hopefully,
bug reports which include the contents of this file will be easier for you
to investigate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ExtUtils-TBone-%{version}
# Remove a copy from lib to be sure we test the lib code
rm t/ExtUtils/TBone.pm
sed -i -e '/^t\/ExtUtils\/TBone.pm/d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license COPYING
%doc docs README 
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
