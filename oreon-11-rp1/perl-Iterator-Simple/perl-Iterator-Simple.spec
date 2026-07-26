%global source0_hash cb574d063bb481c8fb9cb5781a4645896aa0e1ee715ba947cf766f1ff4e9eb44

Name:           perl-Iterator-Simple
Version:        0.07
Release:        25%{?dist}
Summary:        Simple iterator and utilities
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Iterator-Simple
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MICHAEL/Iterator-Simple-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

%description
Iterator::Simple is a collection of Perl general-purpose iterator subroutines.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Iterator-Simple-%{version}
# Remove bundled modules
rm -rf ./inc
sed -i -e '/^inc\//d' MANIFEST
# Fix permissions, CPAN RT#123838
chmod -x Changes README

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
