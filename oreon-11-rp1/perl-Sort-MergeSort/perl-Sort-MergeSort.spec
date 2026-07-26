%global source0_hash ad25e7c8d9a9ac8417d6de96c764ced9f477108490dfb960ae02a3db0a9c6efe

Name:           perl-Sort-MergeSort
Version:        0.31
Release:        31%{?dist}
Summary:        Merge pre-sorted input streams
# Automatically converted from old format: (Artistic 2.0 or LGPLv2) and (GPL+ or Artistic) - review is highly recommended.
License:        (Artistic-2.0 OR LicenseRef-Callaway-LGPLv2) AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
URL:            https://metacpan.org/release/Sort-MergeSort

Source0:        https://cpan.metacpan.org/authors/id/M/MU/MUIR/modules/Sort-MergeSort-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)

# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(integer)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# Testing
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)

%description
Given a comparison function and a bunch of iterators that produce data that
is already sorted, mergesort() will provide an iterator that produces
sorted and merged data from all of the input iterators.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Sort-MergeSort-%{version}

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
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
