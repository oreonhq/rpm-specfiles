Name:           perl-List-Pairwise
Version:        1.03
Release:        33%{?dist}
Summary:        Map/grep arrays and hashes pairwise
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/List-Pairwise
Source0:        https://cpan.metacpan.org/authors/id/T/TD/TDRUGEON/List-Pairwise-%{version}.tar.gz
Patch0:         List-Pairwise-1.03-Fix-building-on-Perl-without-dot-in-INC.patch
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
# Runtime
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
# List::Util is not used
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests only
# Devel::Cover is not used, because t/coverage.pl is not executed
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.42

%description
List::Pairwise provides functions to map and grep lists two elements at a
time, setting $a and $b to each pair instead of setting $_ to each element.

%prep
%setup -q -n List-Pairwise-%{version}
%patch -P0 -p1
# Remove bundled modules
rm -rf inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changelog
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.03-33
- Prepare for Oreon 11 (RP1)
