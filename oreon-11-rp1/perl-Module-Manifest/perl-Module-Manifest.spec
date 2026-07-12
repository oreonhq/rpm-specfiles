%global source0_hash a395f80ff15ea0e66fd6c453844b6787ed4a875a3cd8df9f7e29280250bd539b

Name:           perl-Module-Manifest
Version:        1.09
Release:        25%{?dist}
Summary:        Parse and examine a Perl distribution MANIFEST file
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Manifest
Source0:        https://cpan.metacpan.org/modules/by-module/Module/Module-Manifest-%{version}.tar.gz
BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec) >= 0.80
BuildRequires:  perl(File::Spec::Unix)
BuildRequires:  perl(Params::Util) >= 0.10
# Tests:
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Test::Exception) >= 0.27
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
# Optional tests:
# CPAN::Meta 2.120900 not helpful
# CPAN::Meta::Prereqs not helpful
# Dependencies:
Requires:       perl(File::Spec) >= 0.80
Requires:       perl(Params::Util) >= 0.10

# Do not export under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((File::Spec|Params::Util)\\)

Provides:       perl(Module::Manifest)
%description
Module::Manifest can load a MANIFEST file that comes in a Perl distribution
tarball, examine the contents, and perform some simple tasks. It can also load
the MANIFEST.SKIP file and check that.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Module-Manifest-%{version}

chmod -c -x examples/*

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING README examples
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
