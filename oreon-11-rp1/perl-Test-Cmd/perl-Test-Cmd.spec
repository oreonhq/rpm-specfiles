%global source0_hash cf3320ecdde791e0b8945a20c1f6f265d90f1e3dab18f1e23cb677c79d729684

Name:           perl-Test-Cmd
Version:        1.09
Release:        30%{?dist}
Summary:        Perl module for portable testing of commands and scripts
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Cmd
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/Test-Cmd-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
# Config not used at tests
# Cwd not used at tests
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
# File::Copy not used at tests
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Optional run-time:
BuildRequires:  perl(Algorithm::DiffOld)
# Tests:
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
# Optional tests:
# Test::Pod 1.00 not used
# Optional run-time:
Requires:       perl(Algorithm::DiffOld)

Provides:       perl(Test::Cmd)
%description
The Test::Cmd module provides a framework for portable automated testing
of executable commands and scripts (in any language, not just Perl),
especially commands and scripts that interace with the file system.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Cmd-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test



%files
%doc Changes README
%{perl_vendorlib}/Test/
%{_mandir}/man3/*.3pm*


%changelog
%autochangelog
