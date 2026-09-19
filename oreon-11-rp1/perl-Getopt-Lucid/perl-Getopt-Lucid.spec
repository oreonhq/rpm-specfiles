%global source0_hash 68c80aed996580304f08c434992cc350312bec0e5ddc1e95e6831d94a4770379

Name:           perl-Getopt-Lucid
Version:        1.10
Release:        19%{?dist}
Summary:        Clear, readable syntax for command line processing
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://metacpan.org/release/Getopt-Lucid
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Getopt-Lucid-%{version}.tar.gz
# Do not use /usr/bin/env in example's shellbang
Patch0:         Getopt-Lucid-1.08-Remove-shellbang-from-examples.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exception::Class) >= 1.23
BuildRequires:  perl(Exception::Class::Base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Storable) >= 2.16
# Tests:
# CPAN::Meta not useful
# CPAN::Meta::Prereqs not useful
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exception::Class::TryCatch) >= 1.10
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.62
BuildRequires:  perl(vars)
Requires:       perl(Exception::Class::Base)

%{?perl_default_filter}

%description
The goal of this module is providing good code readability and clarity of
intent for command-line option processing. While readability is a subjective
standard, Getopt::Lucid relies on a more verbose, plain-English option
specification as compared against the more symbolic approach of Getopt::Long.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Getopt-Lucid-%{version}
%patch -P0 -p1
chmod -x examples/cpanget

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING.mkdn examples README Todo
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
