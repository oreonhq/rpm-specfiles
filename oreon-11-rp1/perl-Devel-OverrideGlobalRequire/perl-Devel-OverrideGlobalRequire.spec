%global source0_hash 0791892de3ae292af4a94e382f21db1ee88210875031851e6ea82c3410785ef9

Name:           perl-Devel-OverrideGlobalRequire
Version:        0.001
Release:        28%{?dist}
Summary:        Override CORE::GLOBAL::require safely
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-OverrideGlobalRequire
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Devel-OverrideGlobalRequire-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Test::More)

%description
This Perl module overrides CORE::GLOBAL::require with a code reference in a way
that plays nice with any existing overloading and ensures the right calling
package is in scope.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Devel-OverrideGlobalRequire-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
