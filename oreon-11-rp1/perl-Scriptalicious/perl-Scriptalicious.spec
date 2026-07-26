%global source0_hash a6629caf754d35117ad9332489a37846681924fb0c55d0dc02cda3bf986bbe0f

Name:           perl-Scriptalicious
Version:        1.17
Release:        34%{?dist}
Summary:        Make scripts more delicious to system administrators
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Scriptalicious
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SAMV/Scriptalicious-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Optional run-time:
BuildRequires:  perl(Template)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(YAML)
# Term::ReadKey not used at tests
# Tests:
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
Requires:       perl(Exporter)
# Optional run-time:
Requires:       perl(Term::ReadKey)

%description
This module helps you write scripts that conform to best common practices,
quickly.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Scriptalicious-%{version}
mv Changes{.pod,}
sed -i -e '/^Changes.pod$/d' MANIFEST

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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
