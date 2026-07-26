%global source0_hash 82b2d562608be5a47384bd4e9d0d3b8eef881b365f560d7062e28e5df5b62d2c

Name:           perl-Module-Install-TestML
Version:        0.02
Release:        34%{?dist}
Summary:        Module::Install support for TestML
# The URL to Artistic license is wrong,
# <https://github.com/ingydotnet/module-install-testml-pm/issues/1>
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Install-TestML
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/Module-Install-TestML-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# Module::Install::Base 1.10 not used at tests
# TestML::Setup not used at tests
# vars not used at tests
# Tests:
BuildRequires:  perl(Test::More)
# Test::Pod 1.41 not used
Requires:       perl(Module::Install::Base) >= 1.10
# TestML::Setup not available, removed from TestML-0.54_05,
# <https://github.com/ingydotnet/module-install-testml-pm/issues/2>
Requires:       perl(warnings)
# This module has been split from TestML
Conflicts:      perl-TestML < 0.47

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Module::Install::Base\\)$

%description
This module adds the use_testml_tap directive to Module::Install.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Install-TestML-%{version}

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
%doc Changes CONTRIBUTING LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
