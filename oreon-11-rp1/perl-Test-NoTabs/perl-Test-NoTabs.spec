%global source0_hash fb75c6a38721f0169e11c1e7dbe5329ed7216885a0b01123f342dd86d3356030

Name:		perl-Test-NoTabs
Version:	2.02
Release:	24%{?dist}
Summary:	Check the presence of tabs in your project
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Test-NoTabs
Source0:	https://cpan.metacpan.org/modules/by-module/Test/Test-NoTabs-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Test::More)
# Optional Tests
BuildRequires:	perl(CPAN::Meta) >= 2.120900
# Dependencies
# (none)

Provides:       perl(Test::NoTabs)
%description
This module scans your project/distribution for any perl files (scripts,
modules, etc.) for the presence of tabs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-NoTabs-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::NoTabs.3*

%changelog
%autochangelog
