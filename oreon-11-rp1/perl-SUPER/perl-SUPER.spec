%global source0_hash 685d1ee76e7f0e9006942923bf7df8b11c107132992917593dcf7397d417d39a
Name:		perl-SUPER
Version:	1.20190531
Release:        1%{?dist}
Summary:        Sane superclass method dispatcher
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/SUPER
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHROMATIC/SUPER-%{version}.tar.gz
BuildArch:	noarch
Requires:	perl(Scalar::Util) >= 1.20
Requires:	perl(Sub::Identify) >= 0.03
Provides:       perl(SUPER)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Identify)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
When subclassing a class, you occasionally want to dispatch control to the
superclass - at least conditionally and temporarily. This module provides
an easier, cleaner way for class methods to access their ancestor's
implementation.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n SUPER-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.20190531-21
- Prepare for Oreon 11 (RP1)
