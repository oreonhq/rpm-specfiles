%global source0_hash cbc1e9b35a05e71febc13e5ef547a31c8249899bb6011dbdc9d9ff366ddab6c2
Name:           perl-Test-SubCalls
Version:        1.10
Release:        24%{?dist}
Summary:        Track the number of times subs are called
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-SubCalls
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-SubCalls-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(Test::SubCalls)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Hook::LexWrap)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
There are a number of different situations (like testing caching code) where
you want to want to do a number of tests, and then verify that some underlying
subroutine deep within the code was called a specific number of times. This
module provides a number of functions for doing testing in this way, in
association with your normal Test::More (or similar) test scripts.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-SubCalls-%{version}

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

%autochangelog
