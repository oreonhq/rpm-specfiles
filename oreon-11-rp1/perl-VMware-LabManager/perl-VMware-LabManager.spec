%global source0_hash a76155794441598c464e04b3c63177beae5c1cd0a048ba57ef9525add2c731dd

Name:           perl-VMware-LabManager
Version:        0.01
Release:        40%{?dist}
Summary:        Perl module to provide basic VMware Lab Manager operations
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/VMware-LabManager
Source0:        https://cpan.metacpan.org/authors/id/A/AI/AIVATURI/VMware-LabManager-%{version}.tar.gz
Patch0:         VMware-LabManager-0.01-Fix-building-on-Perl-without-dot-in-INC.patch
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# inc
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(CPAN)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
# Runtime, SOAP::Lite is needed for the debug mode
BuildRequires:  perl(SOAP::Lite)
BuildRequires:  perl(Time::HiRes)
# Tests only
BuildRequires:  perl(Test::More)
# Optional tests
BuildRequires:  perl(Pod::Coverage) >= 0.18
BuildRequires:  perl(Test::CheckManifest) >= 0.9
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
# In evals, not autodetected
Requires:       perl(SOAP::Lite)

%description
This module does not provide a one-to-one mapping of the Lab Manager SOAP
API, but rather it provides an API wrapper, which combines certain SOAP
calls as a meaningful single operation. Thus this module is heavily
tailored for automation purposes. But, it should also cater to the
broader audience as it still does provide overall functionality that
might be required.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n VMware-LabManager-%{version}
%patch -P0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
