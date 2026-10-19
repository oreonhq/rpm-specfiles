%global source0_hash 0e935740c0be6c8c86ff49a9f6de173e09f45f33c996e9a008ebb1b208f375f1
Name:           perl-Test-AutoLoader
Version:        0.03
Release:        1%{?dist}
Summary:        Testing utility for autosplit/autoloaded modules
License:        GPL-1.0-or-later
URL:            https://metacpan.org/release/Test-AutoLoader
Source0:        https://cpan.metacpan.org/authors/id/B/BW/BWARFIELD/NRGN/Test-AutoLoader-%{version}.tar.gz
Patch0:         Test-AutoLoader-0.03-Fix-test-plan-number.patch
Patch1:         Test-AutoLoader-0.03-Skip-POSIX-tests-with-perl-5.16.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Tester)
BuildRequires:  perl-generators
# /oreon:deps
%description
This single-purpose module attempts to eliminate uncaught syntax errors or
other obvious goofs in subroutines that are autosplit, and hence not looked
at by perl -c Module.pm. Ideally, this module will become unnecessary as
you reach full coverage of those subroutines in your unit tests. Until that
happy day, however, this should provide a quick and dirty backstop for
embarrassing typos.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-AutoLoader-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

LC_ALL=C make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
