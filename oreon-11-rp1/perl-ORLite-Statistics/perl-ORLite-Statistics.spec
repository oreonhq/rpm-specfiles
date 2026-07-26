%global source0_hash 7e714b6eda1b922b52013e656c82772754a93e6ce60de19fe1aa9a43b7a0c826

Name:           perl-ORLite-Statistics
Version:        0.03
Release:        43%{?dist}
Summary:        Statistics enhancement package for ORLite
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/ORLite-Statistics
Source0:        https://cpan.metacpan.org/authors/id/A/AD/ADAMK/ORLite-Statistics-%{version}.tar.gz
# Update Makefile.PL to not use Module::Install::DSL CPAN RT#148300
Patch0:         ORLite-Statistics-0.03-Remove-using-of-MI-DSL.patch
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
# Runtime
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ORLite) >= 1.25
BuildRequires:  perl(Statistics::Basic) >= 1.6600
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Test::More) >= 0.47

%description
This is an enhancement module for ORLite table classes, designed to provide
easy integration with the Statistics::Base module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ORLite-Statistics-%{version}
%patch -P0 -p1
# Remove bundled modules
rm -r ./inc/*
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
unset AUTOMATED_TESTING RELEASE_TESTING
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/ORLite*
%{_mandir}/man3/ORLite*

%changelog
%autochangelog
