%global source0_hash 2eeb0ce072b538c3e85ad354ee95c582e92fcf987f67b520e231539622d1dd2e
Name:           perl-DateTime-Format-Epoch
Version:        0.16
Release:        1%{?dist}
Summary:        Convert DateTimes to/from epoch seconds
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DateTime-Format-Epoch
Source0:        https://cpan.metacpan.org/modules/by-module/DateTime/DateTime-Format-Epoch-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(DateTime) >= 0.31
Requires:       perl(Math::BigInt) >= 1.66
Requires:       perl(Math::BigInt::GMP)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Math::BigInt\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(DateTime\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::LeapSecond)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Math::BigInt::GMP)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
This module can convert a DateTime object (or any object that can be
converted to a DateTime object) to the number of seconds since a given
epoch. It can also do the reverse.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DateTime-Format-Epoch-%{version}
find -type f -print0 | xargs -0 sed -i 's/\r$//'

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=true NO_PERLLOCAL=true
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
