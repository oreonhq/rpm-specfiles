%global source0_hash 255a5a38336d048ddb9077222691e000984e907aae09a4ea695a9cfd49a1ddd0
Name:		perl-Statistics-ChiSquare
Version:	1.0000
Release:        14%{?dist}
Summary:        How well-distributed is your data?
License:	(GPL-2.0-only OR Artistic-1.0-Perl) AND CC-BY-SA-3.0
URL:		https://metacpan.org/release/Statistics-ChiSquare
Source0:        https://cpan.metacpan.org/modules/by-module/Statistics/Statistics-ChiSquare-%{version}.tar.gz
BuildArch:	noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Suppose you flip a coin 100 times, and it turns up heads 70 times. Is the coin
fair? Suppose you roll a die 100 times, and it shows 30 sixes. Is the die
loaded?

In statistics, the chi-square test calculates how well a series of numbers fits
a distribution. In this module, we only test for whether results fit an even
distribution. It doesn't simply say "yes" or "no". Instead, it gives you a
confidence interval, which sets upper and lower bounds on the likelihood that
the variation in your data is due to chance.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Statistics-ChiSquare-%{version}

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
