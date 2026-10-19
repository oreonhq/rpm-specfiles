%global source0_hash 61e3cfdb27bb3bee27beb97124dd930760e1039edc1eb7816c2f5627765f8f8f
Name:		perl-Math-Calc-Units
Version:	1.07
Release:        46%{?dist}
Summary:        Human-readable unit-aware calculator
License:	GPL-2.0-only OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Math-Calc-Units
Source0:        https://cpan.metacpan.org/modules/by-module/Math/Math-Calc-Units-%{version}.tar.gz
BuildArch:	noarch
%global __provides_exclude ^perl\\(Parse::Yapp::Driver\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Math::Calc::Units is a simple calculator that keeps track of units. It
currently handles combinations of byte sizes and duration only, although
adding any other multiplicative types is easy. Any unknown type is treated
as a unique user type (with some effort to map English plurals to their
singular forms).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Math-Calc-Units-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
rm %{buildroot}%{perl_vendorlib}/Math/Calc/Units/Grammar.y
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
