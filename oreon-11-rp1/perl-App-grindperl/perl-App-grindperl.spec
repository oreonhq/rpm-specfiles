%global source0_hash d26b1f68777083451dc847c8b1d7e851d9511054590318033cea40a3cae06b0f

Name:           perl-App-grindperl
Version:        0.004
Release:        30%{?dist}
Summary:        Command-line tool to help build and test blead perl
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://metacpan.org/release/App-grindperl
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/App-grindperl-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.17
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# The only test does not exercise the code
# autodie not used at tests
# Carp not used at tests
# File::Copy not used at tests
# File::HomeDir 0.98 not used at tests
# File::Spec not used at tests
# Getopt::Lucid not used at tests
# namespace::autoclean not used at tests
# Path::Class not used at tests
# Tests:
# CPAN::Meta not usefull
# CPAN::Meta::Prereqs not usefull
BuildRequires:  perl(Test::More)
Requires:       git
Requires:       make

%description
Hacking on the Perl source tree requires one to regularly build and test. The
grindperl tool helps automate some common configuration, build and test tasks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n App-grindperl-%{version}

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
%license LICENSE
# CONTRIBUTING.mkdn is a generic file not specific to this package
%doc Changes README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
%autochangelog
