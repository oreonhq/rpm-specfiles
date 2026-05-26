Name:           perl-List-Pairwise
Version:        1.03
Release:        33%{?dist}
Summary:        Map/grep arrays and hashes pairwise
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/List-Pairwise
Source0:        https://cpan.metacpan.org/authors/id/T/TD/TDRUGEON/List-Pairwise-%{version}.tar.gz
Patch0:         List-Pairwise-1.03-Fix-building-on-Perl-without-dot-in-INC.patch
# oreon url source checksums begin
%global source0_sha256 96d716f2b2832cf42875e3a4f81752a025be94c3114a382887dc2eb4515a302e
%global source0_file List-Pairwise-1.03.tar.gz
# oreon url source checksums end
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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/List-Pairwise-1.03.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "96d716f2b2832cf42875e3a4f81752a025be94c3114a382887dc2eb4515a302e" || { echo "oreon: Source0 SHA256 mismatch for List-Pairwise-1.03.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
