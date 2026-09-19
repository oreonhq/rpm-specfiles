%global source0_hash c95602033822822392f1f812a9540af6153d8a96247dfddd1b839f7cdeef760c

Name:           perl-L
Version:        1.0.1
%global cpan_version v%{version}
Release:        22%{?dist}
Summary:        Perl extension to load module automatically in one-liner
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/L
Source0:        https://cpan.metacpan.org/authors/id/S/SO/SONGMU/L-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Carp)
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(version) >= 0.77
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Test::More) >= 0.98
Provides:       perl(L) = %{version}

# Remove under-specified provides
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(L\\)$

%description
This loads perl modules automatically for use in one-liners.

The module is dangerous, so don't use this module in other perl modules,
scripts or production-ready code. This should be used only in one-liners.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n L-%{cpan_version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
