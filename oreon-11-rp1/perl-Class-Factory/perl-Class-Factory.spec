%global source0_hash c37a2d269eb935f36a23e113480ae0946fa7c12a12781396a1226c8e435f30f5

Name:           perl-Class-Factory
Version:        1.06
Release:        48%{?dist}
Summary:        Base class for dynamic factory classes
# see lib/Class/Factory.pm
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-Factory
Source0:        https://cpan.metacpan.org/authors/id/P/PH/PHRED/Class-Factory-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(strict)
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.62
# Optional tests:
# Devel::Cover not used

%description
This is a simple module that factory classes can use to generate new types
of objects on the fly, providing a consistent interface to common groups
of objects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-Factory-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
