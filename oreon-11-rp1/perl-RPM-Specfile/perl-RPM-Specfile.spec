%global source0_hash 7da16191cbc07ff58b176b2c7d1b08495cc4fee8c3b9bd92cad2cd52605ed830

Name:           perl-RPM-Specfile
Version:        1.51
Release:        52%{?dist}
Summary:        Perl extension for creating RPM specfiles

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/RPM-Specfile
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHIPT/RPM-Specfile-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
# Archive::Tar not used at tests
# Cwd not used at tests
# File::Basename not used at tests
# File::Copy not used at tests
# File::Temp not used at tests
# Getopt::Long not used at tests
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
# URI::Escape not used at tests
BuildRequires:  perl(vars)
# YAML not used at tests
# Tests:
BuildRequires:  perl(Test)

%description
This is a simple module for creation of RPM Spec files. Most of the methods
in this module are the same name as the RPM Spec file element they
represent but in lower case.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n RPM-Specfile-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

# This file probably shouldn't be in the upstream version.
rm $RPM_BUILD_ROOT/usr/bin/cpanflute2-old

%check
make test

%files
%doc Changes README
%{_bindir}/cpanflute2
%{perl_vendorlib}/RPM
%{_mandir}/man3/RPM::Specfile.3*

%changelog
%autochangelog
