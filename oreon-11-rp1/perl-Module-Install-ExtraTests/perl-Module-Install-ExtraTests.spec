%global source0_hash 643d528490df5f4fd8c9cf6afe431d32465f2d27b24bdddc0a53b02618e57db0

Name:       perl-Module-Install-ExtraTests 
Version:    0.008
Release:    37%{?dist}
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:    Ignorable, contextual test support for Module::Install
Url:        https://metacpan.org/release/Module-Install-ExtraTests
Source:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Module-Install-ExtraTests-%{version}.tar.gz
Patch0:     Module-Install-ExtraTests-0.008-Fix-building-on-Perl-without-dot-in-INC.patch
BuildArch:  noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(strict)
# Run-time
BuildRequires:  perl(ExtUtils::Command)
BuildRequires:  perl(File::Spec)
# Tests
BuildRequires:  perl(Test::More)
Requires:       perl(ExtUtils::Command)
Requires:       perl(File::Find)
Requires:       perl(File::Spec)

%description
This allows extra_tests; to be declared in Makefile.PL, indicating that the 
test files found in the directory ./xt should be run only in certain 
instances:

  ./xt/author  - run when the tests are being run in an author's working copy
  ./xt/smoke   - run when the dist is being smoked (AUTOMATED_TESTING=1)
  ./xt/release - run during "make disttest"

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Module-Install-ExtraTests-%{version}
%patch -P0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes LICENSE README 
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.008-37
- Prepare for Oreon 11 (RP1)
