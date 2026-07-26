%global source0_hash b60db5ae19cea890c9ae292e96ff5c0789e73b0cce8b20b212057b3904e33e96

Name:           perl-Test-DBICSchemaLoaderDigest
Version:        0.04
Release:        39%{?dist}
Summary:        Test the DBIC::Schema::Loader's MD5 sum
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-DBICSchemaLoaderDigest
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSRCHBOY/Test-DBICSchemaLoaderDigest-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Test::More)
# Tests:
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More) >= 0.88

%description
DBIC::Schema::Loader dumps follow code:

  DO NOT MODIFY THIS OR ANYTHING ABOVE! md5sum:2lkIltTa9Ey3fExXmUB/gw
  But, some programmer MODIFY THE ABOVE OF THIS CODE!

This module tests a module MD5 check sum. If you use this module, you can stop
this problem.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-DBICSchemaLoaderDigest-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
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
