%global source0_hash ff7d78a42f5410ec019442cf54360d61cb97355deb045f116a76e3a4c8a3a0a7
Name:           perl-Module-Depends
Version:        0.16
Release:        23%{?dist}
Summary:        Identify the dependencies of a distribution
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Depends
Source0:        https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/Module-Depends-%{version}.tar.gz
Patch0:         Module-Depends-0.15-Fix-escaping-literal-curly-brackates-in-a-regexp.patch
BuildArch:      noarch
Requires:       perl(warnings)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Class::Accessor::Chained)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Parse::CPAN::Meta)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Module::Depends extracts module dependencies from an unpacked
distribution tree.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Depends-%{version}
%patch -P0 -p1

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
