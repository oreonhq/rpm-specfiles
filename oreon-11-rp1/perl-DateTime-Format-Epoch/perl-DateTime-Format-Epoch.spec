%global source0_hash 2eeb0ce072b538c3e85ad354ee95c582e92fcf987f67b520e231539622d1dd2e

Name:           perl-DateTime-Format-Epoch
Version:        0.16
Release:        31%{?dist}
Summary:        Convert DateTimes to/from epoch seconds
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DateTime-Format-Epoch
Source0:        https://cpan.metacpan.org/modules/by-module/DateTime/DateTime-Format-Epoch-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  sed
# Runtime
BuildRequires:  perl(DateTime) >= 0.31
BuildRequires:  perl(DateTime::LeapSecond)
BuildRequires:  perl(Math::BigInt) >= 1.66
BuildRequires:  perl(Math::BigInt::GMP)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Test::More)
# Optional Tests
BuildRequires:  perl(Test::Pod) >= 1.00
# Dependencies
Requires:       perl(DateTime) >= 0.31
Requires:       perl(Math::BigInt) >= 1.66
Requires:       perl(Math::BigInt::GMP)

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Math::BigInt\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(DateTime\\)

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

%check
make test

%files
%license LICENSE
%doc Changes README TODO
%{perl_vendorlib}/DateTime/
%{_mandir}/man3/DateTime::Format::Epoch.3*
%{_mandir}/man3/DateTime::Format::Epoch::ActiveDirectory.3*
%{_mandir}/man3/DateTime::Format::Epoch::DotNet.3*
%{_mandir}/man3/DateTime::Format::Epoch::JD.3*
%{_mandir}/man3/DateTime::Format::Epoch::Lilian.3*
%{_mandir}/man3/DateTime::Format::Epoch::MJD.3*
%{_mandir}/man3/DateTime::Format::Epoch::MacOS.3*
%{_mandir}/man3/DateTime::Format::Epoch::NTP.3*
%{_mandir}/man3/DateTime::Format::Epoch::RJD.3*
%{_mandir}/man3/DateTime::Format::Epoch::RataDie.3*
%{_mandir}/man3/DateTime::Format::Epoch::TAI64.3*
%{_mandir}/man3/DateTime::Format::Epoch::TJD.3*
%{_mandir}/man3/DateTime::Format::Epoch::Unix.3*

%changelog
%autochangelog
